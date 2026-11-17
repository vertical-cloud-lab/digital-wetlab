"""Checks plate A's protocol before it goes to the robot. Simulation only: nothing here talks to an OT-2.

    pip install opentrons==8.8.1            # the robot's own version (byu-vcl, wireless-color-sensor/ot2/README.md)
    python check_protocol.py                # from this folder; writes plate_map.csv and check_output.txt

What it checks:
  1. the holder definition inside the protocol is the one in ../cad/byuvcl_6_vialholder_20ml/1.json;
  2. the plate map is the SOP animation's plate A (animate.plate_a(), seed 80): 84 wells, the right counts;
  3. opentrons_simulate runs it, with the mix on and with it off;
  4. every well gets 200 uL, every dose is at least 20 uL, and the tips number at most 96;
  5. the tip never goes more than 46.5 mm below a vial's rim, and never below 1 mm above a well's floor;
  6. no sulfate tip goes back into a vial after it has been in a well;
and estimates how long the run takes.
"""
import ast
import io
import json
import math
import pathlib
import re
import sys
from collections import Counter, defaultdict

import numpy as np
import opentrons
import opentrons.simulate as sim

HERE = pathlib.Path(__file__).resolve().parent
PROTOCOL = HERE / "baso4_plate_a.py"
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    OUT.append(line)


def protocol_module(src):
    """The protocol's constants, without importing opentrons' run()."""
    ns = {}
    tree = ast.parse(src)
    keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.FunctionDef))]
    exec(compile(ast.Module(keep, []), str(PROTOCOL), "exec"), ns)
    return ns


def animate_plate_a():
    src = (HERE.parent / "animate.py").read_text()
    ns = {"np": np, "math": math}
    for node in ast.parse(src).body:
        names = [getattr(t, "id", "") for t in getattr(node, "targets", [])]
        if (isinstance(node, ast.Assign) and set(names) & {"LEVELS", "SI_1M"}) or \
                (isinstance(node, ast.FunctionDef) and node.name == "plate_a"):
            exec(compile(ast.Module([node], []), "animate.py", "exec"), ns)
    rows = "ABCDEFGH"
    return {f"{rows[r]}{c + 1}": w for (r, c), w in ns["plate_a"]().items()}


def simulate(src, name):
    runlog, _ = sim.simulate(io.StringIO(src), file_name=name)
    return runlog


def walk(runlog):
    """The simulator's run log is flat; a mix's own aspirates and dispenses have level 1."""
    for e in runlog:
        yield e, e.get("level", 0)


def check_run(runlog, P, mix):
    """Heights, volumes, tips and the sulfate rule, from the simulator's own run log."""
    fails = []
    tips = 0
    per_well = defaultdict(float)
    per_vial = defaultdict(float)
    deepest = 0.0
    lowest_in_well = 99.0
    tip_touched_well = False
    t = 0.0                                                  # a rough clock, seconds
    sulfate_t = []
    last_lw = None
    for e, depth in walk(runlog):
        p = e["payload"]
        text = p.get("text", "")
        loc = p.get("location")
        lw = None
        if loc is not None and hasattr(loc, "labware"):
            lw = loc.labware.as_well() if loc.labware.is_well else None
        if text.startswith("SULFATE"):
            sulfate_t.append(t)
        if text.startswith("Picking up tip"):
            tips += 1
            tip_touched_well = False
            t += 6.0
        elif text.startswith("Dropping tip"):
            t += 5.0
        elif text.startswith("Delaying"):
            t += 60 * float(p.get("minutes", 0)) + float(p.get("seconds", 0))
        if lw is None:
            continue
        parent = lw.parent
        if lw is not last_lw and (last_lw is None or lw.parent is not last_lw.parent):
            t += 3.0                                         # up, across the deck, down
        elif lw is not last_lw:
            t += 1.0
        last_lw = lw
        z = loc.point.z
        in_plate = "plate A" in str(parent)
        is_vial = "vials" in str(parent)
        vol = float(p.get("volume") or 0.0)
        flow = re.search(r"at ([0-9.]+) uL/sec", text)
        if text.lstrip().startswith(("Aspirating", "Dispensing")) and flow:
            t += vol / float(flow.group(1))
        if is_vial and text.lstrip().startswith("Aspirating"):
            depth = lw.top().point.z - z
            deepest = max(deepest, depth)
            if depth > 46.5 + 1e-6:
                fails.append(f"too deep in {lw.well_name} of {parent}: {depth:.2f} mm below the rim")
            if z < lw.bottom().point.z + P["TIP_FLOOR"] - 1e-6:
                fails.append(f"under the floor in {lw.well_name} of {parent}")
            if tip_touched_well and "sulfate" in text and "plate A" not in text:
                fails.append("a tip that was in a well went back into a vial")
            per_vial[(str(parent).split(" on slot")[0], lw.well_name)] += vol
        if in_plate:
            above_floor = z - lw.bottom().point.z
            lowest_in_well = min(lowest_in_well, above_floor)
            if above_floor < 1.0 - 1e-6 or z > lw.top().point.z + 1e-6:
                fails.append(f"bad height in plate well {lw.well_name}: {above_floor:.2f} mm above its floor")
            if text.startswith("Dispensing") and depth == 0:          # not the mix's own dispenses
                per_well[lw.well_name] += vol
                if vol < 20.0 - 1e-6:
                    fails.append(f"{vol} uL into {lw.well_name}: under the P300's 20 uL")
            if text.lstrip().startswith("Aspirating"):            # only the mix aspirates from a well
                tip_touched_well = True
    for w, v in per_well.items():
        if abs(v - 200.0) > 1e-6:
            fails.append(f"{w} ends at {v} uL")
    if len(per_well) != 84:
        fails.append(f"{len(per_well)} wells filled, not 84")
    if tips > 96:
        fails.append(f"{tips} tips")
    return dict(fails=fails, tips=tips, per_vial=per_vial, deepest=deepest, lowest_in_well=lowest_in_well,
                minutes=t / 60.0, first_sulfate=sulfate_t[0] / 60.0, sulfate_span=(sulfate_t[-1] - sulfate_t[0]) / 60.0)


def main():
    say(f"opentrons {opentrons.__version__}, Python {sys.version.split()[0]}")
    src = PROTOCOL.read_text()
    P = protocol_module(src)
    fails = []

    # 1. the holder definition
    cad = json.loads((HERE.parent / "cad" / "byuvcl_6_vialholder_20ml" / "1.json").read_text())
    ok = P["HOLDER_DEF"] == cad
    say("1. holder definition in the protocol matches cad/byuvcl_6_vialholder_20ml/1.json:", ok)
    fails += [] if ok else ["holder definition differs from the cad JSON"]

    # 2. the plate map
    anim = animate_plate_a()
    mine = {w: dict(ba=ba, so=so, nacl=n) for w, ba, so, n, _r in P["PLATE_MAP"]}
    same = set(anim) == set(mine) and all(
        float(anim[w]["ba"]) == mine[w]["ba"] and float(anim[w]["so"]) == mine[w]["so"]
        and anim[w]["nacl"] == mine[w]["nacl"] for w in anim)
    roles = Counter(r.split(", rep")[0] for *_x, r in P["PLATE_MAP"])
    say("2. plate map matches animate.plate_a():", same, "|", len(mine), "wells |", dict(roles))
    fails += [] if same else ["plate map differs from the animation's"]

    # 3-6. simulate: the defaults, the mix off, and the plate straight on the deck
    def with_default(text, name, value):
        out, n = re.subn(r'(variable_name="%s",.*?default=)(True|False)' % name,
                         lambda m: m.group(1) + str(value), text, count=1, flags=re.S)
        assert n == 1, f"no parameter {name}"
        return out

    results = {}
    for mix, hs in ((True, True), (False, True), (True, False)):
        s = with_default(with_default(src, "mix_after_sulfate", mix), "on_heater_shaker", hs)
        runlog = simulate(s, "baso4_plate_a.py")
        r = check_run(runlog, P, mix)
        results[(mix, hs)] = r
        say(f"3. simulated with the mix {'on' if mix else 'off'}, plate {'on the Heater-Shaker' if hs else 'on the deck'}: "
            f"{len(runlog)} commands, {r['tips']} tips, "
            f"deepest {r['deepest']:.2f} mm below a vial rim, lowest {r['lowest_in_well']:.2f} mm above a well "
            f"floor, about {r['minutes']:.0f} min in all; the first sulfate at about {r['first_sulfate']:.0f} min "
            f"and the last {r['sulfate_span']:.0f} min after it (rough estimates)")
        fails += r["fails"]

    say("4. drawn from each vial (uL), and what the protocol assumes is left at the end:")
    for (holder, well), v in sorted(results[(True, True)]["per_vial"].items()):
        key = [k for k, sw in P["VIALS"].items() if sw[1] == well and
               (sw[0] == 4) == holder.startswith("barium")][0]
        left = P["START_UL"][key] - v
        say(f"   slot {P['VIALS'][key][0]} {well}  {(key[0] + ' ' + key[1]).strip():14s} {v:7.0f}"
            f"   left {left / 1000:5.1f} mL of the {P['START_UL'][key] / 1000:.1f} assumed, surface "
            f"{left / P['VIAL_AREA']:.1f} mm above the floor")

    # plate_map.csv
    rows = ["well,role,ba_mM,so4_mM,nacl_M,water_uL,nacl_uL,ba_uL,ba_stock,so4_uL,so4_stock,si_pitzer_25C"]
    si = {(0.01, 0.01): -2.0, (0.01, 0.1): -1.0, (0.01, 1.0): 0.0, (0.01, 3.0): 0.5,
          (0.1, 0.01): -1.0, (0.1, 0.1): 0.0, (0.1, 1.0): 1.0, (0.1, 3.0): 1.5,
          (1.0, 0.01): 0.0, (1.0, 0.1): 1.0, (1.0, 1.0): 2.0, (1.0, 3.0): 2.5,
          (3.0, 0.01): 0.5, (3.0, 0.1): 1.5, (3.0, 1.0): 2.5, (3.0, 3.0): 2.9}   # 1 molal NaCl, docs/baso4-checks
    for w, ba, so, n, role in P["PLATE_MAP"]:
        bs, bu = P["DOSE"][ba] if ba else ("", 0.0)
        ss, su = P["DOSE"][so] if so else ("", 0.0)
        s_i = si.get((ba, so), "") if n and ba != 10.0 else ""
        rows.append(f"{w},{role.replace(',', ';')},{ba:g},{so:g},{1.0 if n else 0.0:g},"
                    f"{P['water_ul'](ba, so, n):g},{P['NACL_UL'] if n else 0:g},{bu:g},{bs},{su:g},{ss},{s_i}")
    (HERE / "plate_map.csv").write_text("\n".join(rows) + "\n")
    say("5. wrote plate_map.csv:", len(rows) - 1, "wells (si_pitzer_25C only for the NaCl pairs, from the 10-30 table)")

    say("RESULT:", "PASS" if not fails else "FAIL")
    for f in fails[:40]:
        say("  -", f)
    (HERE / "check_output.txt").write_text("\n".join(OUT) + "\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
