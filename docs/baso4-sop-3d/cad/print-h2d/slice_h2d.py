#!/usr/bin/env python3
"""Slice the 6-vial holder for the lab's H2D with Bambu Studio's command line (no login needed).

Like ``../print-a1mini/slice_a1mini.py``, this flattens Studio's bundled machine, process and filament profiles into
one JSON each, applies the holder's changes and runs the CLI on the STL. Two things differ on the H2D:

* It has two nozzles. With one filament, Studio's default grouping ("Auto For Flush") puts it on the **left** nozzle
  (``filament_map = 1``; the start G-code heats ``T1``). The command line ignores a manual map in the profiles, and
  stops with "No valid nozzle found" when one is set in a project, so a right-nozzle slice has to be made in Studio's
  GUI. The slice assumes both nozzles are ``--nozzle`` mm with standard flow, as Studio's H2D presets do. Read both
  off the printer first: this repo prints only with 0.2 or 0.4 mm.
* The machine profile pulls Bambu's own start and end G-code in through ``include``. This script resolves it, so the
  file starts with Bambu's H2D start sequence (the A1 mini's CLI slice fell back to a generic one).

    # Bambu Studio 02.08.02.61, the AppImage extracted (byu-vcl bambu/studio/setup_runner.sh does the same)
    xvfb-run -a python3 slice_h2d.py --studio ~/bambu/squashfs-root --nozzle 0.4
    xvfb-run -a python3 slice_h2d.py --studio ~/bambu/squashfs-root --nozzle 0.4 --filament "Bambu PLA Basic"

The holder's changes from Bambu's preset are the A1 mini's: 3 walls (from 2), 0.15 mm elephant-foot compensation (from
0) and no brim, so the bottom edge stays square and drops into the OT-2 slot's corner clips. Layer height, 15 % infill,
no supports and the filament's temperatures are as Bambu has them.
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
STL = HERE.parent / "vial_holder_20ml_x6.stl"
PROCESS = {"0.4": "0.20mm Standard @BBL H2D", "0.2": "0.10mm Standard @BBL H2D 0.2 nozzle"}
CHANGES = {"wall_loops": "3", "elefant_foot_compensation": "0.15", "brim_type": "no_brim",
           "curr_bed_type": "Textured PEI Plate"}


def find(root: Path, cat: str, name: str) -> dict:
    p = root / cat / f"{name}.json"
    if p.exists():
        return json.loads(p.read_text())
    for q in (root / cat).glob("*.json"):
        d = json.loads(q.read_text())
        if d.get("name") == name:
            return d
    raise FileNotFoundError(f"no {cat} profile named {name!r}")


def flat(root: Path, cat: str, name: str) -> dict:
    d = find(root, cat, name)
    out = flat(root, cat, d["inherits"]) if d.get("inherits") else {}
    for inc in d.get("include", []):               # Bambu's start/end G-code templates
        out.update({k: v for k, v in find(root, cat, inc).items() if k not in ("name", "instantiation", "type")})
    out.update(d)
    for k in ("inherits", "include"):
        out.pop(k, None)
    out.update(name=name, **{"from": "system"})
    return out


ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("--studio", required=True, type=Path, help="the extracted AppImage (squashfs-root)")
ap.add_argument("--nozzle", choices=sorted(PROCESS), required=True)
ap.add_argument("--filament", default="Bambu PETG Basic", help='e.g. "Bambu PLA Basic"')
ap.add_argument("--out", type=Path, default=HERE)
a = ap.parse_args()

root = a.studio / "resources" / "profiles" / "BBL"
machine = flat(root, "machine", f"Bambu Lab H2D {a.nozzle} nozzle")
process = flat(root, "process", PROCESS[a.nozzle]) | CHANGES
try:                                   # PETG Basic has a "0.4 nozzle" profile; PLA Basic's 0.4 one has no suffix
    filament = flat(root, "filament", f"{a.filament} @BBL H2D {a.nozzle} nozzle")
except FileNotFoundError:
    filament = flat(root, "filament", f"{a.filament} @BBL H2D")
if machine["name"] not in filament.get("compatible_printers", []):
    sys.exit(f"{filament['name']} doesn't list {machine['name']} as a compatible printer")
stem = f"vial_holder_20ml_x6_H2D_{a.filament.split()[1]}_{a.nozzle}"
with tempfile.TemporaryDirectory() as tmp:
    t = Path(tmp)
    for n, d in (("machine", machine), ("process", process), ("filament", filament)):
        (t / f"{n}.json").write_text(json.dumps(d))
    cli = [str(a.studio / "AppRun"), "--load-settings", f"{t / 'machine.json'};{t / 'process.json'}",
           "--load-filaments", str(t / "filament.json"), "--arrange", "1", "--orient", "0", "--outputdir", str(a.out)]
    for extra in (["--slice", "0", "--export-3mf", f"{stem}.gcode.3mf"], ["--export-3mf", f"{stem}.3mf"]):
        r = subprocess.run(cli + extra + [str(STL)], capture_output=True, text=True, env=os.environ | {"LC_ALL": "C"})
        if r.returncode:
            sys.exit(r.stdout[-2000:] + r.stderr[-2000:])
for junk in ("plate_1.gcode", "result.json"):
    (a.out / junk).unlink(missing_ok=True)
print("wrote", a.out / f"{stem}.gcode.3mf", "and", a.out / f"{stem}.3mf")
