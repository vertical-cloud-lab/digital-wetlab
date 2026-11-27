# Utah critical minerals on the OT-2: refining toward a qualified part, and recycling AM alloys

> Compiled 2026-11-02 for Sterling's comment on
> [PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/pull/83): the Utah critical-minerals
> angle, perhaps the refining process for certain minerals ("mine to qualified part"), or recycling
> processes for AM alloys. This builds on direction 2 of the [README](README.md) and connects it to
> the alloy lab's FLAIME work. A deadline is **verified** only where the funder's own page was read
> on 2026-11-02, or on 2026-10-29 for rows taken from the README.

## Short answer

- **Yes, and it completes the alloy lab's critical-minerals story.**
  - DOE's critical-materials strategy has four pillars: diversify supply, develop alternatives,
    improve materials and manufacturing efficiency, and recycle.
  - FLAIME, the alloy lab's work on critical-mineral-lean aluminium alloys for laser powder bed
    fusion, covers alternatives and efficiency.
  - The OT-2 can take supply (refining Utah sources) and recycling (AM scrap), for their aqueous
    steps.
  - The stakes rose a year ago. Fourteen of the 15 elements in FLAIME's alloying palette (all but
    Fe), and aluminium itself, are on the final 2025 USGS critical-minerals list.
- **The question that ties it together: how refined is refined enough?**
  - Refining costs climb with every step of purity, but a part only has to pass its qualification
    tests.
  - Brine-derived Mg and Li carry Na and K, which embrittle Al–Mg and Al–Li alloys. Recycled scrap
    carries Fe and Cu.
  - Nothing found links how a refining or recycling step is run to whether the printed part
    qualifies.
  - "Mine to qualified part" also seems to be unclaimed: the search found no uses of it. The nearest
    phrases are "mine-to-magnet" (Energy Fuels, MP Materials) and IperionX's "mine to market".
- **Three projects, in the order to start them.**
  - **A. Brine to alloy-grade Mg and Li compounds: where do Na, K, Ca and B go?**
    - This is direction 2, turned into a mechanism question: does each impurity sit on the surface,
      in occluded brine, or in the lattice? The OT-2's programmed dosing paths can answer it.
    - It needs no new hardware.
    - It is the step after the sorbent in today's
      [Separation Science one-pager](bes-white-papers/separation-science.pdf).
  - **B. Recycling AM aluminium.**
    - The alloy lab's ultrasonic atomizer already takes failed prints and scrap.
    - The OT-2 keeps the composition ledger across scrap → powder → print loops.
    - It can also recover Sc, Zr and rare earths from scrap that can't be remelted to spec.
  - **C. Mine (or scrap) to qualified part, as one function network.**
    - The lab's Bayesian optimisation over function networks, with partial evaluations, chooses
      between cheap OT-2 refining runs and expensive print-and-test runs.
    - This is the team proposal; A and B are its preliminary data.
    - A first demonstration needs no OT-2: print Al–Ce alloy made with unseparated mischmetal. The
      search found only cast versions.
- **What's new.**
  - No Opentrons hydrometallurgy paper turned up, apart from one liquid-handling step.
  - The automated precipitation work optimises yield or selectivity, not how impurities get into the
    solid.
  - No closed-loop leaching study turned up.
  - Sc recovery from Al–Sc AM scrap has a single conference paper.
- **Funding.**
  - **Best near-term fits.** Both are new to this folder:
    - ONR's Materials Treatment and Recovery program, white paper by Dec 31, 2026. It asks for
      critical-materials recovery "onboard naval platforms and at remote locations".
    - Two DLA strategic-materials BAAs, open on a rolling basis. Refining, recycling and
      qualification are all in scope.
  - **Project A:** BES Separation Science (Dec 11), NSF's geosciences critical-minerals letter or
    CBET (any time).
  - **Team-building:** Scialog (Mar 15).
  - **Nothing open:** DOE's critical-minerals office.
  - **Watch:** Argonne's MineralWorks challenge and Utah's new Critical Minerals Council.
- **Utah makes it timely.** SB 254 (Mar 2026) sets up a MINES Center at the University of Utah to
  "develop processing and separation processes" and "provide for autonomous sampling and real-time
  analysis". That describes a self-driving lab.

## Why this fits the lab

- **The alloy lab already covers half of DOE's critical-materials strategy.** DOE's
  [strategy](https://www.energy.gov/cmei/ammto/critical-minerals-and-materials) has four pillars:
  diversify supply, develop alternatives, improve materials and manufacturing efficiency, and invest
  in recycling and reuse. The alloy lab's FLAIME work designs critical-mineral-lean aluminium alloys
  for laser powder bed fusion (LPBF), which is "alternatives" and "efficiency"; its own Topic 3B
  analysis maps it there
  ([`edison-3b-deepdive-synthesis.md`](https://github.com/vertical-cloud-lab/digital-alloy-lab/blob/8baf159/edison-trajectories/edison-3b-deepdive-synthesis.md)).
  The OT-2 can take the other two pillars, supply and recycling, for their aqueous steps.
- **The downstream half of a mine-to-part chain already exists.**
  - An ultrasonic atomizer (AMAZEMET rePOWDER) makes small batches of custom powder from a
    15-element palette: Mn, Cr, Zr, Mg, Si, Cu, Ti, Fe, Ni, Ce, Sc, Li, Er, Zn and Sn
    ([TMS 2027 abstract](https://github.com/vertical-cloud-lab/digital-alloy-lab/blob/8baf159/tms-2027-ultrasonic-atomization-abstract.md)).
    AMAZEMET markets it for scrap and failed prints as well as new alloys.
  - LPBF, density cubes and tensile bars on an Aconity MIDI at the University of Utah
    ([TMS 2027 LPBF abstract](https://github.com/vertical-cloud-lab/digital-alloy-lab/blob/8baf159/tms-2027-lpbf-process-parameter-optimization-abstract.md)).
  - Bayesian optimisation over function networks (BOFN), with a mineral-burden node planned in
    the Topic 3B analysis.
- **Utah has three of the palette's elements in quantity.** Great Salt Lake brine holds Mg and Li.
  Monazite processed at White Mesa yields Ce and La alongside the NdPr it is run for (details
  below).
- **BOFN is built for chains.** BOFN ([Astudillo & Frazier 2021](https://arxiv.org/abs/2112.15311))
  and its partial-evaluation version p-KGFN ([Buathong et al. 2023](https://arxiv.org/abs/2311.02146))
  optimise processes made of stages whose outputs feed the next stage, and p-KGFN chooses which
  stage to run next given what each costs. A supply chain from brine or scrap to a tested part is
  such a network: the OT-2 stages cost minutes and cents, a print-and-test costs days.
- **The chemistry is the lab's own.** Selective precipitation, PHREEQC/Pitzer modelling and
  ICP-OES dilution practice all come from the PRF work, including the review's fixes (gravimetric,
  matrix-matched dilutions with an internal standard).

## Utah's critical minerals, and where an aqueous step could help

The final 2025 USGS list ([90 FR 50494](https://www.federalregister.gov/documents/2025/11/07/2025-19813/final-2025-list-of-critical-minerals),
Nov 7, 2025) has 60 minerals. New since 2022: boron, copper, lead, metallurgical coal, phosphate,
potash, rhenium, silicon, silver and uranium. It covers aluminium, magnesium, lithium, the rare
earths, scandium, copper, nickel and every other non-iron element in FLAIME's palette.

| Source | What it yields | Status (source date) | Aqueous step the OT-2 could study | Hazard or limit |
|---|---|---|---|---|
| Great Salt Lake brine | Mg, Li, K, B | North arm typically 45–60 mg/L Li, 8–14 g/L Mg and 5–9 g/L K ([UGS OFR-769](https://doi.org/10.34191/OFR-769)). US Magnesium idled in Nov 2024 and filed for Chapter 11 in Sept 2025 ([USGS](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-magnesium-metal.pdf)). The state bought the site for $30M ([SLTrib](https://www.sltrib.com/news/environment/2026/01/27/utah-buys-bankrupt-us-magnesium), Jan 2026) and offered it for lease, preferring non-evaporative extraction ([FFSL](https://ffsl.utah.gov/wp-content/uploads/CompetitiveLeaseOffering-FormerUS-MagnesiumSite.pdf), Aug 2026). Lilac Solutions plans 5,000 t/yr Li₂CO₃ and was selected for $100M by DOE ([Lilac](https://lilacsolutions.com/news/us-department-of-energy-selects-lilac-solutions-for-100m-award-for-great-salt-lake-lithium-project), Aug 2026) | Sorbent selectivity (the BES one-pager); eluate → Li₂CO₃; Mg(OH)₂ and B from bitterns (project A) | Low. The old US Magnesium residues are Superfund waste, so use lake brine or synthetic solutions |
| Paradox Basin brine (Anson Resources, Green River) | Li | 10,000 t/yr Li₂CO₃ planned for 2029–30 ([Mining Weekly](https://www.miningweekly.com/article/lithium-developer-anson-secures-193m-business-incentive-from-utah-gov-2026-09-04), Sept 2026, secondary) | As above; it also links back to the PRF produced-water work | Low |
| Kennecott (Rio Tinto) | Cu, Mo, Au, Ag; about 20 t/yr Te since 2022 | Te is cemented out of refinery anode slimes as copper telluride ([Rio Tinto](https://www.riotinto.com/en/news/stories/slime-into-solar), 2023) | Te cementation and electrodeposition from synthetic slime leachate | Se, Te and As are toxic, and acid with a reductant can release H₂Se or H₂Te. Synthetic liquors, small scale |
| White Mesa Mill (Energy Fuels, Blanding) | U, V and rare earths: up to 1,000 t/yr NdPr oxide installed; Dy and Tb from a pilot, with a commercial circuit commissioning in Q4 2027 | [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1385849/000138584926000009/efr-20251231.htm); [Metal Tech News](https://www.metaltechnews.com/story/2026/08/05/tech-metals/white-mesa-heavy-rare-earth-build-underway/2865.html), Jul 2026 | Rare-earth double-sulfate or oxalate precipitation and aqueous ligand selectivity, on lanthanide salts. Ce and La, most of monazite's rare earths, feed Al–Ce alloys | Real monazite streams carry U, Th and Ra. Never on the OT-2 |
| 5N Plus (St. George) and the Apex mine | Ge, Ga | 5N Plus won $18.1M for up to 20 t/yr of Ge from residues ([Semiconductor Today](https://semiconductor-today.com/news_items/2026/jan/5n-300126.shtml), Jan 2026). Blue Moon Metals agreed to buy Apex ([6-K](https://www.sec.gov/Archives/edgar/data/1732379/000110465926021808/tm267678d1_ex99-1.htm), Feb 2026) | Ge capture from residue leachates on tannin or chelating resins | As in the ore. Concentrated HCl makes volatile GeCl₄ |
| Spor Mountain (Materion) | Be; the only US mine | [USGS](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-beryllium.pdf), 2026 | None | Never: chronic beryllium disease |

**The state has moved.**
- The governor's "Mission Critical" plan (Jan 2026) aims to process at least half of Utah's
  critical minerals in the state ([KSL](https://www.ksl.com/article/51436025/can-utah-solve-trumps-critical-minerals-dilemma)).
- SB 254, signed Mar 26, 2026 ([enrolled text](https://le.utah.gov/Session/2026/bills/enrolled/SB0254.pdf),
  lines 1516–1521), creates:
  - a Critical Minerals Council;
  - an $11.4M development account for FY2027;
  - a MINES Center at the University of Utah, to partner with industry and academia to "develop
    processing and separation processes", "integrate physical, chemical, electrochemical, and
    thermal processing" and "provide for autonomous sampling and real-time analysis".
- The University of Utah also set up an Institute for Critical and Strategic Minerals in Apr 2026
  ([@TheU](https://attheu.utah.edu/facultystaff/u-announces-new-institute-for-critical-and-strategic-minerals/)).
- The research pilot in Utah's HB 373 is open only to public universities, so BYU's way in is as a
  partner.

## What the OT-2 can and can't do in refining and recycling

| Step | On the OT-2? | Why |
|---|---|---|
| Selective precipitation and crystallisation (hydroxides, carbonates, phosphates, oxalates, double sulfates) | **Yes, the core** | Programmed dosing paths, replicates, heater-shaker to 95 °C; ICP-OES on supernatant and on the dissolved solid; XRD |
| Washing and repulping precipitates | Yes, with a filter plate or a centrifuge step | Separates what sits on a crystal from what is inside it |
| Sorbents and ion exchange (batch isotherms) | Yes | Filter plates; already in direction 2 |
| Leaching ore, residue or scrap | Only at milligram scale, with gas-free lixiviants (ferric or cupric chloride, glycine, citrate) or with EHS sign-off for small amounts of H₂ | Nitric digestions give NOx and HF is out without a hood; dissolving aluminium gives about 1.3 L of H₂ per gram at room temperature |
| Solvent extraction | No | Kerosene-type diluents need a hood |
| Selective electrodeposition and electrowinning | Yes, with direction 1's AMPERE-2 hardware | Aqueous; Ni and Co salts need EHS sign-off |
| Reduction to metal (molten-salt electrolysis, metallothermic), smelting, atomising | No | A metallurgy partner, or the alloy lab |
| ICP-OES sample preparation | Yes | Direction 5's support role |

## Project A. Brine to alloy-grade Mg and Li compounds: where do Na, K, Ca and B go?

This is direction 2 with a sharper question and a reason that reaches the part.

- **Question.** When Mg(OH)₂ is precipitated from lake brine, and Li₂CO₃ or Li₃PO₄ from a lithium
  eluate, how much Na, K, Ca and B ends up in the solid, by which mechanism, and how does the
  precipitation *path* control it? PHREEQC with Pitzer parameters fixes the end state: what
  precipitates and what stays dissolved. The impurity content of the solid depends on how the system
  gets there: the supersaturation profile, seeding, temperature, ageing and washing.
- **Why it reaches the part.**
  - Trace Na embrittles Al–Mg alloys at high temperature
    ([Okada & Kanno 1997](https://doi.org/10.1016/s1359-6462(97)00176-0)).
  - Na and K embrittle Al–Li alloys
    ([Webster 1987](https://doi.org/10.1007/bf02647091)).
  - Brine-derived Mg and Li start out surrounded by Na and K. How much of that survives refining is
    the first number in an impurity budget from brine to part (project C).
- **Three mechanisms, three fingerprints.** Crystallisation research, mostly in pharmaceuticals,
  already has a workflow for telling these apart
  ([Capellades et al. 2022](https://doi.org/10.1039/d1ce01721g)).
  1. *Surface adsorption.* Scales with surface area and mostly washes off.
  2. *Occluded mother liquor.* Grows with growth rate and doesn't wash off. It carries the brine's
     own Na/Cl ratio, so chloride, which has no place in the Li₂CO₃ lattice, traces it.
  3. *Lattice incorporation.* Follows a partition coefficient that shifts with supersaturation. It
     doesn't wash off and brings no matching chloride.
- **What the OT-2 does.**
  - Varies the path at a fixed final dose, with replicates: one shot, stepwise or reverse addition.
    It also varies temperature (to 95 °C), seed loading, ageing time and the wash protocol.
  - ICP-OES measures each element in the supernatant and in the washed, redissolved solid.
  - Chloride is read by AgCl turbidity, using the lab's camera, or by an ion-selective electrode.
  - XRD identifies the phases. Magnesium hydroxychlorides can form in chloride-rich brine.
- **Lithium needs a concentration step first.** North-arm brine typically holds 45–60 mg/L Li beside
  8–14 g/L Mg ([UGS OFR-769](https://doi.org/10.34191/OFR-769)). Li₂CO₃ won't precipitate until Li
  reaches a few g/L, which is why industry concentrates it with a sorbent first. So:
  - use real north-arm brine for the Mg(OH)₂ step;
  - use synthetic eluates with realistic Na, K, Ca, Mg and B for the lithium step.
- **Where Bayesian optimisation fits.** As Bayesian experimental design, choose the next path that
  best separates the three mechanism models, rather than the path that maximises purity. That is a
  mechanism question, which is what DOE BES Separation Science asks for, and the "optimisation is
  out of scope" rule doesn't bite. The fitted models then give project C its purity–recovery
  trade-off for free.
- **Closest precedents.**
  - [Mousavi Masouleh et al. 2024](https://doi.org/10.1039/d4dd00159a) used active learning to
    convert LiCl to Li₂CO₃ on a pipetting robot.
  - [Ritchhart et al. 2026](https://doi.org/10.1039/d6mh00475j) ran closed-loop selective
    precipitation with AI agents.

  Both optimise yield or selectivity. Neither asks how the impurities get into the solid, or what
  purity a part needs. That is the opening.
- **Hardware and hazards.** Nothing new: sealed vials or capped deep-well plates, a filter plate,
  ICP-OES and XRD time. The reagents are brine, NaOH, Na₂CO₃ and Na₃PO₄; redissolving carbonate
  solids releases a little CO₂.

## Project B. Recycling AM aluminium

- **Where AM scrap goes now.**
  - Most aluminium scrap is remelted. Each cycle concentrates what the melt can't remove: above all
    Fe, but also Cu, Zn and Si. That is the central problem of aluminium recycling
    ([Raabe et al. 2022](https://doi.org/10.1016/j.pmatsci.2022.100947), the "dirty alloys"
    review).
  - AM adds its own streams: supports, failed builds, and spent powder that has picked up oxygen.
  - The newest AM aluminium alloys also carry the most expensive alloying elements (Sc, Zr, Ce, Er).
    Their value is lost once they're diluted into commodity scrap.
- **The alloy lab can already close the physical loop.** AMAZEMET says the rePOWDER turns "failed
  printouts, unused powder, scrap or waste powder" back into fine powder
  ([vendor page](https://www.amazemet.com/our-technology)). Ultrasonic atomisation has already
  turned copper cable scrap into AM powder of about 99.5 wt% Cu
  ([Cabrioli et al. 2025](https://doi.org/10.3390/jmmp9090320)) and been reviewed for recycling NiTi
  AM waste ([Sojoodi et al. 2025](https://doi.org/10.1007/s40830-025-00589-y)). So the loop scrap →
  powder → print → scrap can run in-house.
- **What the OT-2 adds.**
  1. *A composition ledger for every loop.* The OT-2 prepares ICP-OES samples for each generation,
     to track:
     - Mg, Li and Zn lost to evaporation;
     - Fe, Ni and Cr picked up;
     - Sc, Zr and Ce retained.

     The method: 10–20 mg digestions in dilute HCl, or in NaOH for the Si in AlSi10Mg, then
     gravimetric, matrix-matched dilutions. This is support work, but qualification needs it, and
     the PRF review's ICP-OES fixes carry straight over. The physical side of AlSi10Mg powder reuse
     is documented ([Raza et al. 2021](https://doi.org/10.1016/j.matdes.2020.109358): oxidised
     spatter and a thickening oxide over 30 months of reuse). Element-by-element chemistry across
     re-atomisation is not.
  2. *Recovering Sc, Zr and rare earths from scrap that can't be remelted into spec.* Hot NaOH
     dissolves aluminium as aluminate. Sc, Zr and the rare earths stay behind in a hydroxide
     residue, together with Mg and Fe. The Bayer process works the same way: there, Sc and the rare
     earths end up in the red-mud residue. Redissolving the residue in acid and splitting it by
     selective precipitation (oxalate for Sc and the rare earths, hydrolysis for Zr) is OT-2 work
     at milligram scale. A gentler first step is cementation: dissolve the aluminium in a salt of a
     more noble metal, which avoids most of the H₂ and heat of acid leaching.
     [Yagmurlu et al. 2023](https://doi.org/10.1007/978-3-031-22532-1_172) did this for Al–Sc
     printing powder. It is the only peer-reviewed Sc-from-scrap study the search found, so there is
     room.
  3. *Copper alloys by electrochemistry.* For nickel–aluminium bronze, the ONR YIP alloy:
     - dissolve scrap at the anode and plate Cu at the cathode;
     - Ni, Fe, Mn and Al stay in solution.

     This runs on direction 1's hardware. It is copper electrorefining in miniature, mature
     chemistry, so it makes a fallback or a teaching example rather than research.
- **The research question.** Over repeated scrap → powder → print cycles, which impurities
  accumulate, and which of them decide whether a part still qualifies? Printing from mixed scrap
  already works ([Monti et al. 2025](https://doi.org/10.1016/j.susmat.2025.e01606)), and LPBF
  tolerates 2–3 wt% Fe in Al–Si–Mg ([Wang et al. 2023](https://doi.org/10.1080/17452759.2023.2235587);
  [Pereira et al. 2024](https://doi.org/10.1016/j.msea.2024.146152)), but those are single
  compositions, not a map. The answer lets FLAIME add
  impurity tolerance as a design objective: the "dirty alloys" idea applied to LPBF, where rapid
  solidification may tolerate more Fe than casting does.
- **Hazards.** Dissolving aluminium gives H₂ (about 1.3 L per gram), and hot NaOH is corrosive.
  Keep to tens of milligrams per well. No nitric acid, no HF.

## Project C. Mine (or scrap) to qualified part, as one function network

This is the team proposal that projects A and B feed. It answers "how refined is refined enough?"
for a qualified part.

- **The network.**
  1. *Source:* lake brine, a rare-earth leachate, or AM scrap.
  2. *Aqueous refining (OT-2).* Inputs: path, wash and dose. Outputs: the compound, its impurity
     vector, and a cost or energy proxy.
  3. *Metal and master alloy.* At first this is bought high-purity metal spiked to the impurity
     vector that step 2 produced (a surrogate feedstock). Later it comes from a metallurgy partner
     that does the reduction for real.
  4. *Alloying and atomisation (rePOWDER).* Particle size, sphericity and oxygen.
  5. *LPBF and testing (U of Utah).* Density and tensile properties, checked pass or fail against
     a qualification specification.
- **The objectives.**
  - Qualification, as constraints.
  - Refining effort.
  - FLAIME's mineral burden.
  - Recycled content.
- **Why BOFN with partial evaluations.** Each stage can be run on its own, at its own cost.
  p-KGFN decides whether the next experiment should be a cheap OT-2 refining run or an expensive
  print. That makes the methods contribution cost-aware optimisation across a whole supply chain,
  not a single process.
- **What it delivers.**
  - For each Utah source, a curve of refining effort against the share of parts that qualify.
  - For scrap, how much recycled content an alloy can take.

  Refiners, defence buyers and state planners can act on those numbers, and nobody publishes them
  now.
- **A first demonstration that needs no OT-2.** Al–Ce alloys exist partly to use the cerium that
  rare-earth mining over-produces, and they print
  ([Plotkowski et al. 2020](https://doi.org/10.1016/j.actamat.2020.07.014)). Unseparated
  mischmetal works in cast Al–Ce ([Sims et al. 2020](https://doi.org/10.1007/978-3-030-36408-3_30)),
  but the search found no printed version. Printing Al–mischmetal on the rePOWDER and the U of Utah
  LPBF asks whether a whole La/Ce separation step can be skipped, which is "how refined is refined
  enough" in a single experiment. Ce is already in FLAIME's palette.
- **Be honest about scale.** The OT-2 makes milligrams of compound; the atomizer needs grams to
  kilograms of metal. Until a partner closes step 3, the link is the impurity specification, not
  material carried from one lab to the other. Reviewers will ask where the metal comes from, so say
  this up front.
- **Who's needed.**
  - An extractive-metallurgy partner for step 3.
  - The U of Utah LPBF group, already a FLAIME partner.
  - Ideally, a Utah operator for real process streams.
- **When.** It is too big for the December–February dates. Aim it at the next DOE critical-minerals
  call, a DoD program or a FY2028 MURI topic, with projects A and B as preliminary data.

## What others have done

A literature search on 2026-11-02 resolved every DOI below on Crossref. "Robot" says what automation
the paper used.

| Area | Paper | What was done | Robot |
|---|---|---|---|
| Selective precipitation, agents | Ritchhart et al. 2026, *Mater. Horiz.* ([10.1039/d6mh00475j](https://doi.org/10.1039/d6mh00475j)) | LLM agents and closed-loop Bayesian optimisation of selective precipitation from produced water and magnet leachates (PNNL) | automated instruments |
| Li₂CO₃ | Mousavi Masouleh et al. 2024, *Digital Discovery* ([10.1039/d4dd00159a](https://doi.org/10.1039/d4dd00159a)) | Gaussian-process active learning for converting LiCl to Li₂CO₃ with CO₂ and NH₄OH | Unchained Labs Junior and a thermoshaker; people ran the batches |
| Rare-earth precipitation | Nelson et al. 2020, *Commun. Chem.* ([10.1038/s42004-019-0253-x](https://doi.org/10.1038/s42004-019-0253-x)) | 96-well screen of ligand-driven La/Nd/Dy precipitation read by ICP-OES; Nd/Dy separation factor 213 at scale | none (plates) |
| Rare-earth extraction | Augustine et al. 2026, *JACS* ([10.1021/jacs.6c04301](https://doi.org/10.1021/jacs.6c04301)) | DFT-chosen aqueous holdback agent plus multi-objective Bayesian optimisation of solvent extraction | LANL automated extraction platform |
| AlSi10Mg powder reuse | Raza et al. 2021, *Mater. Des.* ([10.1016/j.matdes.2020.109358](https://doi.org/10.1016/j.matdes.2020.109358)) | Over 30 months of reuse: up to about 3 vol% oxidised spatter; surface oxide grew from about 4 nm to 38 nm | none |
| Scrap to LPBF aluminium | Monti et al. 2025, *Sustain. Mater. Technol.* ([10.1016/j.susmat.2025.e01606](https://doi.org/10.1016/j.susmat.2025.e01606)) | Powder gas-atomised from mixed scrap (Al 2024, Ti-6Al-4V, 316L) printed with near-virgin properties and about 50% less CO₂ | none |
| Fe tolerance in LPBF | Wang et al. 2023, *Virtual Phys. Prototyp.* ([10.1080/17452759.2023.2235587](https://doi.org/10.1080/17452759.2023.2235587)); Pereira et al. 2024, *MSEA* ([10.1016/j.msea.2024.146152](https://doi.org/10.1016/j.msea.2024.146152)) | 2–3 wt% Fe in LPBF Al–Si–Mg alloys as stand-ins for contaminated scrap | none |
| Sc from Al–Sc AM powder | Yagmurlu et al. 2023, *Light Metals* ([10.1007/978-3-031-22532-1_172](https://doi.org/10.1007/978-3-031-22532-1_172)) | Cementation (dissolving the powder in a salt of a more noble metal) avoids the H₂ and heat of acid leaching | mini-pilot plant |
| Mischmetal in Al–Ce | Sims et al. 2020, *Light Metals* ([10.1007/978-3-030-36408-3_30](https://doi.org/10.1007/978-3-030-36408-3_30)); Qi et al. 2025, *MSEA* ([10.1016/j.msea.2025.147912](https://doi.org/10.1016/j.msea.2025.147912)) | Unseparated mischmetal in place of Ce, cast only | none |
| Al–Ce by AM | Plotkowski et al. 2020, *Acta Mater.* ([10.1016/j.actamat.2020.07.014](https://doi.org/10.1016/j.actamat.2020.07.014)) | ORNL's printed Al–Ce–Mn alloy | none |
| Scrap to powder by ultrasonic atomisation | Cabrioli et al. 2025, *JMMP* ([10.3390/jmmp9090320](https://doi.org/10.3390/jmmp9090320)) | Cable scrap to AM copper powder of about 99.5 wt% | none |
| Co/Ni electrodeposition | Kim et al. 2021, *Nat. Commun.* ([10.1038/s41467-021-26814-7](https://doi.org/10.1038/s41467-021-26814-7)) | Chloride speciation and a polymer coating make Co deposit selectively from battery leachate | none |
| Electrodeposition lab | Pence et al. 2026, *ACS AMI* ([10.1021/acsami.6c08121](https://doi.org/10.1021/acsami.6c08121)) | Low-cost modular self-driving lab optimising metal electrodeposition from camera images (title only) | yes |

**Gaps, searched for and not found.**
- **Opentrons hydrometallurgy.** No OT-2 paper on leaching, precipitation, sorbents or solvent
  extraction, beyond the liquid handling in the lanmodulin work of Diep et al. 2026. The robots in
  this area are Unchained Labs and Chemspeed machines.
- **Purity mechanisms.** No automated study of how impurities get *into* a critical-mineral
  precipitate, or of purity tied to an alloy specification. The work above optimises yield or
  selectivity.
- **Leaching.** No closed-loop leaching of ore, battery black mass or alloy scrap.
- **Sc from Al–Sc scrap.** Only Yagmurlu 2023 and patents.
- **Al–mischmetal by AM.** None. All the mischmetal work is cast.
- **Electrodeposition from impure sources.**
  - No electrochemical AM from leach-derived electrolytes.
  - No automated screen of selective electrodeposition for separating metals.
  - Anomalous codeposition shows up only as an obstacle ([Lupi 2003](https://doi.org/10.1016/s0892-6875(03)00080-3)).
- **Superalloy scrap.** No recovery of Nb or Mo from AM scrap of IN718 or IN625.

## Funding, Nov 2026 – mid-2027

Read on the funders' own pages on 2026-11-02, by a search agent where marked. Programs the alloy lab
already uses (AFOSR YIP, ONR YIP, DOE Early Career, NSF CMMI AMDO, DURIP) are left out.

| By | Program | Project | Size | Status |
|---|---|---|---|---|
| **Dec 11, 2026** (later applications go to the next cycle) | DOE BES **Separation Science** ([DE-FOA-0003665](https://www.grants.gov/search-results-detail/363993)). Make project A the second aim of the sorbent proposal in the [one-pager](bes-white-papers/separation-science.pdf), or pitch it separately | A | standard BES grant | verified (README) |
| **Dec 31, 2026**, then its successor | ONR Code 33 [**Materials Treatment and Recovery**](https://www.onr.navy.mil/organization/departments/code-33/materials-focus-area/materials-treatment-and-recovery), through the [Long Range BAA](https://www.grants.gov/search-results-detail/356605). It asks for "selective extraction and separation techniques" and "critical materials recovery onboard naval platforms and at remote locations": compact recovery from AM scrap where the Navy prints parts. A different program from the ONR YIP | B | not stated; white paper first | verified (page read) |
| Rolling; white papers to May 1, 2028 | [DLA Strategic Materials BAA SP8000-26-B-BAA0](https://sam.gov/opp/54e1bd529fd84e7db45fe5a236374ca0/view): refining, processing, recycling, substitution and qualification. Its list includes rare earths, Mg, Sc/Y and Co | C | Phase I up to the simplified acquisition threshold for 12 months; Phase II ≤ $10M; contracts; 5-page white paper | verified (agent) |
| Rolling, to Jan 2030 | [DLA R&D Strategic Materials BAA SP4701-25-B-0001](https://sam.gov/opp/3510fb2e9dbd4c89bd826b06dd2ea284/view): refining and processing, aerospace alloys and processes, recycling and substitution | B, C | $700M ceiling; 6-page white paper | verified (agent) |
| Any time | NSF GEO [Dear Colleague Letter on critical-minerals research (NSF 23-057, updated Jun 5, 2026)](https://www.nsf.gov/funding/opportunities/dcl-novel-approaches-critical-minerals-research-geosciences-geo): fundamental extraction and separation science from brines and tailings; engineering optimisation is out | A | standard NSF | verified (agent) |
| Any time | NSF CBET 26-518 or CHE CSS 26-519 (send to one) | A | standard NSF | verified (README) |
| Any time | NSF CMMI 26-515, Materials Engineering & Processing or Advanced Manufacturing: impurity-tolerant feedstock, powder reuse. Same division as the alloy lab's AMDO, so coordinate | B | standard NSF | verified (agent) |
| Rolling, to Nov 20, 2027 | ARL foundational-research BAA, topic ARL-BAA-0075: AM, AI/ML for manufacturing, new metal AM feedstocks | B, C | not stated | verified (agent) |
| **Mar 15, 2027** | [Scialog: Sustainable Minerals, Metals & Materials](https://rescorp.org/scialog/sustainable-minerals-metals-and-materials/) Fellow application: the place to meet metallurgists for project C | A, C | seed awards | verified (PR 82) |
| ~late Jan / mid-Feb 2027 | BYU IDR with Geology, Chemistry or Mechanical Engineering | A, B | ≤ $60K/yr for 2 yr | unverified |

**Weaker fits.**
- **DARPA Young Faculty Award.** The executive summary is due Nov 5, but none of the 18 topics
  covers minerals or recycling, and DoD funding caps apply.
- **ARPA-E UNLOCK** (concept paper Nov 20). This is in-situ leaching and needs a field site.
- **FY2027 MURI.** None of its 16 topics covers critical minerals, separations or recycling.
  Amendment 1 (Oct 22) retitles Topic 15 "High-Entropy Electrochemical Materials" and sets Nov 6 for
  questions.

**Watch for.**
- **Argonne's MineralWorks: American Critical Materials Challenge, for DOE's critical-minerals
  office.**
  - Its topics include autonomous materials processing and digital twins.
  - Each team gets over $500K in cash and in-kind support over 3 years.
  - The university call was expected this fall but isn't posted yet.
- **Utah's Critical Minerals Council.** Its FY2027 account may fund research and match federal
  grants, and a MINES Center RFP was being drafted at its summer meetings.
- **DOE Genesis Mission, second round.** Critical materials and advanced manufacturing are topic
  areas.
- **The next REMADE, America Makes and NSF IUCRC calls.**
- **The FY2027 ONR Long Range BAA.**

**Closed or not open.**
- **DOE's Office of Critical Minerals and Energy Innovation lists nothing open.**
  - The accelerator closed in Jul 2026.
  - The PROSPECT planning prize closed Oct 5, and the University of Utah is among its winners.
- **Closed:** ARPA-E RECOVER (Aug 2025).
- **Members only, and nothing open:** REMADE and the Defense Industrial Base Consortium's
  critical-minerals calls.
- **America Makes:** none of its 2026 calls was on recycling.
- **NSF IUCRC:** not taking proposals.
- **Rio Tinto's Centre for Future Materials:** fixed partner universities only.

## Risks and hazards

- **Beryllium: never.** Spor Mountain is the only US beryllium mine, but beryllium is a carcinogen with an
  OSHA limit of 0.2 µg/m³. The alloy lab's answer to beryllium is substitution (Cu–Cr–Zr for Be–Cu),
  not refining.
- **Radioactivity.** Monazite and uranium-mill streams carry Th, U and Ra. The OT-2 uses synthetic
  rare-earth solutions only.
- **Gas.**
  - Dissolving aluminium or magnesium makes H₂.
  - Nitric digestions make NOx.
  - Silicon needs HF or an alkaline route.

  Keep digestions to tens of milligrams per well, vent the vials, and get EHS sign-off before the
  first run.
- **Matrix.** Real brine is hard on ICP-OES: Na and Mg at g/L. This is direction 2's main risk too.
- **Crowding.** Lithium from brine is crowded at pilot scale, and so are magnet recycling and battery
  recycling. The open niche is the mechanism and the link to a part specification, not a better
  sorbent.
- **Scale and overreach.** "Mine to qualified part" invites the question of where the metal comes
  from. Say plainly that the OT-2 sets the impurity specification and the alloy lab tests spiked
  surrogates until a partner closes the reduction step.
- **The Utah operations are in flux.** US Magnesium is bankrupt and its site now belongs to the
  state. Compass Minerals ended its lithium project in 2024, and Lilac's plant has yet to make its
  investment decision. An industry partner
  may be hard to land, so the first results shouldn't depend on one.

## Decisions for Sterling

1. **Which chain to lead with.**
   - Mg and Li from the lake: the fastest, it extends direction 2, and real brine is a drive away.
   - Ce from rare-earth processing: the strongest alloy story, through Al–Ce, but synthetic solutions
     only.
   - AM scrap: the closest to the alloy lab, and the easiest to start.
2. **Whether project A becomes a second aim of the BES Separation Science proposal.** The
   [one-pager](bes-white-papers/separation-science.pdf) drafted today asks why a *sorbent* prefers
   Li. Project A asks what happens next, when the eluate becomes a solid. Together they cover the
   refining chain from brine to compound. Ask Amanda Haes whether one proposal or two suits her
   program better.
3. **Whether the alloy lab will print spiked surrogates.** Project C needs a few LPBF builds with
   deliberate Na, K, Ca or Fe additions, and that is LPBF time FLAIME also wants.
4. **Who closes the metal step.** Look for an extractive-metallurgy group in Utah, or an operator
   with a pilot line. Without one, project C stops at the impurity specification.
5. **EHS, now.** Ask about H₂-evolving digestions at tens of milligrams on an open deck, and about
   Ni and Co salts, which direction 1 needs anyway.

## How this was put together

- **Context.**
  - This folder's [README](README.md) (directions 1, 2 and 5).
  - PR 82's [funding notes](https://github.com/vertical-cloud-lab/digital-wetlab/blob/3d6ba0a/grants/alternative-funding/README.md).
  - The [BES white papers](bes-white-papers/) drafted earlier today.
  - The alloy lab's public repo at [`8baf159`](https://github.com/vertical-cloud-lab/digital-alloy-lab/tree/8baf159):
    README, TMS 2027 abstracts, Topic 3B analysis, powder-production review and company landscape.
- **Searches.** Three ran in parallel on 2026-11-02:
  - the Utah critical-mineral landscape;
  - funders, read on their own pages;
  - the literature, with every DOI resolved on Crossref.

  I checked the Great Salt Lake numbers in the UGS report itself, and the impurity-embrittlement
  and crystallisation references on Crossref.
- **Not done.**
  - No experiments.
  - No contact with Utah operators.
  - No EHS consultation.
  - Edison wasn't used.
