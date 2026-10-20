# Heating Timing in Precipitation Studies — Edison Scientific Analysis

> Generated via [Edison Scientific](https://edisonscientific.com/platform) `job-futurehouse-paperqa3` search.
> Addresses: Does it matter whether heating occurs early (pre-mix) vs. later (post-mix) in sulfide-mineral precipitation experiments?

## Query

In high-throughput precipitation screening experiments for determining thermodynamic solubility products and Pitzer ion-interaction parameters of sparingly soluble minerals (specifically iron sulfide mackinawite FeS and lead sulfide galena PbS), does it matter whether the sample reaches its target temperature (e.g. 60-90 °C) before or after the precipitant reagents are mixed? Specifically: (1) For determining equilibrium thermodynamic parameters (Ksp, Pitzer activity coefficients), does the thermal history during the initial nucleation and crystal growth phase affect the final equilibrium state? In other words, if reagents are mixed at 25 °C and then heated to 60 °C, vs. mixed at 60 °C directly, will the equilibrium precipitate identity, saturation index, and dissolved metal concentrations differ after sufficient equilibration time (e.g. 4 hours to 72 hours)? (2) Does the heating protocol (pre-mix vs. post-mix) affect precipitation kinetics — specifically nucleation rate, induction time, particle size distribution, and polymorphic form of the precipitate (e.g. amorphous FeS vs. crystalline mackinawite vs. greigite)? (3) For high-throughput screening in 96-well plates or sealed glass vials, what is the recommended practice: mix reagents at room temperature then transfer to a heating block, or pre-heat all reagents to the target temperature before mixing? (4) How broadly applicable are these findings? Are the effects of thermal history on precipitation equilibrium and kinetics relevant to other mineral systems beyond sulfides — e.g., carbonates (CaCO3), sulfates (BaSO4, SrSO4), hydroxides (Fe(OH)3), phosphates — and to other fields such as pharmaceutical crystallization, biomineralization, nanoparticle synthesis, or scale prevention in industrial water treatment? (5) What does the literature say about Ostwald's rule of stages in the context of metal sulfide precipitation — do metastable phases (amorphous FeS, nanocrystalline mackinawite) form first and then transform to more stable phases (greigite, pyrite), and does the temperature at which initial precipitation occurs affect which metastable phase forms and how quickly it transforms?

## Edison Scientific Assessment

Question: In high-throughput precipitation screening experiments for determining thermodynamic solubility products and Pitzer ion-interaction parameters of sparingly soluble minerals (specifically iron sulfide mackinawite FeS and lead sulfide galena PbS), does it matter whether the sample reaches its target temperature (e.g. 60-90 °C) before or after the precipitant reagents are mixed? Specifically: (1) For determining equilibrium thermodynamic parameters (Ksp, Pitzer activity coefficients), does the thermal history during the initial nucleation and crystal growth phase affect the final equilibrium state? In other words, if reagents are mixed at 25 °C and then heated to 60 °C, vs. mixed at 60 °C directly, will the equilibrium precipitate identity, saturation index, and dissolved metal concentrations differ after sufficient equilibration time (e.g. 4 hours to 72 hours)? (2) Does the heating protocol (pre-mix vs. post-mix) affect precipitation kinetics — specifically nucleation rate, induction time, particle size distribution, and polymorphic form of the precipitate (e.g. amorphous FeS vs. crystalline mackinawite vs. greigite)? (3) For high-throughput screening in 96-well plates or sealed glass vials, what is the recommended practice: mix reagents at room temperature then transfer to a heating block, or pre-heat all reagents to the target temperature before mixing? (4) How broadly applicable are these findings? Are the effects of thermal history on precipitation equilibrium and kinetics relevant to other mineral systems beyond sulfides — e.g., carbonates (CaCO3), sulfates (BaSO4, SrSO4), hydroxides (Fe(OH)3), phosphates — and to other fields such as pharmaceutical crystallization, biomineralization, nanoparticle synthesis, or scale prevention in industrial water treatment? (5) What does the literature say about Ostwald's rule of stages in the context of metal sulfide precipitation — do metastable phases (amorphous FeS, nanocrystalline mackinawite) form first and then transform to more stable phases (greigite, pyrite), and does the temperature at which initial precipitation occurs affect which metastable phase forms and how quickly it transforms?

## Technical assessment: does “pre-heat then mix” vs “mix then heat” matter for FeS (mackinawite) and PbS (galena) screening?

### Summary
For *equilibrium thermodynamic* targets (Ksp and activity-coefficient/Pitzer fits), the equilibrium state at a given temperature is expected to be path-independent **only if** (i) a single, well-defined solid phase is present and (ii) the system has genuinely reached equilibrium with respect to that phase. For FeS in particular, literature indicates that early-time precipitation commonly proceeds through **metastable, nanoscale, and/or poorly crystalline FeS forms** that can persist and evolve over hours–days, shifting dissolved Fe and sulfide concentrations; in that regime, thermal history during nucleation/growth can measurably affect the *apparent* Ksp and any fitted interaction parameters. (bagander1994insitudetermination pages 1-2, bone2013mechanismsofmercury pages 57-60, bone2013mechanismsofmercury pages 64-67, theberge1997determinationofthe pages 1-4)

For *kinetics and phase selection* (induction time, nucleation rate, PSD, and polymorph), thermal history is intrinsically important because temperature controls supersaturation, nucleation barriers, and transformation rates; transient heating (mix at 25 °C then ramp to 60–90 °C) creates a moving temperature/supersaturation field that can kinetically trap phases and size distributions that may differ from direct isothermal mixing at the target temperature. (espano2023phasecontrolin pages 2-3, espano2023phasecontrolin pages 4-5, liu2017newapproachto pages 1-4)

| Topic | Key Conclusion | When Thermal History Matters | Practical Implication for HT Experiments | Supporting Sources |
| :--- | :--- | :--- | :--- | :--- |
| **1. Equilibrium Thermodynamics (Ksp, Pitzer)** | Initial precipitation history dictates intermediate metastable phases; incomplete aging shifts dissolved metal concentrations and alters apparent Ksp. | Crucial for short-to-medium equilibration times (hours to days) where initial nanoparticle size, aggregation, and metastable phase persistence dominate the measured solubility. | True equilibrium is path-independent, but "apparent" equilibrium requires very long aging. Pre-heating reagents ensures target temperatures dictate the initial metastable phase and its subsequent aging kinetics. | (bagander1994insitudetermination pages 1-2, bone2013mechanismsofmercury pages 57-60, wang2024solubilityprecipitationkinetics pages 59-64, liu2009influenceofgrain pages 15-18, liu2009influenceofsize pages 1-1) |
| **2. Kinetics, Induction, Particle Size, Polymorphism** | Temperature strongly controls initial nucleation rates, particle sizes, and the polymorphic forms. Nanoscale PbS and FeS are highly sensitive to aggregation and temperature-dependent dissolution/growth kinetics. | Highly relevant during the initial nucleation window and early crystal growth stages; ramping temperatures (mix then heat) creates a moving supersaturation target, obscuring true isothermal kinetics. | Reagents should be pre-mixed at the target temperature to avoid transient supersaturation ramps, which can trap minerals in unintended polymorphic forms or alter the particle size distribution. | (theberge1997determinationofthe pages 1-4, liu2008thenonoxidativedissolution pages 1-2, liu2009influenceofsize pages 1-1, espano2023phasecontrolin pages 2-3, liu2017newapproachto pages 1-4) |
| **3. Recommended HT Practice (96-well plates/vials)** | Controlled incubation temperature and intense mixing are critical to minimize artifacts (false positives/negatives) resulting from evaporation or variable desupersaturation. | Vital for reproducibility across wells and plates, particularly for managing evaporation, condensation, and preventing temperature gradients across the plate. | Pre-heat plates and reagents using thermocyclers/incubators before mixing. Use sealed plates with heated lids to prevent condensation and evaporation artifacts during extended heating. | (petrusevska2013evaluationofa pages 6-7, petrusevska2013evaluationofa pages 4-5, petrusevska2013evaluationofa pages 1-2, cirino2003screeningforthermostability. pages 1-4) |
| **4. Broad Applicability (Carbonates, Sulfates, Hydroxides, Pharma)** | The dependence of phase selection and kinetics on thermal history is universal; it controls CaCO3 (ACC to vaterite/calcite), BaSO4, ferrihydrite to goethite, and pharmaceutical polymorphs. | Whenever crystallization passes through amorphous aggregates or intermediate polymorphs where temperature shifts structural activation energy barriers and supersaturation. | Standardized thermal histories (including heating/cooling rates and precursor mixing temperatures) are mandatory across diverse disciplines to prevent "disappearing" or transient polymorphs. | (sarkar2010synthesisofall pages 2-6, wolf2001thermophysicalinvestigationsof pages 4-7, jones2008understandingthekinetics pages 1-2, lee2011crystalpolymorphismin pages 15-16, rodriguez‐hornedo1999significanceofcontrolling pages 1-2, rodriguezblanco2011thekineticsand pages 1-2, hiemstra2019evolutionofthe pages 1-2) |
| **5. Ostwald's Rule of Stages in FeS Precipitation** | FeS follows Ostwald's rule: amorphous FeS/cubic FeS nucleates first, then transforms to mackinawite, greigite, and eventually pyrite. | Lower temperatures (<100 °C) and fast kinetics trap metastable phases (mackinawite); higher temperatures and longer times push toward stable phases (pyrite). | To synthesize or screen specific stages, incubation time and strict isothermal control are required, as mixing at 25 °C then heating may kinetically trap a phase that directly mixing at 90 °C would bypass. | (espano2023phasecontrolin pages 2-3, espano2023phasecontrolin pages 4-5, cunhaUnknownyeartheeffectof pages 1-3) |


*Table: Summary table outlining the effects of thermal history on equilibrium thermodynamics, precipitation kinetics, and polymorph selection for mineral systems, with practical implications for high-throughput screening.*

---

## (1) Equilibrium thermodynamics: will final equilibrium differ if you heat before vs after mixing?

### FeS (mackinawite system)
**What the literature supports:**
* Iron monosulfide precipitation in aqueous systems is widely described as **kinetically controlled**, with an initially formed **non-crystalline/amorphous FeS** that can subsequently crystallize to **mackinawite and/or greigite**, and later evolve toward more stable disulfides (pyrite) under appropriate redox/sulfur conditions. (bagander1994insitudetermination pages 1-2, theberge1997determinationofthe pages 1-4, cunhaUnknownyeartheeffectof pages 1-3)
* Solubility measurements for “mackinawite” are sensitive to **aging time**, nanoparticle/colloid effects, and phase identity; aqueous Fe(II) can continue to decrease for **5–24 h** (and reported steady state can require **5–48 h**) even after rapid initial precipitation, implying that “equilibration time” is a major determinant of observed dissolved concentrations (and thus apparent Ksp). (bone2013mechanismsofmercury pages 57-60, bone2013mechanismsofmercury pages 64-67)
* Because nanoparticle size and surface energy can raise apparent solubility (and because metastable or colloidal FeS species can be mistaken for dissolved species), measured solubility can depend on the precipitation pathway and subsequent evolution, which is temperature dependent. (bone2013mechanismsofmercury pages 39-41, bone2013mechanismsofmercury pages 36-39)

**Implication for your comparison:**
*If* both protocols (mix cold→heat vs mix hot) are allowed to age long enough that the same solid phase dominates and solution compositions stop changing at the target temperature, then equilibrium dissolved concentrations should converge (thermodynamic state function). However, the available evidence indicates that for FeS this convergence can be slow and complicated by metastable solids and nanophases; therefore, for typical “high-throughput” equilibration windows (4–72 h), **thermal history can change what you *think* is equilibrium** by changing which FeS solid (or particle size population) is present and how far transformation/aging has proceeded. (bagander1994insitudetermination pages 1-2, bone2013mechanismsofmercury pages 64-67, bone2013mechanismsofmercury pages 39-41)

### PbS (galena system)
Direct FeS-like “metastable polymorph sequence” evidence for aqueous PbS precipitation was not found in the retrieved set. However, PbS dissolution/solubility and kinetics are strongly affected by **grain size, morphology, and aggregation**:
* Nanocrystalline galena dissolves **~1–2 orders of magnitude faster** than bulk galena under comparable conditions, consistent with size-dependent solubility/reactivity expectations; and aggregation can **suppress** dissolution by transport limitations in confined interparticle spaces. (liu2008thenonoxidativedissolution pages 1-2, liu2009influenceofsize pages 1-1)

**Implication:** even if the *bulk* equilibrium with macroscopic galena is path-independent, protocols that create different particle sizes/aggregation states (and thus different effective solubilities/kinetics on the experiment timescale) can yield different dissolved Pb concentrations over hours–days. (liu2008thenonoxidativedissolution pages 1-2, liu2009influenceofsize pages 1-1)

### Consequence for Ksp/Pitzer parameter estimation
Pitzer fitting assumes that the measured dissolved concentrations represent equilibrium with a known solid at the experiment temperature. If your solids are evolving (phase change and/or size-dependent apparent Ksp), the fitted parameters can absorb that evolution as “thermodynamics,” producing biased Ksp and interaction parameters. This concern is explicitly raised in FeS solubility literature through discussion of metastable solids, nanocrystal effects, and time-to-steady-state. (bone2013mechanismsofmercury pages 64-67, bone2013mechanismsofmercury pages 39-41, wang2024solubilityprecipitationkinetics pages 59-64)

---

## (2) Does heating protocol affect precipitation kinetics (nucleation, induction time, PSD, polymorph)?

### FeS
Evidence strongly supports **temperature- and kinetics-dependent phase selection** for iron sulfides:
* Ostwald-type behavior is reported: high-energy/less stable Fe–S phases can nucleate first and later transform, and kinetic trapping is facilitated by conditions that favor rapid precursor conversion at lower temperature. (espano2023phasecontrolin pages 4-5, cunhaUnknownyeartheeffectof pages 1-3)
* Precipitation rates increase with temperature (and ionic strength) in FeS precipitation kinetics studies; and transformations among FeS phases depend on temperature and solution chemistry. (liu2017newapproachto pages 1-4, wang2024solubilityprecipitationkinetics pages 36-42)

Therefore, “mix at 25 °C then heat” vs “mix at 60–90 °C” can alter:
* **Induction time / nucleation rate** (because the earliest nucleation occurs at different T and supersaturation), (wang2024solubilityprecipitationkinetics pages 36-42, liu2017newapproachto pages 1-4)
* **Particle size distribution** (temperature affects nucleation vs growth balance and subsequent aggregation/aging), (bone2013mechanismsofmercury pages 39-41, bone2013mechanismsofmercury pages 64-67)
* **Which metastable phase is trapped** early (amorphous/nanocrystalline FeS, mackinawite, greigite) and how quickly it transforms. (bagander1994insitudetermination pages 1-2, espano2023phasecontrolin pages 4-5)

### PbS
For PbS, the retrieved evidence primarily addresses dissolution rather than precipitation polymorphs, but it still implies strong pathway dependence for kinetics and size/aggregation outcomes, which will feed back onto precipitation/dissolution transients. (liu2008thenonoxidativedissolution pages 1-2, liu2009influenceofsize pages 1-1)

---

## (3) Recommended practice for high-throughput (96-well plates / sealed vials)

No retrieved mineral-specific high-throughput protocol explicitly compares “preheat then mix” vs “mix then heat.” However, high-throughput precipitation/solubility method literature in other domains converges on the same core principles: **temperature and mixing method materially affect precipitation outcomes and must be controlled and standardized**. (petrusevska2013evaluationofa pages 6-7, petrusevska2013evaluationofa pages 1-2)

### Practical recommendation (supported by the evidence base above)
For extracting thermodynamic parameters (Ksp and Pitzer):
1. **Prefer isothermal initiation** where feasible: pre-equilibrate the plate/vials and (ideally) stock solutions to the target temperature, then mix rapidly and reproducibly, to avoid temperature ramps that change early nucleation conditions. This aligns with the general observation that mixing method and incubation temperature affect precipitation behavior and assay outcomes. (petrusevska2013evaluationofa pages 6-7, petrusevska2013evaluationofa pages 4-5)
2. **Seal and control condensation/evaporation**: use sealing mats/films and a heated lid or equivalent condensation control during elevated-temperature holds; this is recommended in high-throughput heating workflows because volume changes can distort concentrations and thus solubility/thermodynamic interpretations. (cirino2003screeningforthermostability. pages 1-4)
3. **Verify equilibration operationally** (especially for FeS): measure dissolved species vs time and confirm no further change; literature indicates Fe(II) can continue to drift over many hours as suspensions age. (bone2013mechanismsofmercury pages 64-67, bone2013mechanismsofmercury pages 57-60)
4. **Characterize solids** (XRD/EXAFS/Raman/TEM) at representative timepoints to ensure you are fitting to the intended solid (e.g., mackinawite rather than amorphous FeS or a transforming mixture). The need arises directly from FeS metastability and weak XRD signals for nanoscale FeS. (bone2013mechanismsofmercury pages 33-36, bagander1994insitudetermination pages 1-2)

For kinetics screening (nucleation/induction):
*If the objective is to measure induction time or nucleation kinetics at a stated temperature,* preheating is even more important because a post-mix heating ramp makes the experiment non-isothermal and confounds extracted rate parameters. (wang2024solubilityprecipitationkinetics pages 36-42)

---

## (4) How broadly applicable are these findings?

Thermal-history effects on precipitation are broadly applicable because many systems crystallize through **metastable intermediates** and/or **amorphous precursors** whose lifetimes and transformation rates are temperature dependent:

* **Carbonates (CaCO3):** ACC transforms rapidly to vaterite and then more slowly to calcite; the pathway and kinetics depend on temperature, and different conditions can change whether intermediates appear and which polymorph results. (rodriguezblanco2011thekineticsand pages 1-2, sarkar2010synthesisofall pages 2-6)
* **Sulfates (BaSO4):** nucleation can proceed through amorphous aggregates that must restructure into ordered nuclei; that restructuring can be rate-limiting, and the phenomenon is suggested to be relevant to other divalent salts. (jones2008understandingthekinetics pages 1-2)
* **Hydroxides/oxyhydroxides (Fe(III) oxyhydroxides):** ferrihydrite evolves by Ostwald ripening with strong temperature dependence across 4–120 °C and quantified activation energy, illustrating that “aging” and surface area/solubility are thermal-history dependent. (hiemstra2019evolutionofthe pages 1-2)
* **Pharmaceutical crystallization:** metastable forms and “disappearing polymorphs” are governed by kinetic control; solution-mediated phase transformation rates depend on temperature and solubility differences, and thermal/processing history is a recognized driver of polymorph outcomes. (rodriguez‐hornedo1999significanceofcontrolling pages 1-2, lee2011crystalpolymorphismin pages 15-16)

These principles translate directly to biomineralization, nanoparticle synthesis, and scale prevention because those fields likewise operate in regimes where kinetics compete with thermodynamics and metastable intermediates can persist. (lee2011crystalpolymorphismin pages 15-16, hiemstra2019evolutionofthe pages 1-2)

---

## (5) Ostwald’s rule of stages for metal sulfides (focus on FeS)

Multiple retrieved sources explicitly support Ostwald-type sequences in iron sulfide systems:
* Amorphous FeS is described as the first precipitate, unstable, and capable of crystallizing to mackinawite and/or greigite. (bagander1994insitudetermination pages 1-2)
* Formation of amorphous FeS first, with aging to mackinawite and eventually pyrite, is described as a kinetic sequence important for Fe–S chemistry. (theberge1997determinationofthe pages 1-4)
* An explicit statement that Ostwald’s rule of stages applies to FeS→pyrite precipitation sequences is provided in the pyrite-precipitation context (sub-100 °C), with different pathways under different redox conditions (via pyrrhotite/greigite). (cunhaUnknownyeartheeffectof pages 1-3)
* Mechanistic work emphasizes that metastable phases nucleate first and then transform, and that lower temperature/faster kinetics can trap metastable Fe–S phases. (espano2023phasecontrolin pages 4-5)

### Visual support from review literature
Rickard (2025) provides tabulated and structural visual summaries consistent with the above: reactions linking mackinawite with greigite/pyrite and structural relationships among phases, supporting the plausibility of specific transformations (mackinawite↔greigite homology; more extensive rearrangement for mackinawite→pyrite). (rickard2025thechemistryof media e14bb8f8, rickard2025thechemistryof media 2ff6dd9e)

---

## Bottom line for your experimental design
1. **Equilibrium thermodynamic parameters:** in principle, equilibrium at the target temperature should not depend on whether heating occurs before or after mixing; in practice, for FeS (and potentially for PbS if nano/aggregated), metastable solids and particle-size effects can persist on 4–72 h timescales and shift dissolved concentrations, so thermal history can bias “equilibrium” measurements unless phase identity and true steady state are verified. (bone2013mechanismsofmercury pages 64-67, bagander1994insitudetermination pages 1-2, bone2013mechanismsofmercury pages 39-41)
2. **Precipitation kinetics and polymorph selection:** yes, heating protocol matters because temperature controls induction/nucleation and transformation rates; non-isothermal ramps can trap different metastable phases and PSDs than direct isothermal mixing. (espano2023phasecontrolin pages 4-5, liu2017newapproachto pages 1-4)
3. **Recommended HT practice:** standardize and tightly control temperature and mixing; for kinetics and clean thermodynamic inference, **pre-equilibrate to target temperature before mixing when feasible**, and seal/condensation-control to preserve composition. (petrusevska2013evaluationofa pages 6-7, cirino2003screeningforthermostability. pages 1-4)


References

1. (bagander1994insitudetermination pages 1-2): Lars Erik Bågander and Rolf Carman. In situ determination of the apparent solubility product of amorphous iron sulphide. Applied Geochemistry, 9:379-386, Jul 1994. URL: https://doi.org/10.1016/0883-2927(94)90060-4, doi:10.1016/0883-2927(94)90060-4. This article has 24 citations and is from a peer-reviewed journal.

2. (bone2013mechanismsofmercury pages 57-60): SE Bone. Mechanisms of mercury sequestration by nanocrystalline mackinawite (tetragonal fes). Unknown journal, 2013.

3. (bone2013mechanismsofmercury pages 64-67): SE Bone. Mechanisms of mercury sequestration by nanocrystalline mackinawite (tetragonal fes). Unknown journal, 2013.

4. (theberge1997determinationofthe pages 1-4): Stephen M. Theberge and George W. Luther III. Determination of the electrochemical properties of a soluble aqueous fes species present in sulfidic solutions. Aquatic Geochemistry, 3:191-211, Sep 1997. URL: https://doi.org/10.1023/a:1009648026806, doi:10.1023/a:1009648026806. This article has 165 citations and is from a peer-reviewed journal.

5. (espano2023phasecontrolin pages 2-3): Jeremy R. Bairan Espano and Janet E. Macdonald. Phase control in the synthesis of iron sulfides. Journal of the American Chemical Society, 145:18948-18955, Aug 2023. URL: https://doi.org/10.1021/jacs.3c05653, doi:10.1021/jacs.3c05653. This article has 27 citations and is from a highest quality peer-reviewed journal.

6. (espano2023phasecontrolin pages 4-5): Jeremy R. Bairan Espano and Janet E. Macdonald. Phase control in the synthesis of iron sulfides. Journal of the American Chemical Society, 145:18948-18955, Aug 2023. URL: https://doi.org/10.1021/jacs.3c05653, doi:10.1021/jacs.3c05653. This article has 27 citations and is from a highest quality peer-reviewed journal.

7. (liu2017newapproachto pages 1-4): Ya Liu, Zhang Zhang, Narayan Bhandari, Zhaoyi Dai, Fei Yan, Gedeng Ruan, Alex Y. Lu, Guannan Deng, Fangfu Zhang, Hamad Al-Saiari, Amy T. Kan, and Mason B. Tomson. New approach to study iron sulfide precipitation kinetics, solubility, and phase transformation. Industrial & Engineering Chemistry Research, 56:9016-9027, Jul 2017. URL: https://doi.org/10.1021/acs.iecr.7b01615, doi:10.1021/acs.iecr.7b01615. This article has 63 citations and is from a peer-reviewed journal.

8. (wang2024solubilityprecipitationkinetics pages 59-64): X Wang. Solubility, precipitation kinetics, and chemical control of iron sulfide. Unknown journal, 2024.

9. (liu2009influenceofgrain pages 15-18): J Liu. Influence of grain size, morphology and aggregation on galena dissolution. Unknown journal, 2009.

10. (liu2009influenceofsize pages 1-1): Juan Liu, Deborah M. Aruguete, Mitsuhiro Murayama, and Michael F. Hochella. Influence of size and aggregation on the reactivity of an environmentally and industrially relevant nanomaterial (pbs). Environmental science & technology, 43 21:8178-83, Oct 2009. URL: https://doi.org/10.1021/es902121r, doi:10.1021/es902121r. This article has 174 citations and is from a domain leading peer-reviewed journal.

11. (liu2008thenonoxidativedissolution pages 1-2): Juan Liu, Deborah M. Aruguete, Joerg R. Jinschek, J. Donald Rimstidt, and Michael F. Hochella. The non-oxidative dissolution of galena nanocrystals: insights into mineral dissolution rates as a function of grain size, shape, and aggregation state. Geochimica et Cosmochimica Acta, 72:5984-5996, Dec 2008. URL: https://doi.org/10.1016/j.gca.2008.10.010, doi:10.1016/j.gca.2008.10.010. This article has 147 citations and is from a domain leading peer-reviewed journal.

12. (petrusevska2013evaluationofa pages 6-7): Marija Petruševska, Uroš Urleb, and Luka Peternel. Evaluation of a high-throughput screening method for the detection of the excipient-mediated precipitation inhibition of poorly soluble drugs. Assay and drug development technologies, 11 2:117-29, Mar 2013. URL: https://doi.org/10.1089/adt.2012.466, doi:10.1089/adt.2012.466. This article has 14 citations and is from a peer-reviewed journal.

13. (petrusevska2013evaluationofa pages 4-5): Marija Petruševska, Uroš Urleb, and Luka Peternel. Evaluation of a high-throughput screening method for the detection of the excipient-mediated precipitation inhibition of poorly soluble drugs. Assay and drug development technologies, 11 2:117-29, Mar 2013. URL: https://doi.org/10.1089/adt.2012.466, doi:10.1089/adt.2012.466. This article has 14 citations and is from a peer-reviewed journal.

14. (petrusevska2013evaluationofa pages 1-2): Marija Petruševska, Uroš Urleb, and Luka Peternel. Evaluation of a high-throughput screening method for the detection of the excipient-mediated precipitation inhibition of poorly soluble drugs. Assay and drug development technologies, 11 2:117-29, Mar 2013. URL: https://doi.org/10.1089/adt.2012.466, doi:10.1089/adt.2012.466. This article has 14 citations and is from a peer-reviewed journal.

15. (cirino2003screeningforthermostability. pages 1-4): Patrick C. Cirino and Radu Georgescu. Screening for thermostability. Methods in molecular biology, 230:117-25, 2003. URL: https://doi.org/10.1385/1-59259-396-8:117, doi:10.1385/1-59259-396-8:117. This article has 22 citations and is from a peer-reviewed journal.

16. (sarkar2010synthesisofall pages 2-6): Arpita Sarkar and Samiran Mahapatra. Synthesis of all crystalline phases of anhydrous calcium carbonate. Crystal Growth & Design, 10:2129-2135, Apr 2010. URL: https://doi.org/10.1021/cg9012813, doi:10.1021/cg9012813. This article has 152 citations and is from a domain leading peer-reviewed journal.

17. (wolf2001thermophysicalinvestigationsof pages 4-7): Gert Wolf and C. Günther. Thermophysical investigations of the polymorphous phases of calcium carbonate. Journal of Thermal Analysis and Calorimetry, 65:687-698, Sep 2001. URL: https://doi.org/10.1023/a:1011991124181, doi:10.1023/a:1011991124181. This article has 91 citations and is from a peer-reviewed journal.

18. (jones2008understandingthekinetics pages 1-2): F. Jones, S. Piana, and J. D. Gale. Understanding the kinetics of barium sulfate precipitation from water and water–methanol solutions. Crystal Growth & Design, 8:817-822, Jan 2008. URL: https://doi.org/10.1021/cg070110i, doi:10.1021/cg070110i. This article has 58 citations and is from a domain leading peer-reviewed journal.

19. (lee2011crystalpolymorphismin pages 15-16): Alfred Y. Lee, Deniz Erdemir, and Allan S. Myerson. Crystal polymorphism in chemical process development. Annual Review of Chemical and Biomolecular Engineering, 2:259-280, Jul 2011. URL: https://doi.org/10.1146/annurev-chembioeng-061010-114224, doi:10.1146/annurev-chembioeng-061010-114224. This article has 511 citations and is from a peer-reviewed journal.

20. (rodriguez‐hornedo1999significanceofcontrolling pages 1-2): Naír Rodríguez‐hornedo and Denette Murphy. Significance of controlling crystallization mechanisms and kinetics in pharmaceutical systems. Journal of pharmaceutical sciences, 88 7:651-60, Jul 1999. URL: https://doi.org/10.1021/js980490h, doi:10.1021/js980490h. This article has 514 citations and is from a domain leading peer-reviewed journal.

21. (rodriguezblanco2011thekineticsand pages 1-2): Juan Diego Rodriguez-Blanco, Samuel Shaw, and Liane G. Benning. The kinetics and mechanisms of amorphous calcium carbonate (acc) crystallization to calcite, via vaterite. Nanoscale, 3 1:265-71, Jan 2011. URL: https://doi.org/10.1039/c0nr00589d, doi:10.1039/c0nr00589d. This article has 1274 citations and is from a highest quality peer-reviewed journal.

22. (hiemstra2019evolutionofthe pages 1-2): Tjisse Hiemstra, Juan C. Mendez, and Jiayu Li. Evolution of the reactive surface area of ferrihydrite: time, ph, and temperature dependency of growth by ostwald ripening. Environmental Science: Nano, 6:820-833, Mar 2019. URL: https://doi.org/10.1039/c8en01198b, doi:10.1039/c8en01198b. This article has 105 citations.

23. (cunhaUnknownyeartheeffectof pages 1-3): RN Cunha, RMZ Castro, MM Seckler, and SDF Rocha. The effect of silica, ph and temperature on pyrite precipitation. Unknown journal, Unknown year.

24. (bone2013mechanismsofmercury pages 39-41): SE Bone. Mechanisms of mercury sequestration by nanocrystalline mackinawite (tetragonal fes). Unknown journal, 2013.

25. (bone2013mechanismsofmercury pages 36-39): SE Bone. Mechanisms of mercury sequestration by nanocrystalline mackinawite (tetragonal fes). Unknown journal, 2013.

26. (wang2024solubilityprecipitationkinetics pages 36-42): X Wang. Solubility, precipitation kinetics, and chemical control of iron sulfide. Unknown journal, 2024.

27. (bone2013mechanismsofmercury pages 33-36): SE Bone. Mechanisms of mercury sequestration by nanocrystalline mackinawite (tetragonal fes). Unknown journal, 2013.

28. (rickard2025thechemistryof media e14bb8f8): David Rickard. The chemistry of tetragonal fes. Chemical Reviews, 126:799-840, Nov 2025. URL: https://doi.org/10.1021/acs.chemrev.5c00763, doi:10.1021/acs.chemrev.5c00763. This article has 2 citations and is from a highest quality peer-reviewed journal.

29. (rickard2025thechemistryof media 2ff6dd9e): David Rickard. The chemistry of tetragonal fes. Chemical Reviews, 126:799-840, Nov 2025. URL: https://doi.org/10.1021/acs.chemrev.5c00763, doi:10.1021/acs.chemrev.5c00763. This article has 2 citations and is from a highest quality peer-reviewed journal.
