#!/usr/bin/env python3
"""Slice the 6-vial holder for the lab's A1 mini with Bambu Studio's command line (no login needed).

Studio's CLI does not follow a system profile's ``inherits`` chain, so this flattens the bundled machine, process and
filament profiles into one JSON each, applies the holder's changes, and runs the CLI on the STL. Use the nozzle that is
actually in the printer: read it off the printer first.

    # Bambu Studio 02.08.02.61, the AppImage extracted (byu-vcl bambu/studio/setup_runner.sh does the same)
    python3 slice_a1mini.py --studio ~/bambu/squashfs-root --nozzle 0.4          # writes the .gcode.3mf and .3mf here
    python3 slice_a1mini.py --studio ~/bambu/squashfs-root --nozzle 0.2

The holder's changes from Bambu's preset: 3 walls (from 2), 0.15 mm elephant-foot compensation (from 0) and no brim,
so the bottom edge stays square and drops into the OT-2 slot's corner clips. Layer height, 15 % infill, no supports and
the filament's temperatures are as Bambu has them. On Linux, run it under ``xvfb-run -a``.
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
STL = HERE.parent / "vial_holder_20ml_x6.stl"
PROCESS = {"0.4": "0.20mm Standard @BBL A1M", "0.2": "0.10mm Standard @BBL A1M 0.2 nozzle"}
CHANGES = {"wall_loops": "3", "elefant_foot_compensation": "0.15", "brim_type": "no_brim",
           "curr_bed_type": "Textured PEI Plate"}


def flat(root: Path, cat: str, name: str) -> dict:
    p = root / cat / f"{name}.json"
    d = json.loads(p.read_text()) if p.exists() else next(
        (json.loads(q.read_text()) for q in (root / cat).glob("*.json") if json.loads(q.read_text()).get("name") == name),
        None)
    if d is None:
        raise FileNotFoundError(f"no {cat} profile named {name!r}")
    out = flat(root, cat, d["inherits"]) if d.get("inherits") else {}
    out.update(d)
    out.pop("inherits", None)
    out.update(name=name, **{"from": "system"})
    return out


ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("--studio", required=True, type=Path, help="the extracted AppImage (squashfs-root)")
ap.add_argument("--nozzle", choices=sorted(PROCESS), required=True)
ap.add_argument("--filament", default="Bambu PETG Basic", help='e.g. "Bambu PLA Basic"')
ap.add_argument("--out", type=Path, default=HERE)
a = ap.parse_args()

root = a.studio / "resources" / "profiles" / "BBL"
machine = flat(root, "machine", f"Bambu Lab A1 mini {a.nozzle} nozzle")
process = flat(root, "process", PROCESS[a.nozzle]) | CHANGES
try:                                   # PETG Basic has a "0.4 nozzle" profile; PLA Basic's 0.4 one has no suffix
    filament = flat(root, "filament", f"{a.filament} @BBL A1M {a.nozzle} nozzle")
except FileNotFoundError:
    filament = flat(root, "filament", f"{a.filament} @BBL A1M")
if machine["name"] not in filament.get("compatible_printers", []):
    sys.exit(f"{filament['name']} doesn't list {machine['name']} as a compatible printer")
stem = f"vial_holder_20ml_x6_A1mini_{a.filament.split()[1]}_{a.nozzle}"
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
