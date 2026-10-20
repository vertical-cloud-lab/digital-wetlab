# Figure Brainstorming â€” ACS PRF DNI Proposal

> Updated to match the merged draft from [PR #18](https://github.com/vertical-cloud-lab/digital-wetlab-private/pull/18) (now on main).
> Based on [PR #13](https://github.com/vertical-cloud-lab/digital-wetlab-private/pull/13) (Research Question & Hypothesis) and the [Edison Precedent Search](EDISON_PRECEDENT_SEARCH.md).
> Assets generated programmatically as drafts; intended as starting points for final figure design.

---

## Best Practices for Proposal Figures

> Evidence-based recommendations from an [Edison Scientific literature search](https://edisonscientific.com/platform) on figure design in grant proposals, drawing on Rolandi et al. 2011 (*Adv. Mater.*, 43 citations), Jambor et al. 2021 (*PLoS Biology*, 82 citations), Pedwell et al. 2017 (*Biochem. Mol. Biol. Educ.*, 69 citations), and Frane 2015 (*J. Gen. Psychol.*, 23 citations).

### Planning & Strategy
1. **One key message per figure** â€” Treat figures as part of the proposal outline early; identify the storyline and give each figure a single clear message (Rolandi et al. 2011).
2. **Plan content before drawing** â€” Use a planning table to map objectives â†’ visualization type â†’ panels, then sketch the multi-panel layout before producing final graphics (Jambor et al. 2021).
3. **Make each figure earn its footprint** â€” With ~4,000 words and 2â€“3 figures, every element must serve the message; remove unnecessary detail rather than squeeze it in (Principle of Relevance; Rolandi et al. 2011).

### Layout & Information Design
4. **Consistent reading direction** â€” For multi-panel figures, choose left-to-right or top-to-bottom; arrange in clean rows/columns with sufficient whitespace between panels (Jambor et al. 2021).
5. **High signal-to-noise ratio** â€” Remove "chart junk": no drop shadows, 3D effects, unnecessary gradients. Make gridlines and tick marks visually subordinate to data (Rolandi et al. 2011).
6. **Direct labeling over legends** â€” Place labels next to data points/lines rather than in distant legends; reduces cognitive load in dense, page-limited documents (Rolandi et al. 2011).
7. **Contiguity principle** â€” Place explanatory text close to the graphic of interest; use annotations (arrows, boxes) to direct attention to key features (Pedwell et al. 2017; Jambor et al. 2021).

### Color & Accessibility
8. **Use color sparingly and purposefully** â€” Color should emphasize and group, not decorate; avoid deploying every contrast channel simultaneously (Rolandi et al. 2011).
9. **Colorblind-safe palettes** â€” Avoid redâ€“green dependence; use blue/orange or cyan/magenta alternatives. Validate with color-vision-deficiency simulators like Color Oracle (Frane 2015; Jambor et al. 2021).
10. **Don't encode meaning by color alone** â€” Use redundant cues: patterns, line styles, data labels. WCAG-aligned guidance recommends dual encoding for all critical distinctions (W3C Web Content Accessibility Guidelines 2.1).
11. **Black-and-white robustness** â€” Design for laser printing/photocopying; use line styles and marker shapes in addition to color (Rolandi et al. 2011).

### Print & Reproducibility
12. **Design for final size** â€” Check legibility at the size figures will appear in the PDF (column width in a double-spaced 12pt document), not on your monitor (Rolandi et al. 2011).
13. **~70% type/background contrast** â€” Avoid text over patterned backgrounds; place text adjacent or in legends when over complex images (Rolandi et al. 2011).
14. **Include expected data** â€” Showing simulated/expected results demonstrates feasibility and clear thinking.

### ACS PRF Specific Recommendations
- The proposal body is a single PDF with embedded figures (not separate uploads)
- Figures count toward page space but captions do not count toward the 4,000-word limit
- Double-spaced, 12-point font required for body text; figures can use smaller fonts
- Use `wrapfigure` in LaTeX to integrate figures with text and save space
- 2â€“3 well-designed figures is typically optimal for a 4,000-word proposal

### Practical Checklist (from Edison Scientific search)
- [ ] **A. Planning:** Define storyline; one message per figure; draft planning table; sketch layout
- [ ] **B. Layout:** Consistent reading direction; whitespace; direct labels; explanatory text adjacent
- [ ] **C. Density:** Remove chart junk; subordinate gridlines; keep only message-supporting elements
- [ ] **D. Color:** Avoid red/green dependence; use colorblind-safe palettes; simulate CVD
- [ ] **E. Reproducibility:** Check final PDF size and print; ensure ~70% type/background contrast; B/W robustness
- [ ] **F. Accessibility:** Don't rely on color alone; add redundancy; add alt text; export tagged PDF

---

## Proposed Figure Plan

### Figure 1: Overview Schematic (Introduction)

**Purpose:** Graphical abstract for the entire proposal â€” visible in the first half-page.

**Caption from draft.tex:** *"Overview of the proposed prediction framework. A high-throughput experimental platform generates Latin hypercubeâ€“sampled compositions of metal ions, sulfide, and brine matrix in 96-well plates. Precipitation is detected off-line via visual scoring, camera imaging, or microplate-reader absorbance, and results are compared to Pitzer-model predictions to identify deviations and regress new interaction parameters."*

**Subpanels:**
- **A. Problem context** â€” Produced water (~250M bbl/day, >200k mg/L TDS) â†’ sulfide scale (FeS/PbS) formation in pipelines; $1.4B/yr in scale costs (Hamza et al. 2021 [21])
- **B. Knowledge gap** â€” Pitzer activity coefficients uncertain for FeÂ²âº/PbÂ²âº at high ionic strength; 34 missing parameters (6 binary Î²â°/Î²Â¹/Cá¶² + 8 mixing Î¸/Ïˆ + 8 neutral-species Î»/Î¶ + 3 temperature-dependent + 2 metalâ€“hydroxide + 3 PbÂ²âºâ€“SOâ‚„Â²â» + 4 PbClâ‚‚â° neutral-species); PbÂ²âº is the most critical gap (zero Pitzer params for any sulfide interaction [19]); Felmy et al. 2000 showed PbÂ²âº models fail above I â‰ˆ 2 m
- **C. Approach** â€” OT-2 robot â†’ LHS design (~2,500 conditions Ã— 3 reps per metal) + BO follow-up â†’ tiered off-line detection (visual/camera/plate reader)
- **D. Expected result** â€” Systematic overprediction of supersaturation above I â‰ˆ 2 molal
- **E. Deliverables** â€” ~30,000 measurements, 34 new Pitzer parameters, validated model (5-fold CV), 2 M.S. + 2 UG students, seed â†’ CAREER

**Draft asset:** [`workflow-diagrams/proposal_overview_figure.png`](figures/workflow-diagrams/proposal_overview_figure.png)

---

### Figure 2: Aim 1 â€” Experimental Design (Research Plan)

**Purpose:** Show how the automated screening experiment works, from deck layout to data collection.

**Caption from draft.tex:** *"Aim 1 workflow. The high-throughput experimental platform dispenses stock solutions of metal salts, Naâ‚‚S/NaHS, NaCl, CaClâ‚‚, and pH buffers into 96-well plates according to a Latin hypercube sampling design. Plates are then transferred to an off-line detection station (visual scoring, camera imaging, or microplate reader) to identify precipitation vs. no-precipitation for each condition."*

**Subpanels:**
- **A. OT-2 deck layout** â€” Which labware goes where; stock solutions, tip racks, output plates, temperature module. FeS system inside Nâ‚‚ glovebox; PbS system in fume hood.
- **B. LHS sampling design** â€” Latin hypercube sampling across 5D parameter space: [MÂ²âº] Ã— [HSâ»] Ã— I (0.5â€“5 m NaCl Â± CaClâ‚‚) Ã— pH (4â€“9) Ã— T (25â€“90 Â°C). ~1,000 unique conditions per metal system.
- **C. Tiered off-line detection** â€” Three tiers: (1) visual binary scoring of black FeS/PbS precipitates (~$0, fast); (2) overhead camera + Python/OpenCV grayscale analysis (<$100); (3) microplate-reader absorbance at 600 nm (BYU shared facility: BioTek Synergy H1 or SpectraMax iD3)
- **D. Overhead view** â€” Simulated photograph of precipitate wells (clear â†’ turbid â†’ black precipitate gradient)

**Draft assets:**
- [`ot2-robot/ot2_deck_layout.png`](figures/ot2-robot/ot2_deck_layout.png) â€” Deck layout schematic (Nâ‚‚ glovebox / fume hood context)
- [`well-plates/wellplate_precipitation_heatmap.png`](figures/well-plates/wellplate_precipitation_heatmap.png) â€” LHS sampling + overhead well view
- [`characterization-data/tiered_detection_methods.png`](figures/characterization-data/tiered_detection_methods.png) â€” Three-tier detection: visual scoring, camera + Python, plate reader absorbance
- [`precipitates/fes_overhead_view.png`](figures/precipitates/fes_overhead_view.png) â€” Simulated overhead photograph

**Additional assets to source:**
- [ ] Real photograph of OT-2 robot (from Opentrons press kit or lab photo)
- [ ] Real overhead photograph of precipitate well plate (once preliminary experiments are run)
- [ ] Photograph of BYU shared-facility plate reader

---

### Figure 3: Aim 2 â€” Model Validation & Parameter Regression (Research Plan)

**Purpose:** Show how experimental data will be compared to Pitzer-model predictions and how new parameters will be regressed.

**Caption from draft.tex:** *"Aim 2 analysis pipeline. Experimental precipitation boundaries are compared to Pitzer-model predictions (via PHREEQC) to generate deviation maps across the parameter space. Where deviations exceed Â±0.2 SI, new Pitzer interaction parameters are regressed and validated against held-out data."*

**Subpanels:**
- **A. Pitzer model equations** â€” Key equations with the gap (34 missing parameters) highlighted; Î²â°/Î²Â¹/Cá¶² for FeÂ²âºâ€“HSâ» and PbÂ²âºâ€“HSâ», plus Î¸/Ïˆ for mixing with Naâº, CaÂ²âº, Clâ»
- **B. Activity coefficient plot** â€” Î³Â± vs. ionic strength for NaCl (validated) vs. FeClâ‚‚/PbClâ‚‚ (uncertain), with uncertainty bands in the produced-water range (I > 2 m)
- **C. Precipitation boundary comparison** â€” log[MÂ²âº] vs. log[HSâ»] showing model-predicted boundary vs. expected experimental data at different I
- **D. SI deviation plot** â€” Î”SI (experiment âˆ’ model) vs. ionic strength, showing systematic overprediction above I â‰ˆ 2 m; Â±0.2 SI threshold highlighted

**Draft assets:**
- [`pitzer-models/pitzer_activity_coefficients_and_SI.png`](figures/pitzer-models/pitzer_activity_coefficients_and_SI.png) â€” Activity coefficients + SI deviation
- [`pitzer-models/precipitation_boundaries.png`](figures/pitzer-models/precipitation_boundaries.png) â€” FeS/PbS precipitation boundary plots
- [`pitzer-models/pitzer_equations.svg`](figures/pitzer-models/pitzer_equations.svg) â€” Pitzer equation summary (SVG, editable)

---

## Additional Asset Inventory

### Chemical Reaction Diagrams
| File | Description |
|------|-------------|
| [`chemical-reactions/fes_precipitation.svg`](figures/chemical-reactions/fes_precipitation.svg) | FeS (mackinawite) precipitation reaction, Ksp ~10â»Â³Â·â¶ to 10â»â´Â·â¶âµ, competing FeHSâº complexation |
| [`chemical-reactions/pbs_precipitation.svg`](figures/chemical-reactions/pbs_precipitation.svg) | PbS (galena) precipitation reaction, Ksp â‰ˆ 10â»Â²â¹, chloro-complexation; Duan et al. 2007 showed >15% errors in CaClâ‚‚ solutions |

### Detection & Characterization
| File | Description |
|------|-------------|
| [`characterization-hardware/characterization_techniques.svg`](figures/characterization-hardware/characterization_techniques.svg) | Overview of ex-situ (XRD, SEM-EDS, Raman, ICP-OES) and tiered off-line detection (visual scoring, camera + Python, plate reader) |
| [`characterization-data/tiered_detection_methods.png`](figures/characterization-data/tiered_detection_methods.png) | Three-tier detection: visual binary scoring, camera + OpenCV histograms, plate-reader absorbance kinetics |
| [`characterization-data/xrd_raman_eds_example.png`](figures/characterization-data/xrd_raman_eds_example.png) | Simulated XRD, Raman, and EDS spectra for FeS mackinawite |
| [`characterization-data/nephelometry_kinetics.png`](figures/characterization-data/nephelometry_kinetics.png) | Turbidity kinetics + endpoint heatmap (supplementary; primary detection is off-line tiered approach) |

### Workflow & Context
| File | Description |
|------|-------------|
| [`workflow-diagrams/experimental_workflow.png`](figures/workflow-diagrams/experimental_workflow.png) | Linear 6-step workflow: Preparation (LHS) â†’ Screening (Ã—3 replicates) â†’ Off-Line Detection â†’ Characterization â†’ Modeling â†’ Regression |
| [`downstream-applications/petroleum_relevance_diagram.png`](figures/downstream-applications/petroleum_relevance_diagram.png) | Problem context (~250M bbl/day produced water, $1.4B/yr scale costs [Hamza 2021]) â†’ 34 new parameters â†’ downstream impact (PHREEQC, CaCOâ‚ƒ/SrSOâ‚„ transfer, NSF CAREER) |

### Icons & Reusable Components
| File | Description |
|------|-------------|
| [`scientific-icons/scientific_icons.svg`](figures/scientific-icons/scientific_icons.svg) | Library of individual icons: beaker, test tube, 96-well plate, pipette, OT-2 robot, thermometer, pH meter, microscope, data chart, database, oil derrick, publication, FeS/PbS crystal |

---

## Assets Still Needed

The following should be sourced as the project develops:

- [ ] **Real OT-2 photograph** â€” Contact Opentrons for press kit image, or take a lab photo
- [ ] **Real precipitate photograph** â€” Overhead image of FeS precipitate in 96-well plate from preliminary experiments
- [ ] **Crystal structure diagrams** â€” Mackinawite (tetragonal FeS) and galena (cubic PbS) unit cells; consider VESTA or CrystalMaker renders
- [ ] **PHREEQC screenshot or output** â€” Example input file and SI calculation showing model prediction workflow; use pitzer.dat database
- [ ] **Real XRD/Raman data** â€” From preliminary precipitate characterization (replace simulated plots)
- [ ] **Produced water composition table** â€” Representative TDS, ion concentrations from literature (Shafer-Peltier et al. 2020, Ref [5]; Crabtree et al. 1999, Ref [13])
- [ ] **Timeline Gantt chart** â€” 2-year project timeline: both M.S. students start Year 1; Student 1 = FeS + protocol dev; Student 2 = PbS + PHREEQC modeling
- [ ] **Student training schematic** â€” 2 M.S. + 2 UG at BYU Mechanical Engineering; 4 training areas (aqueous chemistry, automation, modeling, communication)
- [ ] **Glovebox photograph** â€” Nâ‚‚ glovebox with OT-2 for FeÂ²âº oxidation prevention
- [ ] **BYU plate reader photograph** â€” BioTek Synergy H1 or SpectraMax iD3 from shared facility

---

## Figure-to-Proposal Mapping

| Proposal Section | Figure | Purpose |
|---|---|---|
| Introduction (Â§1) | Figure 1 (Overview) | Hook the reviewer; show the full story at a glance |
| Research Plan â€” Aim 1 (Â§4.1) | Figure 2 (Experimental Design) | Demonstrate feasibility: LHS sampling, OT-2 deck, tiered detection |
| Research Plan â€” Aim 2 (Â§4.2) | Figure 3 (Model Validation) | Show what "success" looks like; expected deviations; 34-parameter target |
| Background (Â§3) | Chemical reaction SVGs (inline) | Optional small insets for FeS/PbS key reactions |
| Expected Results (Â§5) | Panels from Figures 2â€“3 | Cross-reference expected data panels |

---

## Key Numbers for Figure Labels

These values come directly from the PR #18 draft and should be consistently used across all figures:

| Parameter | Value | Source |
|---|---|---|
| Produced water volume | ~250 million bbl/day globally | draft.tex Â§1 |
| TDS range | >200,000 mg/L | draft.tex Â§1 |
| FeS Ksp (mackinawite) | 10â»Â³Â·â¶ to 10â»â´Â·â¶âµ | draft.tex Â§3 |
| PbS Ksp (galena) | â‰ˆ 10â»Â²â¹ | draft.tex Â§1 |
| Ionic strength range | 0.5â€“5 molal | draft.tex Â§4.1 |
| pH range | 4â€“9 | draft.tex Â§4.1 |
| Temperature range | 25â€“90 Â°C | draft.tex Â§4.1 |
| Unique conditions per metal | ~1,000 (LHS) | draft.tex Â§4.1 |
| Unique conditions total | ~2,000 (both metals) | draft.tex Â§2.1 |
| Total measurements | ~30,000 (Ã—3 replicates) | draft.tex Â§4.1 |
| Target parameters | 34 (6 binary + 8 mixing + 8 neutral-species + 3 temperature-dependent + 2 metalâ€“hydroxide + 3 PbÂ²âºâ€“SOâ‚„Â²â» + 4 PbClâ‚‚â° neutral-species) | draft.tex Â§4.2 |
| SI threshold | Â±0.2 | draft.tex Â§4.2 |
| Validation | 5-fold CV + extrapolatory challenge splits | draft.tex Â§4.2 |
| Scale industry cost | $1.4 billion/yr (Hamza et al. 2021 [21]) | draft.tex Â§3.1 |
| PbS model failure | >15% errors in CaClâ‚‚ above I â‰ˆ 2 m (Duan et al. 2007 [20]) | draft.tex Â§3.2 |
| 8-channel pipette | $3,950 (GEN2, below $5k capital threshold) | budget.tex |
| Students | 2 M.S. + 2 UG (BYU Mech. Eng.) | draft.tex Â§6 |
| Budget | $110,000 over 2 years | budget.tex |
| References | 25 total | draft.tex Â§7 |

---

## Notes on Figure Generation

All programmatic figures were generated with Python (matplotlib + numpy) and can be regenerated or customized by editing the generation scripts. SVG files are fully editable in any vector graphics editor (Inkscape, Illustrator, Figma). Both PNG (300 dpi) and PDF versions are provided where applicable.

Color palette used across figures:
- Teal `#4ECDC4` â€” Preparation / tip racks
- Coral `#FF6B6B` â€” Screening / output plates
- Sky blue `#45B7D1` â€” Detection / problem context
- Sage `#96CEB4` â€” Analysis / datasets
- Yellow `#FFEAA7` â€” Modeling / Pitzer
- Plum `#DDA0DD` â€” Validation / regression
