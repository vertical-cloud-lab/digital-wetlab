# CV Assessment for ACS PRF DNI Proposal

> **Context:** ACS PRF Doctoral New Investigator (DNI) proposal — "Systematic Experimental Validation of Pitzer Activity-Coefficient Models for Sulfide-Scale Precipitation in Produced-Water Brines"
>
> **Review criterion #5 (of 5):** *"Qualifications of the PI and adequacy of facilities"*

---

## 1. How the CV Will Come Across to Reviewers

### Overall Impression

The CV presents a highly productive early-career researcher with an impressive publication record (30+ papers), extensive experience building and operating automated laboratory platforms, and demonstrated Bayesian optimization expertise. However, reviewers on the ACS PRF Inorganic Chemistry panel will immediately notice that **the PI's entire research background is in materials science, machine learning, and self-driving labs — with no publications, prior funding, or stated expertise in aqueous geochemistry, electrolyte thermodynamics, Pitzer models, or petroleum-related chemistry.** This creates a "domain mismatch" that reviewers will likely flag as a risk.

### What Reviewers Will Think

ACS PRF panels comprise discipline experts — for Panel 3 (Inorganic Chemistry) and Panel 9 (Chemical & Petroleum Engineering), reviewers will be aqueous chemists, geochemists, and scale specialists. They will evaluate the CV against the specific technical demands of the proposal:

1. **"Can this PI actually do Pitzer-model thermodynamics?"** — The CV shows no thermodynamics coursework, no publications involving activity coefficients, no experience with PHREEQC or equivalent geochemical modeling software. Reviewers will worry that the PI is underestimating the complexity of electrolyte solution thermodynamics.

2. **"Has the PI ever worked with sulfide chemistry?"** — No. The closest experience is general glovebox operation and synthesis listed under Skills, but nothing specific to H₂S-bearing solutions, iron sulfide precipitation, or lead chemistry.

3. **"Is this genuinely a new direction?"** — Yes, clearly. The DNI program rewards newness, and this proposal is unambiguously different from the PI's graduate/postdoctoral work. This is a **strength** for the "Newness" criterion (#3 of 5) but becomes a **risk** for "Qualifications" (#5).

4. **"What about the automation angle?"** — Reviewers will recognize the PI's automation and liquid-handling expertise as a genuine asset. The OT-2 experience, lab-building track record ($600k, 500 line items), and hardware API development are directly relevant to Aim 1.

5. **"Is the PI established in the new position?"** — The PI joined BYU as an Assistant Professor in December 2025; reviewers will look for evidence that the PI can launch the lab and sustain the project over the 2-year grant period. The prior lab-building track record helps here.

---

## 2. Strengths That Support the Proposal

### A. Automated Experimentation Expertise (★ key differentiator)
- Built the AC Dev Lab from scratch ($600k of equipment, 500 line items) — directly demonstrates ability to set up the proposed OT-2 workflow
- Developed dozens of automation hardware APIs and tools (solid dosing, sample transfer)
- Supervised OT-2-based co-precipitation projects (liquid-liquid extraction, drug discovery lab liaisons)
- The proposal's Aim 1 is fundamentally an automation challenge, and the PI is uniquely qualified for this

### B. Bayesian Optimization Track Record (★ directly cited in proposal)
- Published the CrabNet/SAASBO paper (Baird et al. 2022) that is cited in the proposal as evidence that high-dimensional BO works for 23+ parameters
- Developed Honegumi (interactive BO script generator for materials science)
- Organized a BO hackathon (120 participants, 62 organizations, 14 countries)
- Leveraged BO for battery slurry optimization and electrolysis cell applications
- This expertise is a genuine and credible strength for the adaptive follow-up in Aim 1

### C. Productive Publication Record
- 30+ peer-reviewed publications (including Chemical Reviews, Matter, Digital Discovery, JOSS)
- Demonstrates ability to execute and publish research at high volume
- Several first-author publications showing independent research capability

### D. Student Mentorship
- Currently supervising 8 undergraduate research assistants at BYU
- Previously supervised 8 students as lab liaisons and 12 staff on research projects
- Mentored visiting PhD researchers, undergraduates (accepted to Stanford, Yale)
- Directly supports the "Student education" criterion (#2 of 5)

### E. Grant Experience
- PI or co-PI on NSF EAGER ($200k), industry contract ($34k)
- Demonstrates ability to manage funded research projects

### F. Hardware and Synthesis Skills
- Glovebox operation and maintenance (relevant for Fe²⁺ anaerobic campaigns)
- Furnace design, CVD, photolithography, SEM, XRD — broad experimental capability
- Automated liquid handling and solid dosing listed explicitly

---

## 3. Weaknesses and Gaps Reviewers Will Identify

### A. No Aqueous/Electrolyte Chemistry Background (⚠ critical gap)
- Zero publications in aqueous chemistry, geochemistry, or solution thermodynamics
- No evidence of experience with Pitzer models, PHREEQC, or activity-coefficient calculations
- No coursework listed in aqueous geochemistry or electrolyte theory
- **Reviewer concern:** The PI may underestimate the difficulty of correctly implementing Pitzer-model regression, handling speciation coupling, or interpreting deviations in the context of existing electrolyte literature

### B. No Petroleum/Geochemistry Experience (⚠ critical for ACS PRF)
- The CV contains no petroleum-related research, no oilfield chemistry, no scale-related work
- ACS PRF reviewers specifically evaluate petroleum relevance
- **Reviewer concern:** The PI may not appreciate the practical realities of produced-water chemistry or the extensive existing literature on scale prediction

### C. No Inorganic Chemistry Publications (⚠ for Panel 3)
- If submitting to Panel 3 (Inorganic Chemistry), the CV shows no traditional inorganic chemistry work
- The research is primarily materials informatics, ML, grain boundaries, batteries
- **Reviewer concern:** Misfit between the PI's expertise and the proposal's disciplinary requirements

### D. Very Early Career — Only ~3 Months as Faculty
- Started at BYU December 2025; at time of submission will have been faculty for ~3 months
- No students graduated under supervision yet
- No independent lab established yet (though the proposal indicates the lab is being set up)
- **Reviewer concern:** Can the PI realistically launch this unfamiliar research direction within the grant period?

### E. No Preliminary Data in the Proposed Area
- The DNI program explicitly states "limited or no preliminary results are expected" — so this is somewhat mitigated
- However, even a simple PHREEQC calculation showing the gap (e.g., the Davies vs. Pitzer comparison mentioned in the proposal) would strengthen credibility
- **Reviewer concern:** Without even basic scoping experiments, how confident is the PI in the feasibility?

### F. Publication List Is Not Curated for This Proposal
- The CV lists every publication regardless of relevance, which dilutes the signal
- A reviewer scanning for relevant expertise will not find it among ML/materials informatics papers
- The most relevant publications (Velasco 2021 OT-2 co-precipitation, BO work) are buried

---

## 4. Specific Suggestions for Improving the CV

### High Priority

1. **Add a "Research Statement" or "Relevant Expertise" section** at the top of the CV (1–2 paragraphs) that explicitly connects the PI's skills to the proposed research:
   - Automated liquid-handling and OT-2 operation
   - High-throughput experimental design (Latin hypercube, Bayesian optimization)
   - Statistical modeling and parameter regression
   - Glovebox operation for air-sensitive chemistry
   - Emphasize the *methodology transfer* framing: "bringing high-throughput screening methods to aqueous geochemistry problems"

2. **Highlight the most relevant publications** — consider grouping or annotating publications that directly support the proposal:
   - Baird et al. 2022 (SAASBO/CrabNet — 23-parameter BO)
   - Tom et al. 2024 (Chemical Reviews — self-driving labs, including liquid-handling)
   - Baird & Sparks 2023 (STAR Protocols — "Hello World" for self-driving labs)
   - Lo et al. 2024 (Low-cost self-driving labs)
   - Velasco et al. 2021 and Kumbhakar et al. 2023 are cited in the proposal but are not the PI's own papers

3. **Add any relevant coursework or self-study** — If the PI has taken any coursework in aqueous chemistry, thermodynamics, or geochemistry (even audited or online), list it. If not, consider listing planned coursework or reading (less ideal but better than nothing).

4. **List PHREEQC or geochemical modeling** under Skills if the PI has used it, even briefly. If not yet proficient, consider spending a few hours running basic PHREEQC calculations before submission — this allows honestly listing it as a skill.

5. **Reduce the Presentations section** — The current CV lists 30+ presentations, many from 2016–2018 on batteries and carbon nanotubes. These consume space and signal irrelevant expertise. Keep only the most recent and relevant presentations (e.g., the MRS 2025 talk, SDL-related talks). A biosketch for ACS PRF should be concise and focused.

### Medium Priority

6. **Tailor the Skills section** — Move "Automated liquid handling" and "Glovebox operation & maintenance" to the top of the Synthesis skills. Add "PHREEQC thermodynamic modeling" and "Latin hypercube sampling / Design of Experiments" if applicable. Remove or de-emphasize skills that signal a different research direction (e.g., "Bambu Studio (FDM printing)", "MicroPython", "AprilTag").

7. **Add a "Collaborators" or "Consultants" section** — If the PI has identified a geochemistry or Pitzer-model expert who will serve as an informal advisor (even unfunded), listing this on the CV dramatically mitigates the domain-expertise concern. Names from the proposal references (e.g., someone from the Kan, Wang, or Felmy groups) would be ideal.

8. **Reformat for ACS PRF expectations** — The current CV is comprehensive (8+ pages). ACS PRF biosketches are typically 2–3 pages. Create a condensed version that prioritizes:
   - Education
   - Current and relevant positions
   - 10–15 most relevant publications
   - Relevant grants
   - Relevant skills and equipment access

### Lower Priority

9. **Add equipment/facilities statement** — List the specific equipment available at BYU for this project (OT-2, glovebox, fume hood, plate reader access, ICP-OES access). This can be in the CV or as a separate facilities page.

10. **Remove or shorten the Community Contributions section** — GitHub stats (15k commits, 1.5k issues) signal software engineering rather than chemistry. While impressive, they may not resonate with inorganic chemistry reviewers.

---

## 5. Addressing CV Weaknesses in the Proposal

These strategies can be implemented in the proposal text to preemptively address concerns that reviewers will have after reading the CV.

### Strategy 1: Frame the Methodological Gap, Not the Domain Gap

The proposal should emphasize that the **bottleneck in this field is not domain knowledge but experimental throughput and systematic data collection.** The Pitzer framework is well-established (textbook-level theory) — what's missing is data. The PI brings the experimental methodology (automation, BO, high-throughput screening) to generate that data systematically. Frame it as:

> *"The theoretical framework for regressing Pitzer parameters is well-established [refs]. What has been lacking is a systematic, high-throughput experimental approach to generate the comprehensive solubility data required for parameter regression in sulfide systems. The PI's expertise in automated experimentation and adaptive experimental design directly addresses this methodological gap."*

### Strategy 2: Cite Precedent for Cross-Disciplinary DNI Proposals

The ACS PRF DNI explicitly rewards "newness" — research that is a new direction for the PI. The proposal could include a brief statement acknowledging the interdisciplinary nature:

> *"This project represents a new research direction for the PI, whose prior work focused on automated experimentation and Bayesian optimization in materials science. The ACS PRF DNI is specifically designed to seed new research directions, and the PI's expertise in high-throughput experimental design and adaptive optimization is uniquely suited to address the data-generation bottleneck in electrolyte solution thermodynamics."*

### Strategy 3: Name a Domain Expert Collaborator or Advisor

Even without formal funding, identifying an aqueous geochemistry expert who has agreed to provide informal guidance would substantially mitigate the domain-expertise concern. This could be:
- A colleague at BYU in Chemistry, Chemical Engineering, or Geological Sciences
- A researcher from the Pitzer/geochemistry community who would be willing to answer occasional questions
- Even a statement like *"The PI has consulted with Prof. [X] at [University], who confirmed the approach's feasibility and offered guidance on PHREEQC parameterization"* would help

### Strategy 4: Demonstrate Basic Domain Competence in the Proposal

The proposal text already demonstrates strong domain understanding (correct terminology, appropriate references, well-formulated hypothesis). Strengthen this by:
- Including 1–2 PHREEQC calculation results as preliminary data (even as supplementary)
- Showing the specific gap (e.g., a table comparing available vs. missing Pitzer parameters for sulfide systems)
- Referencing the correct primary literature sources (Pitzer 1973, Harvie & Weare 1980, etc.)

### Strategy 5: Emphasize the Automation Expertise as Essential

Most geochemists who study Pitzer models do not have access to or expertise with automated liquid-handling platforms. The proposal should make clear that:
- 30,000 experiments across a 5-dimensional parameter space is **not feasible manually**
- The PI's lab-building experience ($600k facility, OT-2 operation, Python API development) uniquely enables this approach
- The combination of automation expertise + established Pitzer theory = tractable research plan

### Strategy 6: Leverage the Student Training Angle

ACS PRF heavily weights student education (criterion #2). The CV shows strong mentorship credentials. In the proposal:
- Emphasize that students will receive cross-disciplinary training (aqueous chemistry + automation + computation)
- Note that BYU has strong undergraduate research culture
- Point out that the PI has supervised 8 undergrads and 12 staff — demonstrating capacity for the proposed team

### Strategy 7: Address the "Too New" Timeline Concern

For a PI who started in December 2025 with a March 2026 submission:
- Note that the OT-2 and glovebox are standard equipment items that can be procured quickly
- Highlight that the PI built a $600k lab in a previous position, demonstrating rapid setup capability
- Mention any startup funds or institutional support that will provide equipment independently of this grant
- The July 2026 start date gives 7 months after appointment to prepare

---

## 6. Summary: Risk Matrix for Reviewers

| Aspect | Strength/Risk | Mitigation |
|--------|--------------|------------|
| Automation expertise | ★★★ Strong | Central to proposal feasibility |
| Bayesian optimization | ★★★ Strong | Directly cited in proposal |
| Publication record | ★★★ Strong | Demonstrates productivity |
| Student mentorship | ★★☆ Good | Supports criterion #2 |
| Aqueous geochemistry | ⚠⚠⚠ Critical gap | Domain advisor, proposal framing |
| Pitzer model expertise | ⚠⚠⚠ Critical gap | PHREEQC preliminary calcs, domain advisor |
| Petroleum relevance in CV | ⚠⚠ Moderate gap | Proposal framing, new direction |
| Faculty tenure length | ⚠ Minor concern | Lab-building track record |
| Preliminary data | ⚠ Minor concern | DNI expects minimal prelim data |

### Bottom Line

The CV's greatest risk is the complete absence of aqueous/electrolyte chemistry credentials. To maximize the proposal's competitiveness, the PI should: **(1)** condense the CV to 2–3 pages focused on relevant expertise, **(2)** add a brief research relevance statement connecting automation skills to the proposed work, **(3)** identify an informal domain advisor in geochemistry, and **(4)** use the proposal text to frame the PI's methodology expertise as the critical missing ingredient for this well-defined thermodynamics problem.

---

## 7. Potential BYU Unofficial Advisors

The following BYU faculty could serve as informal domain advisors to mitigate the aqueous geochemistry expertise gap. Even an unfunded advisory role — mentioned briefly in the proposal as *"The PI has consulted with Prof. X regarding..."* — would substantially strengthen reviewer confidence.

### Tier 1: Strongest Fit

#### Dean Wheeler — Chemical & Biological Engineering (Dept. Chair)
- **Why:** Electrolyte thermodynamics and Pitzer-model expertise directly relevant to the proposal. His research group works on concentrated electrolyte solution modeling, activity coefficients, and thermodynamic properties at high ionic strength — the exact theoretical framework underpinning this proposal. Also in the College of Engineering (same college as the PI), making collaboration natural.
- **Relevance to proposal:** Pitzer equations, activity-coefficient modeling, electrolyte solution thermodynamics, statistical mechanics of concentrated solutions.
- **Contact:** [cbe.byu.edu/directory/dean-r-wheeler](https://cbe.byu.edu/directory/dean-r-wheeler)

#### Josh LeMonte — Geological Sciences (Asst. Professor)
- **Why:** Environmental geochemist specializing in metal and sulfide cycling, speciation, and transport. Uses synchrotron X-ray spectroscopy (XAS) for molecular-scale metal-sulfide speciation — directly relevant to understanding FeS and PbS precipitation products. Also a fellow early-career faculty member, making peer collaboration natural. Studies the Great Salt Lake (high-salinity brine system) and metal mobilization in extreme environments.
- **Relevance to proposal:** Metal-sulfide geochemistry, speciation of sulfide-bound metals, environmental metal cycling, synchrotron characterization of precipitates.
- **Contact:** [geology.byu.edu/directory/joshua-j-lemonte](https://geology.byu.edu/directory/joshua-j-lemonte)

### Tier 2: Strong Fit

#### Barry Bickmore — Geological Sciences (Professor)
- **Why:** Mineral surface geochemistry and aqueous thermodynamics expert. PhD from Virginia Tech in mineral surface geochemistry. Research on mineral-solution interactions, dissolution kinetics, and surface complexation modeling. Senior faculty with strong publication record. Teaches geochemistry courses at BYU.
- **Relevance to proposal:** Mineral-water interface chemistry, aqueous thermodynamics, dissolution/precipitation equilibria, surface complexation.
- **Contact:** [geology.byu.edu/directory/barry-bickmore](https://geology.byu.edu/directory/barry-bickmore)

#### Greg Carling — Geological Sciences (Professor, Assoc. Chair)
- **Why:** Geochemistry of surface and groundwater, trace element cycling, hydrogeology. Works on water-mineral interactions in natural systems. Could advise on natural brine geochemistry and field-relevant conditions.
- **Relevance to proposal:** Water chemistry, trace metal geochemistry, natural brine systems, environmental geochemistry.
- **Contact:** [geology.byu.edu/directory/greg-carling](https://geology.byu.edu/directory/greg-carling)

### Tier 3: Supplementary Fit

#### Roger G. Harrison — Chemistry & Biochemistry (Professor, Inorganic)
- **Why:** Inorganic chemist working on metal-ligand interactions, H₂S trapping by ZnO-zeolites, and environmental metal detection. Could advise on inorganic precipitation chemistry and metal-sulfide interactions from a synthetic/molecular chemistry perspective.
- **Relevance to proposal:** Metal-sulfide interactions, inorganic precipitation chemistry, H₂S chemistry.
- **Contact:** [chem.byu.edu/department/faculty/](https://chem.byu.edu/department/faculty/)

### Recommended Approach

1. **Start with Dean Wheeler** — his Pitzer/electrolyte thermodynamics expertise is the most direct match to the proposal's theoretical framework, and he's in the same college. A brief conversation about the feasibility of regressing 34 Pitzer parameters from binary precipitation data would be invaluable and could be referenced in the proposal.

2. **Also contact Josh LeMonte** — his metal-sulfide geochemistry and synchrotron XAS expertise could strengthen both the experimental design (correct handling of FeS/PbS precipitation products) and future directions (phase identification of precipitates). As a fellow early-career faculty member, a collaboration could be mutually beneficial.

3. **For the proposal text**, even a single sentence like *"The PI has consulted with Prof. Dean Wheeler (BYU Chemical Engineering), an expert in electrolyte solution thermodynamics, who confirmed the feasibility of the proposed Pitzer parameter regression approach"* would directly address the #1 reviewer concern about domain expertise.
