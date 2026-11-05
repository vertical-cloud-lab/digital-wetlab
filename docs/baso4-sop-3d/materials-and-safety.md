# Barium sulfate plate run: materials for each step, and the hazards

Asked on [issue 80](https://github.com/vertical-cloud-lab/digital-wetlab/issues/80) by @timothy-commins on
2026-11-05, before running plate A. The step numbers are the 3-D SOP's
([step table](README.md#the-steps-and-where-each-one-happens),
[videos](https://htmlpreview.github.io/?https://github.com/vertical-cloud-lab/digital-wetlab/blob/91a0e7b/docs/baso4-sop-3d/out/steps/player.html)).

- **get**: no record that the lab has it.
- **check**: bought, but it may be used up, somewhere else, or not the right one.
- Everything else is on record as in the lab.

This comes from the written record: the
[10-30 lead plan's lists](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#materials)
and byu-vcl, checked on 11-05. Nothing was checked in the lab.

**Two things on the list don't exist yet:** the OT-2 protocol for plate A, and the Pi's capture job that takes the
stills. Neither is in this repo or byu-vcl.

## Materials, step by step

### EB B125 (Dillon lab): the ten stocks

| Step | Materials |
| --- | --- |
| 2.1 PPE | Lab coat; splash goggles (**get**: only safety glasses are on record); nitrile gloves, two pairs; the barium chloride SDS, printed (**get**) |
| 2.2 Balance | HR-100A (**check** where it is; if it's moved, plug it in 1 h before weighing); check weight |
| 2.3 Load the hood | Absorbent liner and tray (**get**); barium waste, a labelled bottle for liquids and a bag for solids (**get**, from Risk Management); wash bottle of fresh DI water; barium chloride dihydrate (**check** the label: anhydrous needs 312.3 mg, not 366.4 mg); rack with the four empty, labelled barium tubes; spatula; damp wipes |
| 2.4 Tare | 20 mL glass vial with its cap (**check**) |
| 2.5-2.8 Barium chloride into the vial | What's already in the hood |
| 2.9 Weigh and log | Log sheet, pen |
| 2.10-2.11 0.1 M barium chloride | DI water; the 0.1 M tube |
| 2.12 Barium dilutions | 100-1000 µL pipette and tips (**get** or borrow; none on record. Without one, dilute by weight); three tubes: 10, 1 and 0.1 mM |
| 2.13 Cap and label | Labels, marker |
| 2.14-2.15 0.1 M sodium sulfate | Sodium sulfate, anhydrous (213.1 mg); weigh boat; a second spatula; small funnel; tube |
| 2.16 Sulfate dilutions, NaCl, water | Pipette and tips; three tubes; sodium chloride (4.383 g), weigh boat, funnel, tube; a tube of DI water |
| 2.17 Pack and clean up | Second tube rack (**get**, or one rack with 10 or more places); lidded tub (**get**); damp wipes |

For the whole day: about 0.5 L of DI water, fetched that day rather than from the March jug
([why](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cb98aa9/docs/di-water-storage.md#what-to-do)), and
ten 15 mL tubes plus spares (**check**).

### Between the buildings

| Step | Materials |
| --- | --- |
| 1.4 Carry | The lidded tub, with both racks and the ten capped tubes |

### CB 154: the plate

| Step | Materials |
| --- | --- |
| 3.1 Before the day | OT-2 with the P300, calibrated; Pi 5 on its 27 W supply (**check**); rail lights with no off timer; the plate A protocol, simulated (**not written yet**); the capture job, tested (**not written yet**). Beside the OT-2: barium waste, damp wipes, a wash bottle of DI water |
| 3.2-3.5 Load the deck | Lab coat, glasses or goggles, gloves; black paper (**check**); NEST 96-well plate, 200 µL, flat, clear (**check**); a full rack of 300 µL tips (the run uses about 80); the two racks |
| 3.6 Uncap | A clean wipe for the caps |
| 3.7-3.11 Start and fill | Nothing new |
| 3.12 Seal | Clear adhesive plate seal (**get**); the log |
| 3.13 Recap | The caps on the wipe |
| 4.1-4.4 Watch | Event log; temperature and humidity logger (**get**) |
| 4.5 End | Lab coat, glasses, gloves; a balance the plate fits on (**check**: it doesn't fit under the HR-100A's breeze break); black background; phone |
| 4.6 Waste | Barium waste; damp wipes; soap and water |

The [monitoring plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md#1-camera-and-record-keeping-with-no-chemicals)
(step 7) runs a sealed plate of water with a few wells of food dye for 24-48 h first. That needs a second plate and
seal, and food dye.

## Hazards that could realistically hurt someone

| Hazard | When | What to do |
| --- | --- | --- |
| **Swallowing barium chloride.** This is the main one. It's toxic if swallowed. NIOSH cites 0.8-0.9 g as a fatal dose for an adult, and the 0.1 M tube holds about a third of that. It gets in from hand to mouth. | Any time your gloves have touched barium | No food, drink or gum in either room. Take your gloves off before you touch your face, phone, doors or keyboards. Wash your hands before you leave. |
| **Breathing barium chloride dust** (harmful if inhaled) | 2.5-2.8, weighing | Open the bottle only in the hood, with the sash at its sticker and your head outside. Spatula slowly, low down. |
| **Spills and leftover residue.** A spill that dries becomes toxic dust. Residue on the balance, deck or tub ends up on the next person's hands. | Any time, including the carry | Wipe a spill while it's wet, into the barium waste, then wipe again with water. Wipe the balance, deck and tub at the end. Carry the tub closed, with both hands. |
| **Splashes in your eyes** | Uncapping, inverting, sealing | Goggles in the hood; glasses or goggles at the OT-2. Find the eyewash in both rooms before you start. |
| **The OT-2's moving gantry** can pinch fingers | 3.7-3.13 | Keep the door closed while it runs. Reach in only at the pause, once the robot has stopped. Take your hands out before you press resume. |
| **Barium down the drain.** At 1 mM and above, a barium solution is over EPA's 100 mg/L hazardous-waste limit for barium. | Clean-up, end of run | All barium liquids and rinses go into the labelled barium waste, which Risk Management collects. |

Not hazardous here: sodium sulfate, sodium chloride, and the barium sulfate the plate makes. Gloves and glasses are
enough for them.

**If something happens:**
- **Swallowed:** call 911 and Poison Control (1-800-222-1222) right away, even if you feel fine.
- **In your eyes:** use the eyewash for 15 minutes. **On your skin:** wash with soap and water.
- **Then** tell Sterling, and report it to Risk Management.

## Sources

- Hazard classes, toxic if swallowed (H301) and harmful if inhaled (H332): the SOP's
  [hood section](README.md#does-the-ot-2-need-to-be-in-the-hood).
- Fatal dose: NIOSH's [IDLH documentation for barium](https://www.cdc.gov/niosh/idlh/7440393.html): "Patty [1963]
  cited 800 to 900 mg of BaCl2 (550 to 600 mg as Ba) as the fatal dose for man [Sollman 1953]." The same page also
  gives a higher estimate, 43-57 mg of barium per kg (Reeve 1979). The 0.1 M tube holds 312 mg of barium chloride
  (366.4 mg weighed as the dihydrate).
- Waste limit: [40 CFR 261.24](https://www.law.cornell.edu/cfr/text/40/261.24),
  barium (D005), 100.0 mg/L; a liquid waste counts as its own extract. 1 mM barium is 137 mg/L.
- Materials and their status: the 10-30 lead plan's lists, the
  [monitoring plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md)
  and the SOP's [step table](README.md#the-steps-and-where-each-one-happens).
