# The first experiments, revised after the PRF review

> Written 2026-11-02 for Sterling's question on
> [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80): how should the first set
> of experiments in [PR 3](https://github.com/vertical-cloud-lab/digital-wetlab/pull/3) change in light
> of the PRF review, if they are kept as proof-of-concept experiments that need not be about Pitzer
> modelling or petroleum, and using the hardware that is installed now (the heater-shaker, the HQ
> overhead camera and the wireless colour sensor)? The review is paraphrased from the digest in
> [PR 82](https://github.com/vertical-cloud-lab/digital-wetlab/blob/7f49607/grants/acs-prf/REVIEW_2026.md);
> nothing here quotes it. The PHREEQC numbers come from [`phreeqc_checks.py`](phreeqc_checks.py), and
> its output is in [`results.txt`](results.txt).

## Short answer

Keep PR 3's chemistry (barium chloride, sodium sulfate, salt water) but change what is measured.
The 03-05 plate recorded whether precipitate was visible across 80 one-off conditions. The proposal
built on that, and planned to read turbidity onset within 240 min as the solubility boundary
(SI = 0). That was Reviewer B's central practical objection: a precipitate that appears within four
hours marks nucleation, at some supersaturation that depends on time and on how little solid the
detector can see. It does not mark solubility.

There are two sound ways forward, and the installed hardware supports both (items 1 and 2 below).
The other two PR 3 plans change too (items 3 and 4).

1. **Measure nucleation as nucleation (E1, E2).** Use a few conditions with many replicate wells
   each, log a start time for every well, and have the camera watch for 24 h. The fraction of
   wells still clear against time gives a nucleation rate. Barite (BaSO₄) in 1 molal NaCl is the
   right first system:
   - all the chemicals are on hand;
   - its thermodynamics are settled, so the supersaturation is computed, not fitted;
   - He, Oddo and Tomson (1995) measured barite induction times in this same medium from 25 to
     90 °C, so the robot can be checked against a published dataset.

   The heater-shaker shakes the plate at room temperature and then supplies the temperature series.
2. **Measure solubility as solubility (E3).** Take gypsum (CaSO₄·2H₂O) in NaCl and approach
   equilibrium from both sides:
   - seeded wells either dissolve their seed or grow it, and the composition where that switches
     brackets the solubility;
   - unseeded wells beside them show how far past solubility a solution can go before anything
     nucleates;
   - XRD or Raman on a few wells confirms the solid.

   This is the validation the review digest recommends for the platform: a well-studied salt in
   NaCl, approached from both sides, with the solid checked. There is a reference dataset to compare
   against (Marshall and Slusher 1966).
3. **Turn the AgCl plan into a precipitate-colour library for qualitative analysis (E4).** This is
   the original purpose of the robot (Kevin Jablonka's design) and direction 6 of
   [PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/pull/83). This is where the 8-channel
   colour sensor could beat the camera, if it can tell apart pale precipitates that look alike. On
   paint it compressed colour differences 2.6–4.4×, so E4 tests that first.
4. **Defer the PbS vials.** They are the petroleum-specific part and need a hood and an H₂S monitor.
   An open plate can't meet the review's sulfide points either: it needs a controlled H₂S partial
   pressure, closed vessels, and trace analysis.

A commissioning step goes first (E0). The hardware is installed but not yet proven, according to
its own records:
- the camera has no time-lapse capture yet;
- the heater-shaker has no recorded test;
- the P300 has no tip-length or offset calibration on record;
- the colour sensor has only ever read paint.

E0 closes those gaps, then runs a 24 h calibration plate. That plate measures how little precipitate
the camera and the sensor can see, and checks that both record unattended for a full day. That is
also the goal Timothy set on issue 80 for the team's next barium chloride and sodium sulfate run:
show that the lab can monitor and document an experiment over an extended period. E0, then E1, can
be that run.

### How this fits the monitoring plan for Timothy's run

A plan for that run was posted on issue 80 just before this one:
[`docs/baso4-extended-monitoring.md`](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md).
It covers the capture job, record-keeping, the dry run and the run record in more detail than E0
here, so use it for those. The two plans differ only on the first barium plate:
- **The monitoring plan suggests the 10-30 grid** (its Plate A, 0.01–3 mM in triplicate) first, and
  many replicates near the boundary (its option C) later.
- **This plan would swap them.** A grid with three wells per condition can only show where
  nucleation became visible in the time watched, which is the reading the review rejected. Its most
  interesting wells, between SI 0 and +1, can form at most about 5 µg of solid, which may be below
  what the camera can see.
- **E1a** (8 SI levels × 8 replicates at SI 1.0–2.75, 10–109 µg per well) is just as good a
  monitoring demo, and its data mean something.

## What PR 3 planned, and what changes

| PR 3 experiment | What happened | What the review says about it | Revised plan |
|---|---|---|---|
| [001 AgCl formation](https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/001-agcl-formation/README.md): AgNO₃ with NaCl (bench) or HCl (hood), P20, 384-well printed plate | Not run | Not addressed | **E4**: a precipitate-colour library for qualitative analysis. The HCl variant is dropped because it needs a hood |
| [002 BaSO₄ intensity map](https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/002-baso4-precipitation/README.md): 80 Latin-hypercube conditions, 0.1–50 mM Ba and SO₄, 0–3 molal NaCl, images at 5–240 min | Ran on 03-05. All 80 conditions were supersaturated (SI 2.6–5.8). 16 of the 80 got no barium or no sulfate because the protocol rounded sub-µL doses to zero ([found on 10-30](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/baso4-checks/results.txt)). No per-well scores or images tied to its time points were found on 10-30 | A visible onset is nucleation, not solubility, and one onset per condition says little because nucleation is random | **E0** calibration, then **E1/E2**: replicate-well induction-time plates in a constant 1 molal NaCl medium |
| 002's boundary-crossing alternative: 1 mM intermediate stocks to straddle SI = 0 | Not run | A boundary located by onset is still a nucleation boundary | **E3**: gypsum solubility from both sides, which can locate a real boundary |
| [003 PbS vial tests](https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/003-pbs-vial-tests/README.md): 0.5 mM Pb²⁺ with 1 mM sulfide in 1 molal NaCl | Not run | Sulfide needs a controlled H₂S partial pressure and closed vessels. PbS is supersaturated almost everywhere in the old design, and its solubility needs ICP-MS | **Deferred** |

The 10-30 [barium sulfate practice plate](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#barium-sulfate-practice-plate)
(a 4 × 4 grid from 0.01 to 3 mM in 1 molal NaCl) was a workflow shakedown for the lead plates. E0
covers the shakedown, and E1 replaces the grid. Without replicates, a grid that crosses SI = 0 still
only shows where nucleation became visible within the time watched.

## What the review changes for every plate

Paraphrased from the [review digest](https://github.com/vertical-cloud-lab/digital-wetlab/blob/7f49607/grants/acs-prf/REVIEW_2026.md#what-the-review-says-would-work):

- **Say what the observable is.** "First detected at time *t*" is a nucleation-plus-growth time at
  the detector's limit. Report it with that limit (measured in E0) and never as a solubility.
- **Replicate.** Nucleation is random, so a condition gives a distribution of induction times, not
  one number. A rate comes from the whole distribution
  ([Jiang and ter Horst 2011](https://doi.org/10.1021/cg101213q);
  [Brandel and ter Horst 2015](https://doi.org/10.1039/C4FD00230J)).
- **Compute the supersaturation from settled thermodynamics; don't fit it.** Barite and gypsum in
  NaCl are well characterised in the Pitzer framework:
  - gypsum since [Harvie, Møller and Weare (1984)](https://doi.org/10.1016/0016-7037(84)90098-X);
  - barite to 200 °C in [Monnin (1999)](https://doi.org/10.1016/S0009-2541(98)00171-5);
  - both to 200 °C in [Appelo (2015)](https://doi.org/10.1016/j.apgeochem.2014.11.007), whose
    barite, Ba–Cl and Ca–Na–SO₄–Cl entries PHREEQC's `pitzer.dat` carries.

  PHREEQC sets SI here, and no parameter is regressed.
- **Identify the solid** by XRD or Raman on a few wells per plate.
- **Approach from both sides** whenever the claim is about equilibrium (E3).
- **Keep the system closed.** Seal the wells or cover them with oil, and use nothing volatile.
- **No buffers.** None of these salts needs one.
- **Randomise well positions,** so fill order and position on the plate don't line up with the
  condition.
- **Measure what each well actually saw**: its start time, its temperature, and the detection limit.
  The SI values below are for 25 °C. Log the room temperature and recompute SI for it; barite in
  1 molal NaCl moves about 0.01 SI per °C.

Three lab practices matter even more for nucleation work. The first two come from the
[10-21 checklist](https://github.com/vertical-cloud-lab/digital-wetlab/blob/5b29ece/docs/ot2-sulfide-scaling-setup.md):
- **A fresh tip for every trigger dispense.** The 03-05 protocol dipped one tip into wells that
  already held barium and then went back to the stock, which seeds the stock and the next wells.
- **A logged start time for every well.** Filling a plate one well at a time takes tens of minutes.
- **Filter the stocks (0.2 µm).** Dust and fibres nucleate barite and gypsum, and in a replicate
  design they show up as early outliers
  ([Kashchiev and van Rosmalen 2003](https://doi.org/10.1002/crat.200310070)).

## The hardware, as the records describe it

From the byu-vcl records as of 2026-11-02: the colour-sensor notes in
[`wireless-color-sensor/ot2/`](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/README.md),
the lid-camera PR ([byu-vcl PR 234](https://github.com/vertical-cloud-lab/byu-vcl/pull/234)), the
heater-shaker issue ([byu-vcl issue 81](https://github.com/vertical-cloud-lab/byu-vcl/issues/81#issuecomment-6157219356))
and the [calibration snapshot](https://github.com/vertical-cloud-lab/byu-vcl/blob/9c6e76b/wireless-color-sensor/ot2/opentrons-calibration.md).

| | What it is now | Its job in these plates | Still to do (in E0) |
|---|---|---|---|
| **HQ overhead camera** | HQ camera (IMX477) with the 8–50 mm zoom on a Pi 5, taped over the lid window and aimed at a plate on the deck in slot 7. It streams 1920×1440 at 3 fps to YouTube. A full 4056×3040 still comes from a local endpoint in about 0.3 s without stopping the stream: about 200 px across a well, where a planning doc puts about 50 px as enough to detect a precipitate and 100 px to measure it. Focus was reported "very clear" on 11-01 after the spacer was fitted | The main detector. It takes a still of the whole plate every 1–5 min for 24–72 h | Confirm the focus with a measured still. Write the time-lapse job: there is no frame cache or time-lapse yet, so save a still every *N* min with its timestamp and sync it off the Pi. Turn off the 17:00 rail-light timer and hold the three-a-day reboots during a run. Fix the power supply (it sags to 4.81 V). Refocus if the plate moves onto the heater-shaker |
| **Wireless colour sensor** | AS7341 on a Pico W. The P300 nozzle picks it up from its charging base in slot 10. It has 8 channels, but 410 nm is unusable. The LED is off and the rail lights are the light source. A reading takes about 1.4 s, a trip over 6 wells about 15 min, and the battery lasts 14–27 min off the base. Repeatability is 0.1% within a landing and 1.7% between trips. Its colour differences come out 2.6–4.4× too small | A second, independent detector: trips over 4–6 sentinel wells every 1–2 h, and colour spectra in E4 | It has only ever read diluted paint. Nothing is recorded with a precipitate, a seal, oil or the heater-shaker. Light leaking through a clear plate is a known artefact, and an opaque plate is recommended but untried. It needs the only pipette, so it can't read while a plate is being filled, and it blocks the camera while it is over the plate. Read hovering, not resting: resting reads were worst, and one landing lifted an untaped plate |
| **Heater-shaker** | Placed in the robot on 10-13. Opentrons gives 37–95 °C, ±0.5 °C at 55 °C, a 10 °C/min ramp, 200–3000 rpm and a 2 mm orbit; it can't cool. It goes only in slots 1, 3, 4, 6, 7 or 10, with nothing taller than 53 mm to its left or right | Shaking at room temperature (E1, E3), heating to 40–80 °C (E2), and the hot-water steps in E4 | Nothing else is recorded: not its slot, adapter or cable, and no test run. Check each and measure the well temperature |
| **OT-2** | P300 single GEN2 on the left mount, right mount empty (the P20 is on the CubXL). Only one controller can drive the robot at a time | Fills the plates | The deck calibration dates from 01-27 and has been stale since the 09-10 move. The P300 has no tip-length or pipette-offset calibration, and there are no labware offsets. Calibrate, run Labware Position Check, check volumes by weighing water, then re-check the sensor's pickup route |

**Pick one place for the monitored plate.** The camera focus and the sensor heights only hold for
one plate height.
- **Recommended:** put the heater-shaker in slot 7 under the camera, and keep every monitored plate on
  it, heated or not, shaken or not. That costs a refocus and new sensor heights. The plate sits
  several centimetres higher on the module and its adapter than on the deck. The 10-30 spacer set the
  focus for a plate on the deck, so the spacer may have to change.
- **For data this week instead:** run E0's blank plate and E1a on the deck in slot 7 as it is now,
  unshaken, and move to the heater-shaker after.

**Use opaque black plates** if E0 confirms it. White barite and gypsum show up best on black from
above. The sensor notes already recommend opaque walls against light leaking between wells.

## E0. Commission and calibrate: the 24-hour monitoring plate

**Question.** How little solid can the camera and the sensor detect? Do both keep recording
unattended for 24 h? And what does each well actually experience over that time (temperature,
evaporation, light)?

**Before the plate:** close the gaps in the hardware table. In order:
1. calibrate the OT-2 (deck, tip length, pipette offset, Labware Position Check);
2. weigh water dispenses at 20, 50 and 100 µL;
3. connect and test the heater-shaker in its slot;
4. refocus the camera at the chosen plate height and confirm it with a measured still;
5. set up the time-lapse job, the rail lights and the reboot hold. Lock exposure, gain and white
   balance, or wells turning white will make the rest look darker. The monitoring plan spells out
   the schedule, storage, alerts and a check of the OT-2's clock against the Pi's;
6. set the sensor's hover height over that plate.

**Plate** (200 µL per well, sealed or under oil):
- 48 blank wells of 1 molal NaCl, to give the noise floor, drift and false-positive rate (from dust)
  for each well position. Half are filtered and half unfiltered, which shows what filtering buys.
- A barium sulfate dilution series in triplicate: 0.5, 1, 2, 5, 10, 20, 50 and 100 µg per well,
  pipetted from a stirred, fully precipitated stock suspension (24 wells). This gives a rough
  detection limit. Fresh precipitate is finer than crystals grown slowly, so E1's own end points are
  the better calibration (see E1).
- A dye series in triplicate (for example, two food dyes at 4 dilutions each, 24 wells), to check
  colour and focus across the field.

**Run.**
- Image every 2 min for 24 h with the rail lights on throughout. Turn the room lights on and off at
  a few logged times, and have someone walk past, so the effect of each shows in the data. Most of
  the lid's blackout paper came off on 10-19 to let the camera see in, so room light now reaches the
  plate.
- Send the sensor over 6 wells (blanks and standards) every 1–2 h, as the battery allows. Read
  hovering, about 4 mm above the plate, the height the 10-09 tests favoured. Note which camera
  stills it blocks.
- Weigh the plate before and after, which gives the evaporation through the seal or oil.
- If both kinds of plate are on hand, run the plate twice: once in a black plate, and once in a
  clear plate on black paper.

**On the heater-shaker (half a day).**
- Put a thermocouple or thermistor in a well with 200 µL of water. Log the well temperature at set
  points of 40, 60 and 80 °C, and the drop and recovery after a 100 µL room-temperature addition.
  Opentrons specifies ±0.5 °C at 55 °C and a 10 °C/min ramp for the
  [module](https://docs.opentrons.com/heater-shaker/product-specs/). What matters here is what the
  liquid in a well reaches, and how fast.
- Check whether a seal fogs at 60–80 °C. Compare it with a 30–50 µL mineral-oil overlay, the
  microbatch-under-oil method protein crystallographers use to stop evaporation in small wells
  ([Chayen et al. 1992](https://doi.org/10.1016/0022-0248(92)90241-A)).
- Shake a dye plate at 300, 500 and 1000 rpm to find the fastest speed that doesn't splash under a
  seal or disturb the oil layer.

**Deliverables.**
- the detection limit in µg per well for the camera and for the sensor;
- the noise and drift per well position;
- the measured well temperatures;
- the evaporation rate;
- a 24 h recording with no gaps.

These feed straight into E1's threshold and plate design.

## E1. Barite induction-time statistics at room temperature

**Question.** What is the nucleation rate of barite in 1 molal NaCl at 25 °C as a function of
supersaturation, and does the robot reproduce published values?

**Why this system.**
- All the chemicals are on hand.
- The thermodynamics of barite in NaCl are well established, so the supersaturation is known.
- [He, Oddo and Tomson (1995)](https://doi.org/10.1006/jcis.1995.1397) measured barite induction
  periods against supersaturation in 0–6 molal NaCl at 25 °C, and in 1 molal NaCl from 25 to 90 °C.
  From the abstract ([OSTI 106234](https://www.osti.gov/biblio/106234)): at a given SI, induction
  periods get shorter as NaCl rises to about 3 molal, then slightly longer. Their classical-nucleation
  fits give interfacial energies of about 93 mJ/m² in dilute solution and 79 mJ/m² in 1 molal NaCl
  at 25 °C, falling to 71 mJ/m² at 90 °C.
- A constant 1 molal NaCl medium is also the "swamping electrolyte" approach the review describes:
  the NaCl fixes the activity coefficients, so the Ba and SO₄ levels change the supersaturation and
  little else.

**Design.**
- Make both stocks in 1 molal NaCl: barium chloride at twice the target concentration, and sodium
  sulfate at twice the target. Each well gets 100 µL of each. Every well then has the same medium
  and the same 1:1 mixing. The P300 is accurate at 100 µL.
- **E1a, range-finding (1 plate).** Use 8 SI levels from 1.0 to 2.75 in steps of 0.25, with 8
  replicate wells each, plus 16 blanks, 8 barium-only and 8 sulfate-only wells. In 1 molal NaCl at
  25 °C those levels need 0.32 to 2.45 mM of each ion, from stocks of 0.65 to 4.9 mM
  ([results](results.txt), end of section 3). Once at equilibrium a well holds 10–109 µg of BaSO₄
  across that range, since about 0.1 mM stays dissolved. Check that against E0's detection limit. If the camera can't see the low end, move to 2–3
  molal NaCl. At the same SI that holds a quarter to a third more solid, and it is still inside He
  et al.'s range.
- **E1b, statistics (2 plates on different days).** Choose 3 SI levels from E1a, where the median
  detection time falls between about 10 min and 8 h. Use 24 replicate wells per level, plus 12
  blanks, 6 barium-only and 6 sulfate-only wells. The second plate measures day-to-day spread.
- **Add sulfate last,** with a fresh tip for each well, mixing three times with that tip. Log the
  time of each addition.
- **Shake on the heater-shaker at room temperature** (heater off) at the speed E0 found safe, and
  pause the shaking for each image. Shaken wells keep the solid suspended and act more like the
  stirred vials in the induction-time literature. On the deck (the "data this week" layout), don't
  shake. Either way, keep the choice the same across all the plates being compared.
- **Image** every 1 min for the first 2 h, then every 5 min to 24 h. Once filling is done, send the
  sensor over 4–6 sentinel wells (one or two per level, plus a blank) every 1–2 h. Drop the stills
  it blocks.

**Analysis.**
- For each well, find the detection time *t*ᵈ: the first image where the well's signal rises above
  its own starting level by 5σ (σ for that position, from E0) and stays there.
- For each level, plot the fraction of wells detected against *t* − *t*₀ and fit
  *P*(*t*) = 1 − exp[−*JV*(*t* − *t*ᵍ)], following Jiang and ter Horst (2011). Here *J* is the rate,
  *V* the well volume, and *t*ᵍ the growth time to the detection limit.
- Plot ln *J* against 1/ln²*S* to get an interfacial energy, and compare it with He et al.'s
  79 mJ/m². Use their definition of *S* and their shape factor, or the two numbers won't be
  comparable.
- Once a well has nucleated and stopped changing (24–48 h), its solid is the barium above solubility,
  which PHREEQC gives (about 0.1 mM stays dissolved in 1 molal NaCl). That well's final signal
  against this known mass is the in-situ calibration, and it beats E0's standards.
- At the end, filter or centrifuge the solid from 3–4 wells and confirm barite by XRD or Raman.

**What it shows.** The platform measures a well-defined kinetic quantity with uncertainties, checked
against a published dataset, from hardware the lab already has. That is the preliminary-data shape
the [nucleation-statistics direction](https://github.com/vertical-cloud-lab/digital-wetlab/blob/2fb7592/grants/ot2-new-directions/README.md#4-nucleation-statistics-and-crystallisation-inhibitors-the-current-setup-re-aimed)
in PR 83 needs.

**One trap to avoid.** At matched SI, water holds far less barite than brine. At SI 2.0 a 200 µL
well ends up with 6 µg of solid in water but 43 µg in 1 molal NaCl ([results](results.txt),
section 3). A camera will see the brine wells sooner even if both nucleate at the same moment. Any comparison across NaCl
levels needs a threshold relative to each well's final signal, or the colour sensor if it proves
more sensitive. That is why E1 holds NaCl constant.

## E2. The same, on the heater-shaker at 40, 60 and 80 °C

**Question.** How does the barite nucleation rate change with temperature at fixed SI? This is He et
al.'s temperature series, also in 1 molal NaCl.

**Design.**
- Use E1b's layout at each temperature, holding SI fixed. Barite becomes more soluble as it warms,
  so the concentrations rise with temperature. For SI 1.5 in 1 molal NaCl that means 0.57, 0.68,
  0.84 and 0.99 mM at 25, 40, 60 and 80 °C; for SI 2.0 it is 1.02, 1.22, 1.50 and 1.78 mM
  ([results](results.txt), section 3).
- Pre-heat the plate with the barium halves on the heater-shaker. Add the room-temperature sulfate,
  and use E0's measured recovery to set *t*₀ correction or exclusion rules.
- Use an oil overlay rather than a seal if E0 shows fogging. Keep the run under a few hours at 80 °C
  unless E0's evaporation numbers allow longer.
- **Constraints from Opentrons:** the module can't cool and doesn't go below 37 °C, so the "25 °C"
  runs are really room-temperature runs with the heater off; log the temperature. It can sit only in
  slots 1, 3, 4, 6, 7 or 10, nothing taller than 53 mm may stand to its left or right, and no other
  module may be next to it ([API docs](https://docs.opentrons.com/v2/modules/heater_shaker.html)).

**What it shows.** The heater-shaker is used as a controlled variable, with the well temperature
measured, and the result is checked against a published series that runs to 90 °C.

## E3. Gypsum solubility in NaCl, approached from both sides

**Question.** Can the platform measure an equilibrium property correctly, with nucleation kept out of
it? This is the validation the review digest names first: a well-studied salt in NaCl, approached
from both sides, with the solid checked.

**Why gypsum.**
- [Marshall and Slusher (1966)](https://doi.org/10.1021/j100884a044) measured its solubility in
  aqueous NaCl from 0 to 110 °C, and it is a standard test of the Pitzer model (Harvie, Møller and
  Weare 1984).
- It needs only calcium chloride, sodium sulfate, NaCl and a little gypsum powder, so no barium.
- Its solubility is tens of millimolar. A 10% step either side of it is 60–190 µg of gypsum in a
  200 µL well, which is enough to see a seed vanish or grow.
- Its nucleation is slow and its first solid is debated: bassanite or nanoparticle precursors
  ([Van Driessche et al. 2012](https://doi.org/10.1126/science.1215648);
  [Stawski et al. 2016](https://doi.org/10.1038/ncomms11177)). That makes the unseeded wells
  interesting in their own right. They are the system of the BES Synthesis and Processing
  [white paper draft](https://github.com/vertical-cloud-lab/digital-wetlab/blob/2fb7592/grants/ot2-new-directions/bes-white-papers/synthesis-processing.tex)
  in PR 83.

**Predicted solubility** (PHREEQC, `pitzer.dat`, 25 °C), as equal Ca and SO₄. These values include the
NaCl that forms when calcium chloride meets sodium sulfate ([results](results.txt), section 2):

| Added NaCl (molal) | 0 | 0.5 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| Gypsum solubility (mmol/kg water) | 18.1 | 37.4 | 46.8 | 55.8 | 57.6 | 55.6 |

The rise and the flat maximum near 3 molal are the known salting-in behaviour. Anhydrite stays
undersaturated at 25 °C (SI −0.2 to −0.35), so gypsum is the stable solid here.

**Design.**
- Use NaCl levels of 0, 1 and 2 molal. At each, set total Ca = SO₄ at 0.6, 0.8, 0.9, 1.0, 1.1, 1.25
  and 1.5 times the predicted solubility, which gives gypsum SI from about −0.4 to +0.3.
- Run every composition twice, seeded and unseeded, in triplicate: 3 × 7 × 2 × 3 = 126 wells, so use
  two plates or fewer replicates.
- **Seeds:** about 50 µg of reagent gypsum per well, added as 10 µL of a stirred slurry in
  gypsum-saturated solution. Mix the slurry tube before each draw.
  - Count the 10 µL in the composition. It carries about 0.8 mM of Ca and SO₄ into the well, close to
    half the smallest grid step at 0 molal NaCl.
  - Give each unseeded well 10 µL of the same solution, filtered, so the two series match.
  - At 0.9 × solubility a well can dissolve 60–190 µg of gypsum (0 to 2 molal NaCl), and at 1.1 ×
    it has as much to grow. A 50 µg seed should therefore vanish or at least double.
- **Stocks:** use 0.1 M and 0.4 M of each salt so that every P300 dispense is 20 µL or more, plus 5 M
  NaCl and water. Add calcium before sulfate, and mix.
- **Equilibrate for 48–72 h** on the heater-shaker at room temperature, shaking, with images every
  10 min and a sensor trip over sentinel wells every few hours. Evaporation has to stay well under
  10% over the run, or it will move the 0.9× and 1.1× wells across the line. E0 measures it.

**Readouts.**
- **Seeded wells give the solubility bracket.** If the signal falls to the blank level, the seed
  dissolved and the well was undersaturated. If it rises, the seed grew and the well was
  supersaturated. The solubility lies between the last dissolving and the first growing composition,
  within about ±5–10% at this spacing. Compare that bracket with PHREEQC and with Marshall and
  Slusher.
- **Unseeded wells show the metastable limit:** compositions above solubility that stay clear for
  72 h. That gap is the nucleation barrier, measured right beside the equilibrium value.
- **For an actual number, not just a bracket:** run ICP-OES on the filtered supernatant of a few
  equilibrated seeded wells, with gravimetric dilution, matrix-matched standards and an internal
  standard (the review digest's answer to the ICP-OES point).
- **Identify the solid** in seeded and unseeded wells by XRD or Raman at the end: gypsum against
  bassanite or anhydrite.

**What it shows.** The robot can locate a real equilibrium boundary, and show next to it how far
nucleation lags. That is exactly the distinction the review said the proposal missed.

**Later, on the heater-shaker.** Anhydrite becomes the stable phase as the temperature rises. In
these wells PHREEQC puts the crossover just below 60 °C: anhydrite SI is +0.04 at 60 °C and +0.23 at
80 °C at gypsum saturation. Published estimates for pure water range from about 40 to 60 °C.
Anhydrite rarely nucleates at these temperatures, though. A 60–80 °C version of E3 is therefore a clean test of "which solid
forms", with XRD deciding the answer.

## E4. Precipitate colours for qualitative analysis (replaces 001)

**Question.** Can the camera and the 8-channel sensor give a reliable observation library for the
qualitative-analysis benchmark (colour, time course, dissolution), and can the sensor separate
precipitates that look alike?

**Why.**
- This is the robot's original purpose
  ([`opentrons-inorganic-wet-lab-agents.txt`](../../opentrons-inorganic-wet-lab-agents.txt), Phase 1).
- Kevin Jablonka's group has since published the simulated version, the `wetlab` environment in Corral
  ([arXiv:2604.18805](https://arxiv.org/abs/2604.18805)). A real-hardware observation library is what
  the [teaching-and-reasoning direction](https://github.com/vertical-cloud-lab/digital-wetlab/blob/2fb7592/grants/ot2-new-directions/teaching-and-reasoning.md)
  in PR 83 needs first.
- Precedents: a first-year lab determined the solubility product of lead iodide from
  robot-dispensed plates ([Norquist et al. 2023](https://doi.org/10.1021/acs.jchemed.3c00445)).
  Coscientist had a GPT-4 agent drive an OT-2 and work out which colours were in which wells
  ([Boiko et al. 2023](https://doi.org/10.1038/s41586-023-06792-0)).

**Reactions** (aqueous, nothing volatile, so they can run in CB154):

| Precipitate | Reagents | Colour | On hand? |
|---|---|---|---|
| AgCl / AgBr / AgI | silver nitrate with sodium chloride, potassium bromide or potassium iodide | white / cream / pale yellow | sodium chloride only |
| PbI₂ | lead(II) nitrate with potassium iodide | bright yellow | lead nitrate only |
| PbCl₂ | lead(II) nitrate with sodium chloride (precipitates only at the higher concentrations) | white needles | yes |
| PbSO₄ | lead(II) nitrate with sodium sulfate | white | yes |
| BaSO₄ | barium chloride with sodium sulfate | white | yes |

Chromate tests (Ag₂CrO₄ red-brown, PbCrO₄ yellow) are left out unless EHS approves chromium(VI).
The ammonia test (AgCl dissolving in NH₃) needs a hood.

**Design.**
- Use the original plan's concentrations (0.01, 0.05 and 0.1 M) in triplicate.
- Image at 0, 10 and 30 s and at 2 and 10 min, the original time points. Take sensor spectra at
  10 min.
- Two heater-shaker steps:
  - PbCl₂ dissolves in hot water. This is the classical step that separates lead from silver in
    Group I.
  - PbI₂ dissolves when hot and recrystallises as it cools.
- The key test: do the sensor's 8 channels separate AgCl, AgBr and AgI, and AgI from PbI₂, where the
  camera's RGB can't? It may not. The differences between these solids are mostly in the blue,
  410 nm is unusable, and the sensor compresses colour differences 2.6–4.4× on paint. Untried
  remedies listed in its notes may help: a PTFE-tape diffuser, an opaque plate, and a white
  reference at each well. If the sensor can't separate them, that limit belongs in the observation
  model the agents are tested against.
- **Applying the review here:** record time courses, because what is visible depends on
  nucleation. If a solubility product is wanted (as Norquist et al. did for PbI₂), bracket it from
  both sides, as in E3, or by clear points on the heater-shaker. Don't take it from the onset.

**Safety.** Lead nitrate is a carcinogen (Cat. 1B) and reproductive toxin (Cat. 1A). The
designated-area, waste and training steps in the
[lead plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md)
still apply. Without sulfide, aqueous lead salts don't need a hood, but weigh the solid in one, or
buy a ready-made solution. Silver nitrate stains and is corrosive.

## Deferred: PbS and the sulfide work

The PbS vials (003) and the lead plan's sulfide plates are the petroleum-specific part. They need the
hood, an H₂S detector and EHS sign-off. The review's sulfide points also mean an open plate can't
give data worth defending:
- sulfide equilibria need a controlled H₂S partial pressure, in closed vessels;
- PbS is supersaturated across almost the whole old design;
- equilibrium lead at galena saturation is far below what ICP-OES can see after a brine is diluted.

If sulfide comes back, the experiment the review would accept is constant-medium solubility in
sealed vials with trace analysis, not an OT-2 plate. The vial tests can still be run in the hood as
a contrast demo for the camera, but they won't produce publishable data.

## Order, effort and what to buy

| Step | What | Time | Needs |
|---|---|---|---|
| 1 | **E0** commissioning (calibration, heater-shaker check, refocus, time-lapse job), then the 24 h plate | 2–3 days + 24 h unattended | on hand, plus syringe filters, seals or mineral oil, a thermocouple |
| 2 | **E1a** barite range-finding | ½ day + 24 h | on hand |
| 3 | **E1b** barite statistics, 2 plates | 2 × (½ day + 24 h) | on hand; XRD or Raman time for 3–4 samples |
| 4 | **E3** gypsum from both sides | 1 day + 72 h | calcium chloride dihydrate and gypsum powder (both cheap and low-hazard) |
| 5 | **E2** barite at 40/60/80 °C | 3 × (½ day + a few hours) | on hand, plus E0's temperature and evaporation numbers |
| 6 | **E4** colour library | 1–2 days | silver nitrate solution, potassium bromide, potassium iodide |

**To buy:**
- 0.2 µm syringe filters (PES or nylon) and 10–20 mL syringes;
- optically clear adhesive seals, or light mineral oil;
- a thermocouple or thermistor probe thin enough for a well;
- black or clear flat-bottom 96-well plates, chosen from E0;
- calcium chloride dihydrate (CAS 10035-04-8) and calcium sulfate dihydrate (gypsum, CAS 10101-41-4);
- for E4: 0.1 M silver nitrate, potassium bromide and potassium iodide.

The PbS-related purchases (H₂S detector, pH buffers) can wait.

## Where each one leads

| Experiment | Direction in [PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/blob/2fb7592/grants/ot2-new-directions/README.md) | Deadline it could feed |
|---|---|---|
| E1, E2 (barite rates) and E3's unseeded wells (gypsum induction) | 4: nucleation statistics | DOE BES Synthesis and Processing Science: white paper Nov 30, 2026, application Feb 1, 2027. The draft says preliminary distributions can be measured first; E1 is that measurement |
| E3 (solubility from both sides) | Validation the review asked for; 2: brines | A future PRF try with a new design (PR 82 advises Sep–Oct 2027 at the earliest); the Great Salt Lake and Separation Science pitches |
| E4 (colour library) | 6: qualitative analysis for teaching and AI reasoning | NSF IUSE: EDU (Jan 20, 2027) and CyberTraining (Jan 21, 2027), NSF–DFG with Kevin Jablonka's group |
| E0 (24 h monitoring) | All | The TMS 2027 equipment-monitoring abstract and any methods section |

## Decisions for Sterling

1. **E1/E2 before E3, or E3 first?** E1 uses only chemicals on hand. E3 is the more direct answer to
   the review but needs calcium chloride and gypsum (a small order).
2. **Shake or don't shake** during E1–E3. Shaking is closer to the stirred-vial literature, but
   imaging has to pause for it. Pick one and keep it.
3. **Seal or oil.** Let E0 decide, but oil is likely at 60–80 °C.
4. **XRD/Raman and ICP-OES access** for E1 and E3 end points. Which campus instruments, and who books
   them?
5. **E4's chemicals and EHS:** silver nitrate, and whether chromate is in or out.

## Sources

Checked on Crossref on 2026-11-02; induction-time details are from the abstracts on OSTI.

| Paper | Used for |
|---|---|
| He, Oddo and Tomson 1995, *J. Colloid Interface Sci.* 174, 319 [10.1006/jcis.1995.1397](https://doi.org/10.1006/jcis.1995.1397) ([OSTI](https://www.osti.gov/biblio/106234)) | Barite induction times in 0–6 molal NaCl and 25–90 °C: E1, E2 benchmark |
| Lancia, Musmarra and Prisciandaro 1999, *AIChE J.* 45, 390 [10.1002/aic.690450218](https://doi.org/10.1002/aic.690450218) ([OSTI](https://www.osti.gov/biblio/329250)) | Gypsum induction periods by laser light scattering, S 1–4, 25–90 °C: E3 unseeded wells |
| Jiang and ter Horst 2011, *Cryst. Growth Des.* 11, 256 [10.1021/cg101213q](https://doi.org/10.1021/cg101213q) | Nucleation rates from induction-time distributions: E1 analysis |
| Brandel and ter Horst 2015, *Faraday Discuss.* 179, 199 [10.1039/C4FD00230J](https://doi.org/10.1039/C4FD00230J) | Measuring induction times and rates |
| Kashchiev and van Rosmalen 2003, *Cryst. Res. Technol.* 38, 555 [10.1002/crat.200310070](https://doi.org/10.1002/crat.200310070) | Heterogeneous nucleation, filtering |
| Marshall and Slusher 1966, *J. Phys. Chem.* 70, 4015 [10.1021/j100884a044](https://doi.org/10.1021/j100884a044) | Gypsum solubility in NaCl, 0–110 °C: E3 benchmark |
| Harvie, Møller and Weare 1984, *GCA* 48, 723 [10.1016/0016-7037(84)90098-X](https://doi.org/10.1016/0016-7037(84)90098-X) | The 25 °C Pitzer model for gypsum in NaCl (no barium) |
| Monnin 1999, *Chem. Geol.* 153, 187 [10.1016/S0009-2541(98)00171-5](https://doi.org/10.1016/S0009-2541(98)00171-5) | Barite solubility in electrolyte solutions to 200 °C |
| Appelo 2015, *Appl. Geochem.* 55, 62 [10.1016/j.apgeochem.2014.11.007](https://doi.org/10.1016/j.apgeochem.2014.11.007) | Source ("ref. 3") of `pitzer.dat`'s barite, Ba–Cl and Ca–Na–SO₄–Cl entries used here |
| Van Driessche et al. 2012, *Science* 336, 69 [10.1126/science.1215648](https://doi.org/10.1126/science.1215648) | Bassanite as a precursor to gypsum |
| Stawski et al. 2016, *Nat. Commun.* 7, 11177 [10.1038/ncomms11177](https://doi.org/10.1038/ncomms11177) | Gypsum from aggregated nanoscale species |
| Chayen, Shaw Stewart and Blow 1992, *J. Cryst. Growth* 122, 176 [10.1016/0022-0248(92)90241-A](https://doi.org/10.1016/0022-0248(92)90241-A) | Oil overlay against evaporation |
| Norquist et al. 2023, *J. Chem. Educ.* 100, 3445 [10.1021/acs.jchemed.3c00445](https://doi.org/10.1021/acs.jchemed.3c00445) | PbI₂ solubility product with lab automation in teaching: E4 |
| Boiko et al. 2023, *Nature* 624, 570 [10.1038/s41586-023-06792-0](https://doi.org/10.1038/s41586-023-06792-0) | An LLM agent driving an OT-2 on a colour task: E4 |
