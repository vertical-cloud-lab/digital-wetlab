# Barium sulfate plate run: shopping list

Asked on [PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84) by @timothy-commins on 2026-11-11: what
to buy for the dry run and plate A, assuming new vials and consumables. The heater-shaker, the 96-well plates and the
lab's permanent tools (balance, spatulas, the OT-2, the lid camera, the printers) are on hand. There is no hand pipette (Tim, 11-16), so the dilutions are weighed instead ([how](README.md#the-dilutions-by-weight-with-transfer-pipettes)).

- The items and amounts come from the SOP's [materials list](materials-and-safety.md), the
  [monitoring plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md)
  and the [10-30 lead plan's "to buy" list](https://github.com/vertical-cloud-lab/digital-wetlab/blob/127e1db/docs/lead-pbs-materials-and-steps.md#to-buy-for-the-vial-tests-and-the-first-plate).
- The prices are the vendors' public web prices on 2026-11-11. BYU's contract prices may be lower.
- The repo's root [`SHOPPING_LIST.md`](../../SHOPPING_LIST.md) is the grant's list for the whole sulfide project
  (about 400 plates), not this run.

**Updated 2026-11-16:** the stock vials are now the 5-dram (20 mL) vials Tim bought at BYU Chem Stores, $0.59 each.
Until then this list had a case of VOA vials, which are listed at 28 mm across and would stick in the holders'
28.2 mm pockets. One run fills ten vials. Tim has six, so six more makes twelve: ten and two spares.

**Updated later on 2026-11-16:** the lab has no 100-1000 µL hand pipette, and Chem Stores doesn't sell one. So the six 1.5 mL dilution transfers go in with disposable transfer pipettes and are weighed, and the 1000 µL tips are off the list ([how](README.md#the-dilutions-by-weight-with-transfer-pipettes)).

## 1. Order these

| Item | What it's for (SOP step) | One run uses | Order | Where, catalogue no. | Price on 11-11 |
| --- | --- | --- | --- | --- | --- |
| **20 mL (5-dram) glass vials with a neck, with caps**, about 27 × 55 mm | The ten stocks, made up by weight in the vials, then in the two printed holders on the deck (2.2-2.16, 3.5). New ones every run | 10: four barium chloride, four sodium sulfate, the NaCl and the water | 12, so two are spares. **Tim bought 6 on 11-16: get 6 more** | BYU Chem Stores, item 0011486, "vial, w/neck 5 dram w/cap", sold singly. Fisher's 5-dram Kimble vial with a tooled neck, [03-339-10E](https://www.govsci.com/product-detail/Fisher--Scientific/0333910E/CS/), is listed at 27 × 55 mm and 20 mL, the size the holders are built for | $0.59 each at Chem Stores (11-16): about $6 a run |
| **Clear adhesive plate seals**, not the breathable kind | Plate A at the pause (3.12), and the dry-run plate | 1 per plate | 1 case of 100 | Thermo Scientific Nunc sealing tape 232701, clear polypropylene: Fisher [12-565-492](https://www.fishersci.com/shop/products/nunc-sealing-tapes/12565492), or Sigma-Aldrich [T9571](https://www.sigmaaldrich.com/product/sigma/t9571), the same tape | $171.65 (Fisher), $159.00 (Sigma) |
| **Matte black card or paper** | Cut to the adapter and laid under the plate, so the white barium sulfate shows (3.3) | 1 sheet | 1 pack | Any office or craft store | A few dollars |
| **Temperature and humidity logger** | Next to the plate for the 72 h, a reading every 5 min (4.1-4.4) | 1 | 1 | Elitech RC-4HC (USB, 16,000 readings), or any logger that records both and exports a CSV | About $25 |
| **Chemical splash goggles**, indirect vent, marked D3 | The barium solutions (2.1). Only safety glasses are on record | 1 per person on barium | 2 | e.g. Uvex Stealth S3960C. Check the D3 mark | About $16-22 each |
| **Absorbent bench liner**, plastic-backed | The hood floor and the tray for the barium work (2.3) | 1-2 sheets | 1 pack of 50, unless the Dillon lab has some to share | Fisherbrand absorbent underpads, 24 × 20 in, Fisher 14-206-62 | About $100-120 |
| **Polypropylene tray** with a lip, about 30 × 40 cm | Holds the barium work in the hood (2.3) | 1 | 1, unless the Dillon lab has one | Any lab or kitchen supplier | Rough guess: $15-30 |
| **Lidded plastic tub**, at least 18 × 13 cm inside and 7 cm deep | Carries both holders, vials capped, between the rooms (2.17, 1.4) | 1 | 1 | Any store: a 6-quart shoebox tub fits both holders | A few dollars |
| **Food colouring** | The dry run's few dye wells | A few drops | 1 small set | Any grocery store | A few dollars |

**About $235-280 for everything except the liner and the tray, and $350-430 with them** (11-16, with the Chem Stores
vials). The seals are most of it, $159-172, and a case of them covers many plates. Each later plate needs ten new
vials, about $6.

### The vials

- **Buy the same Chem Stores vial.** The holders are built for 27 × 55 mm, Tim's caliper readings of the lab's vials
  (11-11), with 28.2 mm pockets ([`cad/`](cad/README.md)). The VOA vials on this list until 11-16 (Thermo
  [339-20C](https://www.thermofisher.com/order/catalog/product/339-20C), the same as Fisher 12-100-112, the vial in
  byu-vcl's capper BOM) are listed at 28 × 57 mm. Printed holes come out a few tenths of a millimetre small, so a
  28 mm vial would stick, and 20 mL scintillation vials (61 mm tall) would need a new labware definition.
- **Try a new vial in each printed holder** before the run (both were printing on the H2D on 11-16). It should drop
  in and lift out freely. If it's tight, set `VIAL` at the top of [`vial_holder.py`](vial_holder.py) to its calipered
  diameter and height, and rebuild.
- **Use new vials for every run.** A reused vial can carry barium sulfate seeds into a fresh stock, as the March sulfate
  tube may have. The emptied barium vials go in the barium solid waste, unless Risk Management says otherwise.
- **The dry run** needs vials only if the OT-2 fills its plate from them: one for each liquid, say one of water and one
  of dyed water. Don't use the dyed one for a stock afterwards.
- **The stocks need no septa.** The vials are uncapped on the deck (3.6), so the caps that come with them will do.

## 2. Free, but someone has to ask for them

| Item | One run uses | From |
| --- | --- | --- |
| **Barium waste:** a labelled liquid-waste bottle, and a bag or pail for solids (tips, wipes, gloves, the plate, the barium vials) | Leftover stocks, the plate's wells, rinses | BYU Risk Management, on its [pickup-request form](https://riskapps.byu.edu/apps/pickuprequest/). **Requested** on 11-16 (Tim). They collect it afterwards, through the same form |
| **DI water** | About 0.5 L, fetched that day | The Chem Stores breakroom, as before. Not the March jug ([why](https://github.com/vertical-cloud-lab/digital-wetlab/blob/cb98aa9/docs/di-water-storage.md#what-to-do)) |
| **Printed SDSs** for the barium chloride, sodium sulfate and sodium chloride, for the SDS binders in EB B125 and the OT-2's room ([what they are](README.md#the-sds-binder)). A ring binder too, if the OT-2's room has none | Once, not every run | The website of the maker on each bottle, for that product (the barium chloride is anhydrous, Tim, 11-16). None of the SDSs on record is for barium chloride. The March ones for the other two are on [byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640). No SDS binder is on record in CB 154 |

## 3. Probably in the lab: check before ordering

| Item | One run uses | On record | If you do need to buy it (price on 11-11) |
| --- | --- | --- | --- |
| **Barium chloride, anhydrous** (BaCl₂, CAS 10361-37-2) | 0.31 g | **On hand:** Tim, 11-16. No SDS for it on record yet ([section 2](#2-free-but-someone-has-to-ask-for-them)) | Nothing to buy while it's loose and free-flowing. It takes up water from the air, so if it's caked or lumpy, buy the dihydrate, ACS (BaCl₂·2H₂O, CAS 10326-27-9): Sigma-Aldrich [217565-100G](https://www.sigmaaldrich.com/US/en/product/sigald/217565), $56.80. It takes 366.4 mg a run, so 100 g is about 270 runs ([why the masses differ](README.md#the-barium-chloride-anhydrous-or-dihydrate)) |
| **Sodium sulfate, anhydrous**, ACS | 0.21 g | 500 g ([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640)) | Sigma-Aldrich [239313-500G](https://www.sigmaaldrich.com/US/en/product/sigald/239313), about $67-96 depending on seller |
| **Sodium chloride**, ACS | 4.4 g | 500 g ([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3991816640)) | Sigma-Aldrich [S9888-500G](https://www.sigmaaldrich.com/US/en/product/sigald/s9888), $83.30 |
| **Opentrons 300 µL tips** | One full rack, about 78 tips: 72 for the sulfate (a new tip per well) and one for each other stock. The protocol isn't written yet | Ordered on 07-31 ([byu-vcl 168](https://github.com/vertical-cloud-lab/byu-vcl/issues/168#issuecomment-5138098529)); count the full racks left | [Opentrons](https://opentrons.com/products/opentrons-300ul-tips-1000-refills): $850 for 100 racks (999-00009) or $530 for 100 refills. In July eBay had boxes of 10 racks for about $49 |
| **Disposable transfer pipettes**, polyethylene, graduated to 3 mL in 0.5 mL steps | About 8: one for each of the six dilution vials (3 in the hood at 2.12, 3 at the bench at 2.16), and one or two for water only (2.2). Have about 12, for spares and a practice draw. They carry about 1.5 mL each, and the balance measures it ([how](README.md#the-dilutions-by-weight-with-transfer-pipettes)) | About 100 "disposable pipettes" from Chem Stores on 03-04 ([byu-vcl 15](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3999005476)); check what's left, and that they're plastic. No hand pipette (Tim, 11-16) | Chem Stores. A few cents each: e.g. Globe Scientific 135030 (7 mL bulb, graduated to 3 mL, 155 mm), 500 to a box, is about $290-360 for a case of 5,000 ([Transcat](https://www.transcat.com/globe-scientific-transfer-pipet-7ml-graduated-large-bulb-non-sterile)) |
| **Nitrile gloves** | About 10 pairs: two pairs at a time for barium | Yes | A box of 100 in each wearer's size |
| **Weigh boats, two spatulas, a small funnel, labels or labelling tape (1/2 or 3/4 in), a permanent marker, Kimwipes, wash bottles** | 2 weigh boats, 10 labels ([what goes on them](README.md#the-vial-labels)) | Yes (byu-vcl 15: [weigh boats, spatulas](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3987730523); [the rest](https://github.com/vertical-cloud-lab/byu-vcl/issues/15#issuecomment-3999005476)) | |
| **PETG or PLA filament** for the two holders | About 70 g per holder at 15 % infill, about 140 g for both (my estimate from the STL) | The printers' spools | |
| **Raspberry Pi 27 W USB-C power supply** for the lid camera's Pi 5 | 1 | The SOP has it as "check" (3.1). Undervoltage can crash the Pi in a multi-day run | The official Raspberry Pi supply, about $14-16 |
| **The heater-shaker's 96 Flat Bottom Adapter** | 1 | The heater-shaker was bought used and arrived on 04-02 ([byu-vcl 81](https://github.com/vertical-cloud-lab/byu-vcl/issues/81)). A new one comes with [one adapter of the buyer's choice](https://docs.opentrons.com/heater-shaker/adapters/), and which one the lab's has isn't on record | The SOP, the deck check ([`cad/check_deck.py`](cad/check_deck.py)) and the plate's height under the camera assume this adapter. If yours is another one, ask Sterling whether to buy it (listed from $265 on [Opentrons' modules page](https://opentrons.com/products/categories/modules); its PCR and deep-well adapters show $330 today) or to change the protocol's adapter and refocus |

## 4. Not needed for this plate

- **The lead plan's other purchases:** the H₂S detector, the pH meter, buffers and strips, and the 200 µL filter tips.
  They're for the lead and sulfide plates, not barium sulfate.
- **0.2 µm syringe filters.** Filtering the stocks removes dust that can seed nucleation. The monitoring plan makes it
  optional for plate A, and needed for its option C (many replicates near the boundary) later.
- **96-well plates.** On hand. Plate A and the dry run take one NEST 96-well 200 µL flat plate each.
