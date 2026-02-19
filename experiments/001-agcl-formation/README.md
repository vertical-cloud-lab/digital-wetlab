# Experiment 001: AgCl Formation (Silver Chloride Precipitation)

> **Reaction:** AgNO₃ (aq) + HCl (aq) → AgCl (s) ↓ + HNO₃ (aq)
>
> **Observable:** White, curdy precipitate

## Objectives

1. Validate the OT-2 liquid handling setup for a simple precipitation reaction
2. Confirm camera-based detection of white AgCl precipitate formation
3. Establish a baseline protocol for both manual and automated (OT-2) execution
4. Collect time-lapse images and RGB data at varying concentrations for Tier 1 data generation (see [opentrons-inorganic-wet-lab-agents.txt](../../opentrons-inorganic-wet-lab-agents.txt))

## Reagents

| Reagent | Concentration | Quantity Needed | Notes |
|---------|--------------|-----------------|-------|
| AgNO₃ (silver nitrate) | 0.1 M | ~50 mL | Light-sensitive; store in amber/dark container |
| HCl (hydrochloric acid) | 1 M | ~50 mL | Fuming; use in fume hood |

These should be procured through **BYU Chem Stores** in the smallest available amounts (see [Procurement](#procurement) below).

## Equipment

### Minimum Required
- **OT-2 liquid handling robot** with single-channel pipette (P300 or P1000)
- **Standard polypropylene tips** (Opentrons OT-2 compatible, 200 µL or 1000 µL)
- **Filter tips** (recommended — prevents vapor intrusion into pipette shaft)
- **96-well plate or similar vessel** (polypropylene, clear/transparent for imaging)
- **Camera** (positioned above the well plate for top-down imaging)
- **Fume hood** (OT-2 should be placed inside, or at minimum connected to exhaust)

### Optional / Recommended
- **Ocean Optics USB spectrometer** (e.g., USB2000+ UV-Vis, 200–850 nm range) for quantitative absorbance measurements and color profiling of precipitates
- **Light sensor** for consistent illumination characterization
- **Color calibration card** (recorded alongside each image for color correction)

## Safety Considerations

### Silver Nitrate (AgNO₃)

| Hazard | Detail |
|--------|--------|
| GHS classifications | Oxidizer, corrosive, environmental hazard |
| Skin/eye contact | Causes burns; permanently stains skin black |
| Ingestion/inhalation | Harmful; may damage mucous membranes |
| Environmental | Very toxic to aquatic life |
| Incompatibilities | Combustible materials, ammonia (in concentrated form), acetylene |

**Handling:** Wear nitrile gloves, lab coat, and splash goggles. Work in a fume hood or well-ventilated area. Use spatulas/tongs for solid handling. Store in a tightly closed, light-protected container.

### Hydrochloric Acid (HCl)

| Hazard | Detail |
|--------|--------|
| GHS classifications | Corrosive, acute toxicity (inhalation) |
| Skin/eye contact | Causes severe burns |
| Inhalation | Irritating/corrosive fumes, especially at higher concentrations |
| Incompatibilities | Bases, oxidizers, metals (evolves H₂ gas) |

**Handling:** Wear nitrile or neoprene gloves, lab coat, splash goggles, and face shield for pouring. **Always use inside a chemical fume hood.** Store in a corrosion-resistant cabinet with secondary containment.

### Reaction Product — AgCl Precipitate and HNO₃ Byproduct

- The AgCl precipitate is an insoluble solid; relatively low acute toxicity but should still be collected as **heavy metal waste**.
- The supernatant contains dilute HNO₃ (nitric acid); mildly acidic at these concentrations but must not be poured down the drain.

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

Opentrons OT-2 pipette tips are made from **100% virgin polypropylene (PP)**, which has broad chemical resistance.

| Reagent | PP Compatibility | Risk Level | Notes |
|---------|-----------------|------------|-------|
| AgNO₃ (0.1 M) | ✅ Excellent | Low | May stain tips; no structural degradation |
| HCl (1 M) | ✅ Excellent | Low | PP is resistant to HCl at all concentrations |
| HNO₃ (dilute, byproduct) | ✅ Good | Low | Brief contact at dilute concentrations is fine; avoid prolonged hot/concentrated exposure |

### Recommendations

1. **Use filter tips** (Opentrons OT-2 filter tips with polyethylene filter mesh) to prevent acid vapor from reaching the pipette shaft internals. The OT-2 pipette body contains PC-ABS plastic components that could be damaged by prolonged acid vapor exposure.

2. **Use fresh tips for each aspiration** (no tip reuse) to prevent cross-contamination and avoid AgCl buildup on tip surfaces.

3. **Pre-wet tips** before aspirating HCl — aspirate and dispense 2–3 times to saturate the air gap with vapor and reduce dripping.

4. **Trailing air gap** — after aspirating HCl, draw a small air gap (~10 µL) to prevent dripping during transport.

### Workarounds for More Aggressive Reagents (Future Experiments)

For future experiments involving more corrosive reagents (e.g., concentrated HNO₃, H₂SO₄, organic solvents):

- **3D-printed custom tip adapters** can interface commercial PTFE or specialty tips with the OT-2 pipette nozzle, though the tips themselves should remain commercially manufactured PP or PTFE for reliable chemical resistance.
- **Polypropylene filament** is available for FDM 3D printers but is challenging to print (warping, adhesion) and does not match injection-molded PP quality. Best used for prototyping fit, not for final chemical use.
- **PTFE (Teflon) tips** are not available from Opentrons but can be sourced from specialty suppliers and used with custom adapters. PTFE offers near-universal chemical resistance.
- For the current experiment (0.1 M AgNO₃ + 1 M HCl), **standard PP tips are fully adequate** — no custom tips are needed.

## Protocol

### A. Manual Execution (Benchtop Reference)

1. Prepare labeled well plate (or test tubes) in a fume hood
2. Pipette 100 µL of 0.1 M AgNO₃ into each target well using a calibrated micropipette
3. Add 100 µL of 1 M HCl to each well; observe immediately
4. Record observations: precipitate color (white), morphology (curdy), time to visible formation
5. Photograph wells at time points: 0 s, 10 s, 30 s, 2 min, 10 min
6. Repeat at varying concentrations (0.01 M, 0.05 M, 0.1 M AgNO₃) to characterize detection limits

### B. OT-2 Automated Execution

1. Place OT-2 inside fume hood (or connect exhaust duct)
2. Load tip rack (filter tips recommended), reagent reservoirs, and well plate on the OT-2 deck
3. Position camera above well plate for time-lapse capture
4. Run OT-2 protocol:
   - Aspirate AgNO₃ with fresh tip → dispense into target wells
   - Change tip
   - Aspirate HCl with fresh tip (pre-wet 2–3×) → dispense into wells containing AgNO₃
5. Trigger camera capture at defined intervals (0 s, 10 s, 30 s, 2 min, 10 min)
6. (Optional) Position Ocean Optics fiber probe for absorbance readings

### C. Concentration Series

| Well | AgNO₃ (M) | HCl (M) | Expected Result |
|------|-----------|---------|-----------------|
| A1 | 0.01 | 1.0 | Faint white precipitate |
| A2 | 0.05 | 1.0 | Moderate white precipitate |
| A3 | 0.1 | 1.0 | Strong white precipitate |
| B1 | 0.1 | 0.1 | White precipitate (HCl limiting) |
| B2 | 0.1 | 0.5 | White precipitate |
| B3 | 0.1 | 1.0 | White precipitate (excess HCl) |
| C1 | 0.0 (blank) | 1.0 | No change (negative control) |
| C2 | 0.1 | 0.0 (DI water) | No change (negative control) |

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
- HCl — smallest available quantity (e.g., 100 mL of 1 M, or dilute from concentrated stock in Chem Stores)

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

- [ ] Confirm fume hood access and OT-2 placement location
- [ ] Contact BYU Chem Stores to procure AgNO₃ (0.1 M) and HCl (1 M) in small quantities
- [ ] Reach out to Dr. Roger G. Harrison or other gen chem faculty
- [ ] Consult BYU EH&S on waste disposal procedures
- [ ] Set up camera positioning and test image capture on blank well plate
- [ ] Write and test OT-2 protocol script (Python, Opentrons API)
- [ ] Run manual benchtop experiment first as a reference
- [ ] Run OT-2 automated experiment and compare results
- [ ] Evaluate whether Ocean Optics spectrometer purchase is justified based on initial results
