# Lead (PbS) experiments: what to gather and the steps

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) by
@timothy-commins on 2026-10-23. The lead experiments come first because they need a fume hood
and no glovebox. The iron (FeS) experiments wait until the glovebox arrives. The overhead camera
needs a few more days of focusing, so the steps that don't need it come first.

The status column means:

- **have**: a record in byu-vcl, powder-doser or this repo shows it was bought or is in the lab
- **check**: it was bought, but it may be used up, old or somewhere else, so look before relying on it
- **get**: I found no record of it

This all comes from the written record. Nothing was checked in the lab. For the full setup
checklist behind it, see the [2026-10-21 version][prev] (not merged yet).

## The hood

| hood | state | source |
| --- | --- | --- |
| EB B125, the Dillon lab | Interim use agreed on 09-02. The powder doser worked there from 09-03 and has since left. | byu-vcl [195][vcl-195], powder-doser [157][pd-157], [144][pd-144] |
| CB 104, the polishing lab | The BaSO₄ stocks were made there on 03-05. | [issue 1][wl-1-polish] |
| Two ductless benchtop hoods, 49 × 27.4 × 53 in | Won at auction in April, but the invoice charged for the Squidstat instead. The thread stops on 04-30. | digital-alloy-lab [137][dal-137], byu-vcl [31][vcl-31-size] |

Whichever hood it is:

- **Ask the hood's owner about lead and sulfide** before bringing them in. The Dillon lab's
  09-02 note covers tidiness, labels and waste, and mentions neither.
- **A ductless hood needs a filter rated for H₂S**, and for ammonia while the ammonium sulfide is
  in use, plus EHS approval for lead and H₂S work. A ducted hood avoids both questions.
- **Measure it if the OT-2 is going in.** The proposal puts the robot inside a hood for all lead
  and sulfide work. The OT-2 is about 63–66 cm wide and tall, 57 cm deep, and 42–48 kg
  ([specs][ot2-specs]). Check the sash opening, the inside width and the inside depth. The CB 104
  hood's decal asks for work at least 15 cm (6 in) inside the sash ([powder-doser 141][pd-141-decal]).

## Materials

### Safety gear and paperwork

| item | status | notes |
| --- | --- | --- |
| H₂S detector, worn (e.g. BW Clip or Honeywell BW Solo) | **get** | Needed before the sulfide bottle is opened. The safety plan alarms at 5 ppm; take the set point from EHS. About $150–300 ([shopping list][shop-safety]). |
| Lab coats, safety glasses, nitrile gloves | have | [byu-vcl 15][vcl-15-list]. Double-glove for lead. |
| Splash goggles | **get** | [Plan 003][plan-003] asks for goggles and a face shield for sulfide. Only safety glasses are on record. |
| Face shield | have | One ([byu-vcl 15][vcl-15-shield]). |
| Half-face respirators | have, but no use here | Their P100 filters stop dust, not H₂S or ammonia. The hood is the protection. |
| Eyewash, safety shower, spill kit that handles heavy metals | **check** | In the hood's room. |
| SDS binder | **check** | The SDSs for the lead(II) nitrate, ammonium sulfide, sodium chloride and sodium sulfate are on [byu-vcl 15][vcl-15-sds]. Print them, and add barium chloride's and anything new. |
| Written SOP and job hazard analysis, plus training records | **get** | Use the BYU Engineering [SOP template][sop-template]. The lead nitrate SDS lists it as a carcinogen (Cat. 1B) and a reproductive toxin (Cat. 1A). For those, the OSHA lab standard calls for a designated area, containment, and waste and decontamination procedures ([29 CFR 1910.1450(e)(3)(viii)][osha-lab]). |
| Absorbent bench liner, a tray for the hood, a lidded tub for carrying stocks between rooms, a "lead: designated area" sign | **get** | |
| Flammables storage for the ammonium sulfide | **check** | Flash point 32 °C ([SDS][vcl-15-sds]). Keep it away from acids, and from the lead nitrate, which is an oxidiser. |

### Chemicals

The names and CAS numbers of the bottles on hand come from their SDSs on
[byu-vcl 15][vcl-15-sds]. Barium chloride's SDS isn't there, so its form comes from the stock
masses in the [protocol that ran on 03-05][baso4-stocks].

| chemical | formula | CAS no. | status | amount | notes |
| --- | --- | --- | --- | --- | --- |
| Lead(II) nitrate, 500 g | Pb(NO₃)₂ | 10099-74-8 | have | 49.7 mg makes 15 mL of 10 mM | Bought 03-03 ([byu-vcl 15][vcl-15-list]). The proposal names lead(II) chloride (PbCl₂); lead(II) nitrate dissolves far better. |
| Ammonium sulfide solution, about 20 wt% in water, 500 mL | (NH₄)₂S | 12135-76-1 | have, **check** | about 51 µL makes 15 mL of 10 mM | Sigma-Aldrich A1952, bought 03-03. It is sold as 20 wt% (the SDS gives 10–30%), about 2.9 M if its density is near 1 g/mL; check the label. Open it in the hood. If it has turned yellow (ammonium polysulfide), it still works for the vial tests but not for quantitative plates. |
| Sodium chloride, 500 g | NaCl | 7647-14-5 | have | 4.383 g makes 15 mL of 5 M | |
| Barium chloride dihydrate | BaCl₂·2H₂O | 10326-27-9 | have, **check** | 366.4 mg makes 15 mL of 0.1 M | For the barium sulfate positive controls on every plate: 20 µL of the 0.1 M stock in a 200 µL well gives 10 mM. The 03-05 stock was 1.0 M, made from the dihydrate. Check the label: anhydrous barium chloride (BaCl₂, CAS 10361-37-2) needs 15% less mass. |
| Sodium sulfate, anhydrous, 500 g | Na₂SO₄ | 7757-82-6 | have | 213.1 mg makes 15 mL of 0.1 M | The other half of the barium sulfate controls, used the same way. Also used on 03-05. |
| Deionized (DI) water | H₂O | 7732-18-5 | have, refill | about 1 L per session | Free from the Chem Stores breakroom, kept in HDPE ([byu-vcl 15][vcl-15-di]). The jug dates from March. |
| pH 4.00, 7.00 and 10.00 calibration buffers (usually colour-coded red, yellow and blue) | | | **get** | a few tens of mL of each per calibration | For calibrating a pH meter. The safety plan keeps sulfide at pH 8 or above, so check the stocks and a few wells. Unopened they keep 1–2 years. Once opened, pH 4 and 7 keep 1–3 months and pH 10 only 1–4 weeks, because it absorbs CO₂ from the air ([details][ph-buffers]). Buy small bottles or single-use vials. I couldn't confirm that Chem Stores stocks them. |

For the full design later. None of these are needed for the vial tests or the first plate, and
quantities and grades are in the [shopping list][shop].

| chemical | formula | CAS no. | status | notes |
| --- | --- | --- | --- | --- |
| Sodium hydrosulfide hydrate | NaHS·xH₂O | 207683-19-0 | **get** | The proposal's sulfide source. Ammonium sulfide adds ammonium to every well, which buffers near pH 9.25. Make sulfide stocks fresh each day, whichever is used. |
| or sodium sulfide nonahydrate | Na₂S·9H₂O | 1313-84-4 | **get** | The alternative to sodium hydrosulfide. |
| Calcium chloride dihydrate | CaCl₂·2H₂O | 10035-04-8 | **get** | |
| Sodium acetate trihydrate | CH₃COONa·3H₂O | 6131-90-4 | **get** | |
| Sodium propionate | CH₃CH₂COONa | 137-40-6 | **get** | |
| A buffer for pH 8–9: TAPS, N-[tris(hydroxymethyl)methyl]-3-aminopropanesulfonic acid, or CHES, 2-(cyclohexylamino)ethanesulfonic acid | | 29915-38-6 (TAPS), 103-47-9 (CHES) | **get**, once chosen | Instead of the shopping list's sodium bicarbonate, which would precipitate lead carbonate. Check its metal binding first ([earlier checklist][prev-step0]). |
| Hydrochloric acid | HCl | 7647-01-0 | **get** | For adjusting pH |
| Sodium hydroxide | NaOH | 1310-73-2 | **get** | For adjusting pH |

### Names for the other formulas used here

| formula | name | what it is here |
| --- | --- | --- |
| PbS | lead(II) sulfide | the black precipitate being measured |
| BaSO₄ | barium sulfate | the white precipitate in the positive controls |
| H₂S | hydrogen sulfide | the toxic gas sulfide solutions give off, more of it the more acidic they are |
| PbCl₂ | lead(II) chloride | precipitates when there's too much lead in the brine |
| Pb²⁺ | lead(II) ion | |
| FeS | iron(II) sulfide | the precipitate in the iron experiments, after the glovebox arrives |

### Stocks and vial tests, by hand in the hood

| item | status | notes |
| --- | --- | --- |
| 0.1 mg balance (HR-100A, 102 g max) | have, **check** | The powder doser also uses an HR-100A, so check it's free. |
| Weigh boats, spatulas | have | [byu-vcl 15][vcl-15-list] |
| Hand pipettes, about 20–200 µL and 100–1000 µL, with tips | **get** | I found no record of any. The vials need 0.25–4.25 mL, and the sulfide stock needs about 51 µL from the bottle. |
| 15 and 50 mL polypropylene tubes | **check** | 15 mL tubes held the stocks on 03-05. |
| Amber bottles, 50–100 mL | have | Five ([byu-vcl 15][vcl-15-labware]). |
| Volumetric flasks, 25 or 50 mL | **get**, optional | Only graduated cylinders and beakers are on record. Making stocks up by mass also works. |
| Screw-cap glass vials, about 20 mL | **check** | Six per set of vial tests. Ten were bought 03-04. |
| Transfer pipettes, funnels, labels, tape, Kimwipes, squirt bottles | have | [byu-vcl 15][vcl-15-labware], [05-14][vcl-15-squirt] |
| White card, a colour reference card, a phone or camera | **check** | For the vial photos. Black PbS shows best on white. |
| pH meter with a double-junction electrode, or pH strips | **get** | None on record. Sulfide and lead foul the reference of a single-junction electrode ([details][ph-buffers]). Strips need no calibration buffers. |

### OT-2 plates

| item | status | notes |
| --- | --- | --- |
| OT-2 with a P300 single GEN2 on the left mount | have | On 09-29 it picked up a tip and blew air out in a well. It has no tip-length or pipette-offset calibration, and the deck calibration dates from 01-27, before the robot was moved ([calibration notes][calib], [tip test][tip-test]). |
| P20 single GEN2 | **check** | It ran the March plate and is now on the CubXL ([byu-vcl 169][vcl-169]). Without it the OT-2 can't dispense less than 20 µL, so the low concentrations need diluted stocks (step 14). |
| 300 µL tips | have | Ordered 07-31 ([byu-vcl 168][vcl-168]). The rack sits in slot 6. |
| 200 µL filter tips | **get** | The proposal and the safety plan use filter tips for lead and sulfide. They fit the P300. |
| 96-well flat-bottom plates, clear polystyrene and polypropylene | **check** | Clear plates for the camera and the colour sensor. The safety plan names polypropylene for sulfide ([shopping list][shop-plates]). |
| Clear adhesive plate seals | **get** | Each plate is sealed right after the last sulfide addition. |
| Opentrons 15 mL tube rack, or a 12-channel reservoir | **check** | The March run used the tube rack. |
| Heater-shaker | have, not needed yet | In the OT-2 since 10-13, not seated or wired. It runs at 37–95 °C, so it's for the heated runs later ([byu-vcl 81][vcl-81]). |

### Imaging and records

| item | status | notes |
| --- | --- | --- |
| Overhead camera | in progress | A few more days of focusing ([byu-vcl 34][vcl-34]). |
| Colour sensor | have | Works on the OT-2 ([byu-vcl 197][vcl-197]). |
| Plate reader | none | On hold since June ([byu-vcl 68][vcl-68]). The camera and the sensor stand in for the proposal's 600 nm reads. |
| Temperature and humidity logger for the hood | **get** | The proposal logs both for every run. The AirGradient is in the powder enclosure. |

### Waste

| item | status | notes |
| --- | --- | --- |
| Liquid waste container labelled "lead and sulfide, basic, never acidify" | **get** | Register it with Risk Management ([byu-vcl 15][vcl-15-waste], [punch list][punch]). Rinses go in here too. |
| Bagged, labelled solid waste for lead-contaminated tips, plates, wipes and gloves | **get** | |
| Container for leftover BaCl₂ stock | **get** | Or ask EHS whether it can go in with the lead waste. |

### pH buffers: how long they keep, and where to get them

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) on 2026-10-27.

| source | unopened | opened: pH 4 and 7 | opened: pH 10 |
| --- | --- | --- | --- |
| Oakton (Cole-Parmer) 500 mL bottles and One-Shot vials ([bottles][oakton-shelf], [vials][oakton-oneshot]) | 2 years | within 90 days | within 30 days |
| Yokogawa ([FAQ][yokogawa-life]) | 12 months from shipment | up to 1 month | up to 1 month |
| Hanna Instruments ([knowledge base][hanna-open]) | not given | 4–8 weeks | 1–2 weeks, for "a more basic buffer" |
| NIST's guide to pH standards, for buffers made from its salts ([SP 260-53, 1988][nbs-260-53], pp. 15 and 33) | not given | replace about once a month, sooner if mould or particles appear | the carbonate (pH 10.01) buffer "after a few weeks", sooner if it has been exposed repeatedly to air |

The expiry date on the label covers the unopened bottle. Write the opening date on each bottle.

**Why pH 10 goes first.** Alkaline buffers absorb CO₂ from the air, which forms carbonic acid and
lowers their pH ([Yokogawa][yokogawa-life]). Nakamura, Fudagawa and Kawase measured how much
([Bunseki Kagaku 1979][nakamura-1979], Table 5; the PDF is free, in Japanese with an English
abstract):

- The phthalate (pH 4.00) and phosphate (pH 6.86) standards stayed within 0.03 of their starting
  pH for three months in polyethylene bottles.
- In 500 mL polyethylene bottles in lab air, the borax (pH 9.18) and carbonate (pH 10.01)
  standards dropped 0.03–0.06 in the first month. The borax was 0.08–0.09 down after four months.
- Each of those readings came from a bottle opened for the first time, so the drop happened in
  closed bottles. Borax filled to the brim in 25 mL bottles held for three months. Of the
  carbonate bottles, only the one kept over soda lime, a CO₂ absorber, held. The authors expected
  bottles opened at each use to drop faster.

The buffers sold for meter calibration are usually the same chemistry: phthalate, phosphate, and
borate or carbonate.

**What this means here.** For the lead work, the meter mostly has to show that a stock is above
pH 8, and a drift of 0.05 doesn't change that.

- Buy small bottles (100–250 mL), or single-use vials or sachets. A calibration takes a few tens
  of mL of each buffer, so most of a 500 mL bottle of pH 10 would be thrown out at 30 days. The
  [Oakton One-Shot kit][oakton-oneshot], two 100 mL vials each of pH 4, 7 and 10, was listed at
  $22.79–28.60 on 2026-10-27.
- Pour what you need into a clean beaker or vial, use it once and throw it out. Don't pour it back
  or put the electrode in the bottle ([Hanna][hanna-open]).
- Keep the caps tight, and store the bottles at room temperature out of the sun.

**Where to get them.** I couldn't tell whether BYU Chem Stores stocks them. [Its page][chem-stores]
has no catalog, and I found nothing public that lists what it carries. In March, Sterling phoned
them to check what they had in stock ([byu-vcl 15][vcl-15-list]). Ask at 126 NICB (weekdays 8–5),
call 801-422-2678 or email chemstores@chem.byu.edu. Chem Stores special-orders items it doesn't
stock, for $20 per order. Or order them through ME Orders, as with the respirators
([byu-vcl 15][vcl-15-meorder]).

**The meter.** None is on record, and the buffers are only for calibrating one. byu-vcl
[148][vcl-148] compared meters for the CubXL, and on 10-10 Sterling wrote that Atlas pH and other
probes could be bought once new funding comes in ([digital-alloy-lab 148][dal-148-probes]). For the
sulfide stocks and the lead solutions, get a double-junction electrode. Sulfide forms silver
sulfide in the silver/silver chloride reference, and lead forms chloride salts that clog the
junction ([Sensorex][sensorex-poison]). pH strips need no buffers.

## Steps

### While the camera is being focused

None of this needs the camera.

1. **Choose the hood** and measure it against the OT-2 (above). Ask the hood's owner, and find
   the nearest eyewash, shower and spill kit.
2. **Talk to EHS** about the lead nitrate as a particularly hazardous substance, the H₂S alarm
   set point, the waste containers, and whether the OT-2 can run inside the hood.
3. **Write the SOP and the job hazard analysis**, and record the training. Cover stock
   preparation, the vial tests, the OT-2 plates, waste, spills, and what to do when the H₂S
   alarm goes off: stop, close the sash, leave and call. The safety plan also commits to no lone
   work with lead or sulfide.
4. **Order what's marked get** for the vial tests and the first plate. The H₂S detector, hand
   pipettes, filter tips, seals and waste containers come first. Don't open the sulfide until
   the detector is in.
5. **Get the OT-2 ready**, in CB154 and with water only:
   - Clear the colour-sensor rig off the deck, after the [README's][sensor-readme]
     "one controller at a time" check.
   - Calibrate in order: deck, tip length, pipette offset, then Labware Position Check, in the
     separate Opentrons OT-2 App ([calibration notes][calib]).
   - Run the plate protocol with water and weigh the plate to check the volumes. Then run it
     once with food dye, so the camera has a plate to test on later.

### Vial tests in the hood

These follow [plan 003][plan-003], the vial test that the proposal's preliminary results
describe, with two changes. The sulfide comes from the ammonium sulfide on the shelf, not
sodium sulfide nonahydrate (Na₂S·9H₂O). Vial 3 drops from 5 to 3 mM: at 5 mM its volumes add
up to 6 mL, and PHREEQC has lead(II) chloride (PbCl₂) precipitating above 3.4–4.7 mM lead in
1 molal NaCl ([output][phreeqc]).

6. **Set up the hood**: liner and tray, waste containers, the H₂S detector on, and the sash as
   low as you can work.
7. **Make the stocks** in the hood, on the day:

   | stock | recipe |
   | --- | --- |
   | 10 mM lead(II) nitrate, Pb(NO₃)₂, 15 mL | 49.7 mg, made up to 15 mL with DI water. If the balance is outside the hood, weigh by difference in a capped vial so lead dust stays in the hood. |
   | 10 mM sulfide, 15 mL | About 51 µL of the ammonium sulfide solution, (NH₄)₂S, made up to 15 mL with DI water. Fill the tube nearly full and cap it. Check that its pH is above 8. |
   | 5 M sodium chloride, NaCl, 15 mL | 4.383 g, made up to 15 mL with DI water |

   Log the lot, mass, volume and time for each.
8. **Mix the vials**, 5 mL each, in this order: water, NaCl, lead, then sulfide last. Cap each
   vial right away and start the timer.

   | vial | Pb²⁺ (mM) | sulfide (mM) | NaCl (molal) | Pb stock (mL) | sulfide stock (mL) | 5 M NaCl (mL) | water (mL) | expected |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | 1 | 0.5 | 1.0 | 1 | 0.25 | 0.50 | 1.00 | 3.25 | black within 5 min |
   | 2 | 1.0 | 1.0 | 1 | 0.50 | 0.50 | 1.00 | 3.00 | black, denser |
   | 3 | 3.0 | 3.0 | 1 | 1.50 | 1.50 | 1.00 | 1.00 | heavy black at once |
   | 4 | 0.5 | 1.0 | 0 | 0.25 | 0.50 | 0 | 4.25 | black (no-salt control) |
   | 5 | 0.5 | 0 | 1 | 0.25 | 0 | 1.00 | 3.75 | clear (no sulfide) |
   | 6 | 0 | 1.0 | 1 | 0 | 0.50 | 1.00 | 3.50 | clear (no lead) |

9. **Record** for each vial: the time to the first black, a 0–3 score at 5 min (clear, faint,
   moderate, heavy), and a photo on white with the colour card, taken through the sash or of the
   capped vials. Add photos at 15 and 60 min if there's time. Vial 1 is the result the proposal's
   preliminary results claim: black PbS within 5 minutes at 0.5 mM lead in 1 molal NaCl.
10. **Clean up** in the hood. All liquids and rinses go in the lead and sulfide container, and
    solids in the lead solids bag. Wipe the tray with damp wipes, and take the outer gloves off
    before leaving the hood.

### Once the camera is focused

11. **Mount and test the camera** where the OT-2 will run. It needs fixed lighting, the colour
    card in frame, recording for over 4 hours (the 03-05 recording stopped at about 1.5 h), and
    stills named by time point. Test it on the dye plate from step 5.
12. **Set up the colour sensor** on a few sentinel wells, on a white background for black PbS. A
    full pass over 96 wells is too slow for the 1 and 5 min reads.

### First lead plate on the OT-2

13. **Move the OT-2 into the hood**, if that's what EHS agrees to, with the power and network
    cables run in from outside the sash. Check the deck calibration again after the move.
14. **First plate, as a shakedown**: lead against sulfide at 1 molal NaCl, 200 µL per well.
    - Four levels of each, 0.01, 0.1, 1 and 3 mM, in triplicate: 48 wells.
    - Lead-only and sulfide-only blanks at each level, plus water and NaCl blanks. The 3 mM
      lead-only blanks also show whether PbCl₂ comes out.
    - Barium sulfate (BaSO₄) positive controls, for example 10 mM barium chloride and 10 mM
      sodium sulfate in the well, from 20 µL each of the 0.1 M stocks.

    With only the P300 (20 µL minimum), make lead and sulfide stocks at 0.1, 1 and 10 mM. Then
    20 µL of one of them gives 0.01, 0.1 or 1 mM, and 60 µL of the 10 mM stock gives 3 mM. The
    fullest well (3 mM of each, 1 molal NaCl) takes 60 + 60 + 40 µL, plus 40 µL of water. Make
    the dilute sulfide stocks just before the run, since dilute sulfide oxidises in air.
15. **Run it**, with the protocol fixes from the [earlier checklist][prev-protocol]:
    - Add sulfide last, and dispense it from above the liquid. A tip that touches a well with
      lead in it carries PbS back into the sulfide tube.
    - Log each well's start time. Filling well by well spreads time zero over several minutes.
    - Pause after the last sulfide addition so someone can seal the plate in the hood, and log
      the time.
    - Image at 1, 5, 15, 60 and 240 min.
16. **Score and store** the results: a precipitate score per well and time point, and the
    images with the run's metadata (stock IDs and ages, protocol commit, temperature and
    humidity), in MongoDB `digital-wetlab`.
17. **Waste**: the sealed plate goes in the lead solids, and the leftover stocks in the lead and
    sulfide container.

### The lead campaign

18. **Settle these with Sterling** before widening the design toward the proposal's ranges
    ([earlier checklist, step 0][prev-step0]):
    - **Lead tops out at a few mM in brine.** PHREEQC puts PbCl₂ saturation at 3.4–4.7 mM total
      lead in 1 molal NaCl, whichever lead salt is used, and its databases disagree at higher
      salt ([output][phreeqc]). The proposal's range goes to 100 mM.
    - **pH**: the safety plan keeps sulfide at pH 8 and above, while the design runs from 4 to
      9. At pH 6 most of the dissolved sulfide is H₂S.
    - **The sulfide source**: sodium hydrosulfide (NaHS), as in the proposal, or the ammonium
      sulfide on the shelf.
    - **Buffers**: not bicarbonate, which would precipitate lead carbonate.
    - **5 molal NaCl** leaves little room in a well for anything else.
19. **Latin hypercube plates**, with a volume check in the design generator, blanks and BaSO₄
    controls on every plate, and three replicate plates, as in the proposal.
20. **Heated runs (60–90 °C)** come later, in year 2 of the proposal: sealed vials in a heating
    block, or polypropylene plates with heat-rated seals on the heater-shaker.
21. **ICP-OES** on about 300 conditions also comes later.

The FeS work follows, once the glovebox is in.

## To buy for the vial tests and the first plate

- H₂S detector
- splash goggles
- hand pipettes (about 20–200 µL and 100–1000 µL) and tips, if the lab has none
- a pH meter with a double-junction electrode, or pH strips, and pH 4, 7 and 10 calibration
  buffers in small bottles or single-use vials ([how long they keep][ph-buffers])
- 200 µL filter tips, clear plate seals, clear flat-bottom 96-well plates
- waste containers (through Risk Management), bench liner, trays and a sign
- a temperature and humidity logger

Later: sodium hydrosulfide hydrate or sodium sulfide nonahydrate, and the salts and buffers for
the full design.

[prev]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/5b29ece/docs/ot2-sulfide-scaling-setup.md
[prev-step0]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/5b29ece/docs/ot2-sulfide-scaling-setup.md#0-decisions-for-sterling-before-buying-anything
[prev-protocol]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/5b29ece/docs/ot2-sulfide-scaling-setup.md#4-the-protocol
[phreeqc]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/5b29ece/docs/phreeqc-checks/results.txt
[baso4-stocks]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/cded249/Experiment_1__AgCl_Precipitation_V1.py#L116-L118
[plan-003]: https://github.com/vertical-cloud-lab/digital-wetlab/blob/1c0f422/experiments/003-pbs-vial-tests/README.md
[shop]: ../SHOPPING_LIST.md
[shop-plates]: ../SHOPPING_LIST.md#3a-well-plates
[shop-safety]: ../SHOPPING_LIST.md#4-safety--monitoring-equipment
[wl-1-polish]: https://github.com/vertical-cloud-lab/digital-wetlab/issues/1#issuecomment-4001238369
[vcl-15-list]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3987730523
[vcl-15-sds]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640
[vcl-15-shield]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3923531543
[vcl-15-di]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3994028259
[vcl-15-labware]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3999005476
[vcl-15-squirt]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-4454890171
[vcl-15-waste]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3787334515
[vcl-31-size]: https://github.com/vertical-cloud-lab/byu-vcl/issues/31#issuecomment-4274593884
[vcl-34]: https://github.com/vertical-cloud-lab/byu-vcl/issues/34
[vcl-68]: https://github.com/vertical-cloud-lab/byu-vcl/issues/68#issuecomment-4756219428
[vcl-81]: https://github.com/vertical-cloud-lab/byu-vcl/issues/81#issuecomment-6157219356
[vcl-168]: https://github.com/vertical-cloud-lab/byu-vcl/issues/168#issuecomment-5138098529
[vcl-169]: https://github.com/vertical-cloud-lab/byu-vcl/issues/169
[vcl-195]: https://github.com/vertical-cloud-lab/byu-vcl/issues/195
[vcl-197]: https://github.com/vertical-cloud-lab/byu-vcl/issues/197
[pd-141-decal]: https://github.com/vertical-cloud-lab/powder-doser/issues/141#issuecomment-5373539780
[pd-144]: https://github.com/vertical-cloud-lab/powder-doser/issues/144
[pd-157]: https://github.com/vertical-cloud-lab/powder-doser/issues/157
[dal-137]: https://github.com/vertical-cloud-lab/digital-alloy-lab/issues/137
[punch]: https://github.com/vertical-cloud-lab/byu-vcl/blob/00ca2f1/docs/lab-punch-list.md
[calib]: https://github.com/vertical-cloud-lab/byu-vcl/blob/d12504c/wireless-color-sensor/ot2/opentrons-calibration.md
[tip-test]: https://github.com/vertical-cloud-lab/byu-vcl/blob/d12504c/wireless-color-sensor/ot2/results-tip-pickup-2026-09-29.md
[sensor-readme]: https://github.com/vertical-cloud-lab/byu-vcl/blob/d12504c/wireless-color-sensor/ot2/README.md
[sop-template]: https://github.com/vertical-cloud-lab/byu-vcl/blob/d12504c/byu-engineering-sop-template.md
[ot2-specs]: https://docs.opentrons.com/ot-2/system-description/specs/
[osha-lab]: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1450
[ph-buffers]: #ph-buffers-how-long-they-keep-and-where-to-get-them
[oakton-shelf]: https://www.globaltestsupply.com/product/oakton-wd-05942-11-4-01
[oakton-oneshot]: https://www.testequipmentdepot.com/oakton-wd-98767-80-one-shot-buffer-solution-kit-with-nist-traceable-calibration-assorted-colors-ph-4005-7000-10012-6-x-100-ml-vials.html
[yokogawa-life]: https://yokogawa.com/ca/library/resources/faqs/what-is-the-typical-life-time-of-a-buffer-solution-and-after-the-bottle-is-open
[hanna-open]: https://knowledge.hannainst.com/en/knowledge/how-long-will-my-ph-buffer-last-once-i-open-it
[nbs-260-53]: https://doi.org/10.6028/NBS.SP.260-53e1988
[nakamura-1979]: https://doi.org/10.2116/bunsekikagaku.28.7_T39
[chem-stores]: https://chem.byu.edu/fs-dashboard/chem-stores/
[vcl-15-meorder]: https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3923351840
[vcl-148]: https://github.com/vertical-cloud-lab/byu-vcl/issues/148
[dal-148-probes]: https://github.com/vertical-cloud-lab/digital-alloy-lab/issues/148#issuecomment-6353382004
[sensorex-poison]: https://sensorex.com/prevent-ph-reference-poisoning/
