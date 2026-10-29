# The 2026 DNI decision and Reviewer B

> Written 2026-10-29 from the decline letter and the one review ACS PRF sent, both posted in
> [PR 82](https://github.com/vertical-cloud-lab/digital-wetlab/pull/82). The review is ACS material and
> this repo is public, so the PDF is not committed and nothing below quotes it; every point is
> paraphrased. Line numbers refer to the submitted
> [`drafts/main_proposal_final.tex`](../../drafts/main_proposal_final.tex).

## The decision

- The panel rated the proposal not competitive and **does not recommend resubmission**.
- The program officer attached one long review by an expert (Reviewer B) and said the fundamental
  flaws it found weighed heavily in the decision. The letter refers to the reviews in the plural, so
  other reviews or a panel summary may exist. Ask for them.
- PRF's rules don't forbid resubmitting. A resubmission only has to state what changed, entered on the
  submission site
  ([proposal requirements](https://www.acs.org/funding/grants/petroleum-research-fund/applicants/proposal-requirements.html),
  checked 2026-10-29). Every DNI application counts toward the career limit of three, and two remain.
  How to use them is covered in the [funding doc](../alternative-funding/README.md#1-acs-prf-after-the-decline).

## Short version

The review has no complaint about the robot or the writing. Its objection is that the experiment
cannot produce the parameters it promises, because most of them should not exist. Fe²⁺ and HS⁻ (and
Pb²⁺ and HS⁻) never coexist at concentrations high enough for a Pitzer term between them to be
distinguished from the Debye–Hückel limiting law. It adds that a precipitate appearing within four
hours does not mark solubility, and that nothing in the plan identifies the solid that forms.

Almost every point holds, and each one traces to a specific line of the proposal. Revising the same
project would bring back the same objections.

The review also describes an experiment it would accept, and says the platform could run it (see
[What the review says would work](#what-the-review-says-would-work)).

## The three flaws the reviewer ranked as decisive

| Flaw (paraphrased) | Where the proposal does it | Holds? |
|---|---|---|
| It assumes the identity of the solid that precipitates | Precipitation is detected by absorbance and visual scoring (lines 81, 130), and the solids are taken to be mackinawite and galena (line 69). Nothing identifies the solid. Other solids are possible in the planned wells: PbCl₂ at high Pb and Cl, Fe(OH)₂ near pH 9, and siderite, cerussite or calcite from the bicarbonate buffer (line 122) | Yes |
| It assumes equilibrium is reached and bracketed within the experiment | Wells are read up to 240 minutes after mixing (line 130), and the regression treats precipitation onset as SI = 0 (line 188). Onset marks nucleation at some supersaturation that depends on time and detection limit. FeS also ages from disordered to crystalline mackinawite, so its apparent solubility drifts | Yes |
| It assumes every adjustable Pitzer parameter has to be fitted | The plan regresses "the full set of ~48 parameters" (line 188) and calls all 48 identifiable (line 151) | Yes |

## Why the Fe²⁺–HS⁻ and Pb²⁺–HS⁻ terms are not "missing"

This summarizes review points 1, 3, 5 and 6.

- Pitzer's design keeps the parameter count low. Binary terms come from single-salt solutions, and
  mixing terms (θ, ψ) come from two-salt solutions with a common ion.
- A binary term can only be measured where both ions are concentrated. FeS and PbS solubilities are
  millimolal or lower across pH 4–9. At those concentrations an Fe²⁺–HS⁻ interaction cannot be seen
  against the NaCl background, and a third-virial C term even less so. Pitzer and Mayorga (1973) used
  no C term below I ≈ 2 mol/kg.
- In strong NaCl, the activity coefficients of trace Fe²⁺, Pb²⁺ and HS⁻ are set by the background
  salt. Solubility then depends on the solubility product, the complex-formation constants (FeHS⁺,
  the PbClₙ complexes, Pb(HS)₂⁰, the metal–acetate complexes), the limiting law, and the known Pitzer
  terms of the background salts.
- The reviewer judges about half the parameters in Figure 1 unwarranted on this basis. One example is
  a C term for PbSO₄, whose solubility is below 1 mmol/kg. For PbSO₄, an explicit ion-pair formation
  constant can do the job that β⁽²⁾ does in Paige et al. (1992).
- θ_Pb,Fe cannot come from sulfide or sulfate systems, where one or both metals stay dilute. It would
  need a system like Pb(OAc)₂ + Fe(OAc)₂ + H₂O, and is worth fitting only if the binary terms fail
  there.
- *Our note, not the review's:* line 151 based identifiability on |∂SI/∂p| > 0.05 for each parameter
  on its own. A parameter can shift SI and still be unidentifiable if it is correlated with others.
  Identifiability needs the joint picture (Fisher information or profile likelihood), as the mock
  review had suggested.

**Our own rough check on the PbS design.** Galena's log K is −12.78 for PbS + H⁺ = Pb²⁺ + HS⁻
(wateq4f). At that value, the design's most dilute corner (10 µM Pb, 10 µM sulfide) is supersaturated
by about 4 log units at pH 4 and 12 at pH 9, assuming ideal activities and no complexes. Chloride
complexing in 5 mol/kg NaCl lowers that by roughly 4 units at most. The PbS boundary therefore lies
at the most acidic, most dilute, most saline corner of the design, and nearly every Pb well would have
precipitated whatever the Pitzer terms were. Mackinawite (log K −4.65) behaves differently: it crosses
SI = 0 inside the design, around pH 5–7.

## The other points

| Review point (paraphrased) | In the proposal | Holds? / what to do |
|---|---|---|
| **2.** The composition design resembles the classical constant-medium ("swamping electrolyte") method. That method measures FeS or PbS solubility in NaCl, whose Pitzer terms are known and fixed, with or without a little acetate, and fits the solubility and complex-formation constants. Ideally no Pitzer term is fitted. The reviewer says the proposed design could do this | — | The most useful lead in the review ([below](#what-the-review-says-would-work)) |
| **3.** Getting Pb–acetate terms from Pb(OAc)₂ + NaCl solubility needs the Na–Cl, Na–OAc and Cl–OAc terms (and possibly Na–PbCl₃⁻) fixed first. NaCl + NaOAc + H₂O data would show whether ψ_Na,Cl,OAc matters | The hierarchical fit fixes only the Pb–Cl and Pb–SO₄ terms (line 196) | Holds |
| **3.** Pitzer parameters for Fe(OAc)₂ and Pb(OAc)₂ really are missing and would be useful, oil and gas included. Isopiestic data would be best but don't exist. Freezing-point depression would also work, and the platform could be adapted to measure it | Lines 50, 77 | The second lead in the review |
| **4.** The literature parameter sets were taken on trust: <br>• Woosley and Millero (2013) build on Millero and Byrne (1984), which used ZnCl₂ as a stand-in for PbCl₂. ZnCl₂ is very soluble and PbCl₂ is not, and the C_Pb,Cl term has no justification. <br>• Felmy et al. (2000) adopted those terms and added dependent ones: θ_Na,Pb, B_Na,PbCl₃, and C_Na,PbCl₄ without its B. Their model rests on one 1925 PbCl₂–NaCl dataset (Kendall and Sloan) whose solid was later shown to be misidentified. <br>• The Rice group's parameters have the same trace-ion problem | The proposal fixes these values (lines 147–149, 196) | Holds for the proposal, which used them without evaluating them. Felmy et al. do cite Kendall and Sloan (checked on OpenAlex). We have not yet read the later studies on that solid |
| **7.** Fitting β⁽⁰⁾ and β⁽¹⁾ from solubility alone has two problems. They overlap with complex-formation constants (K_PbOAc⁺ against B_Pb,OAc). And when both salts are very soluble, solubility data cover only high I, which leaves the B terms poorly constrained. This is why Pitzer worked from homogeneous-solution data | Lines 85, 188 | Holds |
| **8.** The 25–90 °C range is a problem. The reviewer was unsure whether temperature-dependent models exist for sodium acetate, sodium propionate, PbCl₂ or FeCl₂. There are none for Pb(OAc)₂, and no data at all for Fe(OAc)₂. Enough calorimetric and vapor-pressure data exist to build such models for the sodium salts and FeCl₂, but perhaps not for PbCl₂ | Lines 81, 124 | Holds. Work at 25 °C first |
| **9.** Adding parameter sets to a PHREEQC database is easy. The real work is making them consistent and deriving them from suitable data: a θ_Na,Pb from the Na–Pb–NO₃ system beats one from Na–Pb–Cl | The gap is framed as "pitzer.dat has no Pb²⁺" (line 97) | Holds. The gap is evaluated data, not database entries |
| **10a.** Na–Ca mixing parameters have been measured (Holmes et al. 1981; Oakes et al. 1998) | Line 71 | Holds. Na–Fe mixing data exist too (Chou and Phan 1985; Moog et al. 2004) |
| **10b.** The Pitzer model does not fail above I ≈ 2. For example, NaNO₃ is fitted to about 11 mol/kg with only β⁽⁰⁾ and β⁽¹⁾ (Marion 2002) | Line 99 | Holds |
| **10c.** FeS and PbS misfits do not come from missing mixing terms. Likelier causes are pH₂S handling, model construction, wrong equilibrium constants, or bad data | Line 200 | Holds |
| **11.** OLI is not Pitzer-based. Its mixed-solvent (MSE) databanks are proprietary, and its aqueous model is Bromley's | Lines 71, 200 | Holds. Line 200's promise of parameters for OLI databases can't be kept |
| **12.** Sulfide equilibria need a controlled pH₂S, just as carbonate solubility needs a controlled pCO₂. Wells that lose H₂S are open systems and can't reach equilibrium | Adhesive seals, fume hood (lines 107, 134) | Holds |
| **13.** ICP-OES on high-ionic-strength samples suffers from dilution errors, and precision gets mistaken for accuracy | ICP-OES on 5% of wells (lines 117, 188) | Partly. Gravimetric dilution, matrix-matched standards, an internal standard and a reference check address it |
| **14.** pH buffers complicate the chemistry and gain nothing, since pH follows from the composition rather than being set independently | MES, HEPES and bicarbonate (line 122) | Holds. Bicarbonate also adds carbonate solids. Measure pH in the brine rather than fix it |
| **15.** Fitting through log(Q/K_sp) is a mistake. Each γ in K_sp mixes contributions from several salt pairs, so the parameters are better fixed from single-salt systems. Assuming a_H₂O = 1 would also be inconsistent | SI as log(Q/K_sp) (line 147) | The first half holds. PHREEQC's Pitzer mode computes water activity, so the second half only affects hand-written K_sp expressions for hydrated solids |

## What the review says would work

These are the review's own suggestions.

1. **Constant-medium solubility.** Measure FeS and PbS solubility in NaCl, with the NaCl parameters
   fixed, with and without small amounts of acetate. Fit solubility products and complex-formation
   constants, not Pitzer terms. The reviewer says the proposed design could do this.
2. **Binary data for the metal carboxylates.** Measure freezing-point depression of Fe(OAc)₂ and
   Pb(OAc)₂ solutions, and of the propionates; isopiestic data are the gold standard. The reviewer
   calls these parameters missing and useful, and says an adapted platform could measure them.
3. **Mixing terms only from pairs of salts that share an ion**, such as Pb(OAc)₂ + Fe(OAc)₂ + H₂O.
   Fit them only if the binary terms fail there. NaCl + NaOAc + H₂O would test ψ_Na,Cl,OAc.
4. **Explicit ion-pair and complex constants** instead of β⁽²⁾ or extra virial terms.
5. **Lab practice:**
   - closed vessels with a known pH₂S;
   - solids identified (XRD or Raman) before and after;
   - equilibrium approached from under- and supersaturation until the two agree;
   - no buffers;
   - analytics checked for accuracy, not just precision.

For PbS, item 1 needs trace analysis (ICP-MS, or more acidic conditions). By the rough check above,
galena's equilibrium Pb in these brines is well under a micromole per kilogram over most of pH 4–9.
That is far below what ICP-OES can detect after a brine is diluted.

## Why the pre-submission checks missed this

- The AI mock review ([`MOCK_REVIEWER_FEEDBACK.md`](MOCK_REVIEWER_FEEDBACK.md)) raised several of the
  same practical points:
  - precipitation onset versus equilibrium;
  - metastable FeS phases;
  - too many correlated parameters;
  - how little a yes/no precipitation reading says;
  - the absence of isopiestic or EMF data.

  The submitted version answered these as fitting problems, with a sensitivity analysis,
  hierarchical fitting, and ICP-OES on 5% of wells.
- Neither the personas nor the Edison search ([`EDISON_PITZER_PARAMETER_SEARCH.md`](EDISON_PITZER_PARAMETER_SEARCH.md))
  asked whether Fe²⁺–HS⁻ and Pb²⁺–HS⁻ terms should exist. The mock review called the gap well
  identified.
- As far as the repo records, no one who read the draft works on electrolyte thermodynamics. Barry
  said as much about himself in [issue 64](https://github.com/vertical-cloud-lab/digital-wetlab/issues/64).
- **Lesson:** before the next proposal, get the experimental design (not the prose) read by someone who
  has published Pitzer parameters or solubility constants.

## Next steps

1. Ask the program officer for any other reviews and the panel summary.
2. Read the papers below. Start with Pitzer and Mayorga (1973) and the two Na–Fe mixing papers.
3. Bring in a solution-thermodynamics collaborator, as co-PI or named consultant, before writing
   again.
4. Validate the platform on measurements this reviewer would accept. First, the solubility of a
   well-studied salt in NaCl, approached from both sides, with the solid checked by XRD. Second,
   freezing points of NaCl solutions against literature osmotic coefficients. Then move to NaOAc, then
   Pb(OAc)₂.
5. Choose funders using the [funding doc](../alternative-funding/README.md).

## Papers the review cites

DOIs checked on Crossref and OpenAlex, 2026-10-29.

| Paper | Why it matters |
|---|---|
| Pitzer and Mayorga 1973, *J. Phys. Chem.* [10.1021/j100638a009](https://doi.org/10.1021/j100638a009) | Binary parameters; no C term below I ≈ 2 |
| Millero and Byrne 1984, *GCA* [10.1016/0016-7037(84)90206-0](https://doi.org/10.1016/0016-7037(84)90206-0) | Pb–Cl terms with ZnCl₂ as the stand-in |
| Woosley and Millero 2013, *Mar. Chem.* [10.1016/j.marchem.2012.11.004](https://doi.org/10.1016/j.marchem.2012.11.004) | Builds on Millero and Byrne; used by the proposal |
| Felmy et al. 2000, *GCA* [10.1016/S0016-7037(00)00454-3](https://doi.org/10.1016/S0016-7037(00)00454-3) | The proposal's Pb²⁺ baseline |
| Kendall and Sloan 1925, *JACS* [10.1021/ja01686a006](https://doi.org/10.1021/ja01686a006) | The chloride-solubility dataset Felmy et al. rely on |
| Paige et al. 1992, *GCA* [10.1016/0016-7037(92)90054-M](https://doi.org/10.1016/0016-7037(92)90054-M) | PbSO₄ handled with β⁽²⁾ |
| Holmes, Baes and Mesmer 1981, *J. Chem. Thermodyn.* [10.1016/0021-9614(81)80015-8](https://doi.org/10.1016/0021-9614(81)80015-8) | Na–Ca mixing from isopiestic data |
| Oakes, Pitzer and Sterner 1998, *GCA* [10.1016/S0016-7037(98)00041-6](https://doi.org/10.1016/S0016-7037(98)00041-6) | NaCl–CaCl₂–H₂O heats of dilution and mixing |
| Marion 2002, *GCA* [10.1016/S0016-7037(02)00857-8](https://doi.org/10.1016/S0016-7037(02)00857-8) | The review's example of the model working to high molality |
| Chou and Phan 1985, *J. Chem. Eng. Data* [10.1021/je00040a027](https://doi.org/10.1021/je00040a027) | NaCl–FeCl₂–H₂O solubility, for Na–Fe mixing |
| Moog, Hagemann and Rumyantsev 2004, *Z. Phys. Chem.* [10.1524/zpch.218.9.1063.41672](https://doi.org/10.1524/zpch.218.9.1063.41672) | Isopiestic FeCl₂ mixtures with Na, K, Mg and Ca chlorides |
