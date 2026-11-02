"""The two rooms and everything in them, as groups of PyVista actors in a viz3d Scene.

EB B125 (Chris Dillon's lab, the fume hood) is on the left, with the hood at the origin. CB 154 (the Vertical Cloud
Lab, the OT-2) is on the right, centred on x = CB_X. They are in different buildings; the gap between them stands for
the walk. Every object is its own group, placed by a 4 x 4 matrix, so a step moves it by changing that matrix; caps,
lids, the sash, the door, the gantry and the pipette are child groups of what they belong to.
"""
from __future__ import annotations

import math

import numpy as np
import pyvista as pv

import models as M
from scene import R, T, lighter

CB_X = 6200.0                         # CB 154's origin, world x
OT2_AT = (CB_X - 150.0, 420.0, 760.0)  # the OT-2's footprint centre on its table
BENCH_EB = (1572.0, 0.0)              # the bench beside the hood (centre x, front y)
BENCH_CB = (CB_X + 1350.0, 0.0)       # the side bench in CB 154
WS = M.HOOD["ws_z"]                   # hood work surface
BT = 915.0                            # bench tops
TT = 760.0                            # the OT-2 table top

# 15 mL stock tubes: (key, label, band, mL at the start)
TUBES = [("ba0", "0.1 M BaCl2", "band_ba"), ("ba1", "10 mM BaCl2", "band_ba"), ("ba2", "1 mM BaCl2", "band_ba"),
         ("ba3", "0.1 mM BaCl2", "band_ba"), ("so0", "0.1 M Na2SO4", "band_so4"), ("so1", "10 mM Na2SO4", "band_so4"),
         ("so2", "1 mM Na2SO4", "band_so4"), ("so3", "0.1 mM Na2SO4", "band_so4"), ("nacl", "5 M NaCl", "band_nacl"),
         ("water", "DI water", "band_water")]
RACK_HOLES = [(-35.0, 17.5), (0.0, 17.5), (35.0, 17.5), (-35.0, -17.5), (0.0, -17.5), (35.0, -17.5)]   # labware.tube_rack_6
TUBE_Z_IN_RACK = 4.0
# where each tube sits: the hood's rack (barium) and the bench's rack (sulfate, NaCl, water). The racks are the AC
# 6-tube OT-2 racks, so they travel in the tub and go onto the deck as they are: hood rack -> slot 4, bench rack -> 5.
RACK_OF = {"ba0": ("rack_hood", 0), "ba1": ("rack_hood", 1), "ba2": ("rack_hood", 2), "ba3": ("rack_hood", 3),
           "so0": ("rack_bench", 0), "so1": ("rack_bench", 1), "so2": ("rack_bench", 2), "so3": ("rack_bench", 3),
           "nacl": ("rack_bench", 4), "water": ("rack_bench", 5)}

PLATE_WELL_R = 3.48
WELL_BOTTOM = 3.4                     # NEST 200 uL flat: 14.3 tall, wells 10.9 deep


def well_xy(r: int, c: int) -> tuple[float, float]:
    """Well centre in the plate's frame (A1 at the back left), from labware._grid."""
    return -127.76 / 2 + 14.38 + c * 9.0, 85.48 / 2 - 11.24 - r * 9.0


class World:
    def __init__(self, S, ot2=True, eb=True, cb=True):
        self.S = S
        self.base: dict[str, np.ndarray] = {}
        self.ot = M.cached("ot2", M.build_ot2)
        self.lc = M.cached("lidcam", M.build_lidcam)
        self.lw = M.cached("labware", M.build_labware)
        self.tube_level: dict[str, float] = {}
        if eb:
            self.build_eb()
        if cb:
            self.build_cb()
        self.build_people()
        self.build_tubes()

    # ------------------------------------------------------------------------------------- helpers
    def put(self, group, entries: dict, M4=None, parent=None, prefix=None, shown=True, opacity_scale=1.0):
        S = self.S
        prefix = prefix or group
        for n, e in entries.items():
            if not isinstance(e, dict) or "mesh" not in e:
                continue
            S.add(f"{prefix}:{n}", e["mesh"], e["color"], group=group, opacity=e["opacity"] * opacity_scale,
                  shown=shown, specular=e["specular"])
        if parent:
            S.parent[group] = parent
        S.gmat[group] = np.eye(4) if M4 is None else M4
        self.base[group] = S.gmat[group].copy()

    def set(self, group, M4):
        self.S.gmat[group] = M4

    def show(self, group, a=1.0):
        for n in self.S.members(group):
            self.S.alpha[n] = a

    def parent_world(self, group) -> np.ndarray:
        p = self.S.parent.get(group)
        return self.S.world(p) if p else np.eye(4)

    def set_world(self, group, Mw):
        """Pose a group by its world matrix, whatever its parent."""
        self.S.gmat[group] = np.linalg.inv(self.parent_world(group)) @ Mw

    def reparent(self, group, new_parent):
        Mw = self.S.world(group)
        if new_parent:
            self.S.parent[group] = new_parent
        else:
            self.S.parent.pop(group, None)
        self.set_world(group, Mw)

    def world_of(self, group, local=(0, 0, 0)) -> np.ndarray:
        m = self.S.world(group)
        return (m @ np.array([*local, 1.0]))[:3]

    # ------------------------------------------------------------------------------------- EB B125
    def build_eb(self):
        S = self.S
        self.put("eb_room", M.build_room(-1900, 2900, -2600, 880, 2800, "floor_eb", "wall_eb", door_x=-1500))
        S.add("eb_sign", M.text3d("EB B125", 1100, 875, 2050, 300, depth=8), M.MATS["sign"][:3],
              group="eb_room")
        self.put("hood", M.build_hood())
        self.put("sash", M.build_sash(), parent="hood")
        self.put("bench_eb", M.build_bench(1500, 760, BT), T((BENCH_EB[0], BENCH_EB[1], 0)))
        # zones: inside the hood (red), next to the hood (amber)
        h = M.HOOD
        xi = h["W"] / 2 - h["post"]
        S.add("zone_in", M.box(-xi + 4, 70, WS + 1, xi - 4, h["baffle_y"] - 4, h["open_top"] - 4), M.MATS["zone_in"][:3],
              group="zones_eb", opacity=M.MATS["zone_in"][3], shown=False, specular=0.0)
        S.add("zone_next", M.box(822, -10, BT + 1, 1640, 760, BT + 420), M.MATS["zone_next"][:3], group="zones_eb",
              opacity=M.MATS["zone_next"][3], shown=False, specular=0.0)
        S.add("zone_next_floor", M.box(822, -900, 1, 1640, -10, 6), M.MATS["zone_next"][:3], group="zones_eb",
              opacity=0.35, shown=False, specular=0.0)
        S.add("zone_in_floor", M.box(-700, -900, 1, 700, -10, 6), M.MATS["zone_in"][:3], group="zones_eb",
              opacity=0.30, shown=False, specular=0.0)
        S.gmat["zones_eb"] = np.eye(4)
        # the balance beside the hood, its breeze-break lid separate
        self.put("balance", self.lw["balance"], T((1040, 300, BT)))
        self.put("balance_lid", self.lw["balance_lid"], parent="balance")
        self.pan = (0.0, -131.0 + 168.5, 86.5)          # pan centre in the balance's frame
        # inside the hood, hidden until the hood is set up: liner, tray, waste, wash bottle, barium chloride, rack
        self.put("liner", {"pad": M.entry(M.box(-460, 250, WS, 460, 730, WS + 1.5), "liner_pad")}, shown=False)
        tray = M.merge([M.box(-420, 270, WS + 1.5, 420, 700, WS + 4), M.box(-420, 270, WS + 1.5, -414, 700, WS + 40),
                        M.box(414, 270, WS + 1.5, 420, 700, WS + 40), M.box(-420, 270, WS + 1.5, 420, 276, WS + 40),
                        M.box(-420, 694, WS + 1.5, 420, 700, WS + 40)])
        self.put("tray", {"tray": M.entry(tray, "tray_grey")}, shown=False)
        self.put("ba_waste", M.waste_bottle(), T((540, 600, WS)), shown=False)
        self.put("wash_hood", M.wash_bottle(), T((300, 610, WS + 4)), shown=False)
        bacl2 = M.reagent_bottle("amber", 72, 125, 56, 24, band="band_ba", fill=0.5)
        self.put("bacl2", {k: v for k, v in bacl2.items() if k != "cap"}, T((-290, 560, WS + 4)), shown=False)
        self.put("bacl2_cap", {"cap": bacl2["cap"]}, parent="bacl2", shown=False)
        self.put("rack_hood", self.lw["rack"], T((120, 470, WS + 4)), shown=False)
        self.put("spatula", self.lw["spatula"], T((-120, 360, WS + 4)) @ R((0, 0, 1), 20), shown=False)
        # weighing vial (20 mL, capped) starts on the bench by the balance
        vial = self.lw["vial"]
        self.put("vial", {"glass": vial["glass"]}, T((1240, 520, BT)))
        self.put("vial_cap", {"cap": vial["pp_black"]}, parent="vial")
        S.add("vial_powder", M.cyl(0, 0, 1.6, 12.3, 1.0), M.MATS["powder"][:3], group="vial", shown=False, specular=0.05)
        S.add("vial_liquid", M.cyl(0, 0, 1.6, 12.4, 1.0), M.MATS["solution"][:3], group="vial", opacity=0.5,
              shown=False, specular=0.6)
        # on the bench: sodium sulfate and sodium chloride bottles, weigh boats, a funnel, the bench rack, the tub
        so4 = M.reagent_bottle("hdpe", 78, 135, 60, 26, band="band_so4")
        nacl = M.reagent_bottle("hdpe", 84, 150, 62, 28, band="band_nacl")
        self.put("na2so4", {k: v for k, v in so4.items() if k != "cap"}, T((1330, 560, BT)))
        self.put("na2so4_cap", {"cap": so4["cap"]}, parent="na2so4")
        self.put("nacl_b", {k: v for k, v in nacl.items() if k != "cap"}, T((1450, 560, BT)))
        self.put("nacl_cap", {"cap": nacl["cap"]}, parent="nacl_b")
        self.put("boat", self.lw["weigh_boat"], T((1180, 180, BT)))
        S.add("boat_powder", M.cyl(0, 0, 0.6, 9.0, 1.0), M.MATS["powder"][:3], group="boat", shown=False, specular=0.05)
        self.put("spatula2", self.lw["spatula"], T((1300, 200, BT)) @ R((0, 0, 1), -10))
        funnel = pv.Cone(center=(0, 0, 0), direction=(0, 0, -1), height=40, radius=30, resolution=36, capping=False)
        funnel = M.merge([funnel.translate((0, 0, 40), inplace=False).triangulate(), M.cyl(0, 0, 0, 4, 22)])
        self.put("funnel", {"f": M.entry(funnel, "polypropylene")}, T((1560, 180, BT)), shown=True)
        self.put("rack_bench", self.lw["rack"], T((1700, 330, BT)))
        self.put("wash_bench", M.wash_bottle(), T((1880, 560, BT)))
        self.put("tub", {"tub": M.tub()["tub"]}, T((2120, 300, BT)))
        self.put("tub_lid", {"lid": M.tub()["tub lid"]}, T((0, 0, 150)), parent="tub")
        self.put("notebook", {"n": M.entry(M.box(-150, -110, 0, 150, 110, 12), "label_white"),
                              "c": M.entry(M.box(-150, -110, 12, -130, 110, 14), "sign")},
                 T((1560, 620, BT)) @ R((0, 0, 1), 8))
        self.put("pipette_h", M.hand_pipette(), T((380, 380, WS + 4)), shown=False)

    # ------------------------------------------------------------------------------------- CB 154
    def build_cb(self):
        S = self.S
        self.put("cb_room", M.build_room(CB_X - 1500, CB_X + 2600, -2600, 880, 2800, "floor_cb", "wall_cb", door_x=-1500))
        S.add("cb_sign", M.text3d("CB 154", CB_X + 700, 875, 2050, 300, depth=8),
              M.MATS["sign"][:3], group="cb_room")
        self.put("table_cb", M.build_table(1520, 760, TT), T((OT2_AT[0], 40, 0)))
        self.put("bench_cb", M.build_bench(1200, 760, BT), T((BENCH_CB[0], BENCH_CB[1], 0)))
        S.add("zone_cb", M.box(OT2_AT[0] - 330, OT2_AT[1] - 300, TT + 1, OT2_AT[0] + 330, OT2_AT[1] + 300, TT + 680),
              M.MATS["zone_cb"][:3], group="zones_cb", opacity=M.MATS["zone_cb"][3], shown=False, specular=0.0)
        S.add("zone_cb_floor", M.box(OT2_AT[0] - 700, -900, 1, BENCH_CB[0] + 600, -10, 6), M.MATS["zone_cb"][:3],
              group="zones_cb", opacity=0.30, shown=False, specular=0.0)
        S.gmat["zones_cb"] = np.eye(4)
        # the OT-2 (vendor STEP) and the lid camera (byu-vcl PR 234)
        ot = self.ot
        self.put("ot2", {**ot["frame"], **ot["glass"]}, T(OT2_AT))
        self.put("ot2_door", ot["door"], parent="ot2")
        self.put("ot2_beam", ot["beam"], parent="ot2")
        self.put("ot2_head", ot["head"], parent="ot2")
        self.put("ot2_pip", ot["pipette"], parent="ot2_head")
        S.add("ot2_tip", pv.Cone(center=(0, 0, 0), direction=(0, 0, -1), height=51.0, radius=2.9, resolution=24)
              .translate((0, 0, -25.5), inplace=False).triangulate(), M.MATS["polypropylene"][:3], group="ot2_tipg",
              shown=False, specular=0.2)
        S.parent["ot2_tipg"] = "ot2_pip"
        S.gmat["ot2_tipg"] = T(ot["nozzle"])
        self.nozzle = ot["nozzle"]
        self.put("lidcam", self.lc, parent="ot2")
        # field of view, lens to the plate (about 140 x 105 mm at the plate, ~200 px per well)
        x7, y7 = M.slot_centre(7)
        lens = M.deck(x7, y7, 643.8 - 53.55 + 11.5)
        tgt = M.deck(x7, y7, 14.6)
        pyr = pv.Pyramid([(tgt[0] - 70, tgt[1] - 52, tgt[2]), (tgt[0] + 70, tgt[1] - 52, tgt[2]),
                          (tgt[0] + 70, tgt[1] + 52, tgt[2]), (tgt[0] - 70, tgt[1] + 52, tgt[2]), tuple(lens)])
        S.add("fov", pyr.extract_surface(algorithm="dataset_surface").triangulate(), (1.0, 0.82, 0.2), group="fov", opacity=0.20, shown=False,
              specular=0.0)
        S.parent["fov"] = "ot2"
        S.gmat["fov"] = np.eye(4)
        self.lens = lens
        # fixed parts of the deck as found: colour sensor parked in slot 10 on its base
        x10, y10 = M.slot_centre(10)
        base = {"b": M.entry(M.box(-60, -40, 0, 60, 40, 22), "pla_grey")}
        self.put("sensor_base", base, T(M.deck(x10, y10, 0)), parent="ot2")
        self.put("sensor", self.lw["sensor"], T(M.deck(x10, y10, 22)), parent="ot2")
        # labware, hidden until it goes on: black paper and plate (slot 7), tips (slot 6), two racks (slots 4, 5)
        self.put("paper", {"p": M.entry(M.box(-66, -45, 0, 66, 45, 0.3), "black_paper")}, T(M.deck(x7, y7, 0)),
                 parent="ot2", shown=False)
        self.put("plate", self.lw["plate"], T(M.deck(x7, y7, 0.3)), parent="ot2", shown=False)
        lid = M.box(-64.7, -43.5, 9.0, 64.7, 43.5, 10.0).merge(M.box(-64.7, -43.5, 4.0, -63.7, 43.5, 10.0))
        self.put("plate_lid", {"l": M.entry(lid, "polystyrene")}, parent="plate", shown=False)
        self.put("seal", {"s": M.entry(M.seal_film(), "seal")}, T((0, 0, 14.35)), parent="plate", shown=False)
        for r in range(8):
            for c in range(12):
                x, y = well_xy(r, c)
                S.add(f"well_{r}_{c}", M.cyl(x, y, WELL_BOTTOM, PLATE_WELL_R - 0.15, 1.0, res=20), M.MATS["solution"][:3],
                      group="wells", opacity=0.55, shown=False, specular=0.5)
        S.parent["wells"] = "plate"
        S.gmat["wells"] = np.eye(4)
        x6, y6 = M.slot_centre(6)
        self.put("tiprack", self.lw["tiprack"], T(M.deck(x6, y6, 0)), parent="ot2", shown=False)
        tlid = M.merge([M.box(-64.5, -43.4, 66.0, 64.5, 43.4, 67.5), M.box(-64.5, -43.4, 50.0, -63.5, 43.4, 67.5),
                        M.box(63.5, -43.4, 50.0, 64.5, 43.4, 67.5), M.box(-64.5, -43.4, 50.0, 64.5, -42.4, 67.5),
                        M.box(-64.5, 42.4, 50.0, 64.5, 43.4, 67.5)])
        self.put("tiprack_lid", {"l": M.entry(tlid, "acrylic")}, parent="tiprack", shown=False)
        # side bench: a wipe for the caps, the barium waste for the end of the run, a laptop with the stream
        self.put("wipe", {"w": M.entry(M.box(-160, -110, 0, 160, 110, 0.8), "wipe")}, T((BENCH_CB[0] - 280, 260, BT)))
        self.put("ba_waste_cb", M.waste_bottle(), T((BENCH_CB[0] + 420, 560, BT)))
        lap = M.merge([M.box(-170, -120, 0, 170, 120, 14)])
        scr = M.box(-165, 0, 0, 165, 6, 220).rotate_x(-15, point=(0, 120, 14), inplace=False).translate((0, 114, 14), inplace=False)
        self.put("laptop", {"b": M.entry(lap, "laptop"), "s": M.entry(scr, "screen")}, T((BENCH_CB[0] + 80, 520, BT)))

    # ------------------------------------------------------------------------------------- people
    def build_people(self):
        p = M.person()
        self.put("person", p, T((0, -280, 0)))

    # ------------------------------------------------------------------------------------- stock tubes
    def build_tubes(self):
        """The ten 15 mL tubes, each with a liquid actor and a separate cap. They start empty and hidden."""
        S = self.S
        tube = self.lw["tube"]
        for key, _, band in TUBES:
            g = f"t_{key}"
            ent = {"tube": tube["tube"], "band": M.entry(M.ring(0, 0, 70, 8.95, 8.4, 14), band)}
            rack, hole = RACK_OF[key]
            hx, hy = RACK_HOLES[hole]
            self.put(g, ent, T((hx, hy, TUBE_Z_IN_RACK)), parent=rack if rack in self.S.gmat else None, shown=False)
            S.add(f"{g}:liquid", M.tube_liquid(5), M.MATS["solution"][:3], group=g, opacity=0.5, shown=False, specular=0.6)
            self.put(f"{g}_cap", {"cap": tube["cap"]}, parent=g, shown=False)
            self.tube_level[key] = 0.0

    def tube_fill(self, key, ml):
        self.tube_level[key] = ml
        if ml <= 0.01:
            self.S.alpha[f"t_{key}:liquid"] = 0.0
            return
        self.S.set_mesh(f"t_{key}:liquid", M.tube_liquid(M.ml_to_level(ml)))
        self.S.alpha[f"t_{key}:liquid"] = self.S.alpha[f"t_{key}:tube"]

    def tube_show(self, key, a=1.0):
        self.show(f"t_{key}", a)
        self.show(f"t_{key}_cap", a)
        if self.tube_level[key] <= 0.01:
            self.S.alpha[f"t_{key}:liquid"] = 0.0


def rack_pose(rack_group_world: np.ndarray, hole: int) -> np.ndarray:
    hx, hy = RACK_HOLES[hole]
    return rack_group_world @ T((hx, hy, TUBE_Z_IN_RACK))


def arc(p0, p1, u, lift=120.0) -> np.ndarray:
    """A carried move from p0 to p1: up, across, down (u eased 0 -> 1)."""
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    p = p0 + (p1 - p0) * u
    p[2] += lift * 4 * u * (1 - u)
    return p


def lerp_m(M0, M1, u) -> np.ndarray:
    """Blend two rigid poses: positions linearly, rotations by the angle about their relative axis."""
    from scipy.spatial.transform import Rotation, Slerp
    u = float(min(max(u, 0.0), 1.0))
    r = Rotation.from_matrix(np.stack([M0[:3, :3], M1[:3, :3]]))
    s = Slerp([0, 1], r)
    out = np.eye(4)
    out[:3, :3] = s([u]).as_matrix()[0]
    out[:3, 3] = M0[:3, 3] + (M1[:3, 3] - M0[:3, 3]) * u
    return out


def carry(M0, M1, u, lift=120.0) -> np.ndarray:
    m = lerp_m(M0, M1, u)
    m[2, 3] += lift * 4 * u * (1 - u)
    return m


def cap_off(u, cap_top_z, dx=70.0, dy=-40.0, flip=True, turns=1.5) -> np.ndarray:
    """A cap unscrewing (turns, lifting 8 mm), then set down top-down beside its container, in the container's frame.
    cap_top_z: height of the cap's top above the container's base."""
    a = min(u / 0.35, 1.0)
    b = max((u - 0.35) / 0.65, 0.0)
    spin = R((0, 0, 1), -360 * turns * a)
    up = T((0, 0, 8 * a))
    if b <= 0:
        return up @ spin
    pivot = (0, 0, cap_top_z - 6)
    flipm = R((1, 0, 0), 180 * b, pivot) if flip else np.eye(4)
    # down to the surface: a flipped cap's top lands at z = 0; centre it at (dx, dy)
    drop = -(cap_top_z - 12.0 + 8.0) * b if flip else -8.0 * b
    lift = 60.0 * 4 * b * (1 - b)
    return T((dx * b, dy * b, 8 + drop + lift)) @ flipm @ spin
