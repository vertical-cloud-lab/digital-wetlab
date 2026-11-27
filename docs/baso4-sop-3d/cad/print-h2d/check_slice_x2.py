#!/usr/bin/env python3
"""Check a plate of several vial holders on the H2D, from the G-code (Studio's GUI slice or a .gcode.3mf).

``check_slice.py`` checks one holder. This version splits the toolpaths by object, using the G-code's own
"start printing object, unique label id" markers, and checks every holder on the plate:

* the footprint (outer-wall span plus one line width) at z 1, 10 and 21 mm, which should be the SBS 127.76 x 85.48 mm;
* the six pockets' diameters (a least-squares circle through each pocket's outer wall, minus one line width) at
  z 6, 12 and 18 mm, which should be 28.2 mm;
* where it sits on the bed, and whether that is inside the reach of each nozzle (``extruder_printable_area``).

And for the plate as a whole: the top layer, the settings that matter, which nozzle prints (``filament_map`` 1 is the
left nozzle; the start G-code heats ``T1``), every hotend temperature command (nothing may heat ``T0``, the right
nozzle, which this plate doesn't use), and that there is no prime tower or wipe.

    python check_slice_x2.py PLATE.gcode|PLATE.gcode.3mf plate_layout_x2.png      # needs numpy, matplotlib
"""
import json, math, re, sys, zipfile
from collections import defaultdict

import numpy as np

src, out_png = sys.argv[1], sys.argv[2]
if src.endswith(".3mf"):
    with zipfile.ZipFile(src) as z:
        text = z.read("Metadata/plate_1.gcode").decode()
else:
    text = open(src).read()

num = re.compile(r"([XYZEIJ])(-?\d*\.?\d+)")
walls = defaultdict(lambda: defaultdict(list))  # object -> z -> [(x, y)] on outer-wall moves
lws = {}
moves = []
x = y = 0.0
lz = feat = lw = obj = None
for line in text.splitlines():
    if line.startswith(";"):
        if line.startswith("; Z_HEIGHT:"):
            lz = round(float(line.split(":")[1]), 3)
        elif line.startswith("; FEATURE:"):
            feat = line.split(":", 1)[1].strip()
        elif line.startswith("; LINE_WIDTH:"):
            lw = float(line.split(":")[1])
        elif line.startswith("; start printing object, unique label id:"):
            obj = int(line.rsplit(":", 1)[1])
        elif line.startswith("; stop printing object"):
            obj = None
        continue
    s = line.split(";")[0].split()
    if not s or s[0] not in ("G0", "G1", "G2", "G3"):
        continue
    p = {k: float(v) for k, v in num.findall(" ".join(s[1:]))}
    nx, ny = p.get("X", x), p.get("Y", y)
    if lz is not None and p.get("E", 0) > 0 and (nx, ny) != (x, y):
        pts = [(nx, ny)]
        if s[0] in ("G2", "G3"):
            cx, cy = x + p.get("I", 0), y + p.get("J", 0)
            a0, a1 = math.atan2(y - cy, x - cx), math.atan2(ny - cy, nx - cx)
            if s[0] == "G2":
                a1 = a1 - 2 * math.pi if a1 >= a0 else a1
            else:
                a1 = a1 + 2 * math.pi if a1 <= a0 else a1
            rr = math.hypot(x - cx, y - cy)
            pts = [(cx + rr * math.cos(a), cy + rr * math.sin(a)) for a in np.linspace(a0, a1, 24)[1:]]
        prev = (x, y)
        for q in pts:
            moves.append((lz, prev[0], prev[1], q[0], q[1], -1 if obj is None else obj))
            prev = q
        if feat == "Outer wall" and obj is not None:
            walls[obj][lz] += [(x, y)] + pts
            lws[lz] = lw
    x, y = nx, ny


def circle(pts):
    """Least-squares circle (Kasa): centre and radius."""
    A = np.c_[2 * pts, np.ones(len(pts))]
    b = (pts ** 2).sum(axis=1)
    cx, cy, c = np.linalg.lstsq(A, b, rcond=None)[0]
    return cx, cy, math.sqrt(c + cx * cx + cy * cy)


cfg = dict(re.findall(r"^; (\w+) = (.*)$", text, flags=re.M))
areas = [r.split(",") for r in re.split(r"[#;]", cfg.get("extruder_printable_area", "")) if r]
out = {"file": src.rsplit("/", 1)[-1], "layers": len({m[0] for m in moves}),
       "top_layer_z": max(max(w) for w in walls.values()), "objects": {}}
for o, w in sorted(walls.items()):
    def layer(z):
        return min(w, key=lambda k: abs(k - z))
    f = np.array(w[layer(1.0)])
    lo, hi = f.min(axis=0), f.max(axis=0)
    centre = (lo + hi) / 2
    r = {"centre_on_bed_mm": [round(float(v), 2) for v in centre],
         "bbox_on_bed_mm": [round(float(v), 2) for v in (*lo, *hi)], "footprint_mm": {}, "pocket_diameter_mm": {}}
    for z in (1.0, 10.0, 21.0):
        k = layer(z)
        pts = np.array(w[k])
        big = pts[np.hypot(*(pts - centre).T) > 45]             # the outside wall, not the pockets
        r["footprint_mm"][k] = [round(float(np.ptp(big[:, 0]) + lws[k]), 2), round(float(np.ptp(big[:, 1]) + lws[k]), 2)]
    for z in (6.0, 12.0, 18.0):
        k = layer(z)
        pts = np.array(w[k]) - centre
        ds = []
        for px in (-40, 0, 40):
            for py in (20, -20):
                near = pts[np.hypot(pts[:, 0] - px, pts[:, 1] - py) < 16]
                ds.append(round(2 * circle(near)[2] - lws[k], 2))
        r["pocket_diameter_mm"][k] = ds
    box = r["bbox_on_bed_mm"]
    inside = []
    for a in areas:
        ax = [float(c.split("x")[0]) for c in a]; ay = [float(c.split("x")[1]) for c in a]
        inside.append(min(ax) <= box[0] and box[2] <= max(ax) and min(ay) <= box[1] and box[3] <= max(ay))
    r["inside_left_and_right_nozzle_reach"] = inside
    out["objects"][o] = r
out["extrusion_outside_objects"] = sum(1 for m in moves if m[5] == -1 and m[0] > 0.3)
out["settings"] = {k: cfg.get(k) for k in ("printer_settings_id", "nozzle_diameter", "nozzle_type", "nozzle_volume_type",
                                           "print_settings_id", "filament_settings_id", "curr_bed_type", "layer_height",
                                           "wall_loops", "sparse_infill_density", "elefant_foot_compensation",
                                           "brim_type", "enable_support", "enable_prime_tower", "enable_arc_fitting",
                                           "nozzle_temperature", "textured_plate_temp", "filament_map",
                                           "filament_map_mode", "extruder_printable_area")}
fmap = cfg.get("filament_map", "").strip()
heats = re.findall(r"^(M10[49] [^;\n]*)", text, flags=re.M)
out["nozzle_that_prints"] = {"filament_map": fmap, "side": {"1": "left", "2": "right"}.get(fmap, "unknown")}
out["hotend_temperature_commands"] = [h.strip() for h in heats]
out["right_nozzle_T0_heated"] = any(re.search(r"\bT0\b", h) and not re.search(r"\bS0\b", h) for h in heats)
out["prime_tower_or_wipe_features"] = len(re.findall(r"^; FEATURE: (Prime tower|Wipe)", text, flags=re.M))
m = re.search(r"^;===== machine: (\S+) =+\n;===== date: (\d+)", text, flags=re.M)
out["start_gcode"] = m.group(0).replace("\n", " | ") if m else None
head = text[:3000]
out["estimate"] = re.search(r"total estimated time: ([^\n]+)", head).group(1)
out["filament_g"] = float(re.search(r"total filament weight \[g\] : ([\d.]+)", head).group(1))
print(json.dumps(out, indent=1))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

mv = np.array(moves)
mv = mv[np.argsort(mv[:, 0], kind="stable")]
fig, ax = plt.subplots(figsize=(7.5, 7), dpi=130)
lc = LineCollection(mv[:, 1:5].reshape(-1, 2, 2), array=mv[:, 0], cmap="viridis", linewidths=0.5)
ax.add_collection(lc)
bed = np.array([[float(v) for v in c.split("x")] for c in cfg["printable_area"].split(",")])
ax.plot(*np.vstack([bed, bed[:1]]).T, color="0.6", lw=1)
for a, style in zip(areas, ("--", ":")):
    pa = np.array([[float(v) for v in c.split("x")] for c in a])
    ax.plot(*np.vstack([pa, pa[:1]]).T, color="0.75", lw=0.8, ls=style)
bw, bh = bed.max(axis=0)
ax.set_xlim(-5, bw + 5); ax.set_ylim(-5, bh + 5); ax.set_aspect("equal")
ax.set_xlabel("X (mm)"); ax.set_ylabel("Y (mm)")
fig.colorbar(lc, ax=ax, shrink=0.7, label="Z (mm)")
ax.set_title(f"{len(walls)} vial holders on the H2D's {bw:g} x {bh:g} mm bed ({out['nozzle_that_prints']['side']} nozzle):"
             " extrusion moves, top view\n(dashed: left nozzle's reach, dotted: right's)", fontsize=9)
fig.tight_layout(); fig.savefig(out_png)
print("wrote", out_png)
