#!/usr/bin/env python3
"""3-D animated SOP for the barium sulfate plate run (issue 80): from the bottles to 72 h of monitoring.

Four chapters, each written as a GIF (800 x 450, 10 fps) and an MP4 (1280 x 720, 15 fps), plus all four joined:

1. ``sop1_where``:   where each step happens: EB B125 (the hood, and the bench beside it) and CB 154 (the OT-2)
2. ``sop2_stocks``:  the stocks, in EB B125: what is opened inside the hood, and what next to it at the balance
3. ``sop3_load``:    loading the OT-2 in CB 154, the fill, and the seal
4. ``sop4_monitor``: the lid camera's 72 h record, and the end of the run

    xvfb-run -a python3 animate.py sop1 sop2 sop3 sop4 full
    PREVIEW=1 xvfb-run -a python3 animate.py sop2      # last frame of each sub-step, to /tmp/preview_<name>.png

The procedure is docs/baso4-extended-monitoring.md (11-02) with the stocks of the 10-30 practice plate, the
weighing-by-difference rule of the 10-23 lead plan, and the hood rules from powder-doser 141 and byu-vcl 195. See
README.md for the sources of each step and model.
"""
from __future__ import annotations

import math
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "lab_models"))

import scene                           # noqa: E402
import models as M                      # noqa: E402
import world as Wd                      # noqa: E402
from scene import FPS, OUT, R, Scene, T, ease, window   # noqa: E402
from world import BT, CB_X, OT2_AT, TT, WS, World, carry, cap_off   # noqa: E402

TITLE = "BaSO4 plate run: 3-D SOP"
# SOP_GIF_FPS=8 thins a long part's GIF so it stays under ~5 MB (the MP4 keeps every frame)
scene.GIF_FPS = int(os.environ.get("SOP_GIF_FPS", scene.GIF_FPS))


class StopChapter(Exception):
    pass


class SopScene(Scene):
    """scene.Scene, with two changes:

    * the camera's clipping range is reset every frame: the lid camera's view sits 0.6 m from the plate, inside a
      scene 10 m across, and the near plane left over from the wide shots would clip it;
    * a chapter can be written in parts (so each GIF stays under ~5 MB): steps before `start` are run without
      rendering, to reach their end state, and the part ends after the step labelled `stop`.
    """

    def __init__(self, name, title, start=None, stop=None, **kw):
        super().__init__(name, title, **kw)
        self.start, self.stop = start, stop
        self.recording = start is None

    def step(self, label, caption, seconds, update=None, hold=1.2, cam_to=None, labels=(), still=False,
             view_angle_to=None, live=False):
        if not self.recording and label == self.start:
            self.recording = True
        if not self.recording:
            if update is not None:
                for u in np.linspace(0, 1, 9)[1:]:
                    update(float(ease(u)))
            if cam_to is not None:
                self.cam = [tuple(v) for v in cam_to]
            if view_angle_to is not None:
                self.view_angle = view_angle_to
            return
        super().step(label, caption, seconds, update=update, hold=hold, cam_to=cam_to, labels=labels, still=still,
                     view_angle_to=view_angle_to, live=live)
        if self.stop is not None and label == self.stop:
            raise StopChapter(self)

    def render_base(self):
        self.apply()
        self.pl.camera_position = self.cam
        self.pl.camera.view_angle = self.view_angle
        self.pl.renderer.ResetCameraClippingRange()
        self.pl.render()
        return self.pl.screenshot(return_img=True)
X7, Y7 = M.slot_centre(7)

# ------------------------------------------------------------------------------------------- cameras
UP = (0, 0, 1)
CAM_ALL = [(3300, -13800, 8600), (3250, -200, 600), UP]
CAM_EB = [(2300, -4400, 3100), (520, 300, 1150), UP]
CAM_HOOD = [(-520, -1350, 1820), (-20, 470, 980), UP]
CAM_BAL = [(1420, -760, 1580), (1150, 360, 990), UP]
CAM_BENCH = [(1820, -1050, 1750), (1500, 380, 1000), UP]
CAM_PACK = [(1500, -2500, 3300), (1000, 380, 950), UP]
CAM_MID = [(1700, -3000, 2500), (560, 330, 1050), UP]
CAM_CB = [(CB_X + 1100, -2200, 2150), (CB_X + 250, 380, 1000), UP]
CAM_DECK = [(OT2_AT[0] + 260, -1300, 2150), (OT2_AT[0] - 40, 440, 1170), UP]          # the lid camera in frame
CAM_DECK2 = [(OT2_AT[0] - 380, -560, 1560), (OT2_AT[0] - 90, 440, 900), UP]
CAM_FILL = [(OT2_AT[0] - 720, -230, 1760), (OT2_AT[0] - 120, 470, 890), UP]      # from the left: slot 7 in front


def gauges(room, where, opened="-", extra=None):
    g = [("room", room), ("where", where), ("open", opened)]
    if extra:
        g += list(extra)
    return g


def person_at(W, x, y, rz=0.0, ghost=None):
    W.set("person", T((x, y, 0)) @ R((0, 0, 1), rz))
    if ghost is not None:
        W.show("person", ghost)


def walk(W, p0, p1):
    def f(u):
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        rz = p0[2] + (p1[2] - p0[2]) * u
        bob = 12 * abs(math.sin(u * math.pi * 6))
        W.set("person", T((x, y, bob)) @ R((0, 0, 1), rz))
    return f


def seq(*fs):
    def f(u):
        for g in fs:
            if g is not None:
                g(u)
    return f


def during(t0, t1, fn):
    """Run fn(w) with w the step's u re-mapped (eased) to [t0, t1]; it holds its end state after t1."""
    def f(u):
        if u < t0:
            return
        fn(window(u, t0, t1))
    return f


def fade(W, groups, a0, a1):
    def f(w):
        for g in groups:
            W.show(g, a0 + (a1 - a0) * w)
    return f


def move_world(W, group, M0, M1, lift=100.0):
    def f(w):
        W.set_world(group, carry(M0, M1, w, lift))
    return f


def cap_move(W, capgroup, cap_top_z, off=True, dx=70.0, dy=-40.0, flip=True, dz=0.0):
    def f(w):
        W.set(capgroup, T((0, 0, dz * (w if off else 1.0 - w))) @ cap_off(w if off else 1.0 - w, cap_top_z, dx, dy, flip))
    return f


def tube_world(W, key) -> np.ndarray:
    return W.S.world(f"t_{key}")


CAP_SPOT = {"ba0": -50.0, "ba1": -17.0, "ba2": 16.0, "ba3": 49.0, "so0": -50.0, "so1": -17.0, "so2": 16.0, "so3": 49.0,
            "nacl": 82.0, "water": 115.0}


def tcap(W, key, off=True):
    """A vial's cap off (or back on): set down top-down on the surface in front of its holder, each in its own spot."""
    hx, hy = Wd.RACK_HOLES[Wd.RACK_OF[key][1]]
    return cap_move(W, f"t_{key}_cap", M.VIAL_CAP_TOP, off, dx=CAP_SPOT[key] - hx, dy=-75.0 - hy)


def pour_pose(t_world):
    """The wash bottle leaning over a vial from behind, its spout over the vial's mouth."""
    return t_world @ T((0, 202, 30)) @ R((1, 0, 0), 55)


def tube_cap_top():
    return M.VIAL_CAP_TOP


def fill_tube(W, key, ml0, ml1):
    def f(w):
        W.tube_fill(key, ml0 + (ml1 - ml0) * w)
    return f


def invert(W, key, times=2):
    """Cap on, invert the vial a few times in place (about its middle)."""
    base = W.S.gmat[f"t_{key}"].copy()

    def f(w):
        ang = 180 * math.sin(math.pi * times * w) ** 2 if w < 1 else 0.0
        lift = 140 * math.sin(math.pi * w)
        W.set(f"t_{key}", base @ T((0, 0, lift)) @ R((1, 0, 0), ang, (0, 0, 30)))
    return f


# --------------------------------------------------------------------------------------- set-ups
def show_eb_hood_items(W, a=1.0):
    for g in ("liner", "tray", "ba_waste", "wash_hood", "bacl2", "bacl2_cap", "rack_hood", "spatula"):
        W.show(g, a)


def stocks_done(W):
    """The state at the end of chapter 2: every vial made, capped, in its holder."""
    for key, _, _ in Wd.TUBES:
        W.tube_fill(key, 13.5 if key in ("ba0", "so0") else 15.0)
        W.tube_show(key)


def racks_in_tub(W, at_cb=False):
    """Both holders, with their vials, in the tub (lid on), on the EB bench or on CB 154's side bench."""
    W.show("rack_hood")
    W.show("rack_bench")
    if at_cb:
        W.set("tub", T((Wd.BENCH_CB[0] + 30, 330, BT)))
    tw = W.S.world("tub")
    W.set_world("rack_hood", tw @ T((-95, 0, 3)))
    W.set_world("rack_bench", tw @ T((95, 0, 3)))
    W.reparent("rack_hood", "tub")
    W.reparent("rack_bench", "tub")
    W.set("tub_lid", T((0, 0, 150)))


def head_to(W, x, y, z):
    """Put the P300's nozzle at deck (x, y, z): the head moves in x, y and the mount in z."""
    t = M.deck(x, y, z)
    n = W.nozzle
    W.set("ot2_head", T((t[0] - n[0], t[1] - n[1], 0)))
    W.set("ot2_beam", T((0, t[1] - n[1], 0)))          # the beam carries the head front to back
    W.set("ot2_pip", T((0, 0, t[2] - n[2])))


def nozzle_now(W) -> np.ndarray:
    hx, hy = W.S.gmat["ot2_head"][0, 3], W.S.gmat["ot2_pip"][2, 3]
    n = W.nozzle
    return np.array([n[0] + W.S.gmat["ot2_head"][0, 3], n[1] + W.S.gmat["ot2_head"][1, 3], n[2] + hy]) - M.DECK_TO_OT2


def head_path(W, pts):
    """Move the nozzle through deck waypoints (x, y, z), each leg in equal time."""
    pts = [np.asarray(p, float) for p in pts]

    def f(w):
        k = len(pts) - 1
        s = min(w * k, k - 1e-9)
        i = int(s)
        v = ease(s - i)
        p = pts[i] + (pts[i + 1] - pts[i]) * v
        head_to(W, *p)
    return f


def door(W, opened):
    hinge = W.ot["door_hinge"]

    def f(w):
        a = (w if opened else 1 - w)
        W.set("ot2_door", R((1, 0, 0), -100 * a, hinge))
    return f


SAFE_Z = 205.0
TIP_DROP = 51.0


def tube_deck_xy(slot, hole):
    xs, ys = M.slot_centre(slot)
    hx, hy = Wd.RACK_HOLES[hole]
    return xs + hx, ys + hy


def tip_xy(i):
    x6, y6 = M.slot_centre(6)
    r, c = i % 8, i // 8
    return x6 - 49.5 + c * 9.0, y6 + 31.5 - r * 9.0


def well_deck(r, c):
    x, y = Wd.well_xy(r, c)
    return Wd.PLATE_XY[0] + x, Wd.PLATE_XY[1] + y


# -------------------------------------------------------------------------------- plate A and its timing
LEVELS = (0.01, 0.1, 1.0, 3.0)
SI_1M = {(0.01, 0.01): -2.0, (0.01, 0.1): -1.0, (0.01, 1.0): 0.0, (0.01, 3.0): 0.5,
         (0.1, 0.01): -1.0, (0.1, 0.1): 0.0, (0.1, 1.0): 1.0, (0.1, 3.0): 1.5,
         (1.0, 0.01): 0.0, (1.0, 0.1): 1.0, (1.0, 1.0): 2.0, (1.0, 3.0): 2.5,
         (3.0, 0.01): 0.5, (3.0, 0.1): 1.5, (3.0, 1.0): 2.5, (3.0, 3.0): 2.9}     # PHREEQC, docs/baso4-checks (10-30)


def plate_a():
    """One shuffle of plate A: 48 + 16 + 8 + 8 blanks + 4 controls = 84 wells; 12 empty. Returns {(r, c): well}."""
    conds = []
    for ba in LEVELS:
        for so in LEVELS:
            for _ in range(3):
                conds.append(dict(ba=ba, so=so, nacl=1, si=SI_1M[(ba, so)]))
            conds.append(dict(ba=ba, so=so, nacl=0, si=SI_1M[(ba, so)] + 1.6))
    for lv in LEVELS:
        conds.append(dict(ba=lv, so=0, nacl=1, si=None))
        conds.append(dict(ba=0, so=lv, nacl=1, si=None))
    conds += [dict(ba=0, so=0, nacl=0, si=None)] * 4 + [dict(ba=0, so=0, nacl=1, si=None)] * 4
    conds += [dict(ba=10.0, so=10.0, nacl=1, si=3.9)] * 4
    rng = np.random.default_rng(80)
    pos = [(r, c) for r in range(8) for c in range(12)]
    rng.shuffle(pos)
    return {p: c for p, c in zip(pos, conds)}


def onset_min(si):
    """Illustrative only: minutes after the sulfate until a well looks cloudy, from its saturation index."""
    if si is None or si < 0.3:
        return None
    pts = [(0.3, 5400.0), (0.5, 2880.0), (1.0, 360.0), (1.5, 60.0), (2.0, 10.0), (2.9, 1.0), (4.0, 0.3)]
    for (s0, t0), (s1, t1) in zip(pts[:-1], pts[1:]):
        if si <= s1:
            k = (si - s0) / (s1 - s0)
            return 10 ** (math.log10(t0) + k * (math.log10(t1) - math.log10(t0)))
    return 0.3


def whiteness(w):
    m = min(w["ba"], w["so"])
    if m <= 0:
        return 0.0
    return float(np.clip(math.log10(m / 0.03) / math.log10(10 / 0.03), 0.0, 1.0)) ** 0.7


# ============================================================================================ chapter 1
def sop1():
    S = SopScene("sop1_where", TITLE + " · 1 Where each step happens")
    W = World(S)
    show_eb_hood_items(W)
    for k in ("ba0", "ba1", "ba2", "ba3", "so0", "so1", "so2", "so3", "nacl", "water"):
        W.tube_fill(k, 15.0)
        W.tube_show(k)
    W.set("sash", T((0, 0, M.HOOD["working"] - 30)))
    for g in ("paper", "plate", "tiprack"):
        W.show(g)
    W.show("fov")
    head_to(W, 330, 330, 260)
    person_at(W, 0, -300)
    S.cam = CAM_ALL
    S.view_angle = 30
    S.gauges = [("1", "stocks: EB B125"), ("2", "carry: lidded tub"), ("3", "plate: CB 154 OT-2"),
                ("4", "monitor: 72 h")]
    S.intro = 1.2
    S.step("1.1", "Two rooms in two buildings. The stocks are made in EB B125, Chris Dillon's lab, because it has the "
                  "fume hood. The plate is filled and watched on the OT-2 in CB 154, under the lid camera.",
           3.0, hold=2.6,
           labels=[("EB B125: fume hood\n+ bench with the balance", (300, 400, 2400), (0.10, 0.30)),
                   ("CB 154: OT-2 with the\nlid camera over slot 7", (OT2_AT[0], OT2_AT[1], 1500), (0.86, 0.30))])
    S.gauges = gauges("EB B125 (Dillon lab)", "inside the hood: red")
    S.step("1.2", "Inside the hood (red): the barium chloride bottle is only ever opened here, and every barium "
                  "solution stays here until its vial is capped. Stand outside it with only your arms in, the sash "
                  "at its working-height sticker.",
           3.0, update=during(0.3, 1.0, fade(W, ["zones_eb"], 0, 1)), cam_to=CAM_EB, hold=3.0,
           labels=[("inside the hood:\nbarium chloride, open", (0, 500, 1150), (0.10, 0.56)),
                   ("sash at its sticker\n(working height)", (-650, 50, WS + M.HOOD["working"]), (0.12, 0.80))])
    S.gauges = gauges("EB B125 (Dillon lab)", "next to the hood: amber")
    S.step("1.3", "Next to the hood (amber), on the bench: the A&D HR-100A balance, sodium sulfate and sodium "
                  "chloride (neither is classed as hazardous, so they are weighed on the bench), labels and the log. "
                  "Barium chloride only reaches the balance inside a capped vial.",
           2.4, cam_to=[(2300, -2600, 2300), (1300, 350, 1050), UP], hold=3.0,
           labels=[("A&D HR-100A\n(102 g x 0.1 mg)", (1040, 300, BT + 170), (0.30, 0.20)),
                   ("sodium sulfate,\nsodium chloride", (1390, 560, BT + 150), (0.62, 0.18)),
                   ("lidded tub", (2120, 300, BT + 160), (0.88, 0.32))])
    path = [(2100, -500), (2900, -1200), (4600, -1200), (Wd.BENCH_CB[0], -500)]
    dashes = []
    for (x0, y0), (x1, y1) in zip(path[:-1], path[1:]):
        L = math.hypot(x1 - x0, y1 - y0)
        n = int(L // 180)
        for i in range(n):
            a, b = i / n, (i + 0.55) / n
            dashes.append(M.box(x0 + (x1 - x0) * a - 25, y0 + (y1 - y0) * a - 25, 2,
                                x0 + (x1 - x0) * b + 25, y0 + (y1 - y0) * b + 25, 14))
    S.add("path", M.merge(dashes), M.MATS["path"][:3], group="path", shown=False, specular=0.1)
    S.gmat["path"] = np.eye(4)
    S.gauges = gauges("EB B125 -> CB 154", "the walk", "nothing: vials capped, tub lidded")
    S.step("1.4", "Everything moves between the buildings capped, in the lidded tub: the two vial holders with their "
                  "ten vials. Nothing is opened on the way.",
           3.0, update=during(0.0, 0.8, fade(W, ["path"], 0, 1)), cam_to=CAM_ALL, hold=2.6,
           labels=[("capped vials in the\nlidded tub", (3800, -1200, 50), (0.50, 0.30))])
    S.gauges = gauges("CB 154 (Vertical Cloud Lab)", "at the OT-2: blue")
    S.step("1.5", "In CB 154 (blue): the vials are uncapped only on the OT-2's deck. The plate sits on the "
                  "heater-shaker in slot 7, under the lid camera, and is sealed at the protocol's pause. The run, the "
                  "stills and the end of the run all happen here.",
           3.2, update=during(0.3, 1.0, fade(W, ["zones_cb"], 0, 1)), cam_to=CAM_CB, hold=3.2,
           labels=[("lid camera + Pi 5\n(byu-vcl PR 234)", tuple(W.world_of("lidcam", (W.lens[0], W.lens[1], W.lens[2] + 60))), (0.20, 0.18)),
                   ("slot 7: plate on the\nheater-shaker", tuple(W.world_of("ot2", tuple(M.deck(*Wd.PLATE_XY, Wd.PLATE_TOP)))), (0.22, 0.74)),
                   ("side bench: tub,\nwipe for the caps, waste", (Wd.BENCH_CB[0], 300, BT + 120), (0.86, 0.34))],
           still=True)
    S.gauges = [("1", "stocks: EB B125, hood + bench"), ("2", "carry: lidded tub"), ("3", "load + fill: CB 154"),
                ("4", "watch 72 h: CB 154")]
    S.step("1.6", "The order: make the stocks in EB B125, carry them over, load and fill the plate on the OT-2, "
                  "then let the lid camera record it for 72 h. The next three chapters go through each part.",
           3.0, cam_to=CAM_ALL, hold=2.4)
    S.save()


# ============================================================================================ chapter 2
def sop2(part=None):
    if part == "a":
        S = SopScene("sop2a_hood", TITLE + " · 2a Barium chloride, inside the hood", stop="2.9")
    elif part == "b":
        S = SopScene("sop2b_bench", TITLE + " · 2b Dilutions, then the bench", start="2.10")
    else:
        S = SopScene("sop2_stocks", TITLE + " · 2 Stocks in EB B125")
    W = World(S)
    for k in ("ba1", "ba2", "ba3", "so1", "so2", "so3"):      # the dilution vials: 13.50 g of DI water each, weighed in
        W.tube_fill(k, 13.5)
    W.tube_show("ba0", 0.0)                                   # the 0.1 M barium vial is the weighing vial until 2.11
    for k in ("so0", "so1", "so2", "so3", "nacl", "water"):
        W.tube_show(k)
    pan = W.S.world("balance") @ T(W.pan)
    vial_bench = W.S.world("vial")
    vial_hood = T((-110, 420, WS + 4))
    S.cam = CAM_EB
    S.view_angle = 30
    person_at(W, 1040, -1500)
    S.gauges = gauges("EB B125 (Dillon lab)", "arriving", "-", [("PPE", "nitrile, coat, glasses"),
                                                               ("and", "long pants, closed-toe shoes")])
    S.step("2.1", "Before anything is opened: nitrile gloves (two pairs for barium), a lab coat and safety glasses, "
                  "with long pants and closed-toe shoes. The barium chloride SDS goes in the binder. Chris Dillon's "
                  "rule for the room: keep every container closed and labelled.",
           2.6, update=walk(W, (1040, -1500, 0), (1040, -220, 0)), hold=2.0)
    S.gauges = gauges("EB B125", "next to the hood", "-", [("balance", "warm-up >= 1 h")])
    S.step("2.2", "The balance sits on the bench beside the hood. If it was carried over, plug it in at least an "
                  "hour before weighing: the HR-100A drifts for about an hour after a move (powder-doser 157). "
                  "Level it by its bubble and check it with a check weight. Then weigh 13.50 g of DI water into "
                  "each of six capped vials, for the dilutions.",
           2.4, cam_to=CAM_BAL, hold=2.6, update=during(0, 1, lambda w: person_at(W, 1040, -220, 0, 1 - w)),
           labels=[("bubble level", tuple(W.world_of("balance", (-80, -112, 66))), (0.18, 0.62)),
                   ("breeze-break lid\n(lift it to load)", tuple(W.world_of("balance", (0, 37.5, 176))), (0.70, 0.18))])
    # set up the hood: sash up, things in, sash down
    items = ["liner", "tray", "ba_waste", "wash_hood", "bacl2", "bacl2_cap", "rack_hood", "spatula"]
    for g in items:
        W.show(g, 0.0)

    def setup(u):
        W.set("sash", T((0, 0, 700 * window(u, 0.0, 0.2) - (700 - (M.HOOD["working"] - 30)) * window(u, 0.85, 1.0))))
        for i, g in enumerate(items):
            a = window(u, 0.2 + i * 0.075, 0.2 + i * 0.075 + 0.07)
            W.show(g, a)
            if g == "rack_hood":
                for k in ("ba1", "ba2", "ba3"):
                    W.tube_show(k, a)
            base = W.base[g]
            W.S.gmat[g] = T((0, 0, 80 * (1 - a))) @ base if g not in ("bacl2_cap",) else W.S.gmat[g]
        person_at(W, -80 + 1120 * (1 - window(u, 0, 0.15)), -220, 0, 0.0)
    S.gauges = gauges("EB B125", "inside the hood", "-", [("sash", "up to load, then working height")])
    S.step("2.3", "Load the hood before opening anything: absorbent liner, a tray, the barium waste bottle, a wash "
                  "bottle of fresh DI water, the barium chloride, the barium vial holder with three of the water vials "
                  "and a spatula, all behind the yellow line "
                  "15 cm (6 in) inside the sash. Then lower the sash to its working-height sticker.",
           5.0, update=setup, cam_to=CAM_HOOD, hold=2.4,
           labels=[("15 cm (6 in) line", (-420, 226, WS), (0.10, 0.84)),
                   ("barium waste", (540, 600, WS + 200), (0.88, 0.30)),
                   ("barium chloride\ndihydrate", (-290, 560, WS + 140), (0.10, 0.30))])
    # tare the capped vial on the balance
    lid0 = W.S.gmat["balance_lid"].copy()

    def tare(u):
        a = window(u, 0.0, 0.25)
        b = window(u, 0.65, 0.9)
        W.set("balance_lid", T((0, -40 * (a - b), 130 * (a - b))) @ lid0)
        W.set_world("vial", carry(vial_bench, pan, window(u, 0.25, 0.6), 120))
        person_at(W, 1040, -220, 0, 0.0)
    S.gauges = gauges("EB B125", "next to the hood", "balance lid only", [("balance", "0.0000 g after TARE")])
    S.step("2.4", "At the balance: lift the breeze-break lid, put the empty capped vial for the 0.1 M barium "
                  "chloride on the pan, close the "
                  "lid and press TARE. A capped vial is how barium chloride reaches the balance: the powder never "
                  "leaves the hood in an open container.",
           3.4, update=tare, cam_to=CAM_BAL, hold=1.6)

    def to_hood(u):
        a = window(u, 0.0, 0.2)
        W.set("balance_lid", T((0, -40 * (a - window(u, 0.5, 0.65)), 130 * (a - window(u, 0.5, 0.65)))) @ lid0)
        W.set_world("vial", carry(pan, vial_hood, window(u, 0.2, 1.0), 260))
        x = 1040 + (-80 - 1040) * window(u, 0.2, 0.9)
        person_at(W, x, -220, 0, 1.0)
    S.gauges = gauges("EB B125", "next to -> inside the hood", "-")
    S.step("2.5", "Walk the tared, capped vial from the balance into the hood. Only your arms go in; your head stays "
                  "outside the sash.", 3.0, update=to_hood, cam_to=CAM_MID, hold=0.8)
    # open the barium chloride and the vial
    S.gauges = gauges("EB B125", "INSIDE the hood", "barium chloride bottle, vial")
    S.step("2.6", "Inside the hood only: unscrew the barium chloride bottle and the vial, and set both caps down "
                  "top-down on the liner.",
           2.6, update=seq(during(0.0, 0.6, cap_move(W, "bacl2_cap", 145, True, dx=95, dy=-70)),
                           during(0.4, 1.0, cap_move(W, "vial_cap", 60, True, dx=60, dy=-40)),
                           lambda u: W.show("person", 1 - window(u, 0, 0.3))),
           cam_to=[(-450, -520, 1420), (-200, 480, 985), UP], hold=1.0,
           labels=[("barium chloride dihydrate\n(toxic if swallowed)", (-290, 560, WS + 150), (0.12, 0.22)),
                   ("caps top-down", (-195, 490, WS + 8), (0.60, 0.80))])
    # spatula: three scoops from the bottle into the vial
    sp0 = W.S.world("spatula")
    bottle_mouth = np.array([-290, 560, WS + 4 + 118.0])
    vial_mouth = np.array([-110, 420, WS + 4 + 64.0])

    def spat_pose(p, tilt=-40.0, rz=-35.0):
        return T(p) @ R((0, 0, 1), rz) @ R((0, 1, 0), tilt) @ T((78, 0, 0))
    S.add("spat_powder", M.sphere(-78, 0, 3, 5.5, 14), M.MATS["powder"][:3], group="spatula", shown=False, specular=0.05)

    def scoop(u):
        if u < 0.12:
            W.set_world("spatula", carry(sp0, spat_pose(bottle_mouth + (0, 0, 60)), window(u, 0, 0.12), 80))
            return
        k = min(int((u - 0.12) / 0.29), 2)
        v = (u - 0.12 - 0.29 * k) / 0.29
        down = spat_pose(bottle_mouth - (0, 0, 40))
        up_b = spat_pose(bottle_mouth + (0, 0, 60))
        up_v = spat_pose(vial_mouth + (0, 0, 50), tilt=-25)
        tip = spat_pose(vial_mouth - (0, 0, 8), tilt=-55)
        if v < 0.3:
            m = carry(up_b, down, ease(v / 0.3), 0) if v < 0.15 else carry(down, up_b, ease((v - 0.15) / 0.15), 0)
            W.S.alpha["spat_powder"] = 1.0 if v >= 0.15 else 0.0
        elif v < 0.65:
            m = carry(up_b, up_v, ease((v - 0.3) / 0.35), 40)
            W.S.alpha["spat_powder"] = 1.0
        elif v < 0.85:
            m = carry(up_v, tip, ease((v - 0.65) / 0.2), 0)
            W.S.alpha["spat_powder"] = 1.0 - ease((v - 0.65) / 0.2)
            W.S.set_mesh("vial_powder", M.cyl(0, 0, 1.6, M.VIAL_R_IN - 0.3, 0.8 + 0.9 * (k + ease((v - 0.65) / 0.2))))
            W.S.alpha["vial_powder"] = 1.0
        else:
            m = carry(tip, up_b if k < 2 else up_v, ease((v - 0.85) / 0.15), 30)
        W.set_world("spatula", m)
    S.gauges = gauges("EB B125", "INSIDE the hood", "barium chloride bottle, vial", [("target", "about 366 mg")])
    S.step("2.7", "Spatula about 366 mg of barium chloride dihydrate into the vial, low in the hood and slowly, "
                  "so no dust lifts. It doesn't have to be exact: the balance reading sets the concentration.",
           6.0, update=scoop, cam_to=[(-400, -380, 1360), (-200, 470, 1000), UP], hold=0.5)

    def close(u):
        cap_move(W, "bacl2_cap", 145, False, dx=95, dy=-70)(window(u, 0.0, 0.55))
        cap_move(W, "vial_cap", 60, False, dx=60, dy=-40)(window(u, 0.3, 0.85))
        W.set_world("spatula", carry(W.S.world("spatula"), sp0, window(u, 0.0, 0.4), 40) if u < 0.4 else sp0)
    S.gauges = gauges("EB B125", "INSIDE the hood", "closing both")
    S.step("2.8", "Cap the bottle and the vial before anything leaves the hood. Wipe the vial's outside with a damp "
                  "wipe; the wipe goes in the barium waste.", 2.6, update=close, hold=0.8)

    def weigh(u):
        a = window(u, 0.55, 0.7)
        b = window(u, 0.85, 1.0)
        W.set("balance_lid", T((0, -40 * (a - b), 130 * (a - b))) @ lid0)
        W.set_world("vial", carry(vial_hood, pan, window(u, 0.0, 0.8), 260))
        person_at(W, -80 + 1120 * window(u, 0.0, 0.6), -220, 0, 1.0)
        S.gauges = gauges("EB B125", "inside -> next to the hood", "balance lid only",
                          [("balance", "0.3664 g" if u > 0.92 else "-")])
    S.step("2.9", "Back at the balance: weigh the capped vial and write the reading in the log, with the bottle's "
                  "lot. 0.3664 g is 1.500 mmol (244.26 g/mol): with 15.00 g of water, 0.1000 mol/kg. For another "
                  "mass, work out its concentration and use that in the plate map.",
           3.6, update=weigh, cam_to=CAM_MID, hold=2.0)
    # dissolve in the vial itself: it is the 0.1 M barium vial
    rack_w = W.S.world("rack_hood")
    wash0 = W.S.world("wash_hood")
    hole0 = Wd.rack_pose(rack_w, 0)                     # A1 of the barium holder

    def dissolve(u):
        a = window(u, 0.0, 0.25)
        W.set("balance_lid", T((0, -40 * (a - window(u, 0.12, 0.2)), 130 * (a - window(u, 0.12, 0.2)))) @ lid0)
        W.set_world("vial", carry(pan, vial_hood, window(u, 0.05, 0.3), 260))
        person_at(W, 1040 - 1120 * window(u, 0.05, 0.3), -220, 0, 0.0)
        cap_move(W, "vial_cap", 60, True, dx=60, dy=-40)(window(u, 0.3, 0.42))
        pw = window(u, 0.42, 0.74)
        over = pour_pose(vial_hood)
        if pw > 0:
            W.set_world("wash_hood", carry(wash0, over, min(pw / 0.25, 1.0), 80) if pw < 0.85 else
                        carry(over, wash0, (pw - 0.85) / 0.15, 80))
        fw = window(u, 0.5, 0.7)
        W.S.alpha["vial_liquid"] = 1.0 if fw > 0 else 0.0
        W.S.set_mesh("vial_liquid", M.tube_liquid(max(2.2, M.ml_to_level(15.0 * fw))))
        cap_move(W, "vial_cap", 60, False, dx=60, dy=-40)(window(u, 0.74, 0.84))
        sw = window(u, 0.84, 1.0)
        W.S.alpha["vial_powder"] = 1.0 - sw
        if sw > 0:
            W.set_world("vial", vial_hood @ T((0, 0, 70 * math.sin(math.pi * sw))) @ R((1, 0, 0), 12 * math.sin(sw * math.pi * 6)))
    S.gauges = gauges("EB B125", "INSIDE the hood", "the 0.1 M barium vial")
    S.step("2.10", "In the hood: about 15 mL of DI water into the vial from the wash bottle. Cap it and swirl until "
                   "the solid is gone. The powder never leaves this vial: it is the 0.1 M barium chloride stock.",
           6.0, update=dissolve, cam_to=[(-60, -430, 1380), (40, 470, 1000), UP], hold=0.6)

    def weigh_back(u):
        lift = window(u, 0.3, 0.4) - window(u, 0.47, 0.52) + window(u, 0.6, 0.65) - window(u, 0.76, 0.86)
        W.set("balance_lid", T((0, -40 * lift, 130 * lift)) @ lid0)
        W.set_world("vial", carry(vial_hood, pan, window(u, 0.0, 0.45), 260) if u < 0.66 else
                    carry(pan, hole0, window(u, 0.66, 1.0), 260))
        person_at(W, -80 + 1120 * window(u, 0.0, 0.4) - 1120 * window(u, 0.68, 0.95), -220, 0, 1.0)
        S.gauges = gauges("EB B125", "inside -> next to the hood -> inside", "balance lid only",
                          [("balance", "15.37 g (+ the vial's tare)" if u > 0.52 else "-")])
        if u > 0.985:                                   # it is now A1's vial: hand over to the stock vial ba0
            for g in ("vial", "vial_cap"):
                W.show(g, 0.0)
            W.tube_fill("ba0", 15.0)
            W.tube_show("ba0")
    S.gauges = gauges("EB B125", "INSIDE the hood", "-", [("vial", "0.1 M BaCl2, about 15 g of water")])
    S.step("2.11", "Wipe it, weigh it capped at the balance and log the reading: the water's mass sets the "
                   "concentration (0.3664 g with 15.00 g of water is 0.1000 mol/kg). Then it goes back into the "
                   "hood, into A1 of the barium holder.", 5.0, update=weigh_back, cam_to=CAM_MID, hold=0.6)
    pip0 = W.S.world("pipette_h")
    W.show("pipette_h")

    def dilute(u):
        # uncap the 0.1 M vial and the three water vials, then 1.5 mL down the series with the pipette
        keys = ("ba0", "ba1", "ba2", "ba3")
        for k in keys:
            tcap(W, k, True)(window(u, 0.0, 0.14))
        for j in range(3):
            a, b = 0.16 + 0.28 * j, 0.16 + 0.28 * (j + 1)
            if a <= u < b:
                v = (u - a) / (b - a)
                src = W.S.world(f"t_{keys[j]}") @ T((0, 0, 75))
                dst = W.S.world(f"t_{keys[j + 1]}") @ T((0, 0, 85))
                if v < 0.25:
                    W.set_world("pipette_h", carry(pip0 if j == 0 else W.S.world("pipette_h"), src, ease(v / 0.25), 60))
                elif v < 0.6:
                    W.set_world("pipette_h", carry(src, dst, ease((v - 0.25) / 0.35), 80))
                else:
                    W.set_world("pipette_h", dst @ T((0, 0, -20 * math.sin(math.pi * (v - 0.6) / 0.4))))
                lv = window(v, 0.62, 0.95)
                W.tube_fill(keys[j + 1], 13.5 + 1.5 * lv)
                W.tube_fill(keys[j], 15.0 - 1.5 * window(v, 0.1, 0.25))
        if u >= 0.99:
            W.set_world("pipette_h", carry(W.S.world("pipette_h"), pip0, 1.0, 0))
    S.gauges = gauges("EB B125", "INSIDE the hood", "barium vials", [("series", "0.1 M -> 10 -> 1 -> 0.1 mM")])
    S.step("2.12", "Still in the hood: uncap the 0.1 M vial and the three water vials, then move 1.5 mL down the "
                   "series with a new pipette tip each time: 10, 1 and 0.1 mM barium chloride. Cap and invert each "
                   "before the next transfer.",
           7.0, update=dilute, hold=0.6,
           labels=[("100-1000 uL pipette\n(new tip per transfer)", (380, 380, WS + 280), (0.86, 0.22))])

    def recap(u):
        for k in ("ba0", "ba1", "ba2", "ba3"):
            tcap(W, k, False)(window(u, 0.0, 0.6))
        W.set_world("pipette_h", carry(W.S.world("pipette_h"), pip0, window(u, 0, 0.3), 30) if u < 0.3 else pip0)
    S.gauges = gauges("EB B125", "INSIDE the hood", "closing the vials")
    S.step("2.13", "Cap all four barium vials. Label each one: name, concentration, date, initials. Pipette tips "
                   "and wipes that touched barium go in the barium waste in the hood.", 2.4, update=recap, hold=0.6)
    # ---- sodium sulfate and sodium chloride, at the balance
    boat0 = W.S.world("boat")
    boat_pan = pan
    sp2 = W.S.world("spatula2")
    so4_mouth = np.array([1330, 560, BT + 130.0])
    boat_mouth = (pan @ np.array([0, 0, 10.0, 1]))[:3]

    def so4(u):
        person_at(W, -80 + 1200 * window(u, 0.0, 0.12), -220, 0, 0.0)
        a = window(u, 0.08, 0.16)
        b = window(u, 0.22, 0.28)
        W.set("balance_lid", T((0, -40 * (a - b), 130 * (a - b))) @ lid0)
        W.set_world("boat", carry(boat0, boat_pan, window(u, 0.1, 0.2), 120))
        cap_move(W, "na2so4_cap", 160, True, dx=-80, dy=-60)(window(u, 0.28, 0.38))
        a2 = window(u, 0.38, 0.44)
        b2 = window(u, 0.66, 0.72)
        W.set("balance_lid", T((0, -40 * (a2 - b2 + a - b), 130 * (a2 - b2 + a - b))) @ lid0)
        sv = window(u, 0.42, 0.66)
        up_b = T(so4_mouth + (0, 0, 60)) @ R((0, 0, 1), 200) @ R((0, 1, 0), -40) @ T((78, 0, 0))
        dn_b = T(so4_mouth - (0, 0, 30)) @ R((0, 0, 1), 200) @ R((0, 1, 0), -40) @ T((78, 0, 0))
        up_p = T(boat_mouth + (0, 0, 120)) @ R((0, 0, 1), 200) @ R((0, 1, 0), -30) @ T((78, 0, 0))
        dn_p = T(boat_mouth + (0, 0, 8)) @ R((0, 0, 1), 200) @ R((0, 1, 0), -50) @ T((78, 0, 0))
        if 0.36 < u < 0.42:
            W.set_world("spatula2", carry(sp2, up_b, window(u, 0.36, 0.42), 60))
        elif sv > 0 and u <= 0.68:
            for (s0, s1, A, B, lift) in ((0, 0.2, up_b, dn_b, 0), (0.2, 0.35, dn_b, up_b, 0), (0.35, 0.7, up_b, up_p, 50),
                                         (0.7, 0.9, up_p, dn_p, 0), (0.9, 1.0, dn_p, up_p, 0)):
                if s0 <= sv <= s1:
                    W.set_world("spatula2", carry(A, B, ease((sv - s0) / (s1 - s0)), lift))
            if sv > 0.85:
                W.S.alpha["boat_powder"] = 1.0
        elif u > 0.68:
            W.set_world("spatula2", carry(up_p, sp2, window(u, 0.68, 0.76), 40))
        cap_move(W, "na2so4_cap", 160, False, dx=-80, dy=-60)(window(u, 0.74, 0.84))
        S.gauges = gauges("EB B125", "next to the hood", "sodium sulfate bottle" if 0.3 < u < 0.84 else "balance lid",
                          [("balance", "0.2131 g" if u > 0.66 else ("0.0000 g (boat tared)" if u > 0.28 else "-"))])
    S.gauges = gauges("EB B125", "next to the hood", "-")
    S.step("2.14", "Sodium sulfate is weighed on the bench, in an open weigh boat: tare the boat, open the bottle, "
                   "spatula about 213 mg into the boat, close the bottle. 0.2131 g of anhydrous sodium sulfate "
                   "(142.04 g/mol) with 15.00 g of water is 0.1000 mol/kg.",
           7.0, update=so4, cam_to=CAM_BENCH, hold=1.0,
           labels=[("sodium sulfate,\nanhydrous", (1330, 560, BT + 150), (0.70, 0.20))])
    t_so0 = W.S.world("t_so0")
    funnel0 = W.S.world("funnel")
    wash_b0 = W.S.world("wash_bench")

    def so4_tube(u):
        tcap(W, "so0", True)(window(u, 0.0, 0.12))
        W.set_world("funnel", carry(funnel0, t_so0 @ T((0, 0, 58)), window(u, 0.05, 0.2), 80) if u < 0.75 else
                    carry(t_so0 @ T((0, 0, 58)), funnel0, window(u, 0.75, 0.85), 80))
        a = window(u, 0.15, 0.25)
        b = window(u, 0.3, 0.38)
        W.set("balance_lid", T((0, -40 * (a - b), 130 * (a - b))) @ lid0)
        over = t_so0 @ T((-35, 0, 115)) @ R((0, 1, 0), 110, (0, 0, 0))
        tw = window(u, 0.25, 0.42)
        W.set_world("boat", carry(boat_pan, over, min(tw / 0.6, 1.0), 120) if tw < 1 else boat0)
        if tw >= 0.6:
            W.S.alpha["boat_powder"] = max(0.0, 1 - (tw - 0.6) / 0.4)
        over_w = pour_pose(t_so0)
        ww = window(u, 0.42, 0.75)
        W.set_world("wash_bench", carry(wash_b0, over_w, min(ww / 0.3, 1.0), 80) if ww < 0.85 else
                    carry(over_w, wash_b0, (ww - 0.85) / 0.15, 80))
        W.tube_fill("so0", 15.0 * window(u, 0.48, 0.72))
        tcap(W, "so0", False)(window(u, 0.84, 0.95))
    S.gauges = gauges("EB B125", "next to the hood", "sulfate vial")
    S.step("2.15", "Tip the boat through a funnel into the 0.1 M sodium sulfate vial and rinse the boat and funnel in "
                   "with DI water, to about 15 mL. Cap and invert it, then weigh it capped and log the water's mass.",
           4.6, update=so4_tube, cam_to=[(1950, -700, 1550), (1650, 380, 1000), UP], hold=0.6)

    def rest(u):
        for i, k in enumerate(("so1", "so2", "so3")):
            tcap(W, k, True)(window(u, 0.0, 0.12))
            W.tube_fill(k, 13.5 + 1.5 * window(u, 0.3 + 0.08 * i, 0.38 + 0.08 * i))
            tcap(W, k, False)(window(u, 0.55, 0.65))
        cap_move(W, "nacl_cap", 178, True, dx=-80, dy=-60)(window(u, 0.6, 0.7))
        for k in ("nacl", "water"):
            tcap(W, k, True)(window(u, 0.62, 0.7))
        W.tube_fill("nacl", 15.0 * window(u, 0.7, 0.86))
        W.tube_fill("water", 15.0 * window(u, 0.74, 0.9))
        cap_move(W, "nacl_cap", 178, False, dx=-80, dy=-60)(window(u, 0.8, 0.9))
        for k in ("nacl", "water"):
            tcap(W, k, False)(window(u, 0.9, 1.0))
        S.gauges = gauges("EB B125", "next to the hood", "sulfate vials" if u < 0.6 else "sodium chloride bottle",
                          [("balance", "4.3830 g NaCl" if u > 0.75 else "-")])
    S.step("2.16", "The same tenfold series for sodium sulfate: 1.5 mL into each of its three water vials. Then "
                   "4.383 g of sodium chloride with 13.4 g of DI water (15 mL of 5 M), and a vial of fresh DI water: "
                   "ten vials in all, each labelled and logged.",
           5.0, update=rest, hold=1.2,
           labels=[("5 M NaCl and DI water", tuple(W.world_of("rack_bench", (20, -20, 80))), (0.82, 0.22))])
    # clean up and pack
    tub_w = W.S.world("tub")

    def pack(u):
        W.set_world("rack_hood", carry(rack_w, tub_w @ T((-95, 0, 3)), window(u, 0.15, 0.5), 420))
        W.set_world("rack_bench", carry(W.base["rack_bench"], tub_w @ T((95, 0, 3)), window(u, 0.4, 0.65), 200))
        W.set("tub_lid", T((0, 0, 150 + 200 * (window(u, 0.0, 0.12) - window(u, 0.7, 0.85)))))
        W.set("sash", T((0, 0, (M.HOOD["working"] - 30) * (1 - window(u, 0.85, 1.0)))))
        person_at(W, 1120 - 1200 * window(u, 0.0, 0.15) + 1150 * window(u, 0.5, 0.7), -220, 0, 1.0)
    S.gauges = gauges("EB B125", "inside the hood -> bench", "tub lid")
    S.step("2.17", "Wipe the outside of the barium vials and their holder in the hood, then carry the holder "
                   "straight to the tub; the bench holder joins it. Lid on. Outer gloves off in the hood, liner and wipes into the "
                   "barium waste, sash fully down. Leave the hood as you found it.",
           6.0, update=pack, cam_to=CAM_PACK, hold=2.0, still=True)
    S.save()


# ============================================================================================ chapter 3
def sop3(part=None):
    if part == "a":
        S = SopScene("sop3a_load", TITLE + " · 3a Loading the OT-2 in CB 154", stop="3.7")
    elif part == "b":
        S = SopScene("sop3b_fill", TITLE + " · 3b The fill and the seal", start="3.8")
    else:
        S = SopScene("sop3_load", TITLE + " · 3 Loading the OT-2 in CB 154")
    W = World(S)
    stocks_done(W)
    racks_in_tub(W, at_cb=True)
    W.show("fov", 0.0)
    head_to(W, 330, 330, 260)
    person_at(W, Wd.BENCH_CB[0], -1600, 0, 1.0)
    S.cam = [(CB_X + 700, -3400, 3300), (CB_X + 450, 420, 900), UP]
    S.view_angle = 30
    S.gauges = gauges("CB 154", "side bench", "-", [("before", "OT-2 calibrated, Pi on 27 W")])
    S.step("3.1", "Before the day: the OT-2 calibrated (deck, tip length, pipette offset, then Labware Position "
                  "Check), the Pi 5 on its 27 W supply, the camera's exposure and white balance locked, the rail "
                  "lights on with no off timer, and the capture job tested.",
           2.6, update=walk(W, (Wd.BENCH_CB[0], -1600, 0), (OT2_AT[0] + 760, -380, 0)), hold=2.4,
           cam_to=[(CB_X + 700, -3400, 3300), (CB_X + 450, 420, 900), UP],
           labels=[("tub with both holders", (Wd.BENCH_CB[0] + 30, 330, BT + 170), (0.86, 0.26)),
                   ("lid camera + Pi 5", tuple(W.world_of("lidcam", (W.lens[0], W.lens[1], W.lens[2] + 70))), (0.30, 0.16))])
    S.gauges = gauges("CB 154", "at the OT-2", "OT-2 door")
    S.step("3.2", "Open the OT-2's door. The colour sensor stays parked in its charging station in slot 10, and "
                  "nothing else drives the robot while the protocol runs (one controller at a time). The "
                  "heater-shaker sits in slot 7, under the lid camera.",
           2.6, update=seq(door(W, True), lambda u: W.show("person", 1 - u)), cam_to=CAM_DECK, hold=1.4,
           labels=[("colour sensor in its\ncharging station (slot 10)", tuple(W.world_of("sensor", (*M.WCS_A2[:2], 104))), (0.12, 0.30)),
                   ("lid camera (Pi HQ\n+ Pi 5) over slot 7", tuple(W.world_of("lidcam", (W.lens[0], W.lens[1], W.lens[2] + 70))), (0.40, 0.10)),
                   ("heater-shaker\n(slot 7)", tuple(W.world_of("ot2", tuple(M.deck(X7, Y7 - 40, 60)))), (0.12, 0.66))])
    paper_w = W.S.world("paper")
    plate_w = W.S.world("plate")
    side = T((Wd.BENCH_CB[0] - 250, 120, BT))

    def plate_in(u):
        W.show("paper", window(u, 0, 0.1))
        W.show("plate", window(u, 0.25, 0.3))
        W.show("plate_lid", window(u, 0.25, 0.3))
        W.set_world("paper", carry(paper_w @ T((0, -300, 220)), paper_w, window(u, 0.0, 0.3), 0))
        W.set_world("plate", carry(plate_w @ T((0, -320, 240)), plate_w, window(u, 0.3, 0.65), 0))
        lw = window(u, 0.7, 1.0)
        if lw > 0:
            W.set("plate_lid", T((0, -260 * lw, 60 * math.sin(math.pi * lw) + 30 * lw)))
            W.show("plate_lid", 1 - window(u, 0.9, 1.0))
        W.S.alpha["fov"] = 0.22 * window(u, 0.1, 0.3)
    S.gauges = gauges("CB 154", "on the deck", "plate lid", [("slot 7", "heater-shaker + flat adapter")])
    S.step("3.3", "Slot 7, on the heater-shaker's 96 flat-bottom adapter: black paper cut to the adapter, then the "
                  "NEST 96-well plate with A1 at the back left; close the labware latch. Take the plate's lid off "
                  "only now. The yellow cone is what the camera sees.",
           3.4, update=plate_in, cam_to=CAM_DECK2, hold=1.2)

    def tips_in(u):
        W.show("tiprack", window(u, 0, 0.1))
        W.show("tiprack_lid", window(u, 0, 0.1) * (1 - window(u, 0.85, 1.0)))
        tr = W.base["tiprack"]
        W.set("tiprack", carry(tr @ T((0, -330, 240)), tr, window(u, 0.0, 0.5), 0))
        W.set("tiprack_lid", T((0, -320 * window(u, 0.55, 1.0), 90 * math.sin(math.pi * window(u, 0.55, 1.0)))))
    S.gauges = gauges("CB 154", "on the deck", "tip-rack lid")
    S.step("3.4", "A full rack of Opentrons 300 uL tips in slot 6 (the P300 is the only pipette). Lid off.",
           2.6, update=tips_in, hold=0.8)
    tub_w = W.S.world("tub")
    rh0, rb0 = W.S.world("rack_hood"), W.S.world("rack_bench")
    x4, y4 = M.slot_centre(4)
    x5, y5 = M.slot_centre(5)
    rh1 = W.S.world("ot2") @ T(M.deck(x4, y4, 0))
    rb1 = W.S.world("ot2") @ T(M.deck(x5, y5, 0))

    def racks_on(u):
        W.set("tub_lid", T((0, 0, 150 + 220 * window(u, 0.0, 0.1))))
        W.set_world("rack_hood", carry(rh0, rh1, window(u, 0.1, 0.5), 260))
        W.set_world("rack_bench", carry(rb0, rb1, window(u, 0.45, 0.9), 260))
        person_at(W, OT2_AT[0] + 760, -380, 0, 0.0)
    S.gauges = gauges("CB 154", "side bench -> deck", "tub lid")
    S.step("3.5", "Lift the two vial holders out of the tub and onto the deck as they are, A1 at the back left: barium "
                  "chloride in slot 4; sodium sulfate, the 5 M NaCl and the DI water in slot 5, in the positions the "
                  "protocol's map gives.",
           4.0, update=racks_on, cam_to=CAM_DECK, hold=0.6,
           labels=[("slot 4: BaCl2 x4", tuple(W.world_of("ot2", tuple(M.deck(x4, y4, 75)))), (0.14, 0.40)),
                   ("slot 5: Na2SO4 x4,\n5 M NaCl, DI water", tuple(W.world_of("ot2", tuple(M.deck(x5, y5, 75)))), (0.62, 0.86))])
    W.reparent("rack_hood", "ot2")
    W.reparent("rack_bench", "ot2")
    wipe = W.S.world("wipe")
    order = ["ba0", "ba1", "ba2", "ba3", "so0", "so1", "so2", "so3", "nacl", "water"]
    cap_home = {}
    for i, k in enumerate(order):
        cap_home[k] = wipe @ T((-120 + (i % 5) * 60, 40 - (i // 5) * 80, 0)) @ R((1, 0, 0), 180, (0, 0, M.VIAL_CAP_TOP / 2))
    starts = {k: W.S.world(f"t_{k}_cap") for k in order}

    def uncap(u):
        for i, k in enumerate(order):
            w = window(u, 0.04 + i * 0.085, 0.04 + i * 0.085 + 0.12)
            if w <= 0:
                continue
            spin = R((0, 0, 1), -540 * min(w / 0.3, 1.0))
            lifted = starts[k] @ T((0, 0, 10 * min(w / 0.3, 1.0))) @ spin
            dest = cap_home[k]
            W.set_world(f"t_{k}_cap", lifted if w < 0.3 else carry(lifted, dest, (w - 0.3) / 0.7, 200))
    S.gauges = gauges("CB 154", "on the deck", "the ten stock vials")
    S.step("3.6", "Uncap the ten vials one at a time, here on the deck and only now. Each cap goes top-down on a "
                  "clean wipe, in the same order, so it goes back on its own vial.",
           5.4, update=uncap, cam_to=[(OT2_AT[0] + 520, -900, 1650), (OT2_AT[0] + 330, 330, 900), UP], hold=0.8)

    def close_start(u):
        door(W, False)(window(u, 0.0, 0.6))
        W.show("person", 0.0)
        S.gauges = gauges("CB 154", "at the OT-2", "-", [("capture", "running: 1 still/min"),
                                                         ("protocol", "started" if u > 0.6 else "-")])
    S.step("3.7", "Close the door. Start the capture job on the Pi first, so the record covers the filling too, then "
                  "start the protocol (simulated beforehand with opentrons_simulate).",
           2.6, update=close_start, cam_to=CAM_CB, hold=1.2)
    # ---- the fill
    pm = plate_a()
    vols = {}
    for (r, c), w in pm.items():
        nacl = 40.0 if w["nacl"] else 0.0
        ba = 0.0 if w["ba"] == 0 else (60.0 if w["ba"] == 3.0 else 20.0)
        so = 0.0 if w["so"] == 0 else (60.0 if w["so"] == 3.0 else 20.0)
        vols[(r, c)] = dict(water=200.0 - nacl - ba - so, nacl=nacl, ba=ba, so=so)
    ORDER_K = ("water", "nacl", "ba", "so")

    def set_well(rc, ul):
        r, c = rc
        h = max(0.3, 5.26 * ul / 200.0)
        x, y = Wd.well_xy(r, c)
        S.set_mesh(f"well_{r}_{c}", M.cyl(x, y, Wd.WELL_BOTTOM, Wd.PLATE_WELL_R - 0.15, h, res=20))
        S.alpha[f"well_{r}_{c}"] = 1.0 if ul > 0 else 0.0

    passes = [("water", "water", "DI water", (5, 5)), ("nacl", "nacl", "5 M NaCl", (5, 4)),
              ("ba", "ba2", "barium chloride", (4, 2)), ("so", "so2", "sodium sulfate, last", (5, 2))]
    tip_i = [0]

    def fill_pass(kind, tube_key, slot_hole, detailed=2):
        wells = sorted([rc for rc in pm if vols[rc][kind] > 0], key=lambda rc: (rc[1], rc[0]))
        tx, ty = tube_deck_xy(*slot_hole)
        surf = Wd.TUBE_Z_IN_RACK + M.ml_to_level(W.tube_level[tube_key]) - 8
        ti = tip_i[0]
        tip_i[0] += 1 if kind != "so" else len(wells)
        px, py = tip_xy(ti)
        x12, y12 = M.slot_centre(12)
        trash = (x12 + 20, y12 + 10, 180)
        pick = [(px, py, SAFE_Z), (px, py, 56.0 + TIP_DROP - TIP_DROP), (px, py, SAFE_Z)]
        legs = pick[:]
        for rc in wells[:detailed]:
            wx, wy = well_deck(*rc)
            legs += [(tx, ty, SAFE_Z), (tx, ty, surf + TIP_DROP - 10), (tx, ty, SAFE_Z), (wx, wy, SAFE_Z),
                     (wx, wy, Wd.PLATE_TOP + 3 + TIP_DROP), (wx, wy, SAFE_Z)]
        nd = len(legs)
        f_detail = head_path(W, legs)
        wx_l, wy_l = well_deck(*wells[-1])
        f_rest = head_path(W, [legs[-1], (tx, ty, SAFE_Z), (wx_l, wy_l, SAFE_Z), trash, (330, 330, 260)])

        def f(u):
            if u < 0.6:
                v = u / 0.6
                f_detail(v)
                k = v * (nd - 1)
                W.S.alpha["ot2_tip"] = 1.0 if k >= 1.0 else 0.0
                for j, rc in enumerate(wells[:detailed]):
                    if k >= 3 + 6 * j + 4.3:
                        set_well(rc, sum(vols[rc][q] for q in ORDER_K[:ORDER_K.index(kind) + 1]))
            else:
                v = (u - 0.6) / 0.4
                f_rest(v)
                W.S.alpha["ot2_tip"] = 0.0 if v > 0.8 else 1.0
                n = len(wells)
                upto = int(round(detailed + (n - detailed) * min(v / 0.75, 1.0)))
                for rc in wells[:upto]:
                    set_well(rc, sum(vols[rc][q] for q in ORDER_K[:ORDER_K.index(kind) + 1]))
        return f

    for kind, tube_key, name, slot_hole in passes:
        n = sum(1 for rc in pm if vols[rc][kind] > 0)
        cap = {"water": f"{n} wells: DI water first, one tip for the pass, dispensing from above.",
               "nacl": f"{n} wells: 40 uL of 5 M NaCl (1 molal in 200 uL). Barium chloride and sodium sulfate come from "
                       "the 0.1 M, 10, 1 and 0.1 mM vials: 20 uL gives 1/10 of the stock, 60 uL of 10 mM gives 3 mM.",
               "ba": f"{n} wells: barium chloride, from the vial each well needs (shown: 1 mM). A dose under 20 uL, "
                     "the P300's minimum, stops the protocol instead of becoming zero.",
               "so": f"{n} wells: sodium sulfate last, a new tip for every well, dispensed from above the liquid, so no "
                     "tip that touched barium goes back into a stock. Each well's start time comes from the run log."}[kind]
        S.gauges = gauges("CB 154", "OT-2 running", "door closed", [("pass", name), ("capture", "1 still/min")])
        S.step(f"3.{8 + passes.index((kind, tube_key, name, slot_hole))}", cap, 8.0 if kind in ("water", "so") else 6.0,
               update=fill_pass(kind, tube_key, slot_hole, detailed=2 if kind in ("water", "so") else 1),
               cam_to=CAM_FILL if kind == "water" else None,
               hold=0.6)
    # seal at the pause
    seal_w = W.S.world("seal")

    def seal(u):
        door(W, True)(window(u, 0.0, 0.2))
        W.show("seal", window(u, 0.25, 0.3))
        W.set_world("seal", carry(seal_w @ T((0, -260, 200)), seal_w, window(u, 0.25, 0.65), 0))
        door(W, False)(window(u, 0.8, 1.0)) if u > 0.8 else None
        W.show("person", 0.0)
    S.gauges = gauges("CB 154", "on the deck", "OT-2 door", [("protocol", "paused: seal")])
    S.step("3.12", "At the pause: open the door, lay a clear adhesive seal over the plate and press it down well by "
                   "well, then close the door and resume. Log the time. Over days an open well would lose water and "
                   "concentrate both salts.",
           5.0, update=seal, cam_to=CAM_FILL, hold=1.0)

    def recap(u):
        door(W, True)(window(u, 0.0, 0.15))
        for i, k in enumerate(order):
            w = window(u, 0.15 + i * 0.06, 0.15 + i * 0.06 + 0.12)
            if w > 0:
                W.set_world(f"t_{k}_cap", carry(cap_home[k], starts[k], w, 200))
        door(W, False)(window(u, 0.85, 1.0)) if u > 0.85 else None
        S.gauges = gauges("CB 154", "on the deck", "-", [("protocol", "done; head parked"),
                                                         ("lights", "rail lights on, no timer")])
    S.step("3.13", "When the protocol ends: recap each vial from its place on the wipe (leftover stocks go to the "
                   "barium waste at the end of the run), close the door, and leave the rail lights on. The head parks "
                   "away from slot 7 so the camera has a clear view.",
           4.4, update=recap, cam_to=CAM_DECK, hold=1.6, still=True)
    S.save()


# ============================================================================================ chapter 4
def sop4():
    S = SopScene("sop4_monitor", TITLE + " · 4 Watching it for 72 h")
    W = World(S)
    stocks_done(W)
    racks_in_tub(W, at_cb=True)
    for g in ("paper", "plate", "tiprack", "seal"):
        W.show(g)
    W.show("fov", 0.0)
    W.set("tub_lid", T((0, 0, 150)))
    x4, y4 = M.slot_centre(4)
    x5, y5 = M.slot_centre(5)
    W.reparent("rack_hood", None)
    W.reparent("rack_bench", None)
    W.set_world("rack_hood", W.S.world("ot2") @ T(M.deck(x4, y4, 0)))
    W.set_world("rack_bench", W.S.world("ot2") @ T(M.deck(x5, y5, 0)))
    head_to(W, 330, 330, 260)
    pm = plate_a()
    for (r, c), w in pm.items():
        x, y = Wd.well_xy(r, c)
        S.set_mesh(f"well_{r}_{c}", M.cyl(x, y, Wd.WELL_BOTTOM, Wd.PLATE_WELL_R - 0.15, 5.26, res=20))
        S.alpha[f"well_{r}_{c}"] = 1.0
        S.base_alpha[f"well_{r}_{c}"] = 0.22
    person_at(W, OT2_AT[0] + 900, -900, 0, 0.0)
    lens_world = (W.S.world("ot2") @ np.array([*W.lens, 1.0]))[:3]
    plate_world = (W.S.world("ot2") @ np.array([*M.deck(*Wd.PLATE_XY, Wd.PLATE_TOP), 1.0]))[:3]
    S.cam = CAM_CB
    S.view_angle = 30
    S.gauges = gauges("CB 154", "OT-2, door closed", "-", [("t", "0 min after the last sulfate")])
    S.step("4.1", "The lid camera (Raspberry Pi HQ camera, 8-50 mm zoom, Pi 5) looks straight down through the top "
                  "window at the plate on the heater-shaker, 69 mm closer than a plate on the deck, so refocus it "
                  "first. Stills every minute until 30 min after the last sulfate, every 5 min until 6 h, then every "
                  "15 min: about 400 in 72 h.",
           3.2, update=lambda u: W.S.alpha.__setitem__("fov", 0.25 * u),
           cam_to=[(OT2_AT[0] - 760, -760, 2250), (OT2_AT[0] - 130, 440, 1130), UP], hold=2.4,
           labels=[("lid camera", tuple(lens_world + (0, 0, 60)), (0.70, 0.16)),
                   (f"its view: about\n{W.fov_mm[0]:.0f} x {W.fov_mm[1]:.0f} mm", tuple(plate_world), (0.70, 0.62))])
    cam_view = [tuple(lens_world - (0, 0, 4)), tuple(plate_world), (0, 1, 0)]

    def to_cam(u):
        W.S.alpha["fov"] = 0.25 * (1 - u)
        W.S.base_alpha["plate:polystyrene"] = 0.55 - 0.33 * u      # clear wells look dark on the black paper
        W.S.base_alpha["seal:s"] = 0.35 - 0.25 * u
        W.show("lidcam", 1.0 - window(u, 0.6, 0.9))
        for n in W.S.members("ot2"):
            if "TOP WINDOW" in n:
                W.S.alpha[n] = 1.0 - window(u, 0.6, 0.9)
    S.gauges = gauges("CB 154", "the camera's view", "-", [("t", "0 min")])
    S.step("4.2", "Its view: about 200 pixels across each well. Clear wells look dark on the black paper; barium "
                  "sulfate shows as white.", 2.6, update=to_cam, cam_to=cam_view, view_angle_to=11.0, hold=1.0)
    # time-lapse: t from 0 to 72 h on a log-ish clock
    onsets = {rc: onset_min(w["si"]) for rc, w in pm.items()}
    whites = {rc: whiteness(w) for rc, w in pm.items()}
    base_col = np.array(M.MATS["solution"][:3])

    def clock(u):
        # minutes since the last sulfate: 0 -> 4320 (72 h), slow at first
        return 4320.0 * (10 ** (3 * u) - 1) / (10 ** 3 - 1)

    def fmt(t):
        if t < 60:
            return f"{t:4.0f} min"
        h = t / 60
        return f"{h:4.1f} h" if h < 10 else f"{h:4.0f} h"

    def every(t):
        return "1 min" if t < 30 else ("5 min" if t < 360 else "15 min")

    def n_stills(t):
        if t < 30:
            return 45 + int(t)
        if t < 360:
            return 75 + int((t - 30) / 5)
        return 141 + int((t - 360) / 15)

    def lapse(u):
        t = clock(u)
        for rc, w in pm.items():
            r, c = rc
            o = onsets[rc]
            k = 0.0 if o is None else float(np.clip((math.log10(max(t, 1e-3)) - math.log10(o)) / 0.8 + 0.15, 0, 1))
            k *= whites[rc]
            col = base_col + (np.array([0.98, 0.98, 0.98]) - base_col) * k
            S.color[f"well_{r}_{c}"] = tuple(col)
            S.base_alpha[f"well_{r}_{c}"] = 0.22 + 0.78 * k
        S.gauges = gauges("CB 154", "the camera's view", "-", [("t", fmt(t) + " after the last sulfate"),
                                                               ("stills", f"every {every(t)}, {n_stills(t)} so far")])
    S.step("4.3", "Illustrative timing: wells with the highest saturation index (PHREEQC, 10-30 table) turn white "
                  "within minutes, those near +1 take hours, and those at or below 0 never should. The real times "
                  "are what this run measures.",
           12.0, update=lapse, hold=2.0, still=True)

    def back(u):
        W.show("lidcam", window(u, 0.0, 0.3))
        W.S.base_alpha["plate:polystyrene"] = 0.22 + 0.33 * u
        W.S.base_alpha["seal:s"] = 0.10 + 0.25 * u
        for n in W.S.members("ot2"):
            if "TOP WINDOW" in n:
                W.S.alpha[n] = window(u, 0.0, 0.3)
    S.gauges = gauges("CB 154", "once a day", "-", [("t", "24 h, 48 h, 72 h")])
    S.step("4.4", "Once a day, someone checks the stream and the heartbeat and writes anything that happened in the "
                  "event log: a door opened, a reboot, a missed still. The Pi's 05:00, 13:00 and 21:00 reboots are "
                  "held off while the run's lock is on.",
           2.8, update=back, cam_to=CAM_CB, view_angle_to=30.0, hold=2.0)
    plate_w0 = W.S.world("plate")
    out = T((Wd.BENCH_CB[0] - 250, 160, BT))

    def end(u):
        door(W, True)(window(u, 0.0, 0.2))
        W.set_world("plate", carry(plate_w0, out, window(u, 0.25, 0.6), 300))
        door(W, False)(window(u, 0.85, 1.0)) if u > 0.85 else None
        person_at(W, OT2_AT[0] + 760, -380, 0, 0.0)
    S.gauges = gauges("CB 154", "OT-2 -> side bench", "OT-2 door", [("t", "72 h: last still taken")])
    S.step("4.5", "At 72 h: take a last still, then take the plate out, weigh it (start and end weights give the "
                   "water lost) and photograph it on black with a phone, as in March.",
           4.0, update=end, cam_to=[(Wd.BENCH_CB[0] - 100, -1300, 1800), (OT2_AT[0] + 500, 420, 950), UP], hold=1.2)

    def waste(u):
        W.set_world("plate", carry(out, W.S.world("ba_waste_cb") @ T((0, -150, 260)) @ R((1, 0, 0), -60), window(u, 0.0, 0.5), 200))
        W.show("plate", 1 - window(u, 0.6, 0.8))
        S.gauges = gauges("CB 154", "side bench", "barium waste", [("files", "experiments/004-baso4-monitoring/<run-id>/")])
    S.step("4.6", "The plate's wells, the leftover stocks and the rinses go in the labelled barium waste; Risk "
                  "Management collects it. The run record, plate map, well start times, stills index and the "
                  "environment and event logs go in the repo; the stills go to the agreed storage.",
           4.0, update=waste, hold=2.6, still=True)
    S.save()


# ------------------------------------------------------------------------------------------- full
CHAPTERS = {"sop1": sop1, "sop2": sop2, "sop3": sop3, "sop4": sop4,
            "sop2a": lambda: sop2("a"), "sop2b": lambda: sop2("b"), "sop3a": lambda: sop3("a"), "sop3b": lambda: sop3("b")}
PARTS = ["sop1_where", "sop2a_hood", "sop2b_bench", "sop3a_load", "sop3b_fill", "sop4_monitor"]


def full():
    names = PARTS
    lst = OUT / "mp4" / "concat.txt"
    lst.write_text("".join(f"file '{n}.mp4'\n" for n in names))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    str(OUT / "mp4" / "baso4_sop_full.mp4")], check=True)
    lst.unlink()
    print("full:", (OUT / "mp4" / "baso4_sop_full.mp4").stat().st_size / 1e6, "MB")


if __name__ == "__main__":
    for arg in sys.argv[1:] or list(CHAPTERS):
        if arg == "full":
            full()
        else:
            try:
                CHAPTERS[arg]()
            except StopChapter as stop:
                stop.args[0].save() if stop.args else None
