"""Every model in the SOP animation, tessellated once and cached in .cache/.

Where each one comes from:

* **Opentrons OT-2**: Opentrons' own reference STEP ("Detailed", github.com/Opentrons/ot2), fetched at run time and
  SHA-256 checked, never committed. Its solids are named, so the door, the Z gantry, the P300 single on the left mount
  and the frame come in separately and can move.
* **Lid camera** (Raspberry Pi HQ camera, 8-50 mm zoom, C-CS adapter, Pi 5, printed base and deck): the lab's own
  assembly STEP from byu-vcl PR 234 (``ot2-overhead-camera/lid-mount/exports/assembly.step`` at 49677cf), fetched and
  hash-checked the same way. It sits on the top window over slot 7, as the monitoring plan says.
* **A&D HR-100A balance, NEST 96-well plate, Opentrons 300 uL tip rack, 15 mL Falcon tubes, the AC 6-tube rack,
  20 mL vial, weigh boat, spatula, colour sensor**: ``lab_models/labware.py``, a verbatim copy of byu-vcl's
  ``vertical-lab/lab_models`` at 516f796 (from #199), built from the makers' drawings and Opentrons' labware
  definitions.
* **Modelled here, from typical sizes** (no CAD or measurements on record): the fume hood (a 5 ft bench hood with a
  vertical sash), the benches and rooms, the reagent bottles, the carrying tub, the waste bottles, the wash bottle,
  the seal and the stand-in person. Their sizes are round numbers, not measurements of EB B125 or CB 154.

Coordinates: millimetres, z up, the front of everything towards -y.
"""
from __future__ import annotations

import hashlib
import math
import pickle
import sys
import urllib.request
from pathlib import Path

import numpy as np
import pyvista as pv

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "lab_models"))
CACHE = HERE / ".cache"

import cadquery as cq          # noqa: E402
import common as LM            # noqa: E402
import labware as LW           # noqa: E402

VENDOR = {
    "ot2": dict(
        url="https://raw.githubusercontent.com/Opentrons/ot2/ef9ede131ed1d64daf9a0df5b2140a0a8e56b632/"
            "reference-model/STEP/OT-2%20Reference%20Model%20Detailed.STEP",
        name="OT-2 Reference Model Detailed.STEP",
        sha256="f8bf145b878683337ec0f89b74668bd7e350d674777762fab9befbcd014b42d4"),
    "lidcam": dict(
        url="https://raw.githubusercontent.com/vertical-cloud-lab/byu-vcl/49677cfff31a67765d9182c01765bfa994a7545d/"
            "ot2-overhead-camera/lid-mount/exports/assembly.step",
        name="lid-mount-assembly-49677cf.step",
        sha256="dd015aea0df230f56215424bd1c14c54fc91de910a8626abdeebb4a8facca17b"),
}

# ---------------------------------------------------------------------------------------------- materials
# name: (r, g, b, opacity, specular). The lab_models palette, plus what this scene needs.
MATS = dict(LM.MATERIALS)
MATS.update({
    "epoxy":        (0.16, 0.16, 0.17, 1.00, 0.35),
    "hood_enamel":  (0.86, 0.87, 0.86, 1.00, 0.25),
    "hood_liner":   (0.95, 0.95, 0.93, 1.00, 0.10),
    "hood_dark":    (0.30, 0.31, 0.33, 1.00, 0.20),
    "sash_glass":   (0.78, 0.88, 0.93, 0.22, 0.90),
    "sash_frame":   (0.55, 0.57, 0.60, 1.00, 0.50),
    "hood_light":   (1.00, 0.99, 0.92, 1.00, 0.00),
    "cabinet":      (0.80, 0.80, 0.78, 1.00, 0.20),
    "cab_handle":   (0.45, 0.46, 0.48, 1.00, 0.60),
    "floor_eb":     (0.80, 0.79, 0.75, 1.00, 0.05),
    "floor_cb":     (0.74, 0.76, 0.78, 1.00, 0.05),
    "wall_eb":      (0.93, 0.92, 0.89, 1.00, 0.00),
    "wall_cb":      (0.91, 0.92, 0.93, 1.00, 0.00),
    "tape_yellow":  (0.98, 0.82, 0.10, 1.00, 0.10),
    "liner_pad":    (0.98, 0.98, 0.98, 1.00, 0.00),
    "tray_grey":    (0.62, 0.64, 0.67, 1.00, 0.20),
    "hdpe":         (0.94, 0.94, 0.92, 1.00, 0.15),
    "amber":        (0.55, 0.30, 0.08, 0.75, 0.80),
    "cap_black":    (0.10, 0.10, 0.11, 1.00, 0.30),
    "cap_white":    (0.96, 0.96, 0.95, 1.00, 0.20),
    "label_white":  (0.99, 0.99, 0.98, 1.00, 0.05),
    "band_ba":      (0.95, 0.47, 0.10, 1.00, 0.10),
    "band_so4":     (0.20, 0.66, 0.33, 1.00, 0.10),
    "band_nacl":    (0.45, 0.50, 0.62, 1.00, 0.10),
    "band_water":   (0.30, 0.62, 0.95, 1.00, 0.10),
    "waste_yellow": (0.98, 0.84, 0.15, 1.00, 0.10),
    "powder":       (0.97, 0.97, 0.97, 1.00, 0.05),
    "solution":     (0.62, 0.80, 0.97, 0.45, 0.70),
    "precip":       (0.98, 0.98, 0.98, 1.00, 0.05),
    "black_paper":  (0.04, 0.04, 0.05, 1.00, 0.05),
    "tub":          (0.82, 0.86, 0.90, 0.55, 0.60),
    "tub_lid":      (0.20, 0.42, 0.75, 1.00, 0.30),
    "coat":         (0.97, 0.97, 0.97, 1.00, 0.10),
    "nitrile":      (0.42, 0.40, 0.88, 1.00, 0.30),
    "skin":         (0.87, 0.70, 0.58, 1.00, 0.20),
    "hair":         (0.23, 0.17, 0.12, 1.00, 0.10),
    "trousers":     (0.18, 0.22, 0.33, 1.00, 0.10),
    "shoes":        (0.12, 0.12, 0.12, 1.00, 0.20),
    "goggles":      (0.55, 0.75, 0.90, 0.55, 0.90),
    "zone_in":      (0.88, 0.20, 0.18, 0.16, 0.00),
    "zone_next":    (0.98, 0.68, 0.10, 0.20, 0.00),
    "zone_cb":      (0.20, 0.45, 0.90, 0.16, 0.00),
    "path":         (0.20, 0.45, 0.90, 1.00, 0.10),
    "seal":         (0.92, 0.96, 0.99, 0.35, 0.90),
    "wipe":         (0.96, 0.97, 0.99, 1.00, 0.00),
    "pipette_body": (0.92, 0.92, 0.90, 1.00, 0.30),
    "plunger":      (0.20, 0.45, 0.80, 1.00, 0.30),
    "laptop":       (0.22, 0.23, 0.25, 1.00, 0.40),
    "led_green":    (0.10, 0.90, 0.30, 1.00, 0.20),
    "text_dark":    (0.12, 0.14, 0.20, 1.00, 0.10),
    "door_wood":    (0.62, 0.48, 0.33, 1.00, 0.20),
    "sign":         (0.20, 0.32, 0.55, 1.00, 0.20),
})


def entry(mesh, mat, **kw):
    r, g, b, a, spec = MATS[mat]
    e = dict(mesh=mesh, color=(r, g, b), opacity=a, specular=spec, material=mat)
    e.update(kw)
    return e


# --------------------------------------------------------------------------------------- vendor CAD
def fetch(key: str) -> Path:
    f = VENDOR[key]
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f["name"]
    if not path.exists():
        print(f"downloading {f['url']}", flush=True)
        req = urllib.request.Request(f["url"], headers={"User-Agent": "Mozilla/5.0"})
        path.write_bytes(urllib.request.urlopen(req, timeout=600).read())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != f["sha256"]:
        raise SystemExit(f"{path.name}: sha256 {digest}, expected {f['sha256']}")
    return path


def step_solids(path: Path) -> dict[str, cq.Solid]:
    """Every solid in a STEP file by its name (unnamed ones get 'solid <i>')."""
    from OCP.STEPControl import STEPControl_Reader
    from OCP.TopAbs import TopAbs_SOLID
    from OCP.TopExp import TopExp_Explorer
    reader = STEPControl_Reader()
    reader.ReadFile(str(path))
    reader.TransferRoots()
    tr = reader.WS().TransferReader()
    out, i = {}, 0
    exp = TopExp_Explorer(reader.OneShape(), TopAbs_SOLID)
    while exp.More():
        s = exp.Current()
        ent = tr.EntityFromShapeResult(s, 1)
        name = ent.Name().ToCString() if ent is not None else f"solid {i}"
        out[name] = cq.Solid(s)
        exp.Next()
        i += 1
    return out


def to_mesh(shape, tol: float = 0.5) -> pv.PolyData:
    if isinstance(shape, cq.Workplane):
        shape = shape.val() if len(shape.vals()) == 1 else cq.Compound.makeCompound(shape.vals())
    verts, tris = shape.tessellate(tol, 0.3)
    if not tris:
        return pv.PolyData()
    pts = np.array([(v.x, v.y, v.z) for v in verts], float)
    faces = np.hstack([[3, *t] for t in tris])
    return pv.PolyData(pts, faces).compute_normals(split_vertices=True, feature_angle=35, auto_orient_normals=False)


def merge(meshes) -> pv.PolyData:
    meshes = [m for m in meshes if m is not None and m.n_points]
    if not meshes:
        return pv.PolyData()
    return meshes[0].merge(meshes[1:]) if len(meshes) > 1 else meshes[0]


# ---- the OT-2 -------------------------------------------------------------------------------------------
# The reference STEP is Y-up with +Z toward the front. Deck coordinates (Opentrons: x right, y back, origin at the
# front-left corner of slot 1, z up from the deck surface): x_deck = X + 196.5, y_deck = 214.525 - Z, z_deck = Y - 53.55
# (byu-vcl ot2_context.py, measured on this STEP). The robot frame used here is the STEP turned Z-up, centred on its
# footprint, feet at z = 0: (X, -Z, Y + 15). So deck -> robot is a pure shift:
DECK_TO_OT2 = np.array([-196.5, -214.525, 68.55])
SLOT_PITCH = (132.5, 90.5)


def slot_centre(n: int) -> tuple[float, float]:
    """Slot centre in deck coordinates (Opentrons' ot2_standard deck: 128 x 86 mm slots on a 132.5 x 90.5 pitch)."""
    return ((n - 1) % 3) * SLOT_PITCH[0] + 64.0, ((n - 1) // 3) * SLOT_PITCH[1] + 43.0


def deck(x, y, z=0.0) -> np.ndarray:
    """Deck coordinates -> the OT-2's own frame."""
    return np.array([x, y, z], float) + DECK_TO_OT2


OT2_GROUPS = {
    "frame": ("OT-2 FRAME", "REMOVABLE DECK", "WINDOW FRAME LEFT", "WINDOW FRAME RIGHT"),
    "glass": ("LEFT WINDOW", "RIGHT WINDOW", "REAR WINDOW", "TOP WINDOW"),
    "door": ("DOOR TOP", "DOOR BOTTOM"),
    "head": ("Z-GANTRY TOP COVER", "Z-GANTRY BASE", "Z-GANTRY FRONT COVER", "Z-GANTRY CARRIAGE"),
    "pipette": ("300uL PIPETTE LEFT", "LEFT PIPETTE MOUNT TOP POSITION"),
}


def _ot2_solids() -> dict[str, cq.Solid]:
    sols = step_solids(fetch("ot2"))
    rot = cq.Location(cq.Vector(0, 0, 0), cq.Vector(1, 0, 0), 90)          # Y-up -> Z-up: (X, Y, Z) -> (X, -Z, Y)
    shift = cq.Location(cq.Vector(0, 0, 15.0))
    return {n: s.moved(rot).moved(shift) for n, s in sols.items()}


def build_ot2() -> dict:
    """{group: {name: entry}} for the OT-2, plus 'nozzle': the P300's nozzle tip (robot frame) as modelled."""
    sols = _ot2_solids()
    out = {}
    for g, names in OT2_GROUPS.items():
        out[g] = {}
        for n in names:
            s = sols[n]
            if g == "glass" or g == "door":
                mat = "acrylic"
            elif g == "pipette":
                mat = "printer_grey" if "MOUNT" in n else "printer_white"
            elif n == "REMOVABLE DECK":
                mat = "aluminium"
            elif n == "OT-2 FRAME":
                mat = "printer_white"
            elif g == "head":
                mat = "printer_grey" if "CARRIAGE" in n else "printer_white"
            else:
                mat = "printer_grey"
            mesh = to_mesh(s, 0.6)
            if n == "OT-2 FRAME":
                # the X gantry beam is part of the frame solid in Opentrons' file, parked over slot 7. Cut it out
                # (x within the Y rails, its 70 mm deep, 80 mm tall profile) so it rides front-to-back with the head.
                cc = mesh.cell_centers().points
                sel = (np.abs(cc[:, 0]) < 272) & (cc[:, 1] > -50) & (cc[:, 1] < 40) & (cc[:, 2] > 495) & (cc[:, 2] < 590)
                beam = mesh.extract_cells(np.where(sel)[0]).extract_surface(algorithm="dataset_surface")
                mesh = mesh.extract_cells(np.where(~sel)[0]).extract_surface(algorithm="dataset_surface")
                out["beam"] = {"X GANTRY (cut from OT-2 FRAME)": entry(beam, "printer_white")}
            out[g][n] = entry(mesh, mat)
    # the P300's nozzle: the lowest point of the pipette solid, and the centre of its lowest 4 mm
    pip = to_mesh(sols["300uL PIPETTE LEFT"], 0.3)
    pts = pip.points
    zmin = pts[:, 2].min()
    low = pts[pts[:, 2] < zmin + 4.0]
    out["nozzle"] = np.array([low[:, 0].mean(), low[:, 1].mean(), zmin])
    bb = sols["DOOR TOP"].BoundingBox()
    out["door_hinge"] = np.array([0.0, bb.ymin, bb.zmax])          # top front edge of the door
    return out


def build_lidcam() -> dict:
    """The lab's lid-camera assembly in the robot frame, over slot 7 (base, deck, camera, lens, Pi 5)."""
    sols = step_solids(fetch("lidcam"))
    # mount frame: origin on the top window's top face over the slot centre, axes as the deck (byu-vcl ot2_context.py)
    xc, yc = slot_centre(7)
    origin = deck(xc, yc, 643.8 - 53.55)
    out = {}
    mats = {"base": "pla_grey", "deck": "pla_grey", "camera_pcb": "pcb", "camera_mount": "printer_black",
            "adapter": "printer_black", "lens": "printer_black", "pi5": "pcb"}
    for n, s in sols.items():
        if n == "lid":                      # the window patch: the OT-2's own top window is already there
            continue
        mat = mats.get(n, "printer_black")
        m = to_mesh(s, 0.4).translate(origin, inplace=False)
        out[n] = entry(m, mat)
    return out


# ---- pyvista primitives -----------------------------------------------------------------------------------
def box(x0, y0, z0, x1, y1, z1) -> pv.PolyData:
    return pv.Box(bounds=(min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1), min(z0, z1), max(z0, z1))).triangulate()


def cyl(x, y, z0, r, h, res=40) -> pv.PolyData:
    return pv.Cylinder(center=(x, y, z0 + h / 2), direction=(0, 0, 1), radius=r, height=h, resolution=res,
                       capping=True).triangulate()


def ring(x, y, z0, r_out, r_in, h, res=48) -> pv.PolyData:
    d = pv.Disc(center=(x, y, z0), inner=r_in, outer=r_out, normal=(0, 0, 1), r_res=1, c_res=res)
    return d.extrude((0, 0, h), capping=True).triangulate()


def sphere(x, y, z, r, res=24) -> pv.PolyData:
    return pv.Sphere(radius=r, center=(x, y, z), theta_resolution=res, phi_resolution=res)


def capsule(p0, p1, r, res=20) -> pv.PolyData:
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    d = p1 - p0
    L = float(np.linalg.norm(d))
    c = pv.Cylinder(center=(p0 + p1) / 2, direction=d / L, radius=r, height=L, resolution=res, capping=False)
    return merge([c.triangulate(), sphere(*p0, r, res), sphere(*p1, r, res)])


def text3d(s, x, y, z, height, depth=2.0, facing="-y") -> pv.PolyData:
    """Raised lettering standing upright, readable from the front (-y) or lying flat (facing='+z')."""
    t = pv.Text3D(s, depth=depth / height)        # Text3D letters are about 1 unit tall: depth scales with them
    b = t.bounds
    t = t.translate((-b[0], -b[2], -b[4]), inplace=False).scale(height / max(b[3] - b[2], 1e-6), inplace=False)
    if facing == "-y":
        t = t.rotate_x(90, inplace=False)
    return t.translate((x, y, z), inplace=False).triangulate()


# ---- the fume hood -------------------------------------------------------------------------------------
# A 5 ft (1524 mm) bench hood with a vertical rising sash on a base cabinet: typical catalogue sizes, not EB B125's
# measurements, which aren't on record. Hood frame: x across, the front of the work surface at y = 0, floor at z = 0.
HOOD = dict(W=1524.0, D=864.0, top_z=2420.0, ws_z=920.0, post=100.0, sash_y=(46.0, 66.0), sash_h=780.0,
            open_top=1700.0, baffle_y=790.0, working=457.0)


def build_hood() -> dict:
    h = HOOD
    W, D = h["W"], h["D"]
    x0, x1 = -W / 2, W / 2
    ws = h["ws_z"]
    e: dict[str, dict] = {}
    # base cabinet with two doors, a toe kick and a work surface
    e["hood cabinet"] = entry(merge([box(x0 + 10, 60, 100, x1 - 10, D - 20, ws - 30), box(x0 + 40, 100, 0, x1 - 40, D - 40, 100)]), "cabinet")
    doors = [box(x0 + 20, 54, 120, -8, 60, ws - 50), box(8, 54, 120, x1 - 20, 60, ws - 50)]
    e["hood cabinet doors"] = entry(merge(doors), "hood_enamel")
    e["hood cabinet handles"] = entry(merge([box(-60, 44, ws - 160, -30, 54, ws - 90), box(30, 44, ws - 160, 60, 54, ws - 90)]), "cab_handle")
    e["hood work surface"] = entry(box(x0, -10, ws - 30, x1, D, ws), "epoxy")
    # superstructure: side posts, back, roof, upper fascia above the opening, liner
    post = h["post"]
    e["hood posts"] = entry(merge([box(x0, 0, ws, x0 + post, D, h["top_z"]), box(x1 - post, 0, ws, x1, D, h["top_z"])]), "hood_enamel")
    e["hood back"] = entry(box(x0, D - 30, ws, x1, D, h["top_z"]), "hood_enamel")
    e["hood roof"] = entry(box(x0, 0, h["top_z"] - 40, x1, D, h["top_z"]), "hood_enamel")
    e["hood fascia"] = entry(box(x0, -4, h["open_top"], x1, h["sash_y"][0] - 2, h["top_z"]), "hood_enamel")
    e["hood duct"] = entry(cyl(0, D / 2 + 60, h["top_z"], 160, 260), "steel")
    # interior: white liner side walls and a slotted baffle
    xi0, xi1 = x0 + post, x1 - post
    e["hood liner"] = entry(merge([box(xi0, 70, ws, xi0 + 6, h["baffle_y"], h["top_z"] - 40),
                                   box(xi1 - 6, 70, ws, xi1, h["baffle_y"], h["top_z"] - 40)]), "hood_liner")
    baffle = []
    z = ws
    for zz0, zz1 in ((ws + 40, ws + 360), (ws + 400, ws + 900), (ws + 940, h["top_z"] - 140)):
        baffle.append(box(xi0, h["baffle_y"], zz0, xi1, h["baffle_y"] + 8, zz1))
    e["hood baffle"] = entry(merge(baffle), "hood_liner")
    e["hood baffle slots"] = entry(merge([box(xi0, h["baffle_y"] + 10, ws, xi1, h["baffle_y"] + 20, h["top_z"] - 40)]), "hood_dark")
    e["hood light"] = entry(box(-500, 200, h["top_z"] - 48, 500, 600, h["top_z"] - 40), "hood_light")
    # airfoil sill at the front edge of the work surface
    sill = pv.Cylinder(center=(0, 18, ws + 14), direction=(1, 0, 0), radius=14, height=W - 2 * post, resolution=24).triangulate()
    e["hood airfoil"] = entry(sill, "steel")
    # the 15 cm (6 in) line: work behind it
    e["hood 6in tape"] = entry(box(xi0 + 20, 66 + 150, ws, xi1 - 20, 66 + 170, ws + 1.2), "tape_yellow")
    # airflow monitor on the right post, with a green light; and the sash-height arrow stickers
    e["hood monitor"] = entry(box(x1 - 88, -6, ws + 1050, x1 - 12, 2, ws + 1170), "hood_dark")
    e["hood monitor led"] = entry(box(x1 - 60, -9, ws + 1130, x1 - 40, -5, ws + 1150), "led_green")
    e["hood sash sticker"] = entry(box(x0 + 30, -3, ws + h["working"] - 8, x0 + 80, 1, ws + h["working"] + 8), "tape_yellow")
    return e


def build_sash() -> dict:
    """The sash, closed (its bottom on the airfoil, z = ws_z + 30). The animation lifts it."""
    h = HOOD
    y0, y1 = h["sash_y"]
    xs0, xs1 = -h["W"] / 2 + h["post"] - 10, h["W"] / 2 - h["post"] + 10
    zb = h["ws_z"] + 30
    zt = zb + h["sash_h"]
    frame = merge([box(xs0, y0, zb, xs1, y1, zb + 50), box(xs0, y0, zt - 30, xs1, y1, zt),
                   box(xs0, y0, zb, xs0 + 30, y1, zt), box(xs1 - 30, y0, zb, xs1, y1, zt)])
    handle = box(-500, y0 - 22, zb + 12, 500, y0, zb + 32)
    return {"sash frame": entry(merge([frame, handle]), "sash_frame"),
            "sash glass": entry(box(xs0 + 30, y0 + 6, zb + 50, xs1 - 30, y1 - 6, zt - 30), "sash_glass")}


def build_bench(w=1500.0, d=760.0, h=915.0, sink=False) -> dict:
    """A lab bench with an epoxy top and cabinets, front edge at y = 0, centred on x = 0."""
    e = {}
    e["bench cabinets"] = entry(merge([box(-w / 2 + 10, 50, 100, w / 2 - 10, d - 30, h - 30),
                                       box(-w / 2 + 40, 90, 0, w / 2 - 40, d - 40, 100)]), "cabinet")
    n = 3
    doors, handles = [], []
    for i in range(n):
        a = -w / 2 + 20 + i * (w - 40) / n
        b = a + (w - 40) / n - 12
        doors.append(box(a, 44, 120, b, 50, h - 50))
        handles.append(box((a + b) / 2 - 30, 34, h - 150, (a + b) / 2 + 30, 44, h - 130))
    e["bench doors"] = entry(merge(doors), "hood_enamel")
    e["bench handles"] = entry(merge(handles), "cab_handle")
    e["bench top"] = entry(box(-w / 2, -10, h - 30, w / 2, d, h), "epoxy")
    return e


def build_table(w=1520.0, d=760.0, h=760.0) -> dict:
    """A steel-frame lab table (CB 154's OT-2 table is not measured: a common 30 in table)."""
    legs = [box(sx * (w / 2 - 50) - 25, sy, 0, sx * (w / 2 - 50) + 25, sy + 50, h - 30)
            for sx in (-1, 1) for sy in (30, d - 80)]
    rail = [box(-w / 2 + 40, 40, 120, w / 2 - 40, 70, 160), box(-w / 2 + 40, d - 90, 120, w / 2 - 40, d - 60, 160)]
    return {"table frame": entry(merge(legs + rail), "steel"),
            "table top": entry(box(-w / 2, 0, h - 30, w / 2, d, h), "epoxy")}


def build_room(x0, x1, y0, y1, height, floor_mat, wall_mat, door_x=None, door_side="left") -> dict:
    """A cut-away room: floor, back wall and one side wall (the viewer looks in from the front right)."""
    e = {"room floor": entry(box(x0, y0, -20, x1, y1, 0), floor_mat),
         "room back wall": entry(box(x0, y1, 0, x1, y1 + 120, height), wall_mat),
         "room side wall": entry(box(x0 - 120, y0, 0, x0, y1 + 120, height), wall_mat)}
    if door_x is not None:
        e["room door"] = entry(box(x0 + 2, door_x - 460, 0, x0 + 14, door_x + 460, 2130), "door_wood")
    return e


# ---- containers ------------------------------------------------------------------------------------
def reagent_bottle(kind: str = "hdpe", d: float = 70.0, h: float = 120.0, cap_d: float = 58.0, cap_h: float = 26.0,
                   band: str | None = None, fill: float = 0.55, contents: str = "powder") -> dict:
    """Wide-mouth reagent bottle standing on z = 0: body, contents, label, band, and its cap (separate, to unscrew)."""
    mat = "amber" if kind == "amber" else "hdpe"
    r = d / 2
    neck = cap_d / 2 - 2
    body = merge([cyl(0, 0, 0, r, h - 22, res=48), cyl(0, 0, h - 22, neck + 3, 4), cyl(0, 0, h - 18, neck, 18)])
    e = {"body": entry(body, mat)}
    if kind == "amber" and fill > 0:
        e["contents"] = entry(cyl(0, 0, 3, r - 3, (h - 30) * fill), contents)
    e["label"] = entry(ring(0, 0, 0.18 * h, r + 0.6, r - 1, 0.45 * h, res=48), "label_white")
    if band:
        e["band"] = entry(ring(0, 0, 0.18 * h + 0.45 * h - 12, r + 1.0, r - 1, 12, res=48), band)
    e["cap"] = entry(merge([cyl(0, 0, h - 4, cap_d / 2, cap_h, res=48)]), "cap_black" if kind == "amber" else "cap_white")
    return e


def falcon_tube(band: str | None) -> dict:
    """A 15 mL Falcon tube (lab_models conical, standing on z = 0) with a coloured tape band; the cap is separate."""
    m = LW.conical("15ml")
    e = {}
    for p in m.parts:
        e["tube" if p.name == "tube" else "cap"] = entry(to_mesh(p.shape, 0.25), "polypropylene" if p.name == "tube" else "pp_blue")
    if band:
        e["band"] = entry(ring(0, 0, 70, 8.95, 8.4, 14), band)
    return e


TUBE_LEN = 118.8          # Falcon 352096, without cap
TUBE_R_IN = 7.5           # bore near the top (lab_models: od 17.37, wall ~1.2)


def tube_liquid(level_mm: float) -> pv.PolyData:
    """The liquid in a 15 mL tube up to `level_mm` above its tip (cone then cylinder), as one closed solid."""
    cone = 22.48
    pts = [(0, 1.0), (1.0, 1.0), (TUBE_R_IN - 0.4, cone + 0.5), (TUBE_R_IN, max(level_mm, cone + 1)), (0, max(level_mm, cone + 1))]
    if level_mm < cone:
        k = max(level_mm, 1.5)
        pts = [(0, 1.0), (1.0, 1.0), (1.0 + (TUBE_R_IN - 1.4) * (k - 1) / cone, k), (0, k)]
    prof = np.array([[x, 0, z] for x, z in pts])
    line = pv.lines_from_points(prof)
    return line.extrude_rotate(resolution=36, capping=True).triangulate()


def ml_to_level(ml: float) -> float:
    """Height in a 15 mL Falcon tube for a volume (the cone holds ~1.5 mL; 15 mL at the 15 mL mark ~ 102 mm)."""
    if ml <= 1.5:
        return 1.0 + 21.5 * (ml / 1.5) ** (1 / 3)
    return 22.5 + (ml - 1.5) * (102.0 - 22.5) / 13.5


def tub(w=420.0, d=300.0, h=150.0) -> dict:
    """The lidded carrying tub (secondary containment) for walking the closed tubes between buildings."""
    t = 3.0
    walls = merge([box(-w / 2, -d / 2, 0, w / 2, d / 2, t), box(-w / 2, -d / 2, 0, -w / 2 + t, d / 2, h),
                   box(w / 2 - t, -d / 2, 0, w / 2, d / 2, h), box(-w / 2, -d / 2, 0, w / 2, -d / 2 + t, h),
                   box(-w / 2, d / 2 - t, 0, w / 2, d / 2, h)])
    lid = merge([box(-w / 2 - 6, -d / 2 - 6, 0, w / 2 + 6, d / 2 + 6, 8)])
    return {"tub": entry(walls, "tub"), "tub lid": entry(lid, "tub_lid")}


def waste_bottle(kind="barium", h=240.0, d=150.0) -> dict:
    """A 4 L HDPE waste bottle with a yellow hazardous-waste label."""
    return {"body": entry(merge([box(-d / 2, -d / 2, 0, d / 2, d / 2, h - 40), cyl(0, 0, h - 40, 30, 20)]), "hdpe"),
            "label": entry(box(-d / 2 + 15, -d / 2 - 1.5, 50, d / 2 - 15, -d / 2, h - 80), "waste_yellow"),
            "cap": entry(cyl(0, 0, h - 22, 34, 24), "cap_white")}


def wash_bottle() -> dict:
    """A 500 mL squeeze wash bottle for DI water."""
    body = merge([cyl(0, 0, 0, 38, 150), cyl(0, 0, 150, 24, 12)])
    spout = capsule((0, 0, 165), (0, -10, 215), 3.5).merge(capsule((0, -10, 215), (0, -60, 205), 2.5))
    return {"body": entry(body, "hdpe"), "cap": entry(merge([cyl(0, 0, 160, 26, 14), spout]), "plunger"),
            "band": entry(ring(0, 0, 60, 38.6, 37, 16), "band_water")}


def hand_pipette() -> dict:
    """A 100-1000 uL air-displacement pipette, upright, the tip cone at z = 0."""
    return {"body": entry(merge([capsule((0, 0, 90), (0, 0, 230), 13), cyl(0, 0, 20, 5, 75), cyl(0, 0, 0, 2.5, 22),
                                 box(-6, -25, 205, 6, -10, 225)]), "pipette_body"),
            "plunger": entry(merge([cyl(0, 0, 240, 6, 30), cyl(0, 0, 268, 10, 8)]), "plunger"),
            "tip": entry(pv.Cone(center=(0, 0, -30), direction=(0, 0, -1), height=70, radius=4.2, resolution=24).triangulate(), "polypropylene")}


def person(pose: str = "reach") -> dict:
    """A stand-in person, 1750 mm tall, facing +y (towards what they work on): lab coat, goggles, nitrile gloves.
    pose 'reach': both forearms forward at bench height, hands at about z = 1000-1050 and y = 430."""
    e = {}
    e["legs"] = entry(merge([capsule((sx * 95, 0, 90), (sx * 95, 0, 820), 62) for sx in (-1, 1)]), "trousers")
    e["shoes"] = entry(merge([box(sx * 95 - 50, -40, 0, sx * 95 + 50, 150, 70) for sx in (-1, 1)]), "shoes")
    coat = pv.Cylinder(center=(0, 0, 1050), direction=(0, 0, 1), radius=1, height=1, resolution=36).triangulate()
    torso = pv.ParametricEllipsoid(185, 125, 330).translate((0, 0, 1210), inplace=False)
    skirt = pv.Cone(center=(0, 0, 860), direction=(0, 0, 1), height=420, radius=205, resolution=36, capping=True)
    e["coat"] = entry(merge([torso.triangulate(), skirt.triangulate(), capsule((-190, 0, 1440), (190, 0, 1440), 62)]), "coat")
    del coat
    hand_y, hand_z = 430.0, 1040.0 if pose == "reach" else 1000.0
    arms = []
    for sx in (-1, 1):
        sh = (sx * 205, 0, 1430)
        el = (sx * 215, 120, 1110)
        wr = (sx * 120, hand_y - 40, hand_z)
        arms += [capsule(sh, el, 52), capsule(el, wr, 46)]
    e["sleeves"] = entry(merge(arms), "coat")
    e["gloves"] = entry(merge([pv.ParametricEllipsoid(30, 46, 26).translate((sx * 110, hand_y, hand_z), inplace=False)
                               .triangulate() for sx in (-1, 1)]), "nitrile")
    e["neck"] = entry(cyl(0, 0, 1490, 48, 90), "skin")
    e["head"] = entry(pv.ParametricEllipsoid(92, 105, 122).translate((0, 10, 1660), inplace=False).triangulate(), "skin")
    e["hair"] = entry(pv.ParametricEllipsoid(96, 110, 90).translate((0, -10, 1720), inplace=False).triangulate(), "hair")
    e["goggles"] = entry(box(-88, 85, 1650, 88, 125, 1705), "goggles")
    return e


def seal_film() -> pv.PolyData:
    return box(-63, -42, 0, 63, 42, 0.35)


# ------------------------------------------------------------------------------------------ cache
def _hash(*files) -> str:
    h = hashlib.sha256()
    for f in sorted(files):
        h.update(Path(f).read_bytes())
    return h.hexdigest()[:12]


def cached(key: str, build):
    """build() once per version of this file and lab_models; vendor CAD is checked by hash when it's fetched."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{key}_{_hash(HERE / 'models.py', *(HERE / 'lab_models').glob('*.py'))}.pkl"
    if path.exists():
        return pickle.loads(path.read_bytes())
    print(f"building {key} (cached afterwards in {path.name})", flush=True)
    data = build()
    path.write_bytes(pickle.dumps(data))
    return data


def lab_model(fn, *args, tol=0.3, **kw) -> dict:
    """A lab_models Model -> {material: merged entry}."""
    m = fn(*args, **kw)
    by: dict[str, list] = {}
    for p in m.parts:
        by.setdefault(p.material, []).append(to_mesh(p.shape, tol))
    return {mat: entry(merge(ms), mat) for mat, ms in by.items()}


def build_labware() -> dict:
    out = {}
    out["balance"] = lab_model(LW.balance, lid="stock", tol=0.4)
    # the balance's beaker is the doser's: leave it off the pan here
    bal = LW.balance(lid="stock")
    keep = [p for p in bal.parts if p.name not in ("beaker",)]
    lid_names = ("breeze break lid",)
    by: dict[str, list] = {}
    lid: list = []
    for p in keep:
        (lid if p.name in lid_names else by.setdefault(p.material, [])).append(to_mesh(p.shape, 0.4))
    out["balance"] = {mat: entry(merge(ms), mat) for mat, ms in by.items()}
    out["balance_lid"] = {"lid": entry(merge(lid), "pp_white")}
    out["balance_notes"] = bal.notes
    out["plate"] = lab_model(LW.plate, "96_nest")
    out["tiprack"] = lab_model(LW.tiprack, "300ul")
    rack = LW.tube_rack_6()
    out["rack"] = {"rack": entry(to_mesh([p for p in rack.parts if p.name == "rack"][0].shape, 0.4), "pla_white")}
    out["vial"] = lab_model(LW.vial, "20ml")
    out["weigh_boat"] = lab_model(LW.weigh_boat)
    out["spatula"] = lab_model(LW.spoonula)
    out["sensor"] = lab_model(LW.colour_sensor)
    out["tube"] = falcon_tube(None)
    return out


if __name__ == "__main__":
    ot = cached("ot2", build_ot2)
    print("nozzle", ot["nozzle"], "door hinge", ot["door_hinge"])
    lc = cached("lidcam", build_lidcam)
    print("lid camera parts", list(lc))
    lw = cached("labware", build_labware)
    print("labware", list(lw), lw["balance_notes"])
