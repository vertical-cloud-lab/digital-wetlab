# Experiment 001: AgCl Formation (Silver Chloride Precipitation)

> **Reaction:** AgNO₃ (aq) + NaCl (aq) → AgCl (s) ↓ + NaNO₃ (aq)
>
> **Observable:** White, curdy precipitate

## Reagent Variants

This experiment can be run with two different chloride sources. **Variant A (NaCl) is recommended as the starting point** because it eliminates the need for a fume hood.

| Variant | Reaction | Fume Hood? | Notes |
|---------|----------|-----------|-------|
| **A (NaCl) — recommended first** | AgNO₃ + NaCl → AgCl ↓ + NaNO₃ | **No** | NaCl is non-volatile and non-toxic; same AgCl precipitate; benign NaNO₃ byproduct |
| B (HCl) — original plan | AgNO₃ + HCl → AgCl ↓ + HNO₃ | **Yes** | HCl produces corrosive fumes; needed for consistency with the full R2 reagent set |

Both variants produce **identical AgCl precipitate** (same color, morphology, Ksp). The only differences are the byproduct (NaNO₃ vs. HNO₃) and whether the chloride source is volatile. Running Variant A first lets you validate the full OT-2 + camera + 384-well plate workflow without waiting for fume hood access.

## Objectives

1. Validate the OT-2 liquid handling setup for a simple precipitation reaction
2. Confirm camera-based detection of white AgCl precipitate formation
3. Establish a baseline protocol for both manual and automated (OT-2) execution
4. Collect time-lapse images and RGB data at varying concentrations for Tier 1 data generation (see [opentrons-inorganic-wet-lab-agents.txt](../../opentrons-inorganic-wet-lab-agents.txt))

## Reagents

### Variant A — No Fume Hood Required (Recommended First)

| Reagent | Concentration | Quantity Needed | Notes |
|---------|--------------|-----------------|-------|
| AgNO₃ (silver nitrate) | 0.1 M | ~10 mL | Light-sensitive; store in amber/dark container |
| NaCl (sodium chloride) | 1 M | ~10 mL | Non-hazardous; can be prepared from table salt (58.44 g/mol → 5.8 g in 100 mL DI water) |

**Why this works without a fume hood:** NaCl is non-volatile and non-toxic. AgNO₃ at 0.1 M in 10 µL volumes poses minimal inhalation risk — it is a skin/eye irritant but does not produce fumes. Standard PPE (gloves, goggles, lab coat) is sufficient. The byproduct NaNO₃ is a benign, soluble salt.

### Variant B — Fume Hood Required (Original Plan)

| Reagent | Concentration | Quantity Needed | Notes |
|---------|--------------|-----------------|-------|
| AgNO₃ (silver nitrate) | 0.1 M | ~10 mL | Light-sensitive; store in amber/dark container |
| HCl (hydrochloric acid) | 1 M | ~10 mL | Fuming; **use in fume hood** |

These should be procured through **BYU Chem Stores** in the smallest available amounts (see [Procurement](#procurement) below). With 10 µL of each reagent per well (20 µL total) in a 384-well plate, even 10 mL of each reagent provides enough for hundreds of wells plus waste.

## Equipment

### Minimum Required
- **OT-2 liquid handling robot** with **P20 single-channel pipette** (1–20 µL range)
- **Opentrons 20 µL tips** (standard or filter; filter tips recommended for Variant B with HCl)
- **384-well plate** — custom-printed from Formlabs clear resin v4 (based on [GBO 781209](https://shop.gbo.com/en/usa/products/bioscience/microplates/384-well-microplates/384-well-polypropylene-microplates/781209.html) dimensions, ~120 µL well capacity; see [byu-vcl#5](https://github.com/vertical-cloud-lab/byu-vcl/issues/5) for the Fusion 360 model and print details — confirm actual printed well capacity matches)
- **Camera** (positioned above the well plate for top-down imaging; see [Camera Considerations](#camera-considerations-384-well-format) below)
- **Fume hood** — **only required for Variant B (HCl)**; Variant A (NaCl) can be run on an open benchtop with standard PPE

### Alternative Configuration
- **P300 single-channel pipette** with **96-well plate** (polypropylene, clear) — use if larger per-well volumes are needed for visibility or evaporation management (see [P20 + 384-Well Feasibility](#p20--384-well-feasibility) below)

### Optional / Recommended
- **Ocean Optics USB spectrometer** (e.g., USB2000+ UV-Vis, 200–850 nm range) for quantitative absorbance measurements and color profiling of precipitates
- **Light sensor** for consistent illumination characterization
- **Color calibration card** (recorded alongside each image for color correction)
- **Well plate covers/seals** for evaporation mitigation (see [Evaporation Management](#evaporation-management))

## Safety Considerations

### Silver Nitrate (AgNO₃) — Both Variants

| Hazard | Detail |
|--------|--------|
| GHS classifications | Oxidizer, corrosive, environmental hazard |
| Skin/eye contact | Causes burns; permanently stains skin black |
| Ingestion/inhalation | Harmful; may damage mucous membranes |
| Environmental | Very toxic to aquatic life |
| Incompatibilities | Combustible materials, ammonia (in concentrated form), acetylene |

**Handling:** Wear nitrile gloves, lab coat, and splash goggles. Work in a well-ventilated area. Use spatulas/tongs for solid handling. Store in a tightly closed, light-protected container.

> **Note for this experiment:** At 0.1 M in 10 µL volumes, AgNO₃ does not produce fumes and can be handled on an open benchtop with standard PPE.

### Sodium Chloride (NaCl) — Variant A Only

| Hazard | Detail |
|--------|--------|
| GHS classifications | Not classified as hazardous |
| Skin/eye contact | Mild irritant at high concentrations |
| Inhalation | Not a concern in solution |
| Incompatibilities | None at these concentrations |

**Handling:** No special precautions beyond standard lab PPE. NaCl is non-toxic, non-volatile, and non-flammable.

### Hydrochloric Acid (HCl) — Variant B Only

| Hazard | Detail |
|--------|--------|
| GHS classifications | Corrosive, acute toxicity (inhalation) |
| Skin/eye contact | Causes severe burns |
| Inhalation | Irritating/corrosive fumes, especially at higher concentrations |
| Incompatibilities | Bases, oxidizers, metals (evolves H₂ gas) |

**Handling:** Wear nitrile or neoprene gloves, lab coat, splash goggles, and face shield for pouring. **Always use inside a chemical fume hood.** Store in a corrosion-resistant cabinet with secondary containment.

### Reaction Products

- **AgCl precipitate** (both variants): Insoluble solid; relatively low acute toxicity but should still be collected as **heavy metal waste**.
- **NaNO₃ byproduct** (Variant A): Benign, soluble salt. Low toxicity. Can be collected with the AgCl waste stream.
- **HNO₃ byproduct** (Variant B): Dilute nitric acid; mildly acidic at these concentrations but must not be poured down the drain.

### PPE Summary

- Nitrile gloves (minimum)
- Lab coat
- Splash goggles
- Face shield (recommended when handling concentrated HCl)
- Closed-toe shoes

### Emergency Equipment

- Eyewash station and safety shower must be accessible
- Spill kit with neutralizing agent (sodium bicarbonate for acid spills)
- First aid: flush affected area with water for ≥15 minutes; seek medical attention

### Waste Disposal

| Waste Stream | Disposal |
|-------------|----------|
| AgCl precipitate | Collect in a labeled "heavy metal waste" container; do not discard in trash or drain |
| Acidic supernatant (HNO₃) | Collect in acid waste container; neutralize with sodium bicarbonate before disposal if allowed by local protocols |
| Used pipette tips | If contaminated with Ag⁺, dispose in heavy metal solid waste; otherwise standard sharps/lab waste |
| Rinse water | Collect if potentially contaminated with Ag⁺; do not pour down drain |

Follow BYU Environmental Health & Safety (EH&S) guidelines for all waste disposal.

## OT-2 Tip Chemical Compatibility

### Summary

Opentrons OT-2 pipette tips are made from **100% virgin polypropylene (PP)**, which has broad chemical resistance. The 20 µL tips used with the P20 pipette have the same PP construction as larger tips.

| Reagent | PP Compatibility | Risk Level | Notes |
|---------|-----------------|------------|-------|
| AgNO₃ (0.1 M) | ✅ Excellent | Low | May stain tips; no structural degradation |
| NaCl (1 M) | ✅ Excellent | Low | No chemical concerns whatsoever |
| HCl (1 M) | ✅ Excellent | Low | PP is resistant to HCl at all concentrations |
| HNO₃ (dilute, byproduct) | ✅ Good | Low | Brief contact at dilute concentrations is fine; avoid prolonged hot/concentrated exposure |

### Recommendations

1. **Use filter tips** for Variant B (HCl) to prevent acid vapor from reaching the pipette shaft internals. The OT-2 pipette body contains PC-ABS plastic components that could be damaged by prolonged acid vapor exposure. For Variant A (NaCl), standard tips are fine — filter tips are optional but still a good practice.

2. **Use fresh tips for each aspiration** (no tip reuse) to prevent cross-contamination and avoid AgCl buildup on tip surfaces.

3. **Pre-wet tips** before aspirating HCl — aspirate and dispense 2–3 times to saturate the air gap with vapor and reduce dripping.

4. **Trailing air gap** — after aspirating HCl, draw a small air gap (~2 µL for P20; ~10 µL for P300) to prevent dripping during transport.

### Workarounds for More Aggressive Reagents (Future Experiments)

For future experiments involving more corrosive reagents (e.g., concentrated HNO₃, H₂SO₄, organic solvents):

- **3D-printed custom tip adapters** can interface commercial PTFE or specialty tips with the OT-2 pipette nozzle, though the tips themselves should remain commercially manufactured PP or PTFE for reliable chemical resistance.
- **Polypropylene filament** is available for FDM 3D printers but is challenging to print (warping, adhesion) and does not match injection-molded PP quality. Best used for prototyping fit, not for final chemical use.
- **PTFE (Teflon) tips** are not available from Opentrons but can be sourced from specialty suppliers and used with custom adapters. PTFE offers near-universal chemical resistance.
- For the current experiment (0.1 M AgNO₃ + 1 M HCl), **standard PP tips are fully adequate** — no custom tips are needed.

## P20 + 384-Well Feasibility

Using the **P20 single-channel pipette** with a **384-well plate** is the preferred configuration, dispensing 10 µL + 10 µL = 20 µL total per well. This approach dramatically reduces reagent consumption (10× less per well vs. 100 + 100 µL in a 96-well plate) and allows many more conditions per plate (up to 384 wells).

### Advantages

| Aspect | 384-well + P20 | 96-well + P300 |
|--------|---------------|----------------|
| Volume per well | 20 µL (10 + 10) | 200 µL (100 + 100) |
| Wells per plate | 384 | 96 |
| Total reagent for full plate | ~7.7 mL | ~19.2 mL |
| Reagent per experiment (8 wells) | ~0.16 mL | ~1.6 mL |
| Chemical compatibility | Clear resin v4 (verified for dilute acids) | Polypropylene (excellent) |
| Evaporation risk | **High** (critical concern) | Moderate |

### Dispensing Accuracy

The P20 has ±3–5% accuracy at 10–20 µL, which is sufficient for qualitative analysis where the goal is precipitate detection rather than quantitative yield. At volumes below 5 µL, accuracy degrades and is not recommended for this protocol.

**Recommended dispense volumes:** 10 µL per reagent (20 µL total per well). This stays in the P20's accurate mid-range while leaving headroom in the well capacity (~120 µL for the GBO 781209 reference design; verify actual printed well capacity via the Fusion 360 model's "Internal Volume" body in [byu-vcl#5](https://github.com/vertical-cloud-lab/byu-vcl/issues/5)).

### Camera Considerations (384-Well Format)

Individual 384-well plate wells are smaller (~3.7 mm square or ~3.6 mm diameter) than 96-well plate wells (~6.9 mm diameter), which affects imaging:

- **Resolution requirement:** A camera with sufficient resolution to distinguish individual wells (≥10 pixels across each well at minimum; ≥30 pixels preferred for color analysis). A standard 12 MP camera at ~15–20 cm working distance should suffice for full-plate imaging.
- **White precipitate visibility:** AgCl is an opaque white solid, and even a small amount (from ~1 µmol Ag⁺ in 10 µL of 0.1 M) produces visible turbidity. Against the clear resin background, this should be detectable.
- **Clear resin plate advantage:** The Formlabs clear resin v4 plate allows potential bottom-up or transillumination imaging, which could improve contrast for detecting white precipitates in small wells.
- **Recommendation:** Start with top-down imaging and verify detection. If precipitate is hard to distinguish in small wells, consider transillumination (light source below, camera above) or switching to the alternative 96-well configuration.

### Evaporation Management

Evaporation is the **primary challenge** for 20 µL volumes in open wells. Aqueous solutions in 384-well plates can lose ~0.5–2 µL/hour under typical lab conditions, and significantly faster in a fume hood with active airflow. **Variant A (NaCl) has a significant advantage here**: NaCl is non-volatile, so only water evaporates (no additional reagent loss). Variant B (HCl) adds volatile HCl fumes that further accelerate apparent volume loss.

**Mitigation strategies (ranked by practicality):**

1. **Adhesive plate seals (clear film):** Apply an optically clear adhesive seal over the plate immediately after dispensing. Peel back or puncture individual wells as needed. This is the simplest and most effective approach.

2. **Press-fit transparent covers:** A custom glass or clear acrylic cover that sits over the plate or individual wells. This could be designed as a press-fit "cap mat" in Fusion 360. If using a rigid cover, ensure it does not contact the liquid surface.

3. **Mineral oil overlay:** Dispense ~5–10 µL of mineral oil on top of each aqueous well after adding reagents. The oil layer suppresses evaporation effectively, but may interfere with camera-based precipitate detection (refraction, meniscus effects). Worth testing but not ideal for imaging.

4. **Work fast / batch processing:** Minimize time between dispensing and imaging. Dispense all AgNO₃ first, then add HCl to all wells in quick succession, then image immediately. With 8 wells, the OT-2 can complete dispensing in an estimated ~2–5 minutes (verify with actual P20 timing during dry run).

5. **Reduce fume hood airflow during imaging:** Lower the sash to the minimum safe working height during the observation window to reduce convective evaporation (while maintaining safe ventilation).

6. **Humidified enclosure:** Place a damp sponge or small water reservoir on the OT-2 deck near the plate to raise local humidity. Simple but helps at the margins.

**Recommendation for this experiment:** Use strategy **#1 (adhesive plate seal)** as the primary evaporation control. After dispensing and mixing, apply a clear seal and image through it. If precipitate detection through the seal is insufficient, try **#4 (work fast)** with immediate imaging and accept that 10-minute time-lapse observations may show some volume loss.

## Protocol

### A. Manual Execution (Benchtop Reference)

1. Prepare labeled 384-well plate (**Variant A:** open benchtop is fine; **Variant B:** use fume hood)
2. Pipette 10 µL of 0.1 M AgNO₃ into each target well using a calibrated P20 micropipette
3. Add 10 µL of 1 M NaCl (Variant A) or 1 M HCl (Variant B) to each well; observe immediately
4. (Optional) Apply clear adhesive seal to prevent evaporation during observation
5. Record observations: precipitate color (white), morphology (curdy), time to visible formation
6. Photograph wells at time points: 0 s, 10 s, 30 s, 2 min, 10 min
7. Repeat at varying concentrations (0.01 M, 0.05 M, 0.1 M AgNO₃) to characterize detection limits

### B. OT-2 Automated Execution

1. Set up OT-2 (**Variant A:** open benchtop; **Variant B:** inside fume hood or connected to exhaust)
2. Load 20 µL filter tip rack, reagent reservoirs (Eppendorf tubes or small trough), and 384-well plate on the OT-2 deck
3. Position camera above well plate for time-lapse capture
4. Run OT-2 protocol:
   - Aspirate 10 µL AgNO₃ with fresh tip → dispense into target wells
   - Change tip
   - Aspirate 10 µL NaCl or HCl with fresh tip (pre-wet 2–3×) → dispense into wells containing AgNO₃
5. (Optional) Apply clear seal or cover after dispensing
6. Trigger camera capture at defined intervals (0 s, 10 s, 30 s, 2 min, 10 min)
7. (Optional) Position Ocean Optics fiber probe for absorbance readings

### C. Concentration Series

All wells receive 10 µL of each reagent (20 µL total per well) using the P20 pipette. The chloride source is NaCl (Variant A) or HCl (Variant B) — the AgCl precipitate is identical.

| Well | AgNO₃ (M) | NaCl/HCl (M) | Total Vol (µL) | Expected Result |
|------|-----------|--------------|-----------------|-----------------|
| A1 | 0.01 | 1.0 | 20 | Faint white precipitate |
| A2 | 0.05 | 1.0 | 20 | Moderate white precipitate |
| A3 | 0.1 | 1.0 | 20 | Strong white precipitate |
| B1 | 0.1 | 0.1 | 20 | White precipitate (1:1 stoichiometry) |
| B2 | 0.1 | 0.5 | 20 | White precipitate |
| B3 | 0.1 | 1.0 | 20 | White precipitate (excess Cl⁻) |
| C1 | 0.0 (blank) | 1.0 | 20 | No change (negative control) |
| C2 | 0.1 | 0.0 (DI water) | 20 | No change (negative control) |

> **Note:** With 384 wells available, this series can be run in triplicate (24 wells) with ample room for additional conditions or future experiments on the same plate.

### D. Data Collection

For each well, record:
- **Time-lapse images** at defined intervals
- **RGB values** extracted from a standardized region of interest (ROI) in each well
- **Visual observation score**: 0 = no visible change, 1 = faint, 2 = moderate, 3 = strong precipitate
- **Time to first visible precipitate** (seconds)
- **Settling behavior** over 10 min observation window
- **(Optional) Absorbance spectrum** from Ocean Optics spectrometer

## Procurement

### BYU Chem Stores

- **Location:** 126 Nicholes Building (NICB), Provo, UT 84602
- **Hours:** 8:00 AM – 5:00 PM, Monday–Friday
- **Phone:** 801-422-2678
- **Email:** chemstores@chem.byu.edu

**Management contacts:**
- Matthew Allen, Manager — 801-422-3487, amatthew@chem.byu.edu
- Duane Tucker, Receiving Manager — 801-422-3804, duane.tucker@chem.byu.edu

**Order:**
- AgNO₃ — smallest available quantity (e.g., 5–25 g solid to prepare 0.1 M solution, or request pre-made 0.1 M)
- NaCl (Variant A) — can be prepared from lab-grade NaCl or even table salt (5.8 g in 100 mL DI water for 1 M); check Chem Stores for pre-made solutions
- HCl (Variant B) — smallest available quantity (e.g., 100 mL of 1 M, or dilute from concentrated stock in Chem Stores)

### Centralized Chemical Inventory

- **Location:** BNSN C184A
- **Email:** chemstores@chem.byu.edu
- **Phone:** 801-422-1862
- **Hours:** 12:00 PM – 2:00 PM, Monday–Friday

Check the centralized inventory first — the needed reagents may already be available on campus.

## BYU Faculty & Department Contacts

Engaging with the chemistry department is recommended for safety guidance, potential lab space, and curriculum alignment.

### Suggested Contacts

| Contact | Role | Relevance | Contact Info |
|---------|------|-----------|-------------|
| **Dr. Roger G. Harrison** | Professor of Inorganic Chemistry | Teaches gen chem & inorganic chemistry labs; research in supramolecular/inorganic synthesis | rgharrison@chem.byu.edu, 801-422-8096 |
| **BYU Chem Stores** | Chemistry stockroom | Reagent procurement, inventory check | chemstores@chem.byu.edu, 801-422-2678 |
| **BYU EH&S** | Environmental Health & Safety | Waste disposal protocols, fume hood certification, lab safety review | safety.byu.edu |

### Recommended Outreach Steps

1. **Start with Chem Stores** — inquire about availability and pricing for small quantities of AgNO₃ and HCl; ask about existing pre-made solutions
2. **Contact Dr. Roger G. Harrison** (or other gen chem faculty) — introduce the project, ask about:
   - Qualitative analysis procedures used in their gen chem labs
   - Potential for shared lab space or fume hood access
   - Safety protocols they follow for similar reactions
   - Interest in collaboration on AI-driven chemistry benchmarks
3. **Consult BYU EH&S** — confirm waste disposal procedures for silver-containing and acidic waste; get fume hood certification for the OT-2 setup location
4. **Explore the faculty directory** at [chem.byu.edu/department/faculty/](https://chem.byu.edu/department/faculty/) for additional gen chem instructors and analytical chemistry faculty

## Spectrometer Considerations

An **Ocean Optics USB spectrometer** (e.g., USB2000+ UV-Vis) would provide significant advantages over camera-only observation:

| Feature | Camera Only | Camera + Spectrometer |
|---------|------------|----------------------|
| Precipitate detection | Qualitative (visual/RGB) | Quantitative (absorbance at specific λ) |
| Concentration measurement | Approximate (color intensity) | Precise (Beer-Lambert law) |
| Color calibration | Requires calibration card + controlled lighting | Self-calibrated via reference spectrum |
| Spectral resolution | Limited to RGB channels | ~1.5 nm across 200–850 nm |
| Cost | Low (existing camera) | Moderate (~$1,000–$4,000 depending on model) |

**Recommendation:** For the initial AgCl experiment, camera-based detection is sufficient (white precipitate on clear background is high-contrast). Acquiring a spectrometer is strongly recommended before scaling to experiments with subtler color differences (e.g., distinguishing AgBr pale yellow from AgI yellow, or quantifying concentration-dependent observations for Tier 1 data generation).

## Next Steps

- [ ] Procure or prepare NaCl solution (1 M) for Variant A (no fume hood needed)
- [ ] Contact BYU Chem Stores to procure AgNO₃ (0.1 M) in small quantities
- [ ] Verify 384-well plate fit in OT-2 deck slot (see [byu-vcl#5](https://github.com/vertical-cloud-lab/byu-vcl/issues/5))
- [ ] Test P20 dispensing accuracy at 10 µL with DI water on the 384-well plate
- [ ] Set up camera positioning and test image capture on blank 384-well plate
- [ ] Evaluate evaporation mitigation (adhesive seals, press-fit covers, etc.)
- [ ] Write and test OT-2 protocol script (Python, Opentrons API) for P20 + 384-well plate
- [ ] **Run Variant A (NaCl) on open benchtop** — manual first, then OT-2 automated
- [ ] Confirm fume hood access for Variant B (HCl) when ready to scale
- [ ] Procure HCl (1 M) for Variant B
- [ ] Reach out to Dr. Roger G. Harrison or other gen chem faculty
- [ ] Consult BYU EH&S on waste disposal procedures for silver-containing waste
- [ ] Evaluate whether Ocean Optics spectrometer purchase is justified based on initial results
