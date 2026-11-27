"""A second, independent check of plate A's protocol (PR 84), in the Opentrons simulator, with every planned
gantry move recorded. Written separately from check_protocol.py, by a run that didn't write the protocol.

    pip install opentrons==8.8.1                       # the robot's version; needs Python 3.10-3.12
    python check_independent.py baso4_plate_a.py [--mix=on|off] [--hs=on|off] [--vial-id=24.4] [--start=sop|low]

Records every pipette action (from the protocol's side) and every gantry move (from the hardware side), then checks:
  - each plate well's composition against plate A's design (84 wells: 48 + 16 + 8 + 8 + 4), and 200 uL in each;
  - sulfate last in every well; a fresh tip for every sulfate well; no tip back into a stock after it touched
    liquid in a well that had the other salt in it;
  - every volume >= 20 uL (P300 GEN2);
  - in the vials: the tip end stays under the liquid, using the SOP's own start volumes, and the top of the tip
    stays above the rim;
  - every straight travel move that crosses slot 10, and how high the tip end is there (the colour sensor's
    charging station is about 97 mm tall, its parked sensor about 100 mm);
  - where the pause, the latch and the lights come.
"""
import collections, inspect, io, json, math, re, sys

from opentrons import simulate, types
from opentrons.protocol_api import ProtocolContext
from opentrons.protocol_api.core.engine.instrument import InstrumentCore

ARGS = dict(a[2:].split("=", 1) for a in sys.argv[2:] if a.startswith("--"))
PROTO = sys.argv[1]
VIAL_ID = float(ARGS.get("vial-id", 24.4))
TIP_EFFECTIVE = 59.3 - 7.47

# Start volumes (uL) from the SOP's own recipes and Tim's 13.5 g dilution vials ('sop'), or a deliberately low case
SOP_START = {"BaCl2 0.1 M": 13780, "BaCl2 10 mM": 13530, "BaCl2 1 mM": 13500, "BaCl2 0.1 mM": 15000,
             "Na2SO4 0.1 M": 13600, "Na2SO4 10 mM": 13520, "Na2SO4 1 mM": 13500, "Na2SO4 0.1 mM": 15000,
             "NaCl 5 M": 14990, "DI water": 15000}
if ARGS.get("start") == "low":       # the low ends of what the SOP allows: 1.4 g transfers... and 14 g of water
    SOP_START.update({"DI water": 14000})
STOCKS = {
    "4": {"A1": ("BaCl2 0.1 M", 100.0, 0, 0), "A2": ("BaCl2 10 mM", 10.0, 0, 0),
          "A3": ("BaCl2 1 mM", 1.0, 0, 0), "B1": ("BaCl2 0.1 mM", 0.1, 0, 0)},
    "5": {"A1": ("Na2SO4 0.1 M", 0, 100.0, 0), "A2": ("Na2SO4 10 mM", 0, 10.0, 0),
          "A3": ("Na2SO4 1 mM", 0, 1.0, 0), "B1": ("Na2SO4 0.1 mM", 0, 0.1, 0),
          "B2": ("NaCl 5 M", 0, 0, 5.0), "B3": ("DI water", 0, 0, 0)},
}
SLOT10 = (0.0, 128.0, 271.5, 357.5)      # x0, x1, y0, y1 on the OT-2 deck (ot2_standard deck definition)
SENSOR_POST = (92.8, 316.5)              # the parked sensor's post (byu-vcl 10-14 README, via models.py)
# The colour sensor's charging station in slot 10 (Acceleration Consortium CAD at 07efedd, placed as models.py does):
# its enclosure's top edge is 97 mm above the deck, over x 3.1-124.9 and y 274.8-354.2 (front edge at y 274.8);
# the parked sensor's post reaches 100 mm.
STATION_TOP, STATION_BOX = 97.0, (3.1, 124.9, 274.8, 354.2)

EV = []


def where(loc):
    if loc is None or not isinstance(loc, types.Location):
        return None, None, None, None
    lw_or_well = loc.labware
    well = lw_or_well.as_well() if lw_or_well.is_well else None
    lw = lw_or_well.as_labware() if lw_or_well.is_labware else (well.parent if well is not None else None)
    slot = None
    if lw is not None:
        p = lw.parent
        while p is not None and not isinstance(p, str):
            p = getattr(p, "parent", None)
        slot = p
    return slot, (lw.load_name if lw is not None else None), (well.well_name if well is not None else None), well


def wrap(name):
    orig = getattr(InstrumentCore, name)
    sig = inspect.signature(orig)

    def f(self, *a, **k):
        b = sig.bind(self, *a, **k)
        args = b.arguments
        loc = args.get("location")
        slot, ln, wn, well = where(loc)
        ev = dict(kind=name, volume=args.get("volume"), slot=slot, labware=ln, well=wn,
                  point=(tuple(round(c, 2) for c in loc.point) if isinstance(loc, types.Location) else None),
                  in_place=args.get("in_place"), flow_rate=args.get("flow_rate"), speed=args.get("speed"))
        if well is not None:
            ev["bottom_z"] = round(well.bottom().point.z, 2)
            ev["top_z"] = round(well.top().point.z, 2)
            ev["diameter"] = well.diameter
        EV.append(ev)
        return orig(self, *a, **k)
    setattr(InstrumentCore, name, f)


for n in ["aspirate", "dispense", "blow_out", "touch_tip", "pick_up_tip", "drop_tip", "move_to", "air_gap_in_place"]:
    wrap(n)


def ctxwrap(n):
    orig = getattr(ProtocolContext, n)

    def f(self, *a, **k):
        EV.append(dict(kind="ctx_" + n, args=[str(x)[:160] for x in a]))
        return orig(self, *a, **k)
    setattr(ProtocolContext, n, f)


for n in ["pause", "comment", "set_rail_lights", "delay", "home"]:
    ctxwrap(n)

from opentrons.protocol_engine.execution import gantry_mover as _gm
for _cls in (_gm.VirtualGantryMover, _gm.HardwareGantryMover):
    def _mk(orig):
        async def _move(self, pipette_id, waypoints, speed):
            for wp in waypoints:
                EV.append(dict(kind="hw_move", xyz=(round(wp.position.x, 2), round(wp.position.y, 2), round(wp.position.z, 2)),
                               cp=str(wp.critical_point)))
            return await orig(self, pipette_id, waypoints, speed)
        return _move
    _cls.move_to = _mk(_cls.move_to)

# Parameter variants: rewrite the defaults in a copy of the source
src = open(PROTO).read()


def set_default(src, var, value):
    pat = re.compile(r'(variable_name="%s".*?default=)(True|False)' % var, re.S)
    out, n = pat.subn(lambda m: m.group(1) + value, src, count=1)
    return out if n else src


if "mix" in ARGS:
    src = set_default(src, "mix_after_sulfate", "True" if ARGS["mix"] == "on" else "False")
if "hs" in ARGS:
    src = set_default(src, "on_heater_shaker", "True" if ARGS["hs"] == "on" else "False")
runlog, _bundle = simulate.simulate(io.StringIO(src), file_name="plate_a.py")

# ------------------------------------------------------------------ replay
problems, warnings = [], []
src_of = {(s, w): v for s, d in STOCKS.items() for w, v in d.items()}
conc = {v[0]: (v[1], v[2], v[3]) for v in src_of.values()}
vol = dict(SOP_START)
plate = collections.defaultdict(collections.Counter)
plate_vol = collections.Counter()
order = collections.defaultdict(list)
tip = None
tips = 0
asp_rows, disp_rows = [], []
min_vol = 1e9
sulfate_tips = collections.Counter()
for i, e in enumerate(EV):
    k = e["kind"]
    if k == "pick_up_tip":
        tips += 1
        tip = dict(c=collections.Counter(), touched=set(), id=tips, wells=set())
    elif k == "drop_tip":
        tip = None
    elif k in ("aspirate", "dispense"):
        v = e["volume"] or 0
        if v > 0:
            min_vol = min(min_vol, v)
        if 0 < v < 20 - 1e-6:
            problems.append(f"{k} of {v} uL, under the P300's 20 uL minimum (action {i})")
        if tip is None:
            problems.append(f"{k} with no tip (action {i})")
            continue
        in_plate = bool(e["labware"] and "wellplate" in e["labware"])
        if k == "aspirate" and not in_plate:
            key = (e["slot"], e["well"])
            if key not in src_of:
                problems.append(f"aspirate from slot {e['slot']} {e['well']}, not a stock (action {i})")
                continue
            name = src_of[key][0]
            if tip["touched"]:
                touched_salts = {s for w in tip["touched"] for s in plate[w] if plate[w][s] > 0}
                bad = [s for s in touched_salts if (s.startswith("Na2SO4") and name.startswith("BaCl2")) or
                       (s.startswith("BaCl2") and name.startswith("Na2SO4"))]
                if bad:
                    problems.append(f"tip {tip['id']} goes into {name} after touching liquid with {sorted(set(bad))} (action {i})")
                else:
                    warnings.append((tip["id"], name, tuple(sorted(touched_salts))))
            area = math.pi * (VIAL_ID / 2) ** 2
            h_after = (vol[name] - v) / area
            tip_h = e["point"][2] - e["bottom_z"]
            asp_rows.append(dict(i=i, name=name, v=v, tip_h=tip_h, cover=h_after - tip_h,
                                 tip_top_vs_rim=e["point"][2] + TIP_EFFECTIVE - e["top_z"]))
            vol[name] -= v
            tip["c"][name] += v
        elif k == "aspirate" and in_plate:          # mixing in a well
            w = e["well"]
            tot = sum(plate[w].values())
            for s in list(plate[w]):
                q = v * plate[w][s] / tot
                plate[w][s] -= q
                tip["c"][s] += q
            plate_vol[w] -= v
            tip["touched"].add(w)
        elif k == "dispense" and in_plate:
            w = e["well"]
            tot = sum(tip["c"].values())
            if tot <= 1e-9:
                problems.append(f"dispense into {w} from an empty tip (action {i})")
                continue
            area_w = math.pi * (e["diameter"] / 2) ** 2
            before = plate_vol[w] / area_w
            after = (plate_vol[w] + v) / area_w
            tip_h = e["point"][2] - e["bottom_z"]
            main = max(tip["c"], key=lambda s: tip["c"][s])
            for s in list(tip["c"]):
                q = v * tip["c"][s] / tot
                plate[w][s] += q
                tip["c"][s] -= q
            plate_vol[w] += v
            gap_after = tip_h - after
            # A dispense with the tip end within ~1.5 mm of the liquid it makes: count it as touching (a hanging
            # drop bridges that gap), so that tip is checked for going back into a stock
            if gap_after < 1.5 or e.get("in_place"):
                tip["touched"].add(w)
            if not e.get("in_place"):
                order[w].append((i, main, v))
                disp_rows.append(dict(i=i, well=w, main=main, v=v, tip_h=tip_h, before=before, after=after))
                if main.startswith("Na2SO4"):
                    sulfate_tips[tip["id"]] += 1
        elif k == "dispense":                       # back into a vial or the trash
            tot = sum(tip["c"].values())
            if tot:
                for s in list(tip["c"]):
                    tip["c"][s] -= v * tip["c"][s] / tot

# ------------------------------------------------------------------ design
LEV = (0.01, 0.1, 1.0, 3.0)
design = collections.Counter()
for ba in LEV:
    for so in LEV:
        design[(ba, so, 1.0)] += 3
        design[(ba, so, 0.0)] += 1
for lv in LEV:
    design[(lv, 0.0, 1.0)] += 1
    design[(0.0, lv, 1.0)] += 1
design[(0.0, 0.0, 0.0)] += 4
design[(0.0, 0.0, 1.0)] += 4
design[(10.0, 10.0, 1.0)] += 4
got = collections.Counter()
for w, s in plate.items():
    V = sum(s.values())
    if abs(V - 200) > 0.01:
        problems.append(f"well {w} ends at {V:.2f} uL")
    got[tuple(round(sum(q * conc[n][j] for n, q in s.items()) / V, 4) for j in range(3))] += 1

print(f"== {PROTO} | mix={ARGS.get('mix', 'default')} hs={ARGS.get('hs', 'default')} | vial ID {VIAL_ID} mm | {len(EV)} recorded events")
print(f"tips: {tips}; smallest volume {min_vol} uL; wells filled {len(plate)}")
miss, extra = design - got, got - design
print("plate design:", "matches plate A exactly (84 wells: 48 + 16 + 8 + 8 + 4)" if not miss and not extra else f"DIFFERS: missing {dict(miss)} extra {dict(extra)}")
if miss or extra:
    problems.append("the plate's composition differs from plate A")
not_last = [w for w, seq in order.items() if any(m.startswith("Na2SO4") for _, m, _ in seq) and not seq[-1][1].startswith("Na2SO4")]
if not_last:
    problems.append(f"sulfate isn't the last addition in {not_last}")
n_so_wells = sum(1 for seq in order.values() if any(m.startswith("Na2SO4") for _, m, _ in seq))
multi = [t for t, n in sulfate_tips.items() if n > 1]
print(f"sulfate wells: {n_so_wells}; tips used for more than one sulfate well: {len(multi)}")
if multi:
    problems.append(f"{len(multi)} sulfate tips go into more than one well")
print(f"tips that went back into a stock after touching a well (harmless pairs only): {len(set(w[:2] for w in warnings))} tip/stock pairs, "
      f"e.g. {sorted(set(warnings))[:3]}")

print("\nin the vials (start volumes from the SOP; inner diameter %.1f mm):" % VIAL_ID)
by = collections.defaultdict(list)
for r in asp_rows:
    by[r["name"]].append(r)
for name in sorted(by):
    rows = by[name]
    print(f"  {name:14s} {len(rows):3d} draws, {sum(r['v'] for r in rows):6.0f} uL; tip end {min(r['tip_h'] for r in rows):5.1f}-{max(r['tip_h'] for r in rows):5.1f} mm "
          f"above the floor; under the surface by {min(r['cover'] for r in rows):4.1f}-{max(r['cover'] for r in rows):4.1f} mm after each draw; "
          f"tip top {min(r['tip_top_vs_rim'] for r in rows):4.1f} mm above the rim at the deepest; left {vol[name]:6.0f} uL")
    if min(r["cover"] for r in rows) < 0.5:
        problems.append(f"{name}: the tip end may leave the liquid ({min(r['cover'] for r in rows):.1f} mm)")
    if min(r["tip_top_vs_rim"] for r in rows) < 0:
        problems.append(f"{name}: the top of the tip goes below the rim")

print("\nin the wells: tip end above the liquid it makes, per kind of dispense (mm):")
byk = collections.defaultdict(list)
for r in disp_rows:
    byk[r["main"].split()[0]].append(r["tip_h"] - r["after"])
for kname, gaps in byk.items():
    print(f"  {kname:7s} {len(gaps):3d} dispenses: {min(gaps):.2f} to {max(gaps):.2f}")

# ------------------------------------------------------------------ travel over slot 10
moves = [e for e in EV if e["kind"] == "hw_move"]
cross = []
prev = None
for m in moves:
    if prev is not None:
        (x0, y0, z0), (x1, y1, z1) = prev["xyz"], m["xyz"]
        if abs(z1 - z0) < 0.01 and (abs(x1 - x0) > 0.01 or abs(y1 - y0) > 0.01):
            # sample the segment and find where it is over slot 10
            pts = [(x0 + (x1 - x0) * t / 200, y0 + (y1 - y0) * t / 200) for t in range(201)]
            inside = [(x, y) for x, y in pts if SLOT10[0] <= x <= SLOT10[1] and SLOT10[2] <= y <= SLOT10[3]]
            if inside:
                dmin = min(math.hypot(x - SENSOR_POST[0], y - SENSOR_POST[1]) for x, y in inside)
                over_station = [(x, y) for x, y in inside if STATION_BOX[0] <= x <= STATION_BOX[1] and STATION_BOX[2] <= y <= STATION_BOX[3]]
                cross.append(dict(z=z0, from_=(x0, y0), to=(x1, y1), cp=m["cp"], n=len(inside), dmin=dmin,
                                  over_station=bool(over_station)))
    prev = m
zs = sorted(set(round(m["xyz"][2], 1) for m in moves))
travel = collections.Counter(round(c["z"], 1) for c in cross)
print(f"\ngantry moves: {len(moves)}; travel heights used: {sorted(set(round(a['xyz'][2], 1) for a, b in zip(moves, moves[1:]) if abs(a['xyz'][2] - b['xyz'][2]) < 0.01 and a['xyz'][:2] != b['xyz'][:2]))[-6:]}")
print(f"straight moves that pass over slot 10: {len(cross)}" + (f"; heights (critical point) {dict(travel)}; closest approach to the parked sensor's post "
      f"{min(c['dmin'] for c in cross):.0f} mm" if cross else ""))
if cross:
    ex = min(cross, key=lambda c: c["dmin"])
    print(f"  e.g. from {ex['from_']} to {ex['to']} at z {ex['z']} ({ex['cp']})")
    n_hit = sum(1 for c in cross if c["over_station"] and c["z"] < STATION_TOP)
    print(f"  {n_hit} of them pass over the charging station's footprint with the tip end below its {STATION_TOP:.0f} mm top: "
          "slot 10 must be EMPTY (the robot doesn't know about anything the protocol doesn't load)")

ctxs = [(i, e["kind"][4:], (e.get("args") or [""])[0][:90]) for i, e in enumerate(EV) if e["kind"] in ("ctx_pause", "ctx_set_rail_lights")]
print("\npause and lights:", ctxs)
first_asp = next(i for i, e in enumerate(EV) if e["kind"] == "aspirate")
print("first aspirate at event", first_asp)
print("\n" + ("PROBLEMS:\n  - " + "\n  - ".join(problems[:30]) if problems else "no problems found by these checks"))
