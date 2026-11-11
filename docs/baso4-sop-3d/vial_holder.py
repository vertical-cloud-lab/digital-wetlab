#!/usr/bin/env python3
"""A printed holder that puts six 20 mL vials in one OT-2 deck slot, and its Opentrons labware definition.

Asked on PR 84 by @sgbaird (2026-11-06): the stocks go in the vials the lab already uses, in a holder that sits in an
OT-2 slot, two holders for the ten stocks.

The vials are the 20 mL clear VOA vials in the electromagnetic capper's bill of materials (byu-vcl
``modules/electromagnetic-capper/BOM.md``, item 11: Fisher 12-100-112, 24-400 open-top caps with septa), the ones in
the CubXL's 9-vial holder and stirrer. Fisher lists that family at 28 x 57 mm. @timothy-commins calipered the lab's
vials at **27 mm** across (PR 84, 2026-11-11), and that is the default here. The height is still Fisher's 57 mm until
someone measures it. ``VIAL`` below is the one place the size is set: the pockets, the labware definition, the exports
and the vials in the animation (``models.py``, ``world.py``) all follow it.

    python3 vial_holder.py                       # writes cad/: STEP, STL, the labware JSON and a render
    python3 vial_holder.py --od 27.0 --height 57.4   # a one-off rebuild of cad/ only; change VIAL for the animation too

The holder: the ANSI/SLAS footprint (127.76 x 85.48 mm, 3.18 mm corners) so the slot's corner clips locate it, 23 mm
tall, six round pockets 20 mm deep in 3 columns x 2 rows on a 40 mm pitch (A1 at the back left, as on a plate), each
1.2 mm wider than the vial with a 1.5 mm lead-in chamfer, and the A1 corner cut off like a plate's so it only goes in
one way round. The 13 mm between vials leaves room for gloved fingers on the caps. Print it upright, no supports.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import cadquery as cq

HERE = Path(__file__).resolve().parent
CAD = HERE / "cad"

SBS_W, SBS_D, SBS_R = 127.76, 85.48, 3.18      # ANSI/SLAS 1-2004 footprint and corner radius
# the vial: 20 mL clear VOA (Fisher 12-100-112 family, listed at 28 x 57 mm), 24-400 cap. OD: the lab's vials, calipered
# at 27 mm (PR 84, 2026-11-11). Height: Fisher's, not yet measured. Inside (assumed): 1.2 mm wall, 1.5 mm base.
VIAL = dict(od=27.0, height=57.0, wall=1.2, base=1.5, neck_id=20.0, cap_od=27.8, cap_over=3.0, volume_ul=20000)
HOLDER = dict(cols=3, rows=2, pitch_x=40.0, pitch_y=40.0, height=23.0, floor=3.0, clearance=1.2, chamfer=1.5,
              a1_notch=5.0, label_depth=0.6)
LOAD_NAME = "byuvcl_6_vialholder_20ml"


def pockets(h=HOLDER) -> list[tuple[str, float, float]]:
    """(well, x, y) of each pocket, from the holder's centre: rows A (back, +y) to B, columns 1-3 left to right."""
    out = []
    for r in range(h["rows"]):
        for c in range(h["cols"]):
            x = (c - (h["cols"] - 1) / 2) * h["pitch_x"]
            y = ((h["rows"] - 1) / 2 - r) * h["pitch_y"]
            out.append((f"{'AB'[r]}{c + 1}", x, y))
    return out


def holder(v=VIAL, h=HOLDER, text=True) -> cq.Workplane:
    """The holder as one solid, its underside at z = 0 and centred on its footprint."""
    H = h["height"]
    d = v["od"] + h["clearance"]
    depth = H - h["floor"]
    blk = cq.Workplane("XY").rect(SBS_W, SBS_D).extrude(H).edges("|Z").fillet(SBS_R).edges(">Z").chamfer(0.8)
    # A1 corner (back left) cut off, as on a plate, so it can only go in one way round
    n = h["a1_notch"]
    notch = (cq.Workplane("XY").polyline([(0, 0), (n, 0), (0, -n)]).close().extrude(H + 2)
             .translate((-SBS_W / 2 - 0.01, SBS_D / 2 + 0.01, -1)))
    blk = blk.cut(notch)
    for _, x, y in pockets(h):
        blk = blk.cut(cq.Workplane("XY").circle(d / 2).extrude(depth + 1).translate((x, y, h["floor"])))
        lead = (cq.Workplane("XY").circle(d / 2).workplane(offset=h["chamfer"]).circle(d / 2 + h["chamfer"]).loft()
                .translate((x, y, H - h["chamfer"])))
        blk = blk.cut(lead)
    if text:
        try:
            blk = _engrave(blk, v, h)
        except Exception as exc:                      # no usable font: the holder is the same without the labels
            print(f"labels skipped ({exc})")
    return blk


def _engrave(blk: cq.Workplane, v=VIAL, h=HOLDER) -> cq.Workplane:
    H, dep = h["height"], h["label_depth"]
    px, py = h["pitch_x"], h["pitch_y"]
    xm = -SBS_W / 2 + (SBS_W / 2 - (h["cols"] - 1) / 2 * px - (v["od"] + h["clearance"]) / 2) / 2
    ym = -SBS_D / 2 + (SBS_D / 2 - (h["rows"] - 1) / 2 * py - (v["od"] + h["clearance"]) / 2) / 2
    marks = [("A", xm, py / 2), ("B", xm, -py / 2)] + [(str(c + 1), (c - 1) * px, ym) for c in range(h["cols"])]
    for s, x, y in marks:
        t = cq.Workplane("XY").text(s, 5.0, -dep, combine=False, halign="center", valign="center").translate((x, y, H))
        blk = blk.cut(t)
    face = (cq.Workplane("XZ").text("20 mL VOA x6   BYU VCL", 5.0, -dep, combine=False, halign="center",
                                    valign="center").translate((0, -SBS_D / 2, H / 2)))
    return blk.cut(face)


def labware(v=VIAL, h=HOLDER) -> dict:
    """Opentrons labware definition (schema 2) for the holder with uncapped vials in it."""
    top = h["floor"] + v["height"]
    bottom = h["floor"] + v["base"]
    wells, cols = {}, {}
    for name, x, y in pockets(h):
        wells[name] = {"depth": round(top - bottom, 2), "totalLiquidVolume": v["volume_ul"], "shape": "circular",
                       "diameter": v["neck_id"], "x": round(SBS_W / 2 + x, 2), "y": round(SBS_D / 2 + y, 2),
                       "z": round(bottom, 2)}
        cols.setdefault(name[1:], []).append(name)
    ordering = [cols[k] for k in sorted(cols, key=int)]
    return {
        "ordering": ordering,
        "brand": {"brand": "BYU Vertical Cloud Lab", "brandId": [LOAD_NAME]},
        "metadata": {"displayName": f"BYU VCL 6-vial holder, 20 mL VOA vials ({v['od']:g} x {v['height']:g} mm), "
                                    "uncapped", "displayCategory": "tubeRack", "displayVolumeUnits": "mL", "tags": []},
        "dimensions": {"xDimension": SBS_W, "yDimension": SBS_D, "zDimension": round(top, 2)},
        "wells": wells,
        "groups": [{"metadata": {"displayName": "20 mL VOA vials", "displayCategory": "tubeRack",
                                 "wellBottomShape": "flat"},
                    "brand": {"brand": "Fisher Scientific", "brandId": ["12-100-112"]},
                    "wells": [w for col in ordering for w in col]}],
        "parameters": {"format": "irregular", "quirks": [], "isTiprack": False, "isMagneticModuleCompatible": False,
                       "loadName": LOAD_NAME},
        "namespace": "custom_beta", "version": 1, "schemaVersion": 2,
        "cornerOffsetFromSlot": {"x": 0, "y": 0, "z": 0},
    }


def vial_level(ml: float, v=VIAL) -> float:
    """Liquid height above the vial's outside bottom for a volume in mL (straight body, flat base)."""
    r = v["od"] / 2 - v["wall"]
    return v["base"] + ml * 1000.0 / (math.pi * r * r)


def vial_model(v=VIAL):
    """lab_models' 20 mL vial (glass and cap) at this vial's size. ``lab_models/labware.py`` is a verbatim copy from
    byu-vcl, and its "20ml" vial is Fisher's 28 x 57 mm, so the measured size goes in as a new entry instead."""
    import sys
    sys.path.insert(0, str(HERE / "lab_models"))
    import labware as LW
    LW.VIALS["20ml_vcl"] = dict(LW.VIALS["20ml"], od=v["od"], h=v["height"], wall=v["wall"], base=v["base"],
                                cap_od=v["cap_od"], cap_over=v["cap_over"],
                                title=f"20 mL VOA vial ({v['od']:g} x {v['height']:g} mm), 24-400 cap")
    return LW.vial("20ml_vcl")


def export(v=VIAL, h=HOLDER):
    CAD.mkdir(exist_ok=True)
    shape = holder(v, h)
    stem = CAD / "vial_holder_20ml_x6"
    cq.exporters.export(shape, str(stem.with_suffix(".step")))
    cq.exporters.export(shape, str(stem.with_suffix(".stl")), tolerance=0.05, angularTolerance=0.1)
    lw = CAD / LOAD_NAME
    lw.mkdir(exist_ok=True)
    (lw / "1.json").write_text(json.dumps(labware(v, h), indent=2) + "\n")
    bb = shape.val().BoundingBox()
    print(f"holder {bb.xlen:.2f} x {bb.ylen:.2f} x {bb.zlen:.2f} mm, volume {shape.val().Volume() / 1000:.1f} cm3; "
          f"vial top {h['floor'] + v['height']:.1f} mm above the deck, 15 mL at {vial_level(15.0, v):.1f} mm")
    return shape


def render(shape, v=VIAL, h=HOLDER):
    """A still of the holder with six capped vials, for the README."""
    import numpy as np
    import pyvista as pv

    def mesh(s, tol=0.2):
        s = s.val() if isinstance(s, cq.Workplane) else s
        vs, ts = s.tessellate(tol, 0.2)
        # point normals only: with cell normals as well, VTK 9.6 (pyvista 0.49) renders these meshes unlit, near-black
        return pv.PolyData(np.array([(p.x, p.y, p.z) for p in vs]), np.hstack([[3, *t] for t in ts])).compute_normals(
            split_vertices=True, feature_angle=35, cell_normals=False)
    pl = pv.Plotter(off_screen=True, window_size=(1400, 900))
    pl.set_background("white")
    pl.add_mesh(mesh(shape), color=(0.10, 0.55, 0.55), specular=0.3)
    vm = vial_model(v)
    for i, (name, x, y) in enumerate(pockets(h)):
        if i == 4:
            continue                                   # one pocket left empty to show it
        for p in vm.parts:
            m = mesh(p.shape).translate((x, y, h["floor"]), inplace=False)
            if p.name == "glass":
                pl.add_mesh(m, color=(0.80, 0.90, 0.95), opacity=0.35, specular=0.9)
                lv = vial_level(15.0, v) - v["base"]
                pl.add_mesh(pv.Cylinder(center=(x, y, h["floor"] + v["base"] + lv / 2), direction=(0, 0, 1),
                                        radius=v["od"] / 2 - v["wall"] - 0.2, height=lv), color=(0.62, 0.80, 0.97),
                            opacity=0.5)
            else:
                pl.add_mesh(m, color=(0.09, 0.09, 0.10), specular=0.3)
        pl.add_point_labels([(x - 17, y + 15, h["floor"] + v["height"] + 8)], [name], font_size=22, text_color="black",
                            shape=None, show_points=False, always_visible=True)
    pl.camera_position = [(170, -260, 230), (0, 0, 22), (0, 0, 1)]
    pl.enable_anti_aliasing()
    pl.screenshot(str(CAD / "vial_holder_20ml_x6.png"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--od", type=float, default=VIAL["od"], help="vial outside diameter, mm (caliper it)")
    ap.add_argument("--height", type=float, default=VIAL["height"], help="vial height without its cap, mm")
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()
    vv = dict(VIAL, od=a.od, height=a.height)
    s = export(vv)
    if not a.no_render:
        render(s, vv)
