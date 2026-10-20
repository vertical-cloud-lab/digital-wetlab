# Shopping List — Sulfide-Mineral Pitzer Parameter Study

> **Project:** Development of a Pitzer Ion-Interaction Framework for Predicting Sulfide-Mineral Precipitation in Produced-Water Brines
>
> **Grant:** ACS PRF DNI · $110,000 / 2 years · Supplies budget: **$8,047** ($5,047 Year 1, $3,000 Year 2)
>
> **Personnel:** 1 M.Sc. graduate student + 2 part-time undergraduates
>
> **Scale:** ~30,000 total experiments (~5,000 unique conditions × triplicates × 2 metal systems), plus protocol development and validation

---

## Experiment Scale Summary

| Parameter                                | Value                                                 |
| ---------------------------------------- | ----------------------------------------------------- |
| Total experiments (wells)                | ~30,000                                               |
| 96-well plates (experiments only)        | ~350                                                  |
| Protocol development & validation plates | ~50                                                   |
| **Total plates**                         | **~400**                                              |
| Manual validation vials (5 mL)           | ~200 used; procure 500 total (incl. high-T + repeats) |
| Tips per plate (estimated)               | ~400–600                                              |

---

## 1. Equipment

All major equipment is already available and not purchased from this grant:

> - Opentrons OT-2 robot
> - GEN2 single-channel P300 pipette (left mount)
> - GEN2 8-channel P300 pipette (20–300 µL)
> - N₂ inert-atmosphere glovebox (general-purpose, not ultradry)
> - Chemical fume hood
> - Microplate reader access (BYU shared: BioTek Synergy H1 or Molecular Devices SpectraMax iD3)
> - ICP-OES access (BYU shared instrumentation)

---

## 2. Chemical Reagents

### 2a. Metal Salts

| Reagent                        | Formula    | Purity   | Qty   | Est. Cost | Notes                                                                                                                                          |
| ------------------------------ | ---------- | -------- | ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Iron(II) sulfate heptahydrate  | FeSO₄·7H₂O | ≥99% ACS | 500 g | $30–50    | Primary Fe²⁺ source. Prepare 0.1–0.5 M stock in deoxygenated water.                                                                            |
| Iron(II) chloride tetrahydrate | FeCl₂·4H₂O | ≥99%     | 250 g | $30–50    | Alternative Fe²⁺ source (avoids adding SO₄²⁻ to FeS experiments).                                                                              |
| Lead(II) chloride              | PbCl₂      | ≥99%     | 250 g | $40–60    | Primary Pb²⁺ source. **Caution:** low aqueous solubility (~36 mM at 20°C). Use Pb(NO₃)₂ instead for any well concentrations above ~35 mM Pb²⁺. |
| Lead(II) nitrate               | Pb(NO₃)₂   | ≥99% ACS | 250 g | $30–50    | Alternative Pb²⁺ source with much higher solubility (~1.5 M). Introduces NO₃⁻ but avoids PbCl₂ solubility limit.                               |

### 2b. Sulfide Sources

| Reagent                     | Formula   | Purity | Qty   | Est. Cost | Notes                                                                                                                                                                                                                 |
| --------------------------- | --------- | ------ | ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sodium hydrosulfide hydrate | NaHS·xH₂O | ≥70%   | 500 g | $50–80    | Primary sulfide source (directly provides HS⁻, matching proposal stock solutions). Prepare 0.1–0.5 M stock in deoxygenated water under N₂. **Hazard:** releases H₂S on acidification—prepare and handle in fume hood. |
| Sodium sulfide nonahydrate  | Na₂S·9H₂O | ≥98%   | 1 kg  | $40–60    | Alternative sulfide source (provides S²⁻, which rapidly equilibrates to HS⁻ at working pH). More stable solid; store under N₂.                                                                                        |

### 2c. Brine Matrix Salts

| Reagent                    | Formula    | Purity   | Qty  | Est. Cost | Notes                                                                                                                                                              |
| -------------------------- | ---------- | -------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sodium chloride            | NaCl       | ≥99% ACS | 5 kg | $30–50    | For 5 M stock solution. Estimated ~3 L of 5 M NaCl needed across all experiments (requires ~876 g NaCl). Extra for stock preparation losses and manual validation. |
| Calcium chloride dihydrate | CaCl₂·2H₂O | ≥99% ACS | 2 kg | $30–50    | For 2 M stock solution. Used in subset of experiments with CaCl₂-bearing brines (up to 0.5 molal).                                                                 |

### 2d. Petroleum-Derived Organic Acids

> These reagents represent the short-chain and cyclic organic acids found in crude-oil produced waters, released during thermal maturation of kerogen. Their Pitzer interactions with Fe²⁺ and Pb²⁺ (~14 organic acid–metal parameters) are a primary target of Aim 2.

| Reagent                     | Formula       | Purity     | Qty    | Est. Cost | Notes                                                                                                                                                                                              |
| --------------------------- | ------------- | ---------- | ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sodium acetate trihydrate   | CH₃COONa·3H₂O | ≥99% ACS   | 500 g  | $25–40    | Primary acetate source (introduced as sodium salt to decouple from pH). Acetic acid is the dominant organic acid in produced waters (100–10,000 mg/L). Also serves as acetate buffer at pH 4–5.5.  |
| Glacial acetic acid         | CH₃COOH       | ≥99.7% ACS | 500 mL | $20–30    | Conjugate acid for acetate buffer preparation.                                                                                                                                                     |
| Sodium propionate           | C₃H₅NaO₂      | ≥99%       | 500 g  | $30–50    | Core propionate source (0–5,000 mg/L in screening matrix). Propionic acid is the second most abundant organic acid in produced waters (10–1,000 mg/L).                                             |
| Cyclohexane carboxylic acid | C₇H₁₂O₂       | ≥98%       | 100 g  | $40–80    | Model cyclic naphthenic acid for exploratory subset (~100 experiments). Naphthenic acids are characteristic petroleum-derived compounds that cause corrosion and may modify sulfide precipitation. |

### 2e. pH Buffers & Adjustment Reagents

| Reagent            | Formula        | Purity            | Qty    | Est. Cost | Notes                                                            |
| ------------------ | -------------- | ----------------- | ------ | --------- | ---------------------------------------------------------------- |
| MES hydrate        | C₆H₁₃NO₄S·xH₂O | ≥99%              | 100 g  | $40–70    | Buffer for pH 5.5–6.5 range. Non-coordinating Good's buffer.     |
| HEPES              | C₈H₁₈N₂O₄S     | ≥99.5%            | 100 g  | $30–50    | Buffer for pH 6.8–8.2 range. Non-coordinating Good's buffer.     |
| Sodium bicarbonate | NaHCO₃         | ≥99.7% ACS        | 500 g  | $20–30    | Bicarbonate buffer for pH 8–9 range.                             |
| Sodium carbonate   | Na₂CO₃         | ≥99.5% ACS        | 500 g  | $20–30    | Bicarbonate/carbonate buffer conjugate base (pH > 9 adjustment). |
| Hydrochloric acid  | HCl            | ~12 M (37%), ACS  | 500 mL | $20–30    | pH adjustment of stock solutions.                                |
| Sodium hydroxide   | NaOH           | ≥97% pellets, ACS | 500 g  | $20–30    | pH adjustment of stock solutions.                                |

### 2f. Positive Control & ICP-OES Reagents

| Reagent                         | Formula    | Purity            | Qty    | Est. Cost | Notes                                                                                                                                                       |
| ------------------------------- | ---------- | ----------------- | ------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Barium chloride dihydrate       | BaCl₂·2H₂O | ≥99% ACS          | 100 g  | $25–40    | BaSO₄ positive controls. Well-characterized Pitzer thermodynamics serve as internal validation. Cl⁻ counterion integrates naturally into NaCl brine matrix. |
| Sodium sulfate                  | Na₂SO₄     | ≥99% ACS          | 100 g  | $20–30    | Trigger reagent for BaSO₄ positive controls.                                                                                                                |
| ICP-OES Fe standard (1000 mg/L) | —          | Certified         | 100 mL | $30–50    | For calibration of dissolved-Fe measurements in validation subset.                                                                                          |
| ICP-OES Pb standard (1000 mg/L) | —          | Certified         | 100 mL | $30–50    | For calibration of dissolved-Pb measurements in validation subset.                                                                                          |
| ICP-OES multi-element standard  | —          | Certified         | 100 mL | $40–60    | Quality-control check standard for Fe, Pb, Ba, Na, Ca.                                                                                                      |
| Nitric acid (trace-metal grade) | HNO₃       | ~70%, trace-metal | 500 mL | $40–60    | For acidifying ICP-OES samples to prevent metal adsorption to vial walls.                                                                                   |

### 2g. Fe²⁺ Quality-Control Assay Reagents (1,10-Phenanthroline)

| Reagent                              | Formula             | Purity   | Qty   | Est. Cost | Notes                                                                         |
| ------------------------------------ | ------------------- | -------- | ----- | --------- | ----------------------------------------------------------------------------- |
| 1,10-Phenanthroline monohydrate      | C₁₂H₈N₂·H₂O         | ≥99%     | 25 g  | $30–70    | Colorimetric complexing reagent for Fe²⁺ QC assay at 510 nm.                  |
| Hydroxylamine hydrochloride          | NH₂OH·HCl           | ≥99%     | 100 g | $20–40    | Reducing reagent for total dissolved Fe checks during assay calibration/QC.   |
| Ferrous ammonium sulfate hexahydrate | Fe(NH₄)₂(SO₄)₂·6H₂O | ≥99% ACS | 100 g | $20–40    | Optional in-house Fe²⁺ calibration standards for assay response verification. |

### 2h. Solvents & Gases

| Item                         | Qty        | Est. Cost | Notes                                                                                         |
| ---------------------------- | ---------- | --------- | --------------------------------------------------------------------------------------------- |
| Ultrapure water (18.2 MΩ·cm) | ~20 L      | —         | From lab Milli-Q system (assumed available). Must be deoxygenated for Fe²⁺ experiments.       |
| N₂ gas (high purity)         | 1 cylinder | $50–100   | For deoxygenating water and maintaining inert atmosphere. May be supplied by glovebox system. |

### Reagent Cost Subtotal: ~$850–1,450

---

## 3. Labware & Consumables

### 3a. Well Plates

| Item                                                                  | Qty | Est. Unit Cost | Est. Total | Notes                                                                                                                     |
| --------------------------------------------------------------------- | --- | -------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| 96-well microplates, polypropylene, flat-bottom, chemically resistant | 200 | $3–5 each      | $600–1,000 | Primary plates for sulfide experiments. Chemical resistance required for HS⁻/H₂S. Examples: Corning 3879, Greiner 655261. |
| 96-well microplates, polystyrene, flat-bottom, optically clear        | 200 | $2–4 each      | $400–800   | For plate-reader absorbance/turbidity measurements. Examples: Corning 3596, Greiner 655101.                               |

> **Quantity note:** ~350 plates for experiments + ~40–50 for development, validation, and replacements (≈10–15% margin) = ~390–400 total. Split between PP (sulfide-compatible) and PS (reader-compatible) depending on detection method used per batch.

### 3b. Pipette Tips

| Item                                        | Qty           | Est. Unit Cost | Est. Total   | Notes                                                                                                                                                                              |
| ------------------------------------------- | ------------- | -------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opentrons 200 µL filter tips (96 tips/rack) | 300–400 racks | $7–8/rack      | $2,100–3,200 | Filter tips prevent cross-contamination and protect pipette from corrosive sulfide solutions. Budget target: ~$2,500. Aggressive tip-optimization required (see strategies below). |

> **Tip quantity estimate:**
>
> Per plate (~6 liquid additions per well with fresh tips):
> - Matrix additions (water, NaCl, CaCl₂, buffer) via 8-channel: ~4 racks
> - Metal stock via single-channel: ~1 rack
> - Sulfide trigger via single-channel: ~1 rack
> - **Total: ~6 racks per plate (unoptimized)**
>
> For ~400 plates unoptimized: ~2,400 racks — **far exceeds the $2,500 tip budget.**
>
> **Required cost-reduction strategies:**
> - Reuse tips for same-reagent dispensing within a plate (e.g., one tip pickup for water to all wells)
> - Use multi-dispense mode for water and NaCl additions (aspirate once, dispense to multiple wells)
> - Use non-filter tips for non-hazardous additions (water, NaCl) at ~$5/rack
> - Reserve filter tips only for sulfide and metal stock dispensing
> - **With aggressive optimization: ~0.75–1 rack/plate → 300–400 racks → $2,100–3,200**

### 3c. Reservoirs

| Item                                        | Qty | Est. Unit Cost | Est. Total | Notes                                                                                     |
| ------------------------------------------- | --- | -------------- | ---------- | ----------------------------------------------------------------------------------------- |
| NEST 12-column reservoir, 15 mL per channel | 50  | $3–5 each      | $150–250   | Reagent source for OT-2. Reusable within same reagent batch; replace between experiments. |

### 3d. Plate Seals

| Item                                             | Qty | Est. Unit Cost  | Est. Total | Notes                                                                                                                        |
| ------------------------------------------------ | --- | --------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Adhesive plate seals (clear, chemical-resistant) | 500 | $0.50–1.00 each | $250–500   | Applied immediately after dispensing to minimize H₂S off-gassing and evaporation. One per plate per time point if re-sealed. |

### 3e. Glass Vials (High-Temperature Experiments)

| Item                                                            | Qty | Est. Unit Cost  | Est. Total | Notes                                                                                                                           |
| --------------------------------------------------------------- | --- | --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Borosilicate glass vials, 5 mL, screw-cap with PTFE-lined septa | 500 | $0.50–1.50 each | $250–750   | For 60–90°C experiments (sealed to prevent H₂S loss). Also used for 24–72 h equilibration subset and manual validation repeats. |

### 3f. General Lab Consumables

| Item                                            | Qty          | Est. Cost | Notes                                                               |
| ----------------------------------------------- | ------------ | --------- | ------------------------------------------------------------------- |
| Disposable weigh boats                          | 1 pack (500) | $15–25    | For gravimetric stock solution preparation.                         |
| Volumetric flasks (100 mL, 250 mL, 500 mL, 1 L) | 2 each       | $80–120   | For preparing calibrated stock solutions. May already be available. |
| Graduated cylinders (100 mL, 500 mL)            | 1 each       | $30–50    | For rough volume measurements. May already be available.            |
| pH meter calibration buffers (pH 4, 7, 10)      | 1 set        | $30–50    | For verifying buffer pH values.                                     |
| Parafilm                                        | 2 rolls      | $20–30    | For sealing stock solution bottles.                                 |
| Nitrile gloves (Pb²⁺ handling)                  | 2 boxes      | $20–30    | Standard PPE for lead-containing solutions.                         |
| ICP-OES sample vials (15 mL, acid-washed)       | 500          | $100–200  | For dissolved-metal validation subset (~200–300 samples).           |
| Centrifuge tubes (15 mL and 50 mL)              | 2 packs      | $30–50    | For stock solution storage and waste collection.                    |

### Labware & Consumables Subtotal: ~$4,200–7,000 (with tip optimization)

---

## 4. Safety & Monitoring Equipment

| Item                                    | Qty | Est. Cost | Notes                                                                                                                  |
| --------------------------------------- | --- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| H₂S gas detector (personal, single-gas) | 1   | $150–300  | Continuous monitoring during sulfide experiments. TWA limit: 1 ppm; STEL: 5 ppm. Examples: BW Clip, Honeywell BW Solo. |
| Temperature/humidity data logger        | 1   | $50–100   | Continuous environmental monitoring inside fume hood/glovebox.                                                         |
| Camera mount                            | 1   | $20–50    | For plate imaging (detection Tier 2).                                                                                  |
| LED lightbox or backlight panel         | 1   | $30–50    | Consistent illumination for plate imaging.                                                                             |

### Safety Equipment Subtotal: ~$250–500

---

## 5. Budget Summary

The grant allocates **$8,047** for supplies and materials, broken down in the budget justification as:

| Budget Line (from budget.tex)         | Amount     |
| ------------------------------------- | ---------- |
| Consumable chemicals and reagents     | $2,500     |
| 96-well microplates                   | $2,000     |
| Filter-tipped pipette tips            | $2,500     |
| Plate seals, gloves, misc consumables | $1,047     |
| **Total**                             | **$8,047** |

### Detailed Estimate vs. Budget

| Category                                                       | Low Estimate | High Estimate | Budget Target     |
| -------------------------------------------------------------- | ------------ | ------------- | ----------------- |
| Chemical reagents (incl. ICP-OES standards + Fe²⁺ QC reagents) | $850         | $1,450        | $2,500            |
| Well plates                                                    | $1,000       | $1,800        | $2,000            |
| Pipette tips (aggressively optimized)                          | $2,100       | $3,200        | $2,500            |
| Reservoirs                                                     | $150         | $250          | —                 |
| Plate seals                                                    | $250         | $500          | $1,047 (combined) |
| Glass vials                                                    | $250         | $750          | —                 |
| General lab consumables                                        | $325         | $555          | —                 |
| Safety & monitoring                                            | $250         | $500          | —                 |
| **Total**                                                      | **$5,025**   | **$8,755**    | **$8,047**        |

> **Budget note:** The $8,047 supplies budget is tight but achievable with aggressive tip-optimization protocols (tip reuse for same-reagent dispensing, non-filter tips for water/NaCl, multi-dispense mode). Year 1 ($5,047) covers the initial chemical inventory and first-batch consumables. Year 2 ($3,000) covers ongoing consumables for high-throughput data collection. Safety equipment (H₂S detector, data logger) and imaging hardware may need to come from PI startup funds or shared lab resources.

---

## 6. Suggested Vendor Sources

| Vendor                                                          | Best For                                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------- |
| [Opentrons](https://shop.opentrons.com/)                        | OT-2 tips, tip racks, reservoirs                            |
| [Sigma-Aldrich / MilliporeSigma](https://www.sigmaaldrich.com/) | ACS-grade reagents, buffers, metal salts                    |
| [Fisher Scientific](https://www.fishersci.com/)                 | General lab consumables, plates, vials, PPE                 |
| [VWR](https://www.vwr.com/)                                     | Well plates, plate seals, volumetric glassware              |
| [Corning](https://ecatalog.corning.com/)                        | 96-well microplates (PP and PS)                             |
| [Greiner Bio-One](https://shop.gbo.com/)                        | 96-well microplates, plate seals                            |
| [BYU Chem Stores](https://chemstores.byu.edu/)                  | Common chemicals (NaCl, HCl, NaOH) at institutional pricing |

---

## 7. Year-by-Year Procurement Plan

### Year 1 (Months 1–12) — Budget: $5,047

**Months 1–3: Setup & protocol development**
- [ ] Initial chemical inventory — all metal salts, sulfide sources, brine salts, buffers, ICP-OES standards ($1,500–2,000)
- [ ] Protocol development plates and tips (~50 plates, ~50 tip racks) ($500–700)
- [ ] Reservoirs, plate seals, general consumables ($400–600)
- [ ] Safety equipment — H₂S detector, data logger (from PI startup or shared resources)

**Months 3–10: FeS + PbS campaigns at 25°C**
- [ ] Experiment plates (~200 plates) ($500–900)
- [ ] Experiment tips (~100 racks, optimized) ($700–800)
- [ ] Plate seals, replacement reservoirs ($200–300)

**Months 8–12: Active-learning-guided follow-up begins**
- [ ] Additional plates and tips (from Year 1 stock)

### Year 2 (Months 13–24) — Budget: $3,000

**Months 13–18: Temperature-dependent experiments + BO follow-up**
- [ ] Glass vials for 60–90°C experiments ($250–500)
- [ ] Additional plates (~150 plates) ($375–675)
- [ ] Additional tips (~100 racks, optimized) ($700–800)
- [ ] Replacement reagent stocks (sulfide sources degrade) ($200–400)
- [ ] ICP-OES sample vials ($100–200)

**Months 18–24: Wrap-up validation**
- [ ] Final reagents and consumables as needed

---

## 8. Key Experimental Notes

1. **Fe²⁺ oxidation control:** All FeSO₄/FeCl₂ stock solutions must be prepared in deoxygenated water under N₂. The OT-2 must be placed inside the N₂ glovebox during Fe²⁺ campaigns because standard 96-well plates are not gas-tight. For Fe²⁺/sulfide (FeS) experiments, the glovebox must be used in a configuration that is exhausted to a fume hood (e.g., a vented glovebox or a glovebox located in/ducted to a hood) to satisfy H₂S safety requirements (see Note 4). Use a quantitative QC gate with 1,10-phenanthroline absorbance checks (510 nm) on ~10% of preparations, with rejection/re-preparation if Fe³⁺ contamination exceeds 2%.

2. **PbCl₂ solubility limit:** PbCl₂ is only ~36 mM soluble at 20°C. For any well concentrations above ~35 mM Pb²⁺, use Pb(NO₃)₂ as the source (solubility ~1.5 M). This introduces NO₃⁻ instead of additional Cl⁻, which should be accounted for in PHREEQC speciation calculations.

3. **Sulfide solution stability:** Na₂S and NaHS solutions oxidize in air and degrade over days. Prepare fresh daily or store under N₂ in sealed containers. Verify concentration by iodometric titration or UV absorbance (λ = 230 nm for HS⁻).

4. **H₂S safety:** At pH < 7, dissolved sulfide exists primarily as H₂S(aq), which partitions into the headspace. All sulfide experiments must be conducted in a fume hood or in a nitrogen glovebox that is hard-ducted or otherwise exhausted to a fume hood; this includes FeS experiments run on the OT-2 (see Note 1). The H₂S detector should be worn by the researcher and also placed near the workspace. PEL (OSHA): 10 ppm ceiling; recommended TWA: 1 ppm.

5. **Tip budget is critical:** With the $2,500 tip budget, aggressive optimization is required. The protocol must reuse tips for same-reagent dispensing (e.g., one tip for all water additions), use multi-dispense mode, and reserve filter tips only for sulfide and metal stock dispensing. Non-filter tips ($5/rack) can be used for non-hazardous additions (water, NaCl) to stretch the budget further.

6. **Plate seals for H₂S containment:** Apply adhesive seals immediately after sulfide addition to each plate. This minimizes H₂S off-gassing and protects time-course measurements from evaporation artifacts.

7. **Temperature experiments in vials:** The 60–90°C subset cannot use standard well plates. Sealed borosilicate glass vials with PTFE-lined septa are used instead. These are prepared manually (not via OT-2) and equilibrated in a heating block or oven.

8. **Positive controls every plate:** Include BaSO₄ precipitation controls (BaCl₂ + Na₂SO₄) on every plate to validate detection methodology at each ionic strength condition.
