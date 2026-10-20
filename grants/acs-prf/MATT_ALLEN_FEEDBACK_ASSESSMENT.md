# Matt Allen Feedback Assessment

**Source:** `drafts/summary-of-comments-matt-allen-feedback.pdf` (annotated proposal with sticky notes and highlights)
**Date of feedback:** March 30, 2026
**Related feedback:** Barry Bickmore (#51), Milad Abolhasani (#24, closed)

---

## Summary of Matt Allen's Comments

### Comment 1 — Abstract tense/voice (Page 1, Sticky Note)
> *(Paraphrased)* Use proposal language ("we propose to") so the work does not read as already completed.

**Context:** The abstract's second paragraph opens with "This project determines these parameters through systematic high-throughput experiments" and "we map FeS and PbS precipitation boundaries." These present-tense constructions read as if the work is already complete rather than proposed.

**Assessment:** Valid. A proposal should use future/proposal language ("we propose to," "we will") to clearly convey that the work has not yet been performed.

**Action:** Changed "This project determines" → "We propose to determine" and "we map" → "we will map" in the abstract. Similar present-tense constructions in the body are appropriate since they describe the planned methodology.

---

### Comment 2 — Basic vs. applied science framing (Page 1, Sticky Note)
> *(Paraphrased)* Asked whether the framing suits a basic-science program or reads as more application-oriented.

**Context:** The abstract and introduction emphasize petroleum-industry applications (scale prediction tools, produced-water brines, equipment fouling). The proposal was submitted to ACS PRF Panel 2 (Geochemistry and Biogeochemical Cycling), not a purely basic science panel, but ACS PRF program managers are strict about fundamental science content (per Milad's feedback, #24).

**Assessment:** Important observation. While the proposal targets Panel 2 (which accepts petroleum-relevant research), the framing should still foreground the fundamental science contribution. Milad's prior feedback (#24) stressed clearly stating the fundamental science aspect, since program managers are strict about it.

**Action:** Strengthened the fundamental science framing in the introduction's closing paragraph. The fundamental contribution is determining unmeasured thermodynamic interaction parameters—this is basic physical chemistry. The petroleum context provides motivation, not the research question itself.

---

### Comment 3 — Novelty and timeliness (Page 2, Sticky Note)
> *(Paraphrased)* Asked how new this type of model is, and whether it has only recently become feasible with ML and automated labs.

**Context:** Refers to the Pitzer ion-interaction model description in the introduction. The Pitzer model itself dates to 1973, but systematic parameterization for sulfide systems has never been done.

**Assessment:** Excellent suggestion. The proposal should explicitly address why this work is timely *now*. The Pitzer model is well-established, but determining ~48 parameters for sulfide systems requires systematic variation across hundreds of conditions—infeasible with conventional single-vial methods. Robotic high-throughput platforms and active learning strategies now make this practical.

**Action:** Added a sentence in the introduction explaining that determining these parameters requires systematic measurements across hundreds of conditions varying ionic strength, temperature, and composition simultaneously—a scale of experimentation that has only recently become feasible through robotic high-throughput platforms.

---

### Comment 4 — Why are parameters missing? (Page 2, Sticky Note)
> *(Paraphrased)* Asked why the parameters are missing: were they infeasible to measure, or not considered important?

**Context:** Follows the statement that Fe²⁺–HS⁻ and Pb²⁺–HS⁻ binary parameters are "absent from all standard databases." The reader wants to know the underlying reason for this gap.

**Assessment:** Critical question that must be answered. The gap exists for two compounding reasons: (1) sulfide systems require strict inert-atmosphere handling (O₂ oxidizes Fe²⁺ and reacts with HS⁻), making conventional measurements laborious; and (2) the petroleum industry historically prioritized sulfate-scale parameters (BaSO₄, CaSO₄) because sulfate scales were the dominant production concern, with sulfide-scale problems only gaining prominence as sour-reservoir production increased.

**Action:** Added explanation in the introduction that the gap persists because sulfide measurements require inert-atmosphere handling that makes conventional methods laborious, and because industry historically prioritized sulfate-scale parameters.

---

### Comment 5 — Novelty preview in introduction (Page 3, Sticky Note)
> *(Paraphrased)* Suggested previewing the novelty in the introduction.

**Context:** Refers to content in the Objectives section. The novel elements (first systematic Pitzer parameterization for sulfide-mineral systems, combined metal–sulfide and metal–organic acid framework) should be previewed in the introduction.

**Assessment:** Valid structural suggestion. The introduction should foreshadow what is novel about the proposed approach before the reader reaches the Objectives section.

**Action:** The introduction's closing paragraph already states "the first Pitzer ion-interaction framework." Strengthened this to explicitly note the novelty of systematic experimental determination of the complete parameter set.

---

### Comments 6–8 — Highlights (Pages 5–6)
Several highlights without accompanying sticky notes appear on pages 5–6 of the proposal (Background and Significance, Research Plan sections). These likely indicate passages that caught Matt's attention but did not prompt specific written feedback.

**Assessment:** No specific action required, but the highlighted passages (detection methods, ICP-OES validation, parameter regression) suggest these sections were clear and of interest.

---

## Cross-Referenced Feedback

### Barry Bickmore (#51)
> *(Paraphrased)* Noted that the draft does not justify leaving out organic-organic interaction parameters.

**Assessment:** Valid concern. Organic-organic mixing parameters (e.g., θ(OAc⁻–Prop⁻)) were excluded from the ~48 target parameters because organic acid concentrations in produced waters are 2–4 orders of magnitude below inorganic anion concentrations (Cl⁻, SO₄²⁻), making their mutual mixing contributions negligible compared to metal–organic cross terms. This follows from Pitzer & Kim (1974): mixing parameter contributions scale with the product of the interacting ion concentrations, so trace-species pairs contribute negligibly.

**Action:** Added a brief justification sentence in the parameter inventory paragraph noting that organic-organic mixing parameters are omitted because organic acid concentrations are orders of magnitude below the dominant inorganic anions, making their mutual interaction contributions negligible (citing Pitzer & Kim 1974).

### Milad Abolhasani (#24, closed)
The following feedback was previously incorporated but remains relevant context:
1. Clearly state the "fundamental" science aspect — reinforced in this round of edits
2. Don't mention "liquid handling" in Figure 1 — already addressed (figure uses "high throughput experimentation")
3. Present as a new prediction framework, not just validating existing theory — already addressed in framing
