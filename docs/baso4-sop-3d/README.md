# Barium sulfate plate run: a 3-D animated SOP

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) by @sgbaird on 2026-11-02. It shows
what Tim and Michael do for the next barium chloride and sodium sulfate plate, from scratch:
- where each step happens: CB 154, or Chris Dillon's lab (EB B125) with the fume hood; and inside the hood or next to it;
- which containers are opened, and where;
- weighing the powders;
- loading the OT-2;
- the 72 h record from the lid camera.

The procedure is the one already written down:
- [`docs/baso4-extended-monitoring.md`](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md)
  (11-02): plate A, the stocks, the seal, the stills schedule, and the run record;
- the [10-30 practice plate](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#barium-sulfate-practice-plate):
  the stock recipes and the PHREEQC saturation indices;
- the 10-23 lead plan's rule to weigh by difference in a capped vial when the balance is outside the hood;
- the hood threads: [powder-doser 141](https://github.com/vertical-cloud-lab/powder-doser/issues/141) (barium chloride
  in the hood, sodium sulfate on the bench, work 15 cm inside the sash) and
  [byu-vcl 195](https://github.com/vertical-cloud-lab/byu-vcl/issues/195) (Dillon's rules for the room).

It is built the way the lab's other animations are (byu-vcl's `viz3d`, used for the rePowder training, the lid camera and
the vertical lift module): CadQuery and vendor STEP models, rendered off-screen in PyVista, text drawn with PIL, and
written as MP4 and GIF.

Chapters 2 and 3 are in two parts each, so every GIF stays under the ~5 MB GitHub shows inline. Part 2a's GIF runs at 8 fps for the same reason; every MP4 has all its frames.

| Part | GIF (800 × 450, 10 fps) | MP4 (1280 × 720, 15 fps) |
| --- | --- | --- |
| **1. Where each step happens**: the two rooms, with the zones coloured: inside the hood (red), next to it (amber), the OT-2 (blue). Then the walk between them | [`out/sop1_where.gif`](out/sop1_where.gif) | [`out/mp4/sop1_where.mp4`](out/mp4/sop1_where.mp4) |
| **2a. Barium chloride, inside the hood**: PPE, the balance beside the hood, loading the hood, and the capped vial tared at the balance, filled in the hood and weighed again | [`out/sop2a_hood.gif`](out/sop2a_hood.gif) | [`out/mp4/sop2a_hood.mp4`](out/mp4/sop2a_hood.mp4) |
| **2b. Dilutions, then the bench**: the 0.1 M tube and its tenfold series in the hood; sodium sulfate and sodium chloride at the balance; packing the tub and closing the hood | [`out/sop2b_bench.gif`](out/sop2b_bench.gif) | [`out/mp4/sop2b_bench.mp4`](out/mp4/sop2b_bench.mp4) |
| **3a. Loading the OT-2 in CB 154**: the door, the plate on black paper in slot 7, the tips, the racks, uncapping, and the start | [`out/sop3a_load.gif`](out/sop3a_load.gif) | [`out/mp4/sop3a_load.mp4`](out/mp4/sop3a_load.mp4) |
| **3b. The fill and the seal**: water, NaCl, barium chloride, then sodium sulfate last; the seal at the pause; recapping | [`out/sop3b_fill.gif`](out/sop3b_fill.gif) | [`out/mp4/sop3b_fill.mp4`](out/mp4/sop3b_fill.mp4) |
| **4. Watching it for 72 h**: the lid camera's view and stills schedule, daily checks, the end of the run and the waste | [`out/sop4_monitor.gif`](out/sop4_monitor.gif) | [`out/mp4/sop4_monitor.mp4`](out/mp4/sop4_monitor.mp4) |
| **All of it**, one part after another | | [`out/mp4/baso4_sop_full.mp4`](out/mp4/baso4_sop_full.mp4) |

`out/<name>.json` gives the frame range of every sub-step in the MP4, and `out/<name>_still.png` is a still of one
sub-step.

![Where each step happens](out/sop1_where.gif)

## The steps, and where each one happens

**Rule of thumb:**
- Barium chloride powder is opened only inside the hood, and a barium solution stays there until its tube is capped.
- The balance, sodium sulfate, sodium chloride, labels and the log are next to the hood.
- Every tube is uncapped again only on the OT-2's deck in CB 154.

| # | Where | What | Opened |
| --- | --- | --- | --- |
| 2.1 | EB B125 | Lab coat, splash goggles, nitrile gloves (two pairs for barium). The barium chloride SDS goes in the binder. Keep every container closed and labelled (Dillon's rule) | - |
| 2.2 | next to the hood | The HR-100A on the bench beside the hood. If it was moved, plug it in at least an hour before weighing: it drifts for about an hour after a move ([powder-doser 157](https://github.com/vertical-cloud-lab/powder-doser/issues/157)). Level it, check it with a check weight | - |
| 2.3 | inside the hood | Sash up to load: liner, tray, barium waste bottle, a wash bottle of fresh DI water, the barium chloride, a tube rack, a spatula, all at least 15 cm (6 in) inside the sash. Sash down to its working-height sticker | - |
| 2.4 | next to the hood | Put the empty capped 20 mL vial on the pan and tare it | balance lid |
| 2.5-2.8 | inside the hood | Open the barium chloride and the vial, and spatula about 366 mg into the vial. Close both, and wipe the vial | barium chloride bottle, vial |
| 2.9 | next to the hood | Weigh the capped vial and log the reading. 0.3664 g in 15.00 mL is 0.1000 M (BaCl₂·2H₂O, 244.26 g/mol); for another mass, work out its concentration | balance lid |
| 2.10-2.11 | inside the hood | About 10 mL of DI water into the vial; swirl until clear. Pour into the 0.1 M tube, rinse the vial twice into it, make up to 15 mL, then cap and invert | vial, barium tubes |
| 2.12-2.13 | inside the hood | 13.5 mL of DI water in each of three tubes, then 1.5 mL down the series with a new tip each time: 10, 1 and 0.1 mM. Cap and label | barium tubes |
| 2.14-2.15 | next to the hood | Sodium sulfate in an open weigh boat: 213.1 mg (anhydrous, 142.04 g/mol) to 15 mL is 0.1 M. Through a funnel into its tube, make up, cap | sodium sulfate bottle, tube |
| 2.16 | next to the hood | The same series for 10, 1 and 0.1 mM sulfate. 4.383 g NaCl to 15 mL (5 M). A tube of fresh DI water. Ten tubes in all | sodium chloride bottle, tubes |
| 2.17 | hood, then bench | Wipe the barium tubes and rack, then put both racks in the tub, lid on. Outer gloves off in the hood; liner and wipes into the barium waste. Sash fully down | tub lid |
| 1.4 | between buildings | Carry the tub closed | nothing |
| 3.1 | CB 154 | Before the day: OT-2 calibrated (deck, tip length, pipette offset, Labware Position Check), Pi 5 on its 27 W supply, camera exposure and white balance locked, rail lights on with no timer, capture job tested | - |
| 3.2-3.5 | OT-2 deck | Door open. Black paper and the plate in slot 7 under the lid camera (lid off now), 300 µL tips in slot 6 (lid off), the barium rack in slot 4, the sulfate rack in slot 5. The colour sensor stays parked in slot 10 | plate lid, tip-rack lid |
| 3.6 | OT-2 deck | Uncap the ten tubes one at a time; each cap goes top-down on a wipe, in order | tubes |
| 3.7 | CB 154 | Close the door. Start the capture job, then the protocol | - |
| 3.8-3.11 | OT-2, door closed | Water, then 5 M NaCl, then barium chloride. Sodium sulfate goes in last, with a new tip per well, dispensed from above | - |
| 3.12-3.13 | OT-2 deck | At the pause: a clear adhesive seal, pressed down well by well; log the time. Recap the tubes, close the door, rail lights stay on | door |
| 4.1-4.4 | CB 154 | Stills every 1 min to 30 min after the last sulfate, every 5 min to 6 h, then every 15 min (about 400 in 72 h). Check the stream, the heartbeat and the event log once a day | - |
| 4.5-4.6 | CB 154 | Last still. Take the plate out, weigh it, and photograph it on black. Wells, leftover stocks and rinses go to barium waste. Commit the run record to `experiments/004-baso4-monitoring/<run-id>/` | door, waste |

## The models

| In the scene | Model | Source |
| --- | --- | --- |
| Opentrons OT-2: frame, deck, windows, door, Z gantry, P300 single on the left mount | Opentrons' reference STEP, "Detailed" | **Vendor CAD**, [github.com/Opentrons/ot2](https://github.com/Opentrons/ot2) at `ef9ede1`. Fetched at run time and SHA-256 checked by `models.py`; not committed. Its solids are named, so the door, head, beam and pipette move separately. The X-gantry beam is part of the frame solid in that file, so `models.py` cuts it out so it can move front to back with the head |
| Lid camera: HQ camera, 8-50 mm zoom, C-CS adapter, Pi 5, printed base and deck | `ot2-overhead-camera/lid-mount/exports/assembly.step` | **The lab's own CAD**, [byu-vcl PR 234](https://github.com/vertical-cloud-lab/byu-vcl/pull/234) at `49677cf`, fetched and hash-checked. It sits on the top window over slot 7, where the monitoring plan puts it. The yellow cone is a 140 × 105 mm view at the plate |
| A&D HR-100A with the FXi-10 breeze break and A&D's lid | `lab_models/labware.py`, `balance(lid="stock")` | byu-vcl `vertical-lab/lab_models` at `516f796` (from byu-vcl 199): built from A&D's drawings and the lab's measurements. The doser's AutoTrickler lid is swapped for the stock one here |
| NEST 96-well plate (200 µL, flat), Opentrons 300 µL tip rack, 15 mL Falcon tubes, AC 6-tube rack, 20 mL vial, weigh boat, spatula, colour sensor | `lab_models/labware.py` | Same copy; built from Opentrons' labware definitions and the makers' drawings |
| Fume hood, benches, OT-2 table, rooms | `models.py` | **Modelled here from typical sizes**: a 5 ft bench hood with a vertical sash, 30 in benches. EB B125's hood and both rooms are not measured or photographed on record, so the layout is a stand-in |
| Reagent bottles, waste bottles, wash bottles, 100-1000 µL pipette, tub, seal, plate lid, stand-in person | `models.py` | Modelled here. The coloured bands on bottles and tubes are only for the animation: orange for barium, green for sulfate, grey for NaCl, blue for water |

`lab_models/common.py` and `labware.py`, and `scene.py`, are verbatim copies from byu-vcl at `516f796`, so each
model and the renderer have one source. `animate.py` overrides one method of `scene.Scene`: it resets the camera's
clipping range every frame, which the lid camera's close view needs.

## Assumptions and gaps

- **The balance's place.** The HR-100A sat on the bench beside the EB B125 hood in mid-September
  ([powder-doser 157](https://github.com/vertical-cloud-lab/powder-doser/issues/157)). The 10-23 plan says the doser
  is back in CB 154, and the balance probably went with it, so it may have to be carried over again. If the Dillon lab
  has its own analytical balance beside the hood, use that one instead.
- **The 15 mL tube is too tall for the balance.** It doesn't fit under the HR-100A's breeze-break lid: there is
  79.4 mm from the pan to the lid. That's why the barium chloride is weighed in a capped 20 mL vial and the other
  powders in a weigh boat.
- **The plate won't fit in the breeze break either.** The run plan weighs the plate at the start and the end, so
  that weighing needs another balance, or the breeze break taken off.
- **Hand pipettes.** The 10-23 list marks the 100-1000 µL pipette as "get". Without one, dilute by weight, as the
  monitoring plan describes.
- **Two racks.** Both racks are the 6-tube AC model from the March run. They carry the tubes over and go onto the
  deck as they are. The March run had only one, so a second rack, or a 15-tube Opentrons rack, is needed.
- **The heater-shaker isn't drawn.** Plate A sits on black paper on the deck, unshaken, and the module's slot isn't on
  record. The colour sensor is drawn parked in slot 10. The monitoring plan takes it off the deck for this run, and the
  10-30 first-experiments plan uses it for sentinel reads. Either way, it doesn't drive the robot while the protocol
  runs.
- **The plate map is one shuffle of plate A:**
  - 48 wells: 16 barium and sulfate pairs in 1 molal NaCl, in triplicate;
  - 16 wells: the same pairs without NaCl;
  - 8 single-salt wells;
  - 8 blanks;
  - 4 positive controls at 10 mM each;
  - 12 wells empty.

  The blank and control counts are my choice; the plan doesn't fix them.
- **The time-lapse is illustrative.** When each well turns white comes from its saturation index (the 10-30 PHREEQC
  table, +1.6 without NaCl), through a made-up curve: SI 2.9 at 1 min, 2.0 at 10 min, 1.0 at 6 h, 0.5 at 48 h, and
  nothing below 0.3. It is not a prediction. That is what the run measures.

## Running it

```bash
pip install cadquery pyvista pillow numpy scipy          # plus ffmpeg and gifsicle on the PATH
xvfb-run -a python3 animate.py sop1 sop2a sop2b sop3a sop3b sop4 full   # full joins the six MP4s
PREVIEW=1 xvfb-run -a python3 animate.py sop2              # the last frame of each sub-step, to /tmp
```

The first run downloads the two STEP files into `.cache/` and tessellates everything, which takes about 10 s. The
meshes are cached until `models.py` or `lab_models/` changes. To run chapters in parallel, give each its own display
(`xvfb-run --server-num=N`).
