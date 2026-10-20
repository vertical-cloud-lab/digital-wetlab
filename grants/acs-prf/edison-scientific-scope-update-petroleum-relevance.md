https://platform.edisonscientific.com/trajectories/2cb7cf22-0e32-4d9a-92b5-59cbbb19df19

Addressing ACS PRF Petroleum Relevance Concerns: Analysis and Recommendations
Executive Summary
The program managers' concern is that the current proposal studies FeS/PbS precipitation in NaCl-CaCl₂ brines that contain only inorganic salts — chemistry that could describe any high-salinity water system (geothermal, mining, deep groundwater), not specifically petroleum. The petroleum connection exists only in the motivation (scale costs in oil wells), not in the chemistry itself. To be competitive, petroleum-derived compounds must be experimental reactants, not just contextual motivation.

The Pitzer model is absolutely still relevant — it becomes MORE relevant and the project becomes STRONGER with the proposed modifications. This is NOT a completely different project.

Direct Answers to Your Questions
"Would I simply add these to the search space?"
Yes. The cleanest, most scientifically rigorous approach is to add sodium acetate (NaOAc) as a 6th experimental variable in the Latin hypercube design, at concentrations of 0, 10, 50, 100, and 500 mM (spanning the documented 30–4,900 mg/L range in real produced waters). This literally adds a petroleum-derived compound to the experimental search space.

Why acetate is the ideal choice:

It IS a petroleum-derived compound — short-chain organic acids originate from thermal maturation of kerogen and biodegradation of hydrocarbons (Barth 1991, Applied Geochemistry, DOI: 10.1016/0883-2927(91)90059-x)
It is the dominant dissolved organic species in produced water (30–4,900 mg/L; Fakhru'l-Razi et al. 2009, DOI: 10.1016/j.jhazmat.2009.05.044)
Pitzer parameters for Na⁺-OAc⁻ already exist (Manohar et al. 1992, J. Chem. Eng. Data, DOI: 10.1021/je00008a019), proving acetate fits the Pitzer framework
Fe²⁺-acetate and Pb²⁺-acetate complex thermodynamics are published (Shock & Koretsky 1993, GCA, DOI: 10.1016/0016-7037(93)90128-j)
It is experimentally trivial: cheap, stable, non-volatile, compatible with 96-well plates and OT-2
This creates "stoichiometric studies" because acetate competes stoichiometrically with HS⁻ for metal-ion binding:

Fe²⁺ + HS⁻ → FeS↓ (sulfide precipitation)
Fe²⁺ + OAc⁻ → FeOAc⁺ (organic complexation)
Measuring how the [OAc⁻]/[HS⁻] molar ratio shifts precipitation boundaries is by definition a stoichiometric study of a petroleum-derived compound.
Secondary addition: Cyclohexanecarboxylic acid (a standard naphthenic acid model compound) at 2–3 concentrations as a validation variable, representing the petroleum-specific naphthenic acid class.

"How would that affect the discussion around the Pitzer model?"
It strengthens the Pitzer model discussion. Organic acid anions are ions — they have their own Pitzer interaction parameters. Adding acetate to the system extends the Pitzer framework to include:

Fe²⁺-OAc⁻ binary parameters (β⁰, β¹, Cᶲ): 3 new parameters
Pb²⁺-OAc⁻ binary parameters (β⁰, β¹, Cᶲ): 3 new parameters
Anion mixing parameters: θ(OAc-HS), θ(OAc-Cl): 2 new parameters
Ternary mixing: ψ(OAc-HS-Na), ψ(OAc-Cl-Na), ψ(OAc-Cl-Ca): 3 new parameters
Neutral-species terms for FeOAc⁺ and PbOAc⁺ complexes: 4–8 new parameters
Total: ~15–19 additional Pitzer parameters on top of the original 34, expanding the project to ~50 total parameters. The fundamental science question becomes richer: "How do petroleum-derived organic acids shift sulfide-mineral precipitation boundaries in produced-water brines, and can the Pitzer framework quantitatively predict this competition?"

"Is the Pitzer model still even relevant?"
Absolutely yes. The Pitzer model is a general framework for electrolyte solutions. Organic acid anions are electrolytes. Adding them does not change the theoretical framework — it extends it. You are studying how petroleum-derived organic solutes affect the thermodynamic stability of sulfide minerals in high-ionic-strength brines. That is exactly what the Pitzer model is designed for.

"Or is it a completely different project at that point?"
No. It is the same project with one additional experimental variable. The methodology (OT-2 + LHS + Bayesian optimization + PHREEQC + Pitzer regression) is identical. The detection methods are identical. The validation approach is identical. The only change is that one of your stock solutions is now sodium acetate. The proposal's intellectual merit — filling gaps in Pitzer parameter databases for sulfide systems — is preserved and enhanced.

The only scenario where it becomes a completely different project is if the reviewers literally want metal-sulfide CATALYSIS of hydrocarbon transformations (e.g., FeS-catalyzed cracking or desulfurization). That would require different expertise entirely. But based on the feedback language, adding petroleum-derived compounds as reactants in the existing framework should suffice.

Concrete Proposal Modifications
A. Abstract Modification
Add: "We will additionally determine how petroleum-derived organic acids (acetate, the dominant dissolved organic species in produced water at 30–4,900 mg/L) shift sulfide-mineral precipitation boundaries through stoichiometric competition for metal-ion binding."

B. Aim 1 Modifications
Add [NaOAc] as 6th variable: 0, 10, 50, 100, 500 mM
This increases LHS dimensionality from 5D to 6D
Frame as: "stoichiometric studies of the competition between petroleum-derived acetate and sulfide for Fe²⁺ and Pb²⁺ at controlled molar ratios"
Optional: add cyclohexanecarboxylic acid (naphthenic acid surrogate) at 2–3 concentrations
C. Aim 2 Modifications
Expand Pitzer parameter target to ~50 parameters (adding Fe²⁺-OAc⁻, Pb²⁺-OAc⁻ terms)
Note that Na⁺-OAc⁻ Pitzer parameters already exist (Manohar et al. 1992)
PHREEQC already handles acetate speciation natively in its standard databases
D. Introduction Additions
Add paragraph on produced-water organic chemistry, citing Barth (1991), Fakhru'l-Razi et al. (2009), MacGowan & Surdam (1988)
Explicitly frame H₂S as petroleum-derived via thermochemical sulfate reduction (TSR): "H₂S in petroleum reservoirs is generated by the reaction of petroleum hydrocarbons with sulfate minerals" (Machel 2001, DOI: 10.1016/s0037-0738(00)00176-7)
Note that organic acids in produced water originate from kerogen maturation
E. Petroleum Relevance Statement
Strengthen with three arguments: (1) H₂S itself is petroleum-derived via TSR, (2) acetate is petroleum-derived from kerogen maturation, (3) the project now contains stoichiometric studies of petroleum-derived compounds competing with sulfide for metal-ion binding.

Key New References for the Revised Proposal
Barth (1991) Applied Geochemistry DOI: 10.1016/0883-2927(91)90059-x — Organic acids (acetic up to 5000 mg/L) in petroleum reservoir waters
Manohar et al. (1992) J. Chem. Eng. Data DOI: 10.1021/je00008a019 — Pitzer parameters for NaCl-NaOAc-water systems (proves acetate fits Pitzer framework)
Shock & Koretsky (1993) GCA DOI: 10.1016/0016-7037(93)90128-j — Fe²⁺-acetate and Pb²⁺-acetate complex thermodynamics
Machel (2001) Sedimentary Geology DOI: 10.1016/s0037-0738(00)00176-7 — TSR: H₂S is petroleum-derived
Fakhru'l-Razi et al. (2009) J. Hazardous Materials DOI: 10.1016/j.jhazmat.2009.05.044 — Produced water composition
Jin et al. (2019) Energy & Fuels DOI: 10.1021/acs.energyfuels.9b02182 — Organosulfur compounds affect FeS formation
Eke et al. (2020) J. Pet. Explor. Prod. Technol. DOI: 10.1007/s13202-019-00797-0 — Metal naphthenate formation
MacGowan & Surdam (1988) Organic Geochemistry DOI: 10.1016/0146-6380(88)90262-8 — Carboxylic acids in oilfield waters
Zhang et al. (2007) Organic Geochemistry DOI: 10.1016/j.orggeochem.2007.02.004 — Hydrocarbon effects on TSR/H₂S generation
Helgeson (1992) Applied Geochemistry DOI: 10.1016/0883-2927(92)90021-t — Acetic acid thermodynamics at elevated T/P
Important Caveats
Panel numbering may have changed. The 2021 ACS PRF panel listing shows Panel 3 = Inorganic Chemistry and Panel 6 = Chemical Physics/Physical Chemistry, not Earth Sciences and Engineering. The 2024 panel descriptions were updated but could not be retrieved. You should verify current panel assignments directly with PRF (202-872-4481 or prfinfo@acs.org).

Pre-submission contact recommended. The PRF website explicitly advises: "If you have a question on whether or not your research is within the scope of the ACS Petroleum Research Fund please call 202-872-4481 and ask to speak to a Program Manager before submitting a proposal." Given you have direct contact with the program officer (Dr. Bill Aumiller), I would recommend sharing the proposed acetate-addition modification with him before revising to confirm it addresses their concern.

Scope creep risk. Adding a 6th variable increases the experimental space. The Bayesian optimization approach can manage this efficiently, but you may want to explicitly state that the acetate experiments will be concentrated in the ionic strength regime where Pitzer deviations are expected (>2 molal) rather than exhaustively covering all combinations.

The "catalytic" part of the reviewer suggestion is less natural for this thermodynamic project. If stoichiometric studies of acetate/naphthenic acid competition for metal-ion binding are not sufficient, the time-resolved precipitation measurements (1, 5, 15, 60, 240 min) already in the proposal could be framed as studying the "catalytic" (kinetic) effect of petroleum-derived organic acids on sulfide nucleation rates — but this is a secondary framing option.

Discretionary Analytical Decisions
Identified sodium acetate as the primary recommended petroleum-derived compound based on: (a) it being the dominant organic species in produced water by concentration, (b) existing Pitzer parameters for Na⁺-OAc⁻, and (c) experimental simplicity; other valid choices include propionate, butyrate, or naphthenic acid surrogates
Recommended cyclohexanecarboxylic acid as the naphthenic acid model compound; other valid surrogates include cyclopentanecarboxylic acid or commercial naphthenic acid mixtures
Suggested concentration range 0–500 mM for acetate based on the Barth (1991) and Fakhru'l-Razi et al. (2009) data; the upper bound could reasonably be set at 100 mM or 1000 mM depending on the produced water analogue targeted
Estimated ~15–19 new Pitzer parameters from the acetate addition; the exact count depends on which complexes are included and whether temperature-dependent terms are pursued
Recommended TSR framing (H₂S as petroleum-derived) as a supplementary rather than primary argument for petroleum relevance
Focused the literature search on aqueous-phase organic acid interactions rather than high-temperature refinery-condition naphthenic acid corrosion studies, as the proposal operates at 25–90°C in aqueous solution