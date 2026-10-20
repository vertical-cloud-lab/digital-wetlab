
# Multi-Persona Review Set for ACS PRF DNI Proposal

**Proposal:** "Systematic Experimental Validation of Pitzer Activity-Coefficient Models for Sulfide-Scale Precipitation in Produced-Water Brines"  
**PI:** Sterling G. Baird, Department of Mechanical Engineering, BYU  
**Program:** ACS PRF DNI ($110K / 2 years)

---

## REVIEWER 1: "The Aqueous Geochemist"
**Persona:** Mid-career associate professor in geochemistry (Panel 2/8). Published extensively on Pitzer models for carbonate and sulfate systems. Familiar with PHREEQC and ScaleSoftPitzer. Has prior ACS PRF ND grant on mineral-water interface thermodynamics.

**OVERALL RECOMMENDATION: Fund with minor revisions**

The proposal targets a genuine and important gap in electrolyte solution thermodynamics: the absence of Pitzer interaction parameters for Fe²⁺ and Pb²⁺ with sulfide species in multi-component brines. The standard pitzer.dat database is essentially blind to metal-sulfide interactions at high ionic strength. The PI correctly identifies that current practice falls back on Davies-equation estimates, which are unreliable above I ≈ 0.5 molal.

**1. Scientific Merit (Very Good to Excellent)**

*Strengths:*
- The gap identification is rigorous. The fact that PHREEQC pitzer.dat contains zero Pb²⁺ parameters for any anion is genuinely shocking and deserves systematic attention.
- The 34-parameter enumeration is thorough — including neutral-species interactions (λ, ζ for FeS⁰ₐq, PbCl₂⁰) and temperature-dependent coefficients.
- Benchmarking against both PHREEQC pitzer.dat and Wang (2024)'s ScaleSoftPitzer framework is methodologically sound.
- The hypothesis is testable and falsifiable.

*Weaknesses:*
- **Binary data limitation (MAJOR):** Primarily binary precipitation/no-precipitation scoring to constrain 34 parameters is insufficient. Binary data constrains only the SI = 0 contour — not how far from the boundary you are. For Pitzer parameter regression, you typically need continuous data (dissolved-metal concentrations via ICP-OES or direct activity/osmotic coefficient measurements). The 50-100 ICP-OES conditions described as "supplementary" should be central to the regression.
  - → **Suggestion:** Elevate ICP-OES/colorimetric dissolved-metal measurements to a core component of Aim 2 (200-300 conditions).

- **Wang (2024) overlap:** Wang's dissertation already reports temperature-dependent Pitzer binary coefficients for Fe²⁺–HS⁻. The proposal cites Wang but doesn't clearly acknowledge that some of the "34 missing parameters" may already be partially constrained. The 3 Fe²⁺–HS⁻ binary parameters may have been fitted by Wang.
  - → **Suggestion:** Add a table distinguishing "parameters with no prior estimates" from "parameters with preliminary estimates that require independent validation."

- **Missing parameter sets:** The 34-parameter target omits HS⁻–background electrolyte interactions (HS⁻–Na⁺, HS⁻–Ca²⁺) and H₂S neutral-species interactions with background electrolytes, which are critical for pH 4–6 where H₂S(aq) dominates.

- **Mackinawite Ksp ambiguity:** Published pKsp values range from 2.13 to 3.98 (~70-fold range). The proposal doesn't explain whether Ksp will be fitted simultaneously with Pitzer parameters, or fixed at a literature value — and if fixed, which value.

- **Metastable phases:** Amorphous FeS, disordered mackinawite, and nanocrystalline mackinawite all have different apparent Ksp values. The interpretation of "precipitation onset" vs. equilibrium solubility needs more careful discussion.

**2. Student Education (Excellent):** Thoughtful and well-matched to BYU's M.S. program. Four training areas and specific course recommendations show careful planning.

**3. Newness (Very Good):** Aqueous geochemistry is clearly new for this PI. The automation aspect is more continuous with prior interests.

**4. Impact (Excellent):** Validated parameters would be immediately usable by the oilfield chemistry community (PHREEQC, Thermoddem, ScaleSoftPitzer). Clear path to NSF CAREER.

**5. Qualifications & Facilities (Good):** OT-2 is in hand. PI is in Mechanical Engineering, not Chemistry — raises questions about hands-on sulfide chemistry and glovebox experience. No preliminary experimental data is presented. Even a single BaSO₄ precipitation experiment would have strengthened the case significantly.

---

## REVIEWER 2: "The Inorganic Chemist / Panel 3 Regular"
**Persona:** Recently tenured assistant professor in inorganic chemistry. Expertise in coordination chemistry and metal-ligand reactivity. Prior ACS PRF DNI grantee (2022). Active in ACS Division of Inorganic Chemistry. Represents the "typical" Panel 3 reviewer.

**OVERALL RECOMMENDATION: Fundable, but with reservations**

This is clearly written and well-organized. The research question is sharp, the hypothesis testable, and the petroleum connection direct. My primary concern is that this reads more like a chemical engineering or geochemistry proposal than an inorganic chemistry proposal. The inorganic chemistry content is subordinate to the thermodynamic modeling and parameter-fitting exercise.

**1. Scientific Merit (Very Good)**

*Strengths:*
- The contrast between well-parameterized BaSO₄ and completely unparameterized Pb²⁺ sulfide systems is compelling.
- Latin hypercube sampling is sophisticated and appropriate for high-dimensional parameter spaces.
- The hierarchical contingency plan (34 → 24 → 17 parameters) shows mature project management.
- Safety discussion is thorough.

*Weaknesses:*
- **Panel fit concern (MODERATE):** The core science is electrolyte thermodynamics (Panel 6) applied to petroleum brines (Panel 9 or Geochemistry/Panel 2). The inorganic chemistry content (Panel 3) is present but secondary. A Panel 3 reviewer may question whether this belongs in Panel 3.

- **No preliminary data:** The figure boxes are placeholders. Even a photograph of FeS/PbS precipitate in a well plate or the computational PHREEQC figure would have added credibility.

- **Molecular-level insight missing:** Why would Fe²⁺–Na⁺ mixing parameters be significant specifically in sulfide media? Is it because FeHS⁺ complexation modifies the effective charge distribution? An inorganic chemist reviewer wants to see the molecular picture, not just thermodynamic equations.

- **Speciation complexity underappreciated:** The Fe²⁺/HS⁻ system at pH 6–7.5 involves Fe²⁺, FeOH⁺, FeCl⁺, FeHS⁺, FeS⁰(aq), plus nanoparticulate FeS clusters. Binary precipitation scoring may oversimplify the actual chemistry.

- **Temperature range execution:** How will 96-well plates be heated uniformly to 90°C? Evaporation and H₂S volatility at 90°C? Sealed plates at 90°C generate significant vapor pressure. More methodological detail needed.

**2. Student Education (Excellent):** Strong interdisciplinary training plan.

**3. Newness (Excellent):** Genuine new direction from materials informatics to aqueous geochemistry.

**4. Impact (Very Good):** Clear for oilfield chemistry, but broader impact for fundamental inorganic chemistry is less obvious — more a "completing the database" exercise than discovery of new chemistry.

**5. Qualifications & Facilities (Good to Very Good):** Glovebox situation unclear — is one currently available in the PI's lab?

**Key questions:** Is there a glovebox currently available? Has the PI personally worked with sulfide solutions? Why Panel 3 and not Panel 9?

---

## REVIEWER 3: "The Oilfield Scale Specialist"
**Persona:** Senior researcher in chemical/petroleum engineering (Panel 9). Expertise in oilfield scale prediction, ScaleSoftPitzer, and produced-water chemistry. Industry consulting experience. Familiar with the Kan/Tomson/Wang (Rice/Ohio) group's work.

**OVERALL RECOMMENDATION: Strong fund**

This proposal addresses one of the most practically important gaps in oilfield scale prediction. As someone who regularly uses ScaleSoftPitzer and PHREEQC for scale-risk assessment, I can attest that sulfide-scale prediction is effectively a black box. The PI has done an excellent job identifying the specific parameter gaps.

**1. Scientific Merit (Excellent)**

*Strengths:*
- The central paradox is devastatingly effective: FeS and PbS are among the most problematic scales, yet the Pitzer parameter database is essentially empty.
- The 34-parameter breakdown demonstrates deep understanding.
- The ±0.2 SI threshold is practical and well-justified (can mean the difference between "no treatment" and "aggressive inhibition").
- Contingency plan (prioritizing PbS over FeS if oxidation control proves difficult) is the right call.

*Weaknesses:*
- **Produced-water realism (MODERATE):** Real produced waters contain Mg²⁺, K⁺, Ba²⁺, Sr²⁺, SO₄²⁻, HCO₃⁻, and organic acids. The NaCl ± CaCl₂ simplification should be more explicitly acknowledged.
- **Kinetics vs. thermodynamics:** 240-minute endpoint may not capture equilibrium for all conditions. What if a condition is thermodynamically supersaturated but doesn't precipitate in 4 hours due to nucleation kinetics?
  - → Include a subset with longer equilibration (24–72 hours).
- **Budget for consumables:** $22,000 for ~30,000 experiments seems tight. The $3,950 pipette takes a significant fraction, leaving ~$18,000 for all chemicals, tips, plates across 2 years.

**2–5. Student Education (Excellent), Newness (Good to Very Good), Impact (Excellent), Qualifications (Good)**

*Minor comments:* The SAASBO/CrabNet discussion feels promotional — consider trimming for more experimental detail. Add a table of representative produced-water compositions to anchor the experimental ranges.

---

## REVIEWER 4: "The High-Throughput Experimentation / Lab Automation Expert"
**Persona:** Early-career assistant professor working on self-driving labs and AI-driven materials discovery. Has PRF DNI on ML-driven catalyst screening. Familiar with Opentrons, Bayesian optimization, and experimental design.

**OVERALL RECOMMENDATION: Fund**

Well-conceived proposal applying HTE methodology to an important data gap. The LHS + BO strategy is appropriate and state-of-the-art. Main concerns are about detection methodology and data quality.

**1. Scientific Merit (Very Good to Excellent)**

*Strengths:*
- LHS is the right design choice for 5D parameter space.
- PI has firsthand SAASBO experience — genuine advantage.
- Tiered detection strategy is pragmatic.
- Quasi-random fallback for BO difficulties is sensible.

*Weaknesses:*
- **Detection resolution (MODERATE-MAJOR):** Visual binary scoring is very low information content. Only the microplate reader (Tier 3) provides truly quantitative data — and this depends on shared facility access.
  - → **Strong suggestion:** Prioritize plate reader access. A used/refurbished reader ($3,000-5,000) would dramatically improve data quality.

- **Mixing in 96-well plates:** 5 molal NaCl is quite viscous. OT-2 aspiration/dispense mixing may be incomplete, causing local supersaturation hotspots. Need specific mixing protocol details (cycles, volume, speed).

- **H₂S cross-contamination:** H₂S can diffuse through headspace between wells, especially at elevated temperature and low pH. Include control experiments with alternating high-sulfide/blank wells.

- **OT-2 inside glovebox:** Large instrument (~35 × 25 cm deck). Standard gloveboxes may not accommodate it easily, and glovebox gloves make troubleshooting difficult. Has the PI physically tested this?

- **Manual scoring burden:** ~15,000 wells to score visually = 20-40 hours of manual work. Human fatigue will reduce accuracy. Implement at least simple grayscale thresholding from the start rather than treating computer vision as a "stretch goal."

- **Effective data-to-parameter ratio:** With binary data, only ~10-20% of points near the precipitation boundary carry significant information, dropping the effective ratio from 880:1 to 90-180:1.

**2. Student Education (Very Good to Excellent), 3. Newness (Very Good), 4. Impact (Very Good), 5. Qualifications (Good to Very Good)**

---

## REVIEWER 5: "The Skeptical Physical Chemist"
**Persona:** Tenured professor of physical chemistry (Panel 6). Expertise in electrolyte solution theory, statistical thermodynamics, and molecular simulation. Published critiques of over-parameterization in empirical models. Devil's advocate reviewer.

**OVERALL RECOMMENDATION: Fundable with significant concerns**

The proposal identifies a real gap and proposes an ambitious campaign. However, I have fundamental concerns about whether the methodology can deliver data adequate for robust Pitzer parameter regression, and whether the 34-parameter target is well-posed.

**1. Scientific Merit (Good to Very Good)**

*Weaknesses (in severity order):*

- **Over-parameterization risk (MAJOR):** Fitting 34 parameters simultaneously from binary precipitation data is almost certainly ill-conditioned. β⁰ and Cᶲ are strongly correlated; mixing parameters (θ, ψ) can compensate for errors in binary parameters. The proposal mentions weighted nonlinear least-squares but does not discuss regularization (ridge, LASSO), parameter sensitivity analysis, or information-theoretic model selection (AIC, BIC). I would want to see: (a) formal parameter identifiability analysis (Fisher information or profile likelihood); (b) explicit regularization; (c) hierarchical fitting with model selection criteria. The contingency plan (reduce to 24 or 17) should be the **primary** strategy, not the contingency.

- **Binary data is fundamentally insufficient (MAJOR):** A binary observation provides one bit of information (SI > 0 or SI < 0). A continuous dissolved [Fe²⁺] measurement provides information about the magnitude. Different parameter sets can produce identical SI = 0 surfaces — the classic identifiability problem. The ICP-OES measurements for 50-100 conditions should be the backbone, not a supplement.

- **Thermodynamic vs. kinetic precipitation (MODERATE):** "Precipitation observed within 240 minutes" ≠ "thermodynamic supersaturation." For PbS, the extremely low Ksp means even tiny concentrations exceed solubility — the boundary mapping may actually measure nucleation kinetics rather than equilibrium. Pitzer parameters are thermodynamic quantities; kinetic contamination corrupts derived parameters.

- **H₂S volatility at elevated temperature (MODERATE):** At pH < 6 and 90°C, most sulfide is H₂S(aq), which rapidly partitions into headspace and escapes through seals. Effective [HS⁻] will be lower than nominal, shifting boundaries and corrupting parameters.
  - → Quantify H₂S loss rates in sealed plates at elevated temperature. Consider sealed glass vials for the high-T subset.

- **No activity-coefficient validation:** Pitzer parameters should ideally be validated against measured activity/osmotic coefficients. Any possibility of incorporating isopiestic measurements or EMF cell data?

**2. Student Education (Very Good):** Ambitious scope for M.S. students in Mechanical Engineering to master both sulfide chemistry and Pitzer modeling in 2 years.

**3. Newness (Very Good to Excellent), 4. Impact (Very Good), 5. Qualifications (Good)**

**Bottom line:** Fund with the recommendation to: (1) adopt hierarchical fitting as primary approach; (2) expand ICP-OES significantly; (3) include explicit regularization; (4) address H₂S volatility.

---

## REVIEWER 6: "The PRF Program Compliance Officer"
**Persona:** Represents the ACS PRF program officer's compliance-check perspective.

**COMPLIANCE ASSESSMENT:**

| Criterion | Status |
|-----------|--------|
| Fundamental research | ✅ PASS — addresses fundamental thermodynamic accuracy of Pitzer formalism |
| Petroleum relevance | ✅ PASS (strong) — FeS/PbS scale in produced waters is unambiguously petroleum-relevant |
| New direction | ✅ PASS — aqueous geochemistry is clearly new for this PI (note: verify no overlap with other funded OT-2 projects) |
| Word limit (≤4,000) | ⚠️ CONCERN — appears near or slightly over 4,000 words; verify carefully |
| Budget compliance | ✅ PASS — $110K total, 60.0% student support (exactly at minimum), PI salary at cap, no overhead |
| Abstract | ✅ PASS (~245 words) |
| Petroleum relevance statement | ✅ PASS (~100 words) |
| Figures | ⚠️ CONCERN — placeholder figure boxes must be replaced with real figures before submission |
| Panel selection | ⚠️ AMBIGUOUS — touches Panels 3, 6, 8, and 9; consult program officer |
| Six suggested reviewers | ❌ INCOMPLETE — template is blank; must be completed |

**Budget note:** Student support at exactly 60.0% is compliant but proposals with 65-75% tend to be viewed more favorably. Consider reducing supplies slightly to increase student support.

---

## SYNTHESIS: CROSS-REVIEWER CONSENSUS

**Overall Panel Consensus: Fundable (4/5 external reviewers recommend funding)**

### Unanimous Strengths
1. The Pitzer parameter gap is real, well-documented, and important
2. The hypothesis is testable and falsifiable
3. The LHS + BO experimental design is appropriate
4. Student training plan is strong
5. Petroleum relevance is unambiguous
6. The 34-parameter enumeration demonstrates deep technical understanding
7. Contingency planning is realistic and thoughtful

### Top 10 Action Items (by reviewer consensus frequency)

| Priority | Concern | Reviewers | Action |
|----------|---------|-----------|--------|
| 1 | Binary data limitation | 4/5 | Elevate ICP-OES to core component (200-300 conditions), not supplement |
| 2 | Over-parameterization/identifiability | 3/5 | Make hierarchical fitting the primary strategy; add regularization (ridge/LASSO); discuss AIC/BIC |
| 3 | No preliminary experimental data | 3/5 | Include at least 1 experimental figure + the computational Pitzer gap figure |
| 4 | PI experimental chemistry credentials | 3/5 | Mention any relevant training; describe collaborators/mentors in aqueous chemistry at BYU |
| 5 | H₂S volatility/cross-contamination | 2/5 | Add H₂S loss quantification controls; sealed vials for high-T subset |
| 6 | Kinetics vs. thermodynamics | 2/5 | Include 24-72 hour equilibration subset; discuss nucleation vs. equilibrium |
| 7 | Word count | 2/5 | Verify rigorously; trim SAASBO/CrabNet promotional discussion |
| 8 | Panel selection | 2/5 | Consult program officer; Panel 9 may be better fit than Panel 3 |
| 9 | Placeholder figures | 2/5 | Replace with real figures before submission |
| 10 | Suggested reviewers blank | 1/5 | Complete all six reviewer suggestions |

### Strongest Selling Points (lean into these)
- Zero Pb²⁺ Pitzer parameters for ANY anion in standard databases — a genuinely shocking gap
- Direct BaSO₄ control system with well-validated predictions
- $1.4 billion/year industry impact
- The HTE methodology for mineral precipitation is itself a contribution
- Clear seed-funding path to NSF CAREER/CHE proposal

### Additional Suggestions
- Add a table of representative produced-water compositions (Reviewer 3)
- Mention scale inhibitor applications (Reviewer 3)
- Discuss physical meaning of Pitzer mixing parameters at molecular level (Reviewer 2)
- Implement simple grayscale thresholding from the start (Reviewer 4)
- Clarify which of the 34 parameters are genuinely new vs. partially constrained by Wang (2024), Woosley & Millero (2013), Xiong et al. (2018) (Reviewer 1)

---

## Discretionary Analytical Decisions

- **Reviewer persona selection:** Chose six personas spanning aqueous geochemistry (Panel 2/8), inorganic chemistry (Panel 3), petroleum engineering (Panel 9), high-throughput experimentation, physical chemistry (Panel 6), and compliance — selected to represent the most likely reviewer pool given the interdisciplinary nature of the proposal and ACS PRF's panel structure.
- **Evaluation criteria weighting:** Followed ACS PRF's stated order of importance (Scientific Merit > Student Education > Newness > Impact > Qualifications), with scientific merit receiving the most detailed treatment in each review.
- **Severity classification:** Classified concerns as MAJOR, MODERATE, or MINOR based on how likely they would be to affect a funding decision rather than just improve the proposal.
- **Recommendation calibration:** Calibrated overall recommendations (Strong Fund → Fund → Fundable with concerns → Do not fund) against the assumption that ACS PRF DNI funds ~75 of ~300+ proposals (roughly 25% success rate), so "fundable" means competitive but not guaranteed.
- **Word count estimation:** Used rough LaTeX-stripping heuristic to estimate ~4,600+ words in the body, which informed the compliance concern about the 4,000-word limit; this is approximate and the PI should verify using their own method.
- **Emphasis on binary data concern:** Elevated this as the #1 cross-reviewer concern because 4 of 5 reviewer personas independently identified it, reflecting the high likelihood that real reviewers from multiple disciplines would raise this issue.
