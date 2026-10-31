# Qualitative analysis on the OT-2: teaching people, and testing how AI reasons about chemistry

> Compiled 2026-10-31 for Sterling's comment on
> [PR 83](https://github.com/vertical-cloud-lab/digital-wetlab/pull/83): lean back into teaching and
> training, and go back to what Kevin Jablonka originally suggested, with a dual teaching/training
> and model-based chemical reasoning approach. This expands direction 6 of the [README](README.md).
> A deadline is **verified** only where the funder's own page was read on 2026-10-31, or on
> 2026-10-29 for rows taken from the README.

## Short answer

- **One task, two kinds of solver.** Students and AI agents get the same unknown salt solutions, the
  same reagent rack and the same robot. Each has to name the ions in as few tests as possible. The
  students' runs are the human baseline the AI benchmark needs. The agents' runs, and a model that
  scores every test by how much it narrowed the possibilities, are what the students learn from.
- **This is Kevin Jablonka's original design.** The repo's project description,
  [`opentrons-inorganic-wet-lab-agents.txt`](../../opentrons-inorganic-wet-lab-agents.txt), proposes
  qualitative inorganic analysis as a benchmark for LLM agents, in three tiers: data, agent
  benchmarking, and hypothesis-driven algorithms. It already asks for a comparison of AI with human
  chemists. Teaching supplies the humans.
- **It fixes direction 6's weakness.** Remote teaching on its own had little research novelty.
  Paired with the reasoning benchmark, the course gets a research question, and the benchmark gets
  hundreds of real runs a semester.
- **The robot needs almost nothing new**: a reagent rack, fixed lighting with a colour card, and the
  remote queue the colour-matching demo already uses. The chemistry is the kind of precipitation the
  lab has run since March, starting with its BaSO₄ plates, read by the same camera.
- **"Model-based" is the research hook.** An agent reasons from a model when it keeps the candidate
  answers still open, predicts what each test would show under each one (solubility and speciation
  from PHREEQC, plus a measured threshold for what becomes visible in the observation window), and
  picks the test expected to tell it the most. The open question is whether LLM agents do that or
  replay memorised schemes, and whether handing them the model closes the gap.
- **Where to send it.**
  - **Teaching half:** NSF IUSE: EDU Level 1 on **Jan 20, 2027**, if a chemistry-education partner
    signs on. Otherwise the NSF CyberTraining Pilot on **Jan 21**, with a cyberinfrastructure co-PI.
  - **Research half, with Kevin:** the NSF–DFG Lead Agency route in Chemistry, which takes proposals
    **any time** through NSF's chemistry programs (Chemical Theory, Models and Computational Methods,
    or Chemical Measurement and Imaging). So it can wait for pilot data. NSF's Genesis Mission letter
    names autonomous chemistry labs and AI-for-science workforce, and it attaches to either half.
  - **Agent runs:** API credits and a NAIRR Pilot allocation, both rolling.
  - **The whole design:** NSF CAREER (Jul 28, 2027), because CAREER requires research and education
    to be integrated.
- **First steps.** Write to Kevin to restart the collaboration. Run the ion-lottery pilot, corrected
  as below, in November and December as preliminary data. Apply for API credits now.

## Funding, Nov 2026 – Apr 2027

"Arm" says which half a program pays for. Rows marked (Oct 29) were verified for the README and not
re-read.

| By | What | Arm | Size | Catch | Status |
|---|---|---|---|---|---|
| Any time | [NSF–DFG Lead Agency, Chemistry and Chemical Process Systems (NSF 25-537)](https://www.nsf.gov/funding/opportunities/nsf-dfg-lead-agency-opportunity-chemistry-chemical-process/nsf25-537/solicitation), submitted through [MPS Chemistry, NSF 26-519](https://www.nsf.gov/funding/opportunities/mps-chem-mps-chemistry-research-programs/nsf26-519/solicitation) (CTMC or CMI) with the title prefix "NSF-DFG:". The side doing most of the research leads. If NSF leads, Kevin files the same proposal with DFG within 5 days ([DFG page](https://www.dfg.de/nsf-che-cbet)) | research | the host program's norms; each agency funds its own side | One NSF–DFG proposal per person per year, and it counts toward MPS Chemistry's limit of 2 per year (direction 2 or 4 may want one of those) | verified |
| Any time | [NSF Genesis Mission letter (NSF 26-023)](https://www.nsf.gov/funding/opportunities/dcl-unleashing-new-age-ai-enabled-scientific-discovery-through): names autonomous or semi-autonomous chemistry labs and AI-for-science workforce. It has no deadline of its own and rides on a host program; EDU is one of the participating directorates | both | the host program's | Title prefix "Genesis Mission:". Ask the IUSE program officer whether an IUSE proposal can carry it | verified |
| Rolling | [NAIRR Pilot](https://nairrpilot.org/opportunities/allocations) allocations: start-up (up to 2,000 GPU-hours or equivalent, 3 months), research (monthly cycle) and classroom. Partners include Anthropic, OpenAI, Google and AWS | both | compute and model access | Classroom allocations are for US-based participants only, so not for a joint course with Jena | verified |
| Rolling | [Anthropic AI for Science credits](https://www.anthropic.com/news/expanding-support-for-scientists) | research | up to $50K in API credits | | verified (Oct 29) |
| Rolling | [Google Cloud research credits](https://support.google.com/google-cloud-higher-ed/answer/10724468?hl=en) | research | up to $5,000 per faculty member | One award per person; 6–8 week decision | verified |
| Next review Dec 2026 | [OpenAI Researcher Access Program](https://grants.openai.com/prog/openai_researcher_access_program/) | research | up to $1,000 in API credits | Reviewed quarterly | verified |
| **Jan 20, 2027** | [NSF IUSE: EDU (NSF 23-510)](https://www.nsf.gov/funding/opportunities/iuse-edu-improving-undergraduate-stem-education-directorate-stem/nsf23-510/solicitation), Engaged Student Learning, Level 1 | teaching | up to $400K / 3 yr | At most 3 IUSE proposals per person a year. The solicitation doesn't mention AI, and NSF's AI-education push since the April 2025 executive order has been K-12, so pitch learning, not AI | verified |
| **Jan 21, 2027** | [NSF CyberTraining](https://www.nsf.gov/funding/opportunities/training-based-workforce-development-advanced) Pilot (CHE, DMR, CBET and CMMI take part) | training | up to $300K / 2 yr | Needs a co-PI with cyberinfrastructure expertise | verified (Oct 29) |
| **Feb 4, 2027** (target; any time) | [NSF CISE Future CoRe (NSF 25-543)](https://www.nsf.gov/funding/opportunities/future-core-computer-information-science-engineering-future-computing): Robust Intelligence or Human-Centered Computing for agents against students; Computing Education Research for the AI-literacy half | research (teaching through CER) | up to $1M / 4 yr; typically $150–250K a year | 2 proposals per person in any 12 months. The RI and HCC descriptions don't mention LLM agents, so email a program director first | verified |
| **Feb 4, 2027** | [Camille Dreyfus Teacher-Scholar](https://www.dreyfus.org/camille-dreyfus-teacher-scholar/) (BYU nominates one person) | both | $100K unrestricted | Aimed at chemistry departments; anyone else must be active in a PhD program and advancing the chemical sciences. The research-plus-teaching story is the right one for it | verified |
| **Mar 2, 2027** | [NSF PESOSE (NSF 26-506)](https://www.nsf.gov/funding/opportunities/pesose-pathways-enable-secure-open-source-ecosystems) Track 1, for the open task server and simulator | both | up to $300K / 1 yr | | verified (Oct 29) |
| Rolling | [Sloan Exploratory Grantmaking in Technology](https://sloan.org/programs/digital-technology/exploratory-grantmaking-in-technology) two-page letter (automation in science) | both | recent grants $82K–399K | | unverified |
| Jul 28, 2027 | [NSF CAREER](https://www.nsf.gov/funding/opportunities/career-faculty-early-career-development-program), after the window | both | at least $400K / 5 yr ($500K in Engineering) | One a year; see Risks | verified (PR 82) |

- **Closed or gone.** NSF IRES and AccelNet are archived, so there is no NSF route for student
  exchanges with Jena. RITEL has had no deadline since Nov 2025, ExLENT is waiting for a new
  solicitation, and EDU Core Research next comes round in Oct 2027. RCSA's Scialog: Automating
  Chemical Laboratories made its final awards in July 2026. Dreyfus has discontinued its machine
  learning program. The UK AI Security Institute's Challenge Fund is closed; it takes international
  universities if it reopens.
- **Couldn't confirm.** Coefficient Giving's capability-evaluation request for proposals (page
  blocked), and BYU's Mentoring Environment Grants, which colleges now run; ask the Fulton College
  dean's office. PR 82's notes list College of Engineering seed dates of Nov 15 and Mar 15, also
  unverified.
- **Wording.** NSF pages now say "Super Intelligence (SI)" in places where they used to say AI. Match
  the wording of whichever solicitation the proposal goes to.
- **Odds.** The [earlier reply](https://github.com/vertical-cloud-lab/digital-wetlab/pull/83#issuecomment-6527123274)
  has the base rates: about 18% across NSF in FY2025, and falling.

## What Kevin's group proposed

The project description was committed as a static copy on Feb 19, 2026 and is the one issues 1 and 4
point to. In short:

- **The task.** Given an unknown aqueous salt solution and a reagent set (acids, bases, precipitating
  and complexing agents), choose and run tests, watch for precipitates, colour changes and gas by
  camera, and name the cation and anion, all within a fixed volume of sample.
- **Why it makes a good benchmark.**
  - It needs multi-step deduction from solubility, acid–base, complexation and redox, not recall of
    properties.
  - Concentration-dependent observations are hard to memorise, because no large dataset of them
    exists.
  - Difficulty scales from one ion out of three to five, up to mixtures with interfering ions.
  - Robot experiments give ground truth.
- **Tier 1, data.** Precipitate colour, morphology, time to visible precipitate and settling at
  several concentrations, with colour-calibrated images and conductivity, to make the group's virtual
  wet lab realistic.
- **Tier 2, benchmarking.** LLM agents drive the Opentrons under the simulator's constraints.
  - Scoring: the cation–anion pair is right or wrong, with no partial credit. Tests used, sample
    volume and time are secondary metrics.
  - Pilot: an "ion lottery" of five unknowns drawn from three cations and four anions. Its success
    criteria include a camera that tells every precipitate apart and a baseline agent that solves at
    least one of the five.
- **Tier 3, algorithms.**
  - Minimal experiment sets, measured against an information-theoretic bound.
  - Belief tracking over the candidate ions, and entropy-based choice of the next test.
  - Neuro-symbolic agents that pair an LLM with a constraint solver.
  - A **relabelling ablation**: rename every reagent and observation ("Reagent-7", "Event-Type-3")
    and give only a composition table. An agent that recalls "AgCl is white" should fail; one that
    reasons from the table should only slow down.
  - The notes point to [arXiv:2507.00310](https://arxiv.org/abs/2507.00310) as the model for this
    tier.

Issue 1 then proposed finding the BYU general-chemistry instructors who teach these procedures, and
issue 2 tied the 10,000-experiment goal to the lab's Turing-benchmark thrust. The petroleum framing
came later, for the ACS PRF deadline.

## The dual design

### The shared task

- **The unknown** sits in a vial, beside a rack of about ten reagents.
- **One test** is the robot mixing, say, 50 µL of unknown with 50 µL of one reagent in a fresh well,
  then imaging it at fixed times. Kevin's plan used 0 s, 10 s, 30 s, 2 min and 10 min.
- **The solver** sees the images (or, in an abstracted mode, a structured observation) and either
  asks for another test or answers.
- **Scores.** Right or wrong; tests used against the optimum; sample used; wall-clock time.
- **One server takes every kind of request.** Students come in from a browser, agents from Python,
  and the simulator runs the same tasks offline. The colour-matching demo already works this way,
  with a quota-based queue and a livestream.

### Teaching and training

- **Who.** A general-chemistry lab section, which is where qualitative analysis is taught and what
  issue 1 suggested, or a course or workshop Sterling teaches. Because access is remote, a partner
  campus such as a two-year college can join.
- **What students do.** They solve unknowns on the robot.
  - After each test, the model shows how far that test narrowed the candidates, and which test would
    have narrowed them most.
  - At the end, they compare their path with the optimal one and with an AI agent's, and critique the
    agent's stated reasoning.
- **What they learn.** Solubility and equilibrium reasoning. Experimental design on a budget, which
  is the information-gain idea behind Bayesian optimisation. And judging when an AI is reasoning and
  when it is bluffing.
- **Training.** Upper-level students write their own agent or protocol against the same interface,
  the Opentrons HTTP API the lab already drives remotely. That is the CyberTraining framing.
- **Why a robot helps a teaching lab.**
  - Students never handle the silver, lead, barium or chromate.
  - A test uses about 100 µL instead of millilitres in a test tube, so there is far less waste.
  - Every decision is logged.
- **What gets measured**, which is what IUSE reviewers ask about first: concept questions on
  solubility and equilibria before and after, tests to solution against the optimum, correctness,
  and whether students get better at judging AI reasoning. This needs an education researcher or an
  external evaluator on the team.

### Model-based chemical reasoning

- **Solvers to compare.**
  1. An LLM agent alone, with real reagent names, so recall is available.
  2. The same agent with the reagents relabelled (Kevin's ablation).
  3. An LLM agent given the model as a tool: PHREEQC saturation indices for any mixture it proposes,
     and a belief state over the candidates that it has to update after each test.
  4. A Bayesian designer with no LLM, choosing tests by expected information gain under the same
     model. This is the ceiling for playing from the model.
  5. Students, before and after the module.
- **Questions.**
  - Do LLM agents update on evidence, or follow the textbook scheme whatever they see?
  - Does relabelling collapse them?
  - Does the model tool close the gap to the Bayesian designer?
  - Where does the model disagree with the robot?
- **Where the model breaks is the interesting part.**
  - Solubility rules fail near the borderline. Ag₂SO₄, PbCl₂ and PbBr₂ dissolve only to roughly
    0.01–0.02 M, so whether a test shows a precipitate depends on concentration, ionic strength and
    time.
  - A supersaturated well can stay clear for the whole observation window, because nucleation is
    slow. That is Reviewer B's point, that a precipitate appearing within four hours doesn't mark
    solubility, turned into part of the design.
  - So the observation model needs both the thermodynamics (PHREEQC, with activities) and a measured
    visibility threshold and induction time. The lab's BaSO₄ plates are the first calibration data
    for it.
- **Fit with the lab.**
  - Choosing tests by expected information gain is Bayesian experimental design, the advanced-BO
    thrust.
  - Calibrating the virtual wet lab against the robot until its runs can't be told from real ones is
    the Turing-benchmark idea in the
    [org profile](https://github.com/vertical-cloud-lab/.github/blob/main/profile/README.md).
  - Remote access is the cloud-lab theme.
  - The PHREEQC set-up already exists
    ([`preliminary_results/phreeqc_si_comparison.py`](../../preliminary_results/phreeqc_si_comparison.py)).

## Fixes before running Kevin's pilot

1. **Most of the pilot's unknowns can't be made.** The ion lottery pairs Ag⁺, Pb²⁺ and Ba²⁺ with Cl⁻,
   I⁻, SO₄²⁻ and CrO₄²⁻. Of those 12 salts, only BaCl₂ and BaI₂ dissolve at 0.1 M. Ag₂SO₄ and PbCl₂
   dissolve only to about 0.015 M, and the other eight are insoluble. Do what teaching labs do: give
   cation unknowns as nitrates, with NaNO₃ as the case where nothing precipitates, and anion unknowns
   as sodium or potassium salts. Or draw single salts from the roughly three dozen in Kevin's full ion
   set that do dissolve: every K⁺, Na⁺ and NH₄⁺ salt, the barium halides and nitrate, AgNO₃ and
   Pb(NO₃)₂.
2. **There's no fume hood in CB154.** Drop H₂S, (NH₄)₂S and the Na₂S task, since acid releases H₂S,
   or run those in the polishing-lab hood. Carbonate with acid gives only CO₂, which is fine. Use the
   dilute acids and bases where they work.
3. **Sample budget.** The simulator's 20 mL becomes 1–2 mL in a plate. Kevin's notes flag that the
   real lower limit has to be found; set it by the camera's detection limit first.
4. **Vision.** White, cream and pale-yellow silver halides look alike, and so do a yellow chromate
   solution and a yellow precipitate. Use fixed lighting, a colour card in every frame (Kevin's notes
   ask for one), the AS7341, and both a white and a black background.
5. **A fresh tip for every test.** Issue 12 planned to reuse tips. In qualitative analysis, a trace
   of Ag⁺ or Cl⁻ carried over gives a false positive.
6. **Waste.** Silver, lead, barium and chromium(VI) waste needs EHS sign-off. Small volumes keep
   it small.

## A worked example of the score

Take cation unknowns that are Ag⁺, Pb²⁺, Ba²⁺ or Na⁺ (as nitrates, 0.05–0.1 M), all equally likely.

- **Chloride first**, the textbook route, splits them two and two, so a second test is always
  needed: 2 tests.
- **Chromate first** gives brick-red Ag₂CrO₄, no precipitate (Na⁺), or a yellow one (Pb²⁺ or Ba²⁺).
  Only the yellow branch needs a second test, chloride or iodide, which precipitates Pb²⁺ and not
  Ba²⁺: 1.5 tests on average.
- **1.5 is the best possible** if the camera can't tell bright-yellow PbCrO₄ from paler BaCrO₄. No
  test here has more than three outcomes a camera can be sure of, so one test can settle at most two
  of the four candidates. If the camera *can* tell the two yellows apart, chromate alone settles all
  four, in one test.

So a test is only worth what the camera can resolve, which is why Tier 1 comes first. Scoring every
solver against the optimal tree is Kevin's "minimal experiment set" metric, and the same calculation
is the feedback students see.

<!-- PRECEDENTS -->

## Six-month plan

| When | Step | What it buys |
|---|---|---|
| Nov 2026 | Write to Kevin. Is the virtual wet lab still active, can the robot tasks match its constraints, and would his group co-author the benchmark and co-propose? | The design and the simulator are theirs |
| Nov 2026 | Meet the general-chemistry lab coordinators (as issue 1 proposed) and a chemistry-education researcher or evaluator | IUSE needs a host course and an evaluation plan |
| Nov 2026 | Apply for API credits | Agent runs through the spring |
| Nov – Dec | Tier 1 pilot: Kevin's Phase 1 reactions (the PbS one only in a hood) at 0.01, 0.05 and 0.1 M, imaged from 0 s to 10 min with a colour card; find the smallest volume per test the camera can read | Shows the camera can tell the precipitates apart; gives the first observation model |
| Dec | The corrected ion lottery on the robot, with one or two baseline agents, named and relabelled, and a few volunteer students | Preliminary data for January |
| Jan 20 or 21, 2027 | IUSE Level 1 (teaching-led) or CyberTraining Pilot (training-led). Pick one | |
| Jan – Apr | Classroom pilot in the winter semester; compare student and agent paths | Data for the CAREER and a first paper |
| Mar 2, 2027 | Optional: PESOSE Track 1 for the open task server and simulator | |
| Apr – May | Preprint of the first real-hardware results, with Kevin's group | A citable benchmark before the CAREER |
| Jul 28, 2027 | NSF CAREER with this as the integrated research and education plan, if it is chosen over the brine work | |

## Risks

- **Kevin's group may have moved on.** Ask first. The design stands without them, but the simulator
  and much of the benchmark's credibility are theirs.
- **Education evaluation needs a partner.** IUSE reviewers expect a learning-outcomes design and an
  evaluator, and Sterling is in Mechanical Engineering.
- **Throughput.** Each test waits up to 10 minutes for its images, and each test depends on the last,
  so one unknown can take most of an hour. The robot is free while wells develop, so queue several
  solvers at once, as the colour-matching demo does, and run most agent trials in the simulator,
  keeping the robot for ground truth.
- **Benchmark leakage.** Once published, tasks end up in training data. Random unknowns, relabelling
  and fresh robot observations limit the damage.
- **Agents driving a lab.** The chemistry is benign, and the agent acts only through a fixed reagent
  rack with volume limits the robot enforces. That sandbox is worth describing in any proposal.
- **One CAREER a year.** If this becomes the July 2027 CAREER, the brine CAREER in PR 82's notes waits.

## Decisions for Sterling

1. Confirm that the project description is Kevin's proposal, and whether to re-engage his group now.
2. Teaching-led (IUSE) or training-led (CyberTraining) in January. Either needs a partner on board by
   early December: an education researcher or evaluator for IUSE, a cyberinfrastructure co-PI for
   CyberTraining.
3. Which course hosts the classroom pilot.
4. Whether this or the brine work is the July 2027 CAREER.

## How this was put together

- **Read.** The project description; issues 1, 2, 4, 12, 24 and 79; the Feb 2026 funding guide for a
  US–German team ([`FUNDING_OPPORTUNITIES.md`](https://github.com/vertical-cloud-lab/digital-wetlab/blob/814b1ec/FUNDING_OPPORTUNITIES.md),
  from PR 5); PR 82's
  [funding notes](https://github.com/vertical-cloud-lab/digital-wetlab/blob/3d6ba0a/grants/alternative-funding/README.md)
  and [review digest](https://github.com/vertical-cloud-lab/digital-wetlab/blob/3d6ba0a/grants/acs-prf/REVIEW_2026.md);
  and the org profile.
- **Searched.** Two searches ran in parallel on 2026-10-31, one for funders (each date read on the
  funder's own page) and one for precedents (each DOI or arXiv ID checked).
- **Solubilities.** From standard 25 °C solubility products, without activity corrections. PHREEQC
  with activities would refine the borderline cases; that calculation is part of the proposed work.
