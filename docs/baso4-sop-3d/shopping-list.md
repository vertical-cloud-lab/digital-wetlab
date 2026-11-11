# Barium sulfate plate run: shopping list

Asked on [PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84) by @timothy-commins on 2026-11-11: what
to buy for the dry run and plate A, assuming new vials and consumables. The heater-shaker, the 96-well plates and the
lab's permanent tools (balance, pipettes, spatulas, the OT-2, the lid camera, the printers) are on hand.

- The items and amounts come from the SOP's [materials list](materials-and-safety.md), the
  [monitoring plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md)
  and the [10-30 lead plan's "to buy" list](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#to-buy-for-the-vial-tests-and-the-first-plate).
- The prices are the vendors' public web prices on 2026-11-11. BYU's contract prices may be lower.
- The repo's root [`SHOPPING_LIST.md`](../../SHOPPING_LIST.md) is the grant's list for the whole sulfide project
  (about 400 plates), not this run.

## 1. Order these

| Item | What it's for (SOP step) | One run uses | Order | Where, catalogue no. | Price on 11-11 |
| --- | --- | --- | --- | --- | --- |
| **20 mL clear VOA vials**, 28 × 57 mm, 24-414 caps with bonded PTFE/silicone septa, unprocessed | The ten stocks, made up by weight in the vials, then in the two printed holders on the deck (2.2-2.16, 3.5) | 10 | 1 case of 72 | Thermo Scientific [339-20C](https://www.thermofisher.com/order/catalog/product/339-20C). Fisher sells the same vial as [12-100-112](https://www.fishersci.com/shop/products/clear-voa-glass-vials-0-125in-septa/12100112), the one in byu-vcl's capper BOM | $138.00, or $120.52 online, at Thermo. Fisher's pages showed $180-260 |
| **Clear adhesive plate seals**, not the breathable kind | Plate A at the pause (3.12), and the dry-run plate | 1 per plate | 1 case of 100 | Thermo Scientific Nunc sealing tape 232701, clear polypropylene: Fisher [12-565-492](https://www.fishersci.com/shop/products/nunc-sealing-tapes/12565492), or Sigma-Aldrich [T9571](https://www.sigmaaldrich.com/product/sigma/t9571), the same tape | $171.65 (Fisher), $159.00 (Sigma) |
| **Matte black card or paper** | Cut to the adapter and laid under the plate, so the white barium sulfate shows (3.3) | 1 sheet | 1 pack | Any office or craft store | A few dollars |
| **Temperature and humidity logger** | Next to the plate for the 72 h, a reading every 5 min (4.1-4.4) | 1 | 1 | Elitech RC-4HC (USB, 16,000 readings), or any logger that records both and exports a CSV | About $25 |
| **Chemical splash goggles**, indirect vent, marked D3 | The barium solutions (2.1). Only safety glasses are on record | 1 per person on barium | 2 | e.g. Uvex Stealth S3960C. Check the D3 mark | About $16-22 each |
| **Absorbent bench liner**, plastic-backed | The hood floor and the tray for the barium work (2.3) | 1-2 sheets | 1 pack of 50, unless the Dillon lab has some to share | Fisherbrand absorbent underpads, 24 × 20 in, Fisher 14-206-62 | About $100-120 |
| **Polypropylene tray** with a lip, about 30 × 40 cm | Holds the barium work in the hood (2.3) | 1 | 1, unless the Dillon lab has one | Any lab or kitchen supplier | Rough guess: $15-30 |
| **Lidded plastic tub**, at least 18 × 13 cm inside and 7 cm deep | Carries both holders, vials capped, between the rooms (2.17, 1.4) | 1 | 1 | Any store: a 6-quart shoebox tub fits both holders | A few dollars |
| **Food colouring** | The dry run's few dye wells | A few drops | 1 small set | Any grocery store | A few dollars |

**About $350-410 for everything except the liner and the tray, and $460-560 with them.** The vials and the seals
alone come to $280-310. One case of vials covers seven runs and a case of seals covers many more, so the next plates
need little else.

### Before you order the vials

- **Order the same vial.** Thermo lists it as 28 mm across. Tim calipered the lab's current vials at 27 mm (11-11), and
  the holder is now built for 27 mm, with 28.2 mm pockets ([`cad/`](cad/README.md)). A vial of another make may be
  wider or taller, and then it won't fit.
- **Caliper a new vial before printing the holders.** Measure its outside diameter and its height without the cap, set
  `VIAL` at the top of [`vial_holder.py`](vial_holder.py) to those numbers, and rebuild. Printed holes come out a few
  tenths of a millimetre small, so a 28 mm vial would stick in a 28.2 mm pocket. Print one holder, try several vials
  in it, then print the second.
- **Use new vials for every run.** A reused vial can carry barium sulfate seeds into a fresh stock, as the March sulfate
  tube may have. The emptied barium vials go in the barium solid waste, unless Risk Management says otherwise.
- **Spare caps are 24-414,** which is what Thermo and Fisher list. The SOP said 24-400 until 11-11. The caps
  come on the vials, so this only matters if you buy caps separately.
- **A cheaper vial would mean a new holder.** 20 mL scintillation vials cost less but are 61 mm tall. The holder's
  labware definition would need rebuilding for them, and the capper and the CubXL use the VOA vials.

## 2. Free, but someone has to ask for them

| Item | One run uses | From |
| --- | --- | --- |
| **Barium waste:** a labelled liquid-waste bottle, and a bag or pail for solids (tips, wipes, gloves, the plate, the barium vials) | Leftover stocks, the plate's wells, rinses | BYU Risk Management. Ask well before the run. They collect it afterwards |
| **DI water** | About 0.5 L, fetched that day | The Chem Stores breakroom, as before. Not the March jug ([why](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cb98aa9/docs/di-water-storage.md#what-to-do)) |
| **The barium chloride SDS,** printed for the binder | 1 | The maker's website. It was missing from the binder in October |

## 3. Probably in the lab: check before ordering

| Item | One run uses | On record | If you do need to buy it (price on 11-11) |
| --- | --- | --- | --- |
| **Barium chloride dihydrate**, ACS (BaCl₂·2H₂O, CAS 10326-27-9) | 0.37 g | Used for the March plate. Nobody has checked the bottle since, and its SDS isn't in the binder | Sigma-Aldrich [217565-100G](https://www.sigmaaldrich.com/US/en/product/sigald/217565), $56.80. 100 g is about 270 runs. Check the label says dihydrate: anhydrous takes 312.3 mg, not 366.4 mg |
| **Sodium sulfate, anhydrous**, ACS | 0.21 g | 500 g ([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640)) | Sigma-Aldrich [239313-500G](https://www.sigmaaldrich.com/US/en/product/sigald/239313), about $67-96 depending on seller |
| **Sodium chloride**, ACS | 4.4 g | 500 g ([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640)) | Sigma-Aldrich [S9888-500G](https://www.sigmaaldrich.com/US/en/product/sigald/s9888), $83.30 |
| **Opentrons 300 µL tips** | One full rack, about 78 tips: 72 for the sulfate (a new tip per well) and one for each other stock. The protocol isn't written yet | Ordered on 07-31 ([byu-vcl 168](https://github.com/vertical-cloud-lab/byu-vcl/issues/168#issuecomment-5138098529)); count the full racks left | [Opentrons](https://opentrons.com/products/opentrons-300ul-tips-1000-refills): $850 for 100 racks (999-00009) or $530 for 100 refills. In July eBay had boxes of 10 racks for about $49 |
| **100-1000 µL tips** for the hand pipette | 6, one per dilution (2.12, 2.16) | Not on record, and neither is a hand pipette (the 10-23 list) | The pipette's own brand. Without a pipette, dilute by weight with disposable transfer pipettes, which are on record |
| **Nitrile gloves** | About 10 pairs: two pairs at a time for barium | Yes | A box of 100 in each wearer's size |
| **Weigh boats, two spatulas, a small funnel, labels, a marker, Kimwipes, wash bottles** | 2 weigh boats, 10 labels | Yes (byu-vcl 15: [weigh boats, spatulas](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3987730523); [the rest](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3999005476)) | |
| **PETG or PLA filament** for the two holders | About 70 g per holder at 15 % infill, about 140 g for both (my estimate from the STL) | The printers' spools | |
| **Raspberry Pi 27 W USB-C power supply** for the lid camera's Pi 5 | 1 | The SOP has it as "check" (3.1). Undervoltage can crash the Pi in a multi-day run | The official Raspberry Pi supply, about $14-16 |
| **The heater-shaker's 96 Flat Bottom Adapter** | 1 | The heater-shaker was bought used and arrived on 04-02 ([byu-vcl 81](https://github.com/vertical-cloud-lab/byu-vcl/issues/81)). A new one comes with [one adapter of the buyer's choice](https://docs.opentrons.com/heater-shaker/adapters/), and which one the lab's has isn't on record | The SOP, the deck check ([`cad/check_deck.py`](cad/check_deck.py)) and the plate's height under the camera assume this adapter. If yours is another one, ask Sterling whether to buy it (listed from $265 on [Opentrons' modules page](https://opentrons.com/products/categories/modules); its PCR and deep-well adapters show $330 today) or to change the protocol's adapter and refocus |

## 4. Not needed for this plate

- **The lead plan's other purchases:** the H₂S detector, the pH meter, buffers and strips, and the 200 µL filter tips.
  They're for the lead and sulfide plates, not barium sulfate.
- **0.2 µm syringe filters.** Filtering the stocks removes dust that can seed nucleation. The monitoring plan makes it
  optional for plate A, and needed for its option C (many replicates near the boundary) later.
- **96-well plates.** On hand. Plate A and the dry run take one NEST 96-well 200 µL flat plate each.
