#!/usr/bin/env python3
"""Check the vial holder's sliced plate against the model, from the G-code in the .gcode.3mf.

From the outer-wall toolpaths: the footprint (span plus one line width) at a few heights, which should be the SBS
127.76 x 85.48 mm; each pocket's diameter (a least-squares circle through its wall, minus one line width), which
should be 28.2 mm; the top layer's height (23 mm); and the settings that matter, from the G-code's config block.
Also draws a top view of every extrusion move, shaded by height.

    python check_slice.py vial_holder_20ml_x6_A1mini_PETG_0.4.gcode.3mf plate_layout.png    # needs numpy, matplotlib
"""
import json, math, re, sys, zipfile
from collections import defaultdict

import numpy as np

src, out_png = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(src) as z:
    text = z.read("Metadata/plate_1.gcode").decode()

num = re.compile(r"([XYZEIJ])(-?\d*\.?\d+)")
walls = defaultdict(list)                    # z -> [(x, y)] on outer-wall moves
lws = {}
moves = []
x = y = 0.0
lz = feat = lw = None
for line in text.splitlines():
    if line.startswith(";"):
        if line.startswith("; Z_HEIGHT:"):
            lz = round(float(line.split(":")[1]), 3)
        elif line.startswith("; FEATURE:"):
            feat = line.split(":", 1)[1].strip()
        elif line.startswith("; LINE_WIDTH:"):
            lw = float(line.split(":")[1])
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
            moves.append((lz, prev[0], prev[1], q[0], q[1]))
            prev = q
        if feat == "Outer wall":
            walls[lz] += [(x, y)] + pts
            lws[lz] = lw
    x, y = nx, ny


def layer(z):
    return min(walls, key=lambda k: abs(k - z))


def circle(pts):
    """Least-squares circle (Kasa): centre and radius."""
    A = np.c_[2 * pts, np.ones(len(pts))]
    b = (pts ** 2).sum(axis=1)
    cx, cy, c = np.linalg.lstsq(A, b, rcond=None)[0]
    return cx, cy, math.sqrt(c + cx * cx + cy * cy)


out = {"file": src, "layers": len({m[0] for m in moves}), "top_layer_z": max(walls)}
k1 = layer(1.0)
f = np.array(walls[k1])
lo, hi = f.min(axis=0), f.max(axis=0)
centre = (lo + hi) / 2
out["centre_on_bed_mm"] = [round(float(v), 2) for v in centre]
out["footprint_mm"] = {}
for z in (1.0, 10.0, 21.0):
    k = layer(z)
    pts = np.array(walls[k])
    big = pts[np.hypot(*(pts - centre).T) > 45]                 # the outside wall, not the pockets
    out["footprint_mm"][k] = [round(float(np.ptp(big[:, 0]) + lws[k]), 2), round(float(np.ptp(big[:, 1]) + lws[k]), 2)]
out["pocket_diameter_mm"] = {}
for z in (6.0, 12.0, 18.0):
    k = layer(z)
    pts = np.array(walls[k]) - centre
    ds = []
    for px in (-40, 0, 40):
        for py in (20, -20):
            near = pts[np.hypot(pts[:, 0] - px, pts[:, 1] - py) < 16]
            cx, cy, r = circle(near)
            ds.append(round(2 * r - lws[k], 2))
    out["pocket_diameter_mm"][k] = ds
cfg = dict(re.findall(r"^; (\w+) = (.*)$", text, flags=re.M))
out["settings"] = {k: cfg.get(k) for k in ("printer_settings_id", "nozzle_diameter", "print_settings_id",
                                           "filament_settings_id", "curr_bed_type", "layer_height", "wall_loops",
                                           "sparse_infill_density", "elefant_foot_compensation", "brim_type",
                                           "enable_support", "nozzle_temperature", "textured_plate_temp")}
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
fig, ax = plt.subplots(figsize=(7, 7), dpi=130)
lc = LineCollection(mv[:, 1:].reshape(-1, 2, 2), array=mv[:, 0], cmap="viridis", linewidths=0.5)
ax.add_collection(lc)
ax.plot([0, 180, 180, 0, 0], [0, 0, 180, 180, 0], color="0.6", lw=1)
ax.set_xlim(-5, 185); ax.set_ylim(-5, 185); ax.set_aspect("equal")
ax.set_xlabel("X (mm)"); ax.set_ylabel("Y (mm)")
fig.colorbar(lc, ax=ax, shrink=0.7, label="Z (mm)")
ax.set_title("Vial holder on the A1 mini's 180 x 180 mm bed: extrusion moves, top view", fontsize=9)
fig.tight_layout(); fig.savefig(out_png)
print("wrote", out_png)
