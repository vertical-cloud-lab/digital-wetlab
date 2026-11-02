# One-page white papers for DOE BES program managers

> Drafted 2026-11-02 for the PM emails suggested in
> [PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/pull/83): one page each, text plus one
> flow diagram, no data. Program text, dates and contacts were read in the
> [FY2027 Office of Science call, DE-FOA-0003665](https://www.grants.gov/search-results-detail/363993)
> (Part 1, version 4.1) on 2026-11-02.

| White paper | BES subprogram and contact | White-paper target | Applications for FY2027 by | Direction |
|---|---|---|---|---|
| [Dehydration or co-ion pairing: what sets lithium selectivity in near-saturated brines?](separation-science.pdf) ([source](separation-science.tex)) | Separation Science: Amanda Haes | Oct 30, 2026 (passed) | Dec 11, 2026 | 2 |
| [Losing iron sites or losing the nickel host? Why Ni–Fe oxygen-evolution catalysts deactivate](catalysis-science.pdf) ([source](catalysis-science.tex)) | Catalysis Science: Viviane Schwartz, Chris Bradley | Oct 30, 2026 (passed) | Dec 14, 2026 | 1 |
| [Entropy-stabilized or kinetically trapped? Why some multi-metal hydroxides co-precipitate as one phase](materials-chemistry.pdf) ([source](materials-chemistry.tex)) | Materials Chemistry: Christopher Chervin | none given | Feb 1, 2027 | 3 |
| [One barrier or two steps? Nucleation statistics for gypsum and how additives change its pathway](synthesis-processing.pdf) ([source](synthesis-processing.tex)) | Synthesis and Processing Science: Shawn Chen | **Nov 30, 2026** | Feb 1, 2027 | 4 |

Target dates are not hard deadlines. An application that misses one is held for the next cycle
rather than rejected. Catalysis Science gives a range of $550K–$1M for three years; the other three
give no figure.

## How each page is built

Every page follows the same plan: the research question, the knowledge gap, two competing
hypotheses with opposite predictions, how the OT-2 experiments tell them apart, the flow diagram,
expected outcomes, and a "fit" paragraph. The fit paragraph names the program's own priority
wording and says which of its exclusions the work avoids. All four programs ask for "why" questions
and rule out optimization, synthesis for its own sake, or automation and AI as the aim. So Bayesian
methods appear only as experimental design that picks the samples which best separate the two
hypotheses.

The pages follow the call's rules for a formal pre-application (US letter, 1-inch margins, body text
at 11 pt, three pages at most), so each can also be submitted in PAMS. Build with
`pdflatex <name>.tex`; the shared layout and the flow-diagram macro are in
[`bes-whitepaper.sty`](bes-whitepaper.sty), and [`previews/`](previews/) has PNGs of each page.

## Suggested order

1. **Synthesis and Processing Science (Shawn Chen).** Its white-paper target, Nov 30, is still
   ahead. The work uses the current setup, so distributions can be measured before a Feb 1
   application. Ask whether aqueous mineral nucleation fits; the portfolio leans toward films and
   crystals.
2. **Materials Chemistry (Christopher Chervin).** It also runs to Feb 1. It is in the same division
   as Synthesis and Processing, and both pages are about precipitation, so say in each email that
   the other idea exists and ask where each belongs.
3. **Separation Science (Amanda Haes)** and **Catalysis Science (Viviane Schwartz, Chris Bradley).**
   Their December dates are five to six weeks away, and BES says successful applications usually
   have preliminary data. Ask whether to aim for December or the FY2028 cycle. The catalysis work
   also needs the potentiostat and the AMPERE-2 hardware first.

## Before submitting in PAMS

A formal pre-application needs more than this page. Keep these in the private repo; they shouldn't
be committed here.

- A title page, which doesn't count toward the page limit: the title; the PI's name and job title;
  the institution; the PI's phone and email; the NOFO number; and the senior or key personnel.
- A list of senior/key personnel, and the list of people who should not review a later application
  (Part 2 of the call has rules on who must be on it), uploaded as an "Additional Attachment".
- A machine-readable PDF, not a scan. Pick the PM named above when you submit.

## Claims to check before sending

- **Catalysis.** That Fe dissolution–redeposition has been tested for only "a few compositions" and
  not systematically against host restructuring. This is the most likely place a PM knows newer
  work. Search for composition-resolved stability studies of Ni–Fe–Co/Mn (oxy)hydroxides since
  Chung et al. 2020.
- **Separation.** That selectivity is "usually reported as a distribution coefficient in a few
  brines". Also check that PHREEQC's `pitzer.dat` has the Li–Na and Li–Mg mixing terms the
  activity correction needs.
- **Materials Chemistry.** That room-temperature "high-entropy" hydroxides are often reported as
  single-phase. Also, Cu(OH)₂ and Zn(OH)₂ can dehydrate to oxides when aged hot in base, which would
  mix a dehydration step into the segregation test; start the hot aging with the Mg–Co–Ni set.
- **Synthesis and Processing.** That scale and additive studies "usually report one onset time per
  condition". Static jar tests do; check for recent microfluidic or droplet studies of gypsum.

## Draft cover emails

Short enough to paste. Attach the matching PDF. Edit anything that's out of date, and add a line if
you have not been funded by the Office of Science before: the call lists "promoting principal
investigators not previously supported by SC" among its selection factors.

**To Shawn Chen, Synthesis and Processing Science.**
Subject: White paper inquiry: nucleation statistics and precursor pathways in gypsum crystallization

> Dear Dr. Chen,
>
> I'm an assistant professor of mechanical engineering at BYU. Before I submit a pre-application
> under DE-FOA-0003665 by your Nov 30 target, I'd value your view on whether the attached one-page
> idea fits Synthesis and Processing Science. It asks whether gypsum crystallization is limited by
> a single nucleation barrier or by a precursor step, and which step additives act on. To find out,
> we measure induction-time distributions over 48–96 replicate wells per condition on a
> liquid-handling robot. I know the portfolio leans toward films and crystals, so I'd especially
> welcome your advice on whether aqueous mineral nucleation belongs here. I am also sending a
> separate idea on multi-metal hydroxide phase formation to Materials Chemistry. Would you have 15
> minutes for a call in the next few weeks?
>
> Best regards,
> Sterling Baird

**To Christopher Chervin, Materials Chemistry.**
Subject: White paper inquiry: entropy stabilization versus kinetic trapping in multi-metal hydroxides

> Dear Dr. Chervin,
>
> I'm an assistant professor of mechanical engineering at BYU, and I'm planning an application to
> Materials Chemistry under DE-FOA-0003665 for the Feb 1 target. The attached one-page white paper
> asks why some multi-metal ("high-entropy") hydroxides co-precipitate as a single phase. Is that
> single phase an equilibrium solid solution, or is it trapped by fast precipitation? We test this
> by approaching the phase boundary from both sides, varying base-addition rate and aging
> temperature, and following each metal by ICP-OES and XRD. We use active learning only to place
> the samples that best separate the two explanations. I'm also sending a separate nucleation idea
> to Synthesis and Processing Science and would welcome your view on where each belongs. Could we
> talk for 15 minutes?
>
> Best regards,
> Sterling Baird

**To Amanda Haes, Separation Science.**
Subject: White paper inquiry: mechanism of lithium selectivity in concentrated brines

> Dear Dr. Haes,
>
> I'm an assistant professor of mechanical engineering at BYU. The attached one-page white paper
> proposes a separation-mechanism study for lithium from Great Salt Lake and produced-water brines.
> Once Pitzer-model activities account for the solution side, is a sorbent's Li⁺ selectivity set by
> ion dehydration, or by co-ion pairing at the solid? Comparing a titanate ion sieve with a
> layered double hydroxide gives each hypothesis a control. Bayesian experimental design chooses
> the brines that best separate the two mechanisms; there is no screening or optimization. I know
> the Oct 30 white-paper target has passed. Would you advise applying by Dec 11 or in the next
> cycle, and does the idea fit the "cooperative chemical interactions" priority?
>
> Best regards,
> Sterling Baird

**To Viviane Schwartz and Chris Bradley, Catalysis Science.**
Subject: White paper inquiry: iron-site exchange versus host restructuring in Ni–Fe OER deactivation

> Dear Dr. Schwartz and Dr. Bradley,
>
> I'm an assistant professor of mechanical engineering at BYU. The attached one-page white paper
> asks why Ni–Fe oxyhydroxide OER catalysts deactivate. Do Fe active sites dissolve faster than
> they redeposit, or does the Ni host restructure? We would test this across matched,
> robot-electrodeposited compositions, with Fe added to purified electrolyte, electrochemical
> probes, and ICP analysis of the electrolyte. Both mechanisms are written as kinetic models, and
> the next experiment is chosen where they disagree most. I know the Oct 30 white-paper target has
> passed. Would you advise applying by Dec 14 or in the next cycle, and is the deactivation
> mechanism, rather than the films themselves, the right emphasis for Catalysis Science?
>
> Best regards,
> Sterling Baird
