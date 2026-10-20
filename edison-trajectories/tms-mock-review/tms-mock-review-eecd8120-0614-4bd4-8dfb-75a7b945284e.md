## Mock review panel feedback

### Reviewer A: industrial hydrometallurgist

**Score**
- Fit to symposium scope: **7/10**
- Technical quality of abstract: **7/10**
- Likely audience interest: **6/10**

**Review**
This is within scope because the symposium explicitly includes hydrometallurgical solution chemistry, impurity management, thermodynamic modeling, and AI-enabled processing. The Fe/Pb sulfide chemistry is relevant to impurity control and possibly Pb processing, but the current abstract spends too much of its first impression on petroleum brines and the autonomous wet lab. For this audience, lead with metallurgical process-water chemistry, sulfide precipitation control, and model gaps that affect plant decisions. The robot is useful, but it should not be the headline. I would support this as a poster if the authors frame it as early-stage platform validation plus initial precipitation-boundary data, not as a finished parameter set.

### Reviewer B: academic extractive-metallurgy professor

**Score**
- Fit to symposium scope: **8/10**
- Technical quality of abstract: **8/10**
- Likely audience interest: **7/10**

**Review**
The abstract maps well onto leaching/solution chemistry, thermodynamic modeling, reagent effects, and automated experimentation. It is especially appealing as a poster because the platform, design-of-experiments strategy, and early boundary maps could be shown visually. The title, however, reads more like a self-driving-lab methods poster than an extractive metallurgy poster. I would make “hydrometallurgical brines,” “sulfide precipitation,” and “Pitzer/PHREEQC” more visible. The abstract should also specify what will be available by March 2027: platform validation, reproducibility, and initial FeS/PbS precipitation-boundary data. Avoid implying that the 30,000-experiment campaign and full parameter regression are complete.

### Reviewer C: thermodynamics/modeling skeptic

**Score**
- Fit to symposium scope: **6/10**
- Technical quality of abstract: **6/10**
- Likely audience interest: **6/10**

**Review**
The problem is real: Pitzer parameter gaps for sulfide and metal-organic systems can limit prediction in concentrated brines. But the abstract currently overclaims. “The result is a validated framework” sounds like completed validation, while the provided context says the full parameter set is a future deliverable. I would want to see calibration strategy, temperature control, reproducibility, pH accuracy in high-ionic-strength media, sulfide oxidation control, and whether image-based precipitation detection can support quantitative parameter fitting rather than only qualitative boundary classification. The phrase “deviations from PHREEQC Pitzer predictions drive regression” is plausible, but parameter identifiability across ~48 unknowns is a major concern. For acceptance, soften the claims and make the experimental validation plan explicit.

## Specific line edits to improve acceptance likelihood

### Title

**Current title**
Closed-Loop Mapping of Iron and Lead Sulfide Precipitation in Concentrated Brines Using a Low-Cost Autonomous Digital Wet Lab

**Problem**
The title foregrounds “closed-loop” and “digital wet lab,” which may feel like AI/robotics jargon. It does not immediately tell the extraction audience why this matters.

**Better title options**
1. **Autonomous Mapping of Iron and Lead Sulfide Precipitation for Hydrometallurgical Brine Chemistry**
2. **Automated FeS and PbS Precipitation Mapping to Improve Pitzer Modeling of Concentrated Hydrometallurgical Brines**
3. **Mapping FeS and PbS Precipitation Boundaries in Concentrated Brines for Hydrometallurgical Impurity Control**

My preferred version is option 2 if the poster emphasizes modeling, or option 3 if it emphasizes process relevance.

### Abstract wording changes

**Change petroleum-first framing**
- Replace: “and causes flow-restricting scale during petroleum production”
- With: “and complicates process-water chemistry in concentrated metallurgical brines”

Petroleum/oilfield-scale framing **mostly hurts** for this symposium if it appears in the opening sentence. It makes the work look adjacent to extractive metallurgy rather than inside it. Keep at most one phrase later, such as “including produced-water analog brines,” only if needed to justify the chemistry space. For this submission, I would remove the oilfield framing from the abstract body.

**Make hydrometallurgy concrete without overclaiming**
- Replace: “governs impurity control and metal recovery”
- With: “affects impurity control, metal recovery, and process-water chemistry in hydrometallurgical operations”

This is concrete but not too strong. “Governs” may overstate the role of FeS/PbS precipitation across all circuits.

**Reduce robot-centered language**
- Replace: “We present a low-cost digital wet laboratory that addresses this gap through autonomous, closed-loop experimentation.”
- With: “We will present an Opentrons-based autonomous precipitation-mapping platform designed to generate reproducible boundary data for thermodynamic model assessment.”

This makes the robot a means to a metallurgical chemistry endpoint.

**Clarify stage of work**
- Replace: “The result is a validated framework…”
- With: “Early results will emphasize platform validation, reproducibility, and initial FeS/PbS precipitation-boundary data rather than a completed parameter database.”

This is the most important line edit. It prevents a reviewer from dinging the abstract for presenting proposed work as completed results.

**Add temperature-control credibility**
- Replace: “temperature (25–90 °C)”
- With: “25–90 °C using temperature-controlled reaction staging”

This does not fully prove the method, but it signals that temperature control has been considered.

**De-jargon the methods**
- Replace: “digital wet laboratory” with “autonomous precipitation-mapping platform”
- Replace: “closed-loop experimentation” with “Latin hypercube sampling with active learning” or “adaptive experimental design”
- Avoid “SDL” unless expanded and immediately tied to the chemistry.

## Red flags an organizer or reviewer might ding

- **Proposal-stage overclaiming:** The current sentence “The result is a validated framework…” reads as if the campaign and model validation are complete. The context says only platform and early campaign results are expected by March 2027.
- **Robot upstaging the chemistry:** “Low-cost autonomous digital wet lab” is prominent in the title and abstract. For this symposium, the chemistry and hydrometallurgical relevance should lead.
- **Temperature control from 25–90 °C:** A standard liquid handler does not automatically imply credible 90 °C operation. Mention temperature-controlled reaction staging or an external heated module, and be prepared to show calibration.
- **Image-based detection limits:** Image detection may identify precipitation boundaries, but parameter fitting needs reproducibility, threshold validation, and probably confirmatory measurements for selected points.
- **Pitzer parameter identifiability:** ~48 missing parameters is a lot. A skeptical thermodynamics reviewer will ask whether the campaign can uniquely estimate them, especially with correlated variables and boundary-only data.
- **High-ionic-strength pH measurement:** Automated pH in 0.5–5 molal brines requires careful calibration and junction-potential awareness.
- **Sulfide chemistry stability:** Fe2+/HS- systems are sensitive to oxidation, volatilization/speciation, and pH. The abstract does not mention atmosphere or sulfide handling.
- **Scope drift:** Petroleum produced-water framing makes the work look less central to a mine-to-refinery symposium. Keep the focus on hydrometallurgical brines, impurity control, Pb-containing streams, and solution chemistry.
- **Jargon:** “digital wet lab,” “closed-loop,” and “active learning” are acceptable if tied to experimental design, but too much AI language may weaken fit with the extraction audience.

## Revised version

**Revised title**
Automated FeS and PbS Precipitation Mapping to Improve Pitzer Modeling of Concentrated Hydrometallurgical Brines

**Revised abstract, 129 words**
Iron and lead sulfide precipitation affects impurity control, metal recovery, and process-water chemistry in hydrometallurgical operations, but concentrated-brine thermodynamic models remain limited by missing Pitzer interactions for Fe2+–HS-, Pb2+–HS-, and metal–organic-acid complexes. We will present an Opentrons-based autonomous precipitation-mapping platform with automated pH measurement, temperature-controlled reaction staging, and image-based detection of FeS/PbS formation. The campaign combines Latin hypercube sampling with active learning to map precipitation boundaries across ionic strength (0.5–5 molal), pH 4–9, 25–90 °C, and acetate/propionate concentration, then compares boundary shifts with PHREEQC Pitzer predictions to identify parameter gaps. Early results will emphasize platform validation, reproducibility, and initial FeS/PbS boundary data rather than a completed parameter database. The work aims to provide practical solution-chemistry data for sulfide precipitation control and a low-cost template for automated hydrometallurgical experiments.

## Bottom line

**Verdict for this symposium as a poster: revise, then likely accept.** The single highest-impact change is to reframe the abstract around hydrometallurgical sulfide precipitation and early validation results, not around petroleum scaling or a completed autonomous parameter-generation campaign.

**Backup symposiums**
- **Rare Metal Extraction & Processing:** Probably not better unless the abstract is reframed around Pb, Bi, Te, rare earth, or precious-metal process streams. Current Fe/Pb sulfide-brine modeling is only a partial fit.
- **AI-Enabled Materials Processing:** Could score better on methods novelty, especially autonomous experimentation and active learning, but the chemistry may feel too narrow unless the poster foregrounds the closed-loop platform.
- **Advances in Recycling and Environmental Technologies:** Could fit if framed around process-water treatment, sulfide precipitation, impurity removal, or brine reuse, but that would require application claims not yet demonstrated. For the current abstract, the Shijie Wang symposium remains the better target after revision.

## Discretionary decisions

- Treated the submission as a **poster** rather than an oral/proceedings paper, so I allowed early-stage platform validation as acceptable if clearly labeled.
- Weighted fit toward the provided symposium scope: hydrometallurgy, solution chemistry, impurity control, thermodynamic modeling, and AI applications.
- Recommended removing most petroleum/oilfield framing because multiple valid framings exist, but the target audience is extractive metallurgy.
- Chose a revised title that foregrounds **Pitzer modeling and hydrometallurgical brines** rather than autonomous-lab novelty.
- Kept the revised abstract below 150 words and explicitly stated that the parameter database is not complete.
- Used “aims to provide” rather than “provides” to avoid overclaiming future deliverables.
- Retained Latin hypercube sampling and active learning because they support technical credibility, but reduced self-driving-lab jargon.