# One vial holder on the A1 mini: sliced, not yet printed (2026-11-11)

@timothy-commins calipered the lab's vials at 27 × 55 mm, then asked for the holder ("the base") on the lab's A1 mini
([PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84#issuecomment-6804648055)). This folder has it
sliced for that printer. **Nothing has been sent.** The run that sliced it had no login to the lab's Bambu account,
and only the approval-gated print workflow (`claude-print.yml`) or a person at the lab can send a print.

It is one holder. Try several vials in it before printing the second (see [`../README.md`](../README.md)).

![Top view of the sliced plate](plate_layout.png)

| File | What it is |
| --- | --- |
| [`vial_holder_20ml_x6_A1mini_PETG_0.4.gcode.3mf`](vial_holder_20ml_x6_A1mini_PETG_0.4.gcode.3mf) | Sliced for a **0.4 mm nozzle**, Bambu PETG Basic: **2 h 0 min, 76 g**, 115 layers |
| [`vial_holder_20ml_x6_A1mini_PLA_0.4.gcode.3mf`](vial_holder_20ml_x6_A1mini_PLA_0.4.gcode.3mf) | The same in Bambu PLA Basic, in case no PETG is loaded: **1 h 41 min, 80 g** |
| [`vial_holder_20ml_x6_A1mini_PETG_0.4.3mf`](vial_holder_20ml_x6_A1mini_PETG_0.4.3mf) | The PETG one as an unsliced project, to open in Bambu Studio and slice there |
| [`slice_a1mini.py`](slice_a1mini.py) | Makes all of these from [`../vial_holder_20ml_x6.stl`](../vial_holder_20ml_x6.stl) with Bambu Studio's command line |
| [`check_slice.py`](check_slice.py), [`check_slice_output.txt`](check_slice_output.txt), [`plate_layout.png`](plate_layout.png) | The checks of the G-code below, and the top view above |
| [`print.json`](print.json) | The record: source file and hashes, settings, estimates, checks, and what still has to be read off the printer |

## Settings

| | |
| --- | --- |
| Slicer | Bambu Studio 02.08.02.61 (AppImage), its own profiles, run from the command line |
| Printer | Bambu Lab A1 mini 0.4 nozzle, Textured PEI plate |
| Process | Bambu's `0.20mm Standard @BBL A1M` with three changes: **3 walls** (from 2), **0.15 mm elephant-foot compensation** (from 0) and **no brim** (from auto). The last two keep the bottom edge square, so it drops into the OT-2 slot's corner clips without trimming. The third wall stiffens the pockets |
| Left as Bambu has them | 0.2 mm layers, 15 % grid infill, no supports; PETG at 245 °C with the bed at 70 °C, PLA at 220 °C and 65 °C |
| Part | The STL at `5d9dd9d` (MD5 `90bbb63e…`), upright as exported, centred on the 180 × 180 mm bed |

## Checked in the G-code

[`check_slice.py`](check_slice.py) reads the G-code in each file ([output](check_slice_output.txt)). Sizes are outer-wall
toolpath spans plus one line width; each pocket is a least-squares circle through its wall, minus one line width.
Both files give the same numbers:

| | From the toolpaths | Model |
| --- | --- | --- |
| Footprint at z 1, 10 and 21 mm | 127.76 × 85.48 mm | 127.76 × 85.48 mm (SBS) |
| All six pockets at z 6, 12 and 18 mm | 28.20 mm | 28.2 mm |
| Top layer | z 23.0 mm | 23.0 mm |
| Config block | `printer_settings_id = Bambu Lab A1 mini 0.4 nozzle`, `nozzle_diameter = 0.4`, `curr_bed_type = Textured PEI Plate`, `wall_loops = 3`, `sparse_infill_density = 15%`, `elefant_foot_compensation = 0.15`, `brim_type = no_brim`, `enable_support = 0` | |

## Not checked, and what to check first

- **The nozzle.** This run couldn't read it off the printer: it had no Bambu login, and this repo has no LAN access code
  for the A1 mini. The files are for 0.4 mm, the nozzle byu-vcl read off it on 2026-10-28
  ([record](https://github.com/vertical-cloud-lab/byu-vcl/tree/main/hardware/vial-stirrer-cubxl/print/2026-10-28-a1mini-compact)).
  Read it again before printing (Studio's Device page, *Printer Parts*):
  - **0.4 mm:** print one of these files.
  - **0.2 mm:** re-slice with `--nozzle 0.2`. That takes about 15 h for this part, so swapping to 0.4 mm may be better.
  - **Anything else** (tensegrity-optimization uses 0.6 mm): don't print. Swap the nozzle first.
- **The filament.** On 10-28 the AMS Lite had dark blue PLA Basic (A1), black PLA Basic (A3) and white PETG Basic (A4).
  Use the file for what is loaded now, and map it to that slot when sending. Either material holds up to the aqueous
  stocks at room temperature. PETG is tougher, and is what byu-vcl prints its lab fixtures in.
- **The plate.** The files are sliced for the Textured PEI plate, which was on the printer on 10-28.
- **No plate thumbnails, and a blank printer-model ID.** The command line can't open a display for its thumbnails on
  the runner. It also leaves `printer_model_id` empty in `Metadata/slice_info.config` (the GUI writes `N1` for the
  A1 mini). If Studio objects when sending, open the project `.3mf` (or the STL with the three changes above) in
  Studio and slice it there.
- **Not bit-for-bit repeatable.** Two command-line runs of the same slice differed in a few gap-fill paths and by 11 s
  in the estimate. The files here are the ones `slice_a1mini.py` wrote.

## To print it

- **At the lab:** read the nozzle (above). Open the `.gcode.3mf` for the loaded filament in Bambu Studio, logged in to
  the lab's account, and use *Print plate*, mapping the filament to its AMS Lite slot. Or copy the file to the
  printer's microSD card and start it from the printer's screen.
- **Through the print workflow:** comment on PR 84 with the print trigger, naming the file (branch
  `claude/issue-80-20261105-2203`, path `docs/baso4-sop-3d/cad/print-a1mini/…`) and the printer (the A1 mini). A
  member of `bambu-print-approvers` approves the run. The run posts a fresh camera frame and reads the plate and the
  nozzle itself before it sends anything.

To slice again (for example for a 0.2 mm nozzle, or after a change to the holder):

```bash
# Bambu Studio 02.08.02.61's AppImage, extracted (byu-vcl's bambu/studio/setup_runner.sh downloads and checks it)
xvfb-run -a python3 slice_a1mini.py --studio ~/bambu/squashfs-root --nozzle 0.4
xvfb-run -a python3 slice_a1mini.py --studio ~/bambu/squashfs-root --nozzle 0.4 --filament "Bambu PLA Basic"
python3 check_slice.py vial_holder_20ml_x6_A1mini_PETG_0.4.gcode.3mf plate_layout.png     # needs numpy, matplotlib
```
