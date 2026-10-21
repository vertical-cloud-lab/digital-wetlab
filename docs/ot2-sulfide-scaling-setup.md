# Setting up the OT-2 for the sulfide-scaling experiments

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) by
@timothy-commins: pull from the grant proposal for the petroleum sulfide-scaling experiments
and list what has to be done to set up for testing.

**Revised 2026-10-21 from the proposal itself.** The first version (2026-10-15, in this file's
history) was written without it, because the proposal was still in `digital-wetlab-private`. It
is now in this repo as [`drafts/main_proposal_final.tex`](../drafts/main_proposal_final.tex).
Nothing on the robot or the Pis was touched for either version. The lab's state comes from the
byu-vcl issues cited below.

## Sources

| source | what it gives |
| --- | --- |
| [`drafts/main_proposal_final.tex`](../drafts/main_proposal_final.tex) | the plan: aims, stocks, design, ranges, platform, detection, timeline |
| [`drafts/safety_explanation.md`][safety] | the safety plan written for the application |
| [`SHOPPING_LIST.md`][shop] | reagents, consumables, tip budget, and the experimental notes at its end |
| [`grants/acs-prf/PARAMETER_INVENTORY.md`](../grants/acs-prf/PARAMETER_INVENTORY.md) | the ~48 target parameters |
| [`BATCH_TEMPERATURE_AND_TIMING.md`][batch-temp] (branch for [issue 62](https://github.com/vertical-cloud-lab/digital-wetlab/issues/62)) | how the heated runs would be done |
| plans [`002`][plan-002] and [`003`][plan-003] and the [protocol that ran on 03-05][march-protocol] (PRs [3](https://github.com/vertical-cloud-lab/digital-wetlab/pull/3) and [8](https://github.com/vertical-cloud-lab/digital-wetlab/pull/8)) | the BaSO₄ plate and the PbS vial tests |
| byu-vcl [15][vcl-15-bought], [29][vcl-29], [30][vcl-30], [34][vcl-34], [68][vcl-68], [81][vcl-81], [195][vcl-195], [197][vcl-197] and the [calibration notes][calib] | what the lab has: chemicals, fume hood, glovebox, camera, plate reader, heater-shaker, pipettes |
| PHREEQC runs for this revision (step 2) | competing precipitates and impossible corners of the design |

## What the proposal plans

| | the proposal says | where |
| --- | --- | --- |
| Systems | FeS and PbS. BaSO₄ positive controls on every plate. About 100 wells with cyclohexanecarboxylic acid, a model naphthenic acid. | [Aim 1][p-aim1], [controls][p-qa] |
| Design | Latin hypercube over 19 inputs, "18 independent stock-solution compositions plus temperature". About 2,500 conditions per metal, each on 3 replicate plates (7,500 wells per metal), then about 15,000 adaptive wells: about 30,000 in all. | [design][p-design], [adaptive][p-adaptive] |
| Ranges | metal 0.01–100 mM (log-spaced); sulfide 0.01–50 mM (log-spaced); sodium acetate or propionate 0–5,000 mg/L; NaCl 0.5–5 molal ± 0.5 molal CaCl₂; pH 4–9; 25, 60 and 90 °C | [design][p-design] |
| Stocks | FeSO₄ (or FeCl₂), PbCl₂, NaHS, NaCl, CaCl₂, sodium acetate, sodium propionate, MES, HEPES and bicarbonate, made up by mass in deoxygenated ultrapure water. Fe²⁺ stocks fresh daily in water sparged with N₂ for over 30 min; about 10% checked by the 1,10-phenanthroline assay at 510 nm, and remade above 2% Fe³⁺. | [stocks][p-stocks] |
| Robot | OT-2 with single- and 8-channel GEN2 pipettes (20–300 µL) and a heater-shaker "(25–90 °C)" that mixes by orbital shaking | [platform][p-robot] |
| Containment | The OT-2 inside a chemical fume hood for all sulfide and lead work, and inside an N₂ glovebox (O₂ < 5 ppm, monitored) for Fe²⁺ work. Adhesive seals right after dispensing. Continuous H₂S detection and temperature and humidity logging. 60–90 °C runs in sealed glass vials. | [safety][p-safety], [stocks][p-stocks] |
| Detection | A plate reader bought from startup funds, at 600 nm, read at 1, 5, 15, 60 and 240 min. Visual scoring as a backup. An overhead camera and in-situ spectrophotometry (Fig. 2). ICP-OES on about 300 conditions, repeated in 5 mL vials, at $24 per sample. | [detection][p-detect], [Fig. 2][p-fig2], [ICP-OES][p-icp], [controls][p-qa] |
| Records | Timestamps, ambient temperature, humidity, solution ages and OT-2 protocol version for every run, in a structured database. Plate images archived; over 2,000 wells annotated by hand to train an OpenCV classifier. | [design][p-design], [images][p-images] |
| Order | Months 1–3: stocks and protocol validation. Months 3–10: FeS at 25 °C across ionic strength and pH. Year 2: PbS at 25–90 °C, and FeS at temperature. If Fe²⁺ oxidation can't be controlled, PbS goes first. | [timeline][p-timeline], [fallback][p-fallback] |

## Where the lab stands against that

The shopping list's [equipment section][shop-equip] says everything major is "already
available": a fume hood, a glovebox, an 8-channel pipette, plate-reader access and ICP-OES
access. Of those, the lab has the OT-2 and a P300 single-channel.

| needed | state | source |
| --- | --- | --- |
| A fume hood around the OT-2 | **None in CB154.** Facilities ruled one out and offered a canopy hood. Interim use of the Dillon lab's hood is agreed; putting the OT-2 in it hasn't been discussed. | byu-vcl [29][vcl-29], [195][vcl-195] |
| An N₂ glovebox around the OT-2 | **Not bought.** byu-vcl 30 is choosing a box for the alloy work; on 09-27 a used Terra Universal isolator looked best. No box has been checked against the OT-2's size or against wet H₂S work. | byu-vcl [30][vcl-30] |
| Lead and sulfide salts | On the shelf since 03-03: **Pb(NO₃)₂ (500 g) and (NH₄)₂S solution (500 mL)**, plus NaCl, Na₂SO₄, AgNO₃ and BaCl₂. **No PbCl₂, NaHS, iron(II) salt, CaCl₂, organic salts or buffers.** | byu-vcl [15][vcl-15-bought] |
| Pipettes | A P300 single GEN2 on the left mount, uncalibrated, on 09-11. A P20 single GEN2 ran the March plate. **No record of an 8-channel.** | [calibration notes][calib] |
| Heater-shaker | In the OT-2 since 10-13, not seated or wired. It holds 37–95 °C, so not 25 °C, and it can't cool. The temperature module (4–95 °C) went back in its box. | byu-vcl [81][vcl-81], [Opentrons docs][hs-docs] |
| Plate reader | **On hold since 06-20** (a Byonoy Absorbance 96 quote). No shared reader is booked. | byu-vcl [68][vcl-68] |
| Overhead camera | byu-vcl 34 is still open; last update in June. | byu-vcl [34][vcl-34] |
| In-situ sensor | The colour sensor works on the OT-2 (paint tests, closed 10-15). | byu-vcl [197][vcl-197] |
| H₂S detector, temperature and humidity logger, ICP-OES | No record of any of them. | |
| Balance | HR-100A: 102 g × 0.1 mg. | [issue 9](https://github.com/vertical-cloud-lab/digital-wetlab/issues/9) |

## The checklist

### 0. Decisions for Sterling, before buying anything

The proposal, its safety plan and its shopping list disagree on these points. Each one changes
what to buy or how the robot is set up.

- [ ] **pH of the sulfide wells: 4–9, or 8 and above?** The design varies pH from 4 to 9, but
  the proposal's safety paragraph and the [safety plan][s-ph] both say all experiments run at
  pH ≥ 8 "where HS⁻ dominates", so that H₂S stays negligible. In 0.5 molal NaCl, PHREEQC puts
  30–40% of the dissolved sulfide in the H₂S form at pH 7, 82–87% at pH 6 and over 99.8% at
  pH 4, against 2–6% at pH 8 (step 2). Either keep sulfide wells at pH 8 and above and drop the
  acid half of the design, or tell EHS that the plan includes acidic sulfide and agree controls
  for it. Most of step 1 depends on this.
- [ ] **How the 60 and 90 °C runs are done.** The proposal has the heater-shaker covering
  25–90 °C in plates, and also says 60–90 °C runs use sealed glass vials. The shopping list
  ([note 7][shop-n7]) and the [temperature brainstorm][batch-temp] go with vials in a heating
  block, filled by hand. Plates at 90 °C need polypropylene plates and seals rated for the
  heat; vials need a heating block for 5 mL vials. Either way, 25 °C is not a heater-shaker
  setting. Use the room and log its temperature, or the boxed temperature module.
- [ ] **Lead and sulfide sources.** The proposal says PbCl₂ and NaHS. The lab has Pb(NO₃)₂ and
  (NH₄)₂S.
  - Ammonium is a buffer (pKa 9.25) and one more ion for the model to carry, so (NH₄)₂S
    works against the pH axis. Buy NaHS, or the Na₂S·9H₂O the shopping list gives as the
    alternative.
  - PbCl₂ dissolves only to about 36 mM at 20 °C ([shopping list, note 2][shop-n2]), too little
    for the 100 mM top of the metal range. Pb(NO₃)₂ reaches it, but puts nitrate in every lead
    well. Lead chloride also caps the lead-only blanks: in 0.5 molal NaCl, PbCl₂ saturates at
    about 5 mM lead (step 2).
- [ ] **FeCl₂ rather than FeSO₄.** With 0.5 molal CaCl₂ in the matrix, the sulfate from FeSO₄
  saturates gypsum at 7–10 mM iron, a tenth of the top of the iron range (step 2). The shopping
  list already carries FeCl₂ as the sulfate-free option.
- [ ] **Can a well reach 5 molal NaCl?** Saturated NaCl is about 6.1 mol/kg (5.4 M). To reach
  5 molal in a well, about 83% of the well has to be saturated brine. That leaves about 34 µL
  of a 200 µL well for metal, sulfide, CaCl₂, organic salt, buffer and pH adjustment. With
  0.5 molal CaCl₂, halite saturates at 5.3 molal NaCl, so a 5 molal well is one 5% loss of water
  away from growing salt crystals (step 2). Either make every stock up in brine (matrix-matched
  stocks, so mixing doesn't dilute the salt) or lower the top of the range. The design
  generator needs a volume check in any case: a Latin hypercube picks each concentration
  independently, and many of its corners won't fit in one well.
- [ ] **Name the 18 stocks.** The design has "18 independent stock-solution compositions plus
  temperature", but no file lists the 18; the proposal names ten. Write them down with their
  concentrations, then check the design against them for volume and solubility.
- [ ] **Buffers for each pH band.** MES (pH 5.5–6.7) and HEPES (6.8–8.2) leave pH 4–5.5 covered
  only by acetate, which is a design variable. Bicarbonate, listed for pH 8–9, gives off CO₂
  when acidified. At 10 mM and pH 7–8 it also leaves 1–10 mM lead supersaturated with
  cerussite (PbCO₃) by 2.5–4.4 SI units, and iron with siderite (FeCO₃) by up to 3.5 (step 2).
  A Good's buffer such as TAPS or CHES covers pH 8–9 without carbonate; check its metal binding
  first. Also decide how pH is checked, for example with a micro pH electrode on a few wells per
  plate. Readings in concentrated NaCl carry a junction-potential error.
- [ ] **Plate type.** The safety plan picks [polypropylene plates][s-pp] "for compatibility with
  HS⁻/H₂S". The camera and the 600 nm reads need clear polystyrene. The shopping list buys 200
  of each. Decide which campaign uses which.
- [ ] **The 8-channel pipette.** The proposal lists one and the shopping list counts it as
  owned. There's no record of one in the lab, and the 8-channel was taken out of the budget
  ([issue 53](https://github.com/vertical-cloud-lab/digital-wetlab/issues/53)). Buy or borrow
  one, or plan for single channels only.
- [ ] **Which metal first.** The timeline starts with FeS, which needs the glovebox. The
  proposal's fallback starts with PbS, which needs only the hood. With neither in place, PbS
  first is the shorter path.

### 1. Containment and safety, before any lead or sulfide is opened

- [ ] **A fume hood that holds the OT-2.** The proposal promises that the robot sits inside a
  chemical fume hood for all sulfide and lead work. The OT-2 is 57 cm deep and 63–66 cm wide
  and tall (Opentrons' pages swap the two), weighs 42–48 kg, and should have 20 cm of
  clearance around it ([specs][ot2-specs]). CB154 has no hood ([byu-vcl 29][vcl-29]). Ask
  whether the Dillon lab's hood ([byu-vcl 195][vcl-195]) can take the robot, or what EHS will
  accept in CB154 instead (the canopy hood Facilities offered, or a ventilated enclosure). If
  the answer differs from the proposal, change its safety text to match.
- [ ] **A glovebox for the Fe²⁺ work.** It has to:
  - hold the OT-2 with room to work, and have a way to get it in (it won't go through an
    antechamber);
  - pass power, USB for the heater-shaker, and Ethernet through the wall;
  - keep O₂ below 5 ppm, with a monitor (proposal);
  - vent to a hood, since FeS runs make H₂S ([shopping list, note 1][shop-n1]).

  Keep it separate from the alloy box in [byu-vcl 30][vcl-30]. Sulfur compounds poison the
  copper catalyst in standard glovebox purifiers, and open aqueous plates load the drier. The
  proposal says the box "will not be compromised for more moisture-sensitive projects"; that
  holds only if it is a different box. Add a room O₂-depletion alarm if N₂ is used in volume
  (safety plan; [byu-vcl 41][vcl-41]).
- [ ] **H₂S detectors.** One worn during all sulfide work ([safety plan][s-detector]: alarm at
  5 ppm), and a second at the robot ([shopping list, note 4][shop-n4]). The lab's 3M half-masks
  have P100 particle filters, which don't stop H₂S ([byu-vcl 15][vcl-15-resp]).
- [ ] **Get the H₂S limits right in the SOP.** The safety plan gives "OSHA TWA 1 ppm; STEL
  5 ppm" ([line 45][s-limits]) and the shopping list "OSHA 10 ppm ceiling". Neither is OSHA's:
  1 and 5 ppm are ACGIH's TLVs, a 10 ppm ceiling is NIOSH's REL, and OSHA's general-industry
  limit is a 20 ppm ceiling with a 50 ppm peak for 10 minutes ([OSHA Table Z-2][osha-z2],
  [NIOSH][niosh-h2s]). Take the alarm set points from EHS.
- [ ] **Written SOPs before any work starts.** The safety plan names five ([line 106][s-sops]):
  NaHS stock preparation, Pb²⁺ handling and waste, Fe²⁺ glovebox work, OT-2 operation, and
  high-temperature vials. Use the BYU Engineering [SOP template][sop-template] with an emergency
  section. Include the seal step: the OT-2 can't seal plates, so a person seals each plate
  "immediately after dispensing". Say where (in the hood), when, and how it fits the 1-min read.
- [ ] **A job safety analysis before each new campaign** (first PbS plate, first FeS plate,
  first heated run), training records, a two-person rule for sulfide and lead work, and an SDS
  binder. The safety plan commits to all four.
- [ ] **Treat the lead salts as particularly hazardous substances.** The Pb(NO₃)₂ SDS on file
  classes it Carc. 1B and Repr. 1A. OSHA's lab standard,
  [29 CFR 1910.1450(e)(3)(viii)][osha-lab], then calls for a designated area, containment, and
  waste and decontamination procedures. Ask EHS how BYU wants that done. Double gloves (safety
  plan).
- [ ] **Storage.** Oxidisers (Pb(NO₃)₂, HNO₃) away from reducers (NaHS, hydroxylamine); acids
  away from sulfide. While the (NH₄)₂S is kept, it goes in a flammable cabinet (flash point
  32 °C).
- [ ] **Waste.** Lead waste, including lead-bearing sulfide waste, goes to hazardous waste and
  never down the drain. The safety plan oxidises sulfide-only waste with dilute H₂O₂ or bleach
  in the hood ([line 153][s-waste]); don't use bleach on the ammonium sulfide (chloramines) or on
  anything acidic (chlorine). Keep barium waste and contaminated solids separate.
- [ ] **Eyewash, shower, a spill kit that handles heavy metals, and an extinguisher**, checked
  before each campaign (safety plan).

### 2. Chemicals and stocks

- [ ] **Buy what isn't on the shelf.** The [shopping list][shop] has quantities, grades and
  examples:
  - NaHS·xH₂O or Na₂S·9H₂O; FeCl₂·4H₂O; PbCl₂, if step 0 keeps it; CaCl₂·2H₂O
  - sodium acetate trihydrate, sodium propionate, cyclohexanecarboxylic acid
  - the buffers chosen in step 0, HCl and NaOH, pH calibration buffers
  - trace-metal HNO₃ and ICP standards (Fe, Pb, multi-element)
  - 1,10-phenanthroline, hydroxylamine hydrochloride, ferrous ammonium sulfate
  - an N₂ cylinder with a regulator and a sparging line
- [ ] **Standardise the sulfide stock.** "Prepared gravimetrically" doesn't work for NaHS: the
  solid is at least 70% NaHS with variable water, and its solutions oxidise within days
  ([shopping list, note 3][shop-n3]). Make it fresh daily, in the hood, in deoxygenated water.
  Then titrate it (iodometric: iodine, sodium thiosulfate and starch, none of them on the
  shopping list) or read it at 230 nm (a UV spectrophotometer and a quartz cuvette).
- [ ] **Fe²⁺ stocks:** fresh daily from the solid, in water sparged with N₂ for over 30 min,
  inside the glovebox. Run the phenanthroline check on about 10% and remake above 2% Fe³⁺
  (proposal). The 510 nm read needs an instrument: the plate reader if its filters include
  510 nm, or a spectrophotometer.
- [ ] **Ultrapure water.** The proposal says ultrapure, and the shopping list assumes a Milli-Q
  in the lab. The lab has used DI from the Chem Stores tap ([byu-vcl 15][vcl-15-di]). Find an
  18.2 MΩ·cm source, or write DI in the methods.
- [ ] **Weigh the solids, not the bottles.** The 0.1 mg balance tops out at 102 g.
- [ ] **Keep a stock log:** lot, mass, volume, time made and standardisation result. The proposal
  records "solution ages" for every run.
- [ ] **Run a saturation check on the final stock list and ranges** for phases other than FeS
  and PbS. For this revision PHREEQC was run at 25 °C on the planned stocks and ranges:
  pitzer.dat for gypsum and halite; llnl.dat, minteq.v4.dat and wateq4f.dat for lead, which
  pitzer.dat lacks; phreeqc.dat for iron sulfide and siderite. Outside pitzer.dat the activity
  models are Davies or B-dot, so anything above about 1 molal is rough.

  | check | result | what it means for setup |
  | --- | --- | --- |
  | Gypsum: FeSO₄ with 0.5 molal CaCl₂ | Saturates at 7–10 mM FeSO₄ in 0.5–5 molal NaCl; SI ≈ +1 at 100 mM. With 0.05 molal CaCl₂, at 30–65 mM. | Use FeCl₂. |
  | Halite: 5 molal NaCl with CaCl₂ | Saturates at 6.1 molal NaCl alone, 5.7 with 0.25 molal CaCl₂, 5.3 with 0.5. | A 5 molal + 0.5 molal CaCl₂ well grows salt crystals after losing 5% of its water. Seal plates and check evaporation by weight. |
  | PbCl₂ in lead-only blanks | Dissolves to 34 mM in water (literature: about 36). In 0.5 molal NaCl, about 5 mM (5–9 mM across the three databases). Above 1 molal the databases disagree by orders of magnitude. | White PbCl₂ in high-lead blanks at low salt. |
  | Carbonates: 10 mM NaHCO₃ at pH 7–8, 0.5 molal NaCl | Cerussite SI +2.5 to +4.4 at 1–10 mM Pb; siderite SI +0.2 to +3.5 at 1–10 mM Fe. | Don't buffer with bicarbonate. |
  | Hydroxides: pH 9, 0.5 molal NaCl, no CO₂ | Lead hydroxychloride SI about +2.5 at 1–10 mM Pb; Fe(OH)₂ SI +0.4 to +1.4 at 1–10 mM Fe (llnl.dat). | Metal-only blanks at pH 9 can precipitate without any sulfide. |
  | Share of dissolved sulfide present as H₂S, 0.5 molal NaCl | 99.8% at pH 4; 82–87% at pH 6; 30–40% at pH 7; 2–6% at pH 8; under 1% at pH 9 | Step 0, the pH range. |
  | Where the boundaries fall, for equal metal and sulfide | FeS (mackinawite to fresh FeS): saturates at about 2–7 mM at pH 4, 0.03–0.07 mM at pH 6 and about 0.001 mM at pH 9. PbS at 0.5 molal NaCl: supersaturated across the whole design in both databases checked, by 3 or more SI units even at 0.01 mM and pH 4. PbS at 5 molal NaCl: llnl.dat still says supersaturated everywhere; minteq.v4.dat puts the boundary at 0.1–6 mM. | The FeS boundary crosses the design at pH 4–7. Low-salt PbS plates measure how fast PbS forms, not where. Where the high-salt PbS boundary lies can't be predicted to within orders of magnitude, which is the gap the proposal is about. |

### 3. The robot

- [ ] **Clear the colour-sensor rig off the deck,** or agree a shared layout, after the
  [README][sensor-readme]'s "one controller at a time" check.
- [ ] **Pipettes.** Put the P20 back on (right mount) for 1–20 µL. Below 20 µL the P300 can't
  pipette, so each extra factor of 10 in a log-spaced range would need another intermediate
  stock. Add the 8-channel if step 0 keeps it.
- [ ] **Calibrate in order:** deck (last done 01-27, before the robot was moved on 09-10), tip
  length, pipette offset, then Labware Position Check inside a protocol run. Use the separate
  Opentrons OT-2 App; the main app dropped the OT-2 in v9.1.1 ([calibration notes][calib]).
  Give the app a way to reach the robot, or run protocols over HTTP from the Pi.
- [ ] **Seat the heater-shaker,** if heated or shaken plates stay in the plan: slot 1, 3, 4, 6, 7
  or 10, with USB and power ([Opentrons docs][hs-docs]).
  - Nothing taller than 53 mm directly to its left or right. A 15 mL tube rack is 61 mm.
  - The NEST flat plate needs the `opentrons_96_flat_bottom_adapter`. Check which adapters
    came with this second-hand unit.
  - The latch must be closed for it to shake.
  - A plate on it can't be lit from below, so plates imaged over a light panel go in another
    slot.
- [ ] **Deck layout and tips.** Place plates, tip racks, stock tubes or reservoirs and the
  heater-shaker in 11 slots. The shopping list's [tip budget][shop-tips] allows about one rack
  per plate: reuse tips for water and NaCl, and keep filter tips for metal and sulfide.
  Opentrons' P300 filter tips hold 200 µL.
- [ ] **Fit the robot into the enclosure** EHS approves: power, network and heater-shaker cables,
  and the camera's view.
- [ ] **Dry-run with water, then with dye** ([preliminary-results plan][prelim-plan], options W1
  and W3): weigh a plate to check volumes, and image a dye gradient to check the camera
  pipeline.

### 4. The protocol

Start from [`preliminary_results/baso4_nacl_gradient_protocol.py`][baso4-protocol] or from the
[protocol that ran on 03-05][march-protocol] (the BaSO₄ plate, despite its file name).

- [ ] **The plate layout the proposal describes:** Latin hypercube wells, matrix-matched blanks
  and BaSO₄ positive controls on every plate, and three replicate plates per batch. Decide how
  many blanks and controls each plate gets.
- [ ] **The volume check** from step 0, in the design generator.
- [ ] **Don't carry precipitate back into the stock tubes.** The 03-05 protocol uses one tip per
  reagent and dispenses 1 mm above the well bottom. The last reagent's tip touches wells that
  already hold the first reagent, then goes back into its tube. With sulfide, that grows PbS in
  the sulfide tube. Dispense the last reagent from above the liquid, or use a fresh tip for
  each well.
- [ ] **Time zero for each well, and the 1-min read.** Adding the last reagent well by well
  spreads t = 0 over minutes, longer than the first read interval. Log each well's start time.
  With an 8-channel there is a way round it: fill two half-plates (a metal side and a sulfide
  side) and combine them column by column, so each column starts at once.
- [ ] **Reads at 1, 5, 15, 60 and 240 min,** as in the final proposal (the March draft had 5, 15,
  60 and 240). Only an on-deck read, by camera or sensor, can make 1 and 5 min: the plate reader
  is off the deck, and the OT-2 has no gripper.
- [ ] **A pause for the seal,** with the sealing time logged.
- [ ] **The metadata the proposal promises:** protocol version (git commit), stock IDs and ages,
  ambient temperature and humidity, and timestamps.
- [ ] **Replace the placeholder two-parameter search space** in
  [`experimentation_script.py`](../experimentation_script.py) with the 19 inputs, once step 0
  names them. The adaptive stages (fully Bayesian, then standard Bayesian optimisation, then
  Latin hypercube again) come after the first campaign.

### 5. Measuring the plates

- [ ] **Plate reader.** It is the proposal's main detector, at 600 nm. Restart the purchase with a
  filter set that includes 600 nm, and 510 nm for the Fe²⁺ assay, or book a shared reader (the
  shopping list names a BioTek Synergy H1 or SpectraMax iD3). With a shared reader, sealed
  plates travel, and hot plates fog their seals as they cool.
- [ ] **Overhead camera** ([byu-vcl 34][vcl-34]): fixed lighting, a colour card in frame,
  recording for over 4 h (the video of the 03-05 dry run
  [stopped after about 1.5 h](https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4005965449)),
  and stills named with their time point.
- [ ] **The colour sensor as the proposal's "in-situ spectrophotometry".** A pass over 96 wells
  takes several minutes, so read sentinel wells. Use a white background for black PbS and FeS.
- [ ] **Scoring and annotation:** a precipitate/no-precipitate score for every well, images
  archived with their metadata, and a labelling sheet or tool for the 2,000-plus hand
  annotations that train the OpenCV classifier.
- [ ] **ICP-OES** (about 300 conditions, paid from startup). Find the instrument and ask about
  salt: 5 molal NaCl needs heavy dilution, so check the Pb and Fe detection limits after
  dilution. Buy syringe filters for the dissolved fraction (they aren't on the shopping list).
  Acidify sulfide-bearing filtrate in the hood, because acid releases H₂S.

### 6. Data

- [ ] **Store each run in MongoDB `digital-wetlab`** (`ot2-runs` exists): each well's conditions
  and start time, images and time points, scores and reads, stock IDs, and the environment log.
- [ ] **Commit design matrices, protocols and analysis to this repo.** It is public, so check
  [CLAUDE.md](../CLAUDE.md) for what must stay out.

## Suggested order

1. **Step 0 with Sterling, and a meeting with EHS** on containment: a hood for the OT-2, glovebox
   venting, and the pH range.
2. **Order** the reagents and consumables for the first campaign.
3. **The robot:** deck cleared, P20 on, calibrated, then water and dye dry runs.
4. **The camera and the sensor.**
5. **A BaSO₄-only plate run through the full machinery:** design generator with the volume check,
   layout with blanks and controls, seal step, per-well timing, reads and metadata. It needs no
   lead or sulfide.
6. **PbS in vials, in a hood.** This tests the NaHS stock, its standardisation and how visible
   PbS is at the low end of the range.
7. **The first PbS plate on the OT-2,** inside whatever EHS approves.
8. **FeS,** once the glovebox is in and the phenanthroline check passes.
9. **The heated runs** (year 2 in the timeline).

## What changed from the 2026-10-15 version

- The proposal names the ranges, stocks and controls, so step 0 is no longer "get the numbers
  from the proposal". It is now a list of places where the proposal, its safety plan and its
  shopping list contradict one another.
- FeS is in scope, and comes first in the timeline. It needs a glovebox that holds the OT-2.
- The proposal promises far more containment than the first version suggested asking EHS for:
  the OT-2 inside a fume hood for all lead and sulfide work.
- Reads are at 1, 5, 15, 60 and 240 min, not 5, 15, 60 and 240.
- New items: the lead and sulfide salts on the shelf aren't the ones the proposal names; the
  5 molal and solubility limits; gypsum from FeSO₄; buffers; plate type; the 8-channel; ICP-OES.
- Corrected: the first version said any PbS mix the robot can pipette will precipitate. That
  holds at 0.5 molal NaCl, but at 5 molal the databases disagree by orders of magnitude on where
  the PbS boundary lies (step 2).

[safety]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md
[s-ph]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L15
[s-limits]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L45
[s-pp]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L94
[s-sops]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L106
[s-detector]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L127
[s-waste]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/safety_explanation.md#L153
[shop]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md
[shop-equip]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L26
[shop-tips]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L134
[shop-n1]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L277
[shop-n2]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L279
[shop-n3]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L281
[shop-n4]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L283
[shop-n7]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/SHOPPING_LIST.md#L289
[p-aim1]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L81
[p-safety]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L107
[p-fig2]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L117
[p-stocks]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L122
[p-design]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L124
[p-adaptive]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L126
[p-robot]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L128
[p-detect]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L130
[p-qa]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L134
[p-images]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L186
[p-icp]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L188
[p-timeline]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L194
[p-fallback]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/2f91cfb/drafts/main_proposal_final.tex#L196
[batch-temp]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/5f01ea7/BATCH_TEMPERATURE_AND_TIMING.md
[plan-002]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/002-baso4-precipitation/README.md
[plan-003]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/003-pbs-vial-tests/README.md
[march-protocol]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/cded249/Experiment_1__AgCl_Precipitation_V1.py
[baso4-protocol]: ../preliminary_results/baso4_nacl_gradient_protocol.py
[prelim-plan]: ../grants/acs-prf/PRELIMINARY_RESULTS_PLAN.md
[vcl-15-bought]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3987730523
[vcl-15-resp]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3923351840
[vcl-15-di]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3993989121
[vcl-29]: https://github.com/vertical-cloud-lab/byu-vcl/issues/29#issuecomment-4093457224
[vcl-30]: https://github.com/vertical-cloud-lab/byu-vcl/issues/30#issuecomment-5853120780
[vcl-34]: https://github.com/vertical-cloud-lab/byu-vcl/issues/34
[vcl-41]: https://github.com/vertical-cloud-lab/byu-vcl/issues/41
[vcl-68]: https://github.com/vertical-cloud-lab/byu-vcl/issues/68#issuecomment-4756219428
[vcl-81]: https://github.com/vertical-cloud-lab/byu-vcl/issues/81#issuecomment-6157219356
[vcl-195]: https://github.com/vertical-cloud-lab/byu-vcl/issues/195
[vcl-197]: https://github.com/vertical-cloud-lab/byu-vcl/issues/197
[calib]: https://github.com/vertical-cloud-lab/byu-vcl/blob/b31a75d/wireless-color-sensor/ot2/opentrons-calibration.md
[sensor-readme]: https://github.com/vertical-cloud-lab/byu-vcl/blob/b31a75d/wireless-color-sensor/ot2/README.md
[sop-template]: https://github.com/vertical-cloud-lab/byu-vcl/blob/b31a75d/byu-engineering-sop-template.md
[ot2-specs]: https://docs.opentrons.com/ot-2/system-description/specs/
[hs-docs]: https://docs.opentrons.com/v2/modules/heater_shaker.html
[osha-lab]: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1450
[osha-z2]: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1000TABLEZ2
[niosh-h2s]: https://www.cdc.gov/niosh/npg/npgd0337.html
