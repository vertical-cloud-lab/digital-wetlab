# Plate A on the OT-2: the protocol, and how to run it

Asked on [PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84) by @timothy-commins on 2026-11-17: the
stocks are made, everything is on the deck, a phone replaces the lid camera and goes in once the liquids are in, and
the robot should now fill the plate.

**A person starts this run from the Opentrons OT-2 App.** An `@claude` run can't: the robot answers only on its own
Ethernet cable, and the 11-17 run couldn't reach the lab network at all. Nothing in this folder has run on the robot.
It has only been simulated.

| File | What it is |
| --- | --- |
| [`baso4_plate_a.py`](baso4_plate_a.py) | **The protocol.** Import this one file in the App. The vial holder's labware definition is inside it, so nothing else needs importing |
| [`plate_map.csv`](plate_map.csv) | Every well: its role, barium, sulfate and NaCl, the volume of each liquid, and which vial it comes from |
| [`check_protocol.py`](check_protocol.py), [`check_output.txt`](check_output.txt) | The checks, run in opentrons 8.8.1 (the robot's own version), and what they printed |

## What the robot does

| | What | Tips | Roughly when, after Start |
| --- | --- | --- | --- |
| 1 | **Pauses** with a checklist on the App's screen. Nothing moves until you press Resume | | 0 |
| 2 | Rail lights on; closes the Heater-Shaker's latch. It doesn't heat or shake | | |
| 3 | DI water into 84 wells, 40-180 µL each, from slot 5 B3 | 1 | 0-12 min |
| 4 | 5 M NaCl, 40 µL into each of 64 wells, from slot 5 B2 | 1 | 12-21 min |
| 5 | Barium chloride into 72 wells, 20 or 60 µL, from slot 4 | 4, one per vial | 21-33 min |
| 6 | **Sodium sulfate, last,** into 72 wells, 20 or 60 µL, from slot 5. A new tip for every well, then (by default) three gentle 80 µL mixes with that tip. The run log gets "SULFATE &lt;well&gt;" just before each one: that's the well's start | 72 | 33-67 min |
| 7 | The run says **Completed**. The pipette parks at the back right and stays there | | about 67 min |

The times are my rough estimate from the simulation, not a measurement. Without the mixing the sulfate takes about 22
min instead of 34.

**Every well ends at 200 µL**, and every dose is 20, 40 or 60 µL, never under the P300's 20 µL. 78 of the rack's 96
tips are used. Water and NaCl go in before any salt that matters, and the barium before the sulfate. A tip never goes
back into a vial after it has touched a well that has sulfate in it.

**In the vials,** the tip follows each vial's level down: it draws about 2.5 mm below where the surface should be,
assuming about 1 mL less than the SOP put in each vial, so it errs on the deep side. It never goes more than 46.5 mm
below a vial's rim (7 mm above the inside floor), which keeps the pipette itself about 5 mm above the glass. In the
plate it dispenses 1 mm above the liquid it's making, and blows out above the liquid, so no bubbles go into a well.

## Before you start

1. **Use the Opentrons OT-2 App.** Since v9.1.1 (June 2026) the plain Opentrons App is for the Flex only, and an OT-2
   doesn't show up in it. Download the OT-2 App from [opentrons.com/app](https://opentrons.com/app); it runs on Windows,
   a Mac or x86-64 Linux, not on a Raspberry Pi
   ([byu-vcl's notes](https://github.com/vertical-cloud-lab/byu-vcl/blob/main/wireless-color-sensor/ot2/opentrons-calibration.md#step-0--get-an-app-that-still-supports-the-ot-2)).
2. **Connect the computer to the robot.** The OT-2 has one Ethernet jack, at the back, and its cable normally goes to
   a USB adapter on the camera Pi. Move that cable to the computer (its Ethernet port, or a USB-Ethernet adapter). The
   App can take two minutes or more to find the robot. If it doesn't, see
   [If the app still cannot find the robot](https://github.com/vertical-cloud-lab/byu-vcl/blob/main/wireless-color-sensor/ot2/opentrons-calibration.md#if-the-app-still-cannot-find-the-robot).
3. **Check the pipette's calibration.** Devices → the OT-2 → ⋮ → Robot Settings → Calibration. In September and on
   10-30 the P300 had **no tip length or pipette offset calibration**, and the App won't run a protocol without them.
   If they're missing, run **Pipette Offset Calibration** with the **Opentrons 96 Tip Rack 300 µL** (it measures the
   tip length in the same pass). The App shows which slots it needs. If it needs a slot that has a vial holder in it,
   cap that holder's vials and lift the holder out, then put it back afterwards and uncap them again. The deck
   calibration is from January, but Labware Position Check corrects every piece of labware, so I wouldn't redo it now.
4. **Check the deck against this list:**
   - **Slot 7:** the Heater-Shaker, powered and plugged into the robot, with the plate on its 96 Flat Bottom Adapter,
     A1 at the back left. If the plate is straight on the deck instead, set the parameter below to off.
   - **Slot 4:** barium chloride. A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM. B2 and B3 empty.
   - **Slot 5:** sodium sulfate A1 0.1 M, A2 10 mM, A3 1 mM, B1 0.1 mM; **B2 the 5 M NaCl; B3 the DI water.**
   - **Slot 6:** a **full** rack of Opentrons 300 µL tips. The robot can't tell if a tip is missing, and it would
     then draw liquid with no tip on.
   - **Slots 8 and 10 empty.** Nothing taller than 53 mm may stand next to the Heater-Shaker (slot 8). Take the colour
     sensor and its charging base out of slot 10: the robot doesn't know they're there, and in the simulation the
     pipette's path from the plate to the trash crosses the corner of slot 10.
   - **All ten vials uncapped,** each cap top-down on a clean wipe in order (SOP step 3.6). A cap left on would be hit
     by the tip.
5. **Top up the DI water vial (slot 5, B3) to about 18 mL.** Add about 3 mL from the bottle that has only held DI
   water. The plate takes 10.0 mL of it. With the SOP's 15 mL the tip still reaches it, but only just at the end.
6. **No phone or tripod in the robot yet.**

## Running it

1. **Import** [`baso4_plate_a.py`](baso4_plate_a.py): download it (the "Download raw file" button), then Protocols →
   Import in the App. Its analysis should finish with no errors. If it shows one, post a screenshot on PR 84.
2. **Parameters.** Leave both on unless you have a reason:
   - **Plate on the Heater-Shaker:** on. Off if the plate sits straight on slot 7.
   - **Mix after the sulfate:** on. Off follows the SOP's videos (sulfate dropped in from above, no mixing). See
     [the mixing](#the-mixing) below.
3. **Setup.** Start setup and pick the robot, then:
   - **Robot calibration:** all green.
   - **Modules:** the Heater-Shaker shows as connected.
   - **Labware:** the deck map matches the deck.
   - **Liquids:** each vial's name matches its label. The colours are red for barium, blue for sulfate, orange for
     NaCl and light blue for water.
4. **Labware Position Check.** Run it. The App picks up a tip and takes it over each piece of labware in turn: the tip
   rack, both vial holders (vial A1 in each) and the plate (well A1). Jog until the tip's end sits **level with the
   vial's rim, centred over its opening,** without touching the glass, and for the plate level with the top of well
   A1. Then Confirm. It puts the tip back where it found it.
5. **Start the run.** It pauses at once with a checklist. Read it, check the deck, keep your hands out, then press
   **Resume**. Note the time on the phone when you do.
6. **Watch the first draw from each vial** (the water, then the NaCl, then each barium vial, then the first sulfate).
   The tip should go under the surface and the pipette shouldn't touch the vial's rim. If anything looks wrong, press
   **Pause** in the App, or **Cancel**. Never reach in while the gantry moves.
7. **When the App says Completed:**
   1. Check the rail lights are still on (robot's ⋮ menu → Lights).
   2. Seal the plate: lay the clear seal on and press it down well by well. The latch can stay closed.
   3. Set up the phone and tripod, start its photos (every 2 minutes, as on 11-16), and note the time of the first
      photo.
   4. Recap the vials from the wipe, each with its own cap. They stay in the holders for the waste at the end.
8. **Save the run log.** Each well's start is the time of its "SULFATE" line. In the App, the run's ⋮ menu (on the
   protocol's page or under Recent Protocol Runs) has *Download run log*. Post the file on PR 84. If your App doesn't
   offer it, say so: the robot keeps the run, and it can be read later over the robot's API.

**For the 72 h:**
- **Leave the robot's cable off the camera Pi** (in the computer, or unplugged) until the run is over. Nothing remote
  can then move the gantry into the tripod or switch the rail lights off. In October the Pi switched them off at 17:00
  every day.
- **Put a sign on the robot:** plate A running until the date and time it ends; don't home it, calibrate it or start a
  protocol. Starting anything, pressing *Home*, or a restart after a power cut moves the pipette
  ([why](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84#issuecomment-6924663610)).

## The mixing

**Mixing is on by default.** That's a change from the SOP's videos, which drop the sulfate in from above with no
mixing. The 11-02 plan left the choice open ("decision 4") and asked only that every well get the same.

- **Why mix.** Without mixing, the 20 or 60 µL of sulfate sits as a layer on the well's surface. In the 1 M NaCl wells
  it's lighter than the brine under it (about 1.00 against 1.04 g/mL), so it floats. Mixing by diffusion alone across
  5 mm of liquid takes hours. Until then the well isn't at the concentrations in the plate map, and the layer where
  the two meet is more supersaturated than the well as a whole. Plate A's question is which of those concentrations
  precipitate, and how fast.
- **How.** With the well's own sulfate tip, three cycles of 80 µL, 1 mm above the floor: about 35 µL/s up and
  70 µL/s down, about 10 s a well. Then it blows out above the liquid and drops the tip.
- **The cost.** Mixing stirs, and stirring changes when barium sulfate nucleates. That's why every well gets exactly
  the same mixing. The run log records which way it ran.
- **Off** gives the SOP's way: the sulfate dispensed 1 mm above the liquid and left. This is Sterling's call if he
  disagrees.

## The phone, and what it misses

- **The fill takes about an hour,** and the phone goes in after it. By the first photo the first wells will have had
  their sulfate for about 40 minutes, the last ones for a few minutes. Wells that turn white in minutes (the 10 mM
  controls and the 3 mM pairs) will probably already be white in the first photo. The run log still gives each well's
  exact start.
- **The phone's settings from 11-16 still apply:** every 2 minutes if each photo is 3.7 MB or less, 12 MP, focus,
  exposure and white balance locked on the plate with the rail lights on, airplane mode, on the charger, no automatic
  updates ([the photo interval](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84#issuecomment-6924888746),
  [phone settings](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84#issuecomment-6923980181)).
- **Line up the clocks.** You'll have noted the phone's time when you pressed Resume and at the first photo. The run
  log gives the robot's time of each SULFATE line. Together they put every photo on each well's own clock.

## Checked, and not checked

`python check_protocol.py` (in a Python 3.11 environment with `opentrons==8.8.1`; it prints PASS or FAIL) checks:
- the holder definition inside the protocol is the one in [`../cad/`](../cad/README.md);
- the plate map is the SOP animation's plate A: 48 NaCl pairs, 16 pairs without NaCl, 4 barium-only, 4 sulfate-only,
  4 water and 4 NaCl blanks, 4 positive controls at 10 mM each, and 12 empty wells;
- the protocol simulates three ways: as it is, with the mix off, and with the plate straight on the deck;
- every well ends at 200 µL, no dose is under 20 µL, and it uses 78 tips;
- the tip never goes more than 46.5 mm below a vial's rim, nor closer than 1 mm to a well's floor;
- how much is drawn from each vial: 10.0 mL of water, 2.6 mL of NaCl, and 1.36 mL from each 10 mM vial, the most from
  any stock.

**Not checked:**
- **Nothing has run on the robot,** and the printed holders have never been on it. Labware Position Check is the
  first time the robot sees them.
- **The vials' inside diameter (24.6 mm) is assumed:** 27 mm outside, less 1.2 mm of glass on each side. If the glass
  is thicker, the levels are higher than the protocol thinks, and the tip just goes deeper. That's the safe side.
- **The calibration state is from September and October.** The App will show today's.
- **That the App offers *Download run log* in your version.**
- **The run time is a rough estimate.**
