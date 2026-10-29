#!/usr/bin/env python3
"""One low-effort Edison LITERATURE query per claim in Reviewer B's 2026 PRF review.

The review itself is ACS material and is not in this repo (see
grants/acs-prf/REVIEW_2026.md for the paraphrased digest). Each claim below is a
paraphrase, and each query is phrased as an open question so that Edison is not
handed the reviewer's conclusion to confirm.

Usage (EDISON_PLATFORM_API_KEY must be set):
    python scripts/edison/review_b_claims.py submit   # submit every query not yet submitted
    python scripts/edison/review_b_claims.py wait     # block until all tasks finish (one foreground call)
    python scripts/edison/review_b_claims.py fetch    # write answers and full task dumps
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import httpx
from edison_client import EdisonClient, JobNames, TaskRequest

HERE = Path(__file__).resolve().parents[2]
OUT = HERE / "edison-trajectories" / "review-b-claims"
TASK_IDS = OUT / "_task_ids.json"
TERMINAL = {"success", "fail", "failed", "cancelled", "error", "crashed", "truncated"}
POLL_S = int(os.environ.get("EDISON_POLL_S", "120"))
MAX_WAIT_S = int(os.environ.get("EDISON_MAX_WAIT_S", "3300"))

# (id, review point, paraphrased claim, query)
CLAIMS = [
    ("F1a", "decisive flaw 1",
     "The proposal assumes it knows which Fe solid precipitates.",
     "What solid phases form when dissolved Fe(II) and sulfide are mixed in NaCl solutions at pH 4-9 "
     "and 25-90 C (for example nanocrystalline or disordered mackinawite, crystalline mackinawite, "
     "greigite, pyrrhotite, Fe(OH)2, or siderite when bicarbonate is present)? How does the identity "
     "of the first-formed solid depend on time, temperature and supersaturation, and how have studies "
     "identified the phase (XRD, Raman, Mossbauer)?"),
    ("F1b", "decisive flaw 1",
     "The proposal assumes it knows which Pb solid precipitates.",
     "Which lead solids can precipitate in aqueous Pb(II)-NaCl-sulfide-carbonate-sulfate systems at "
     "pH 4-9 and 25-90 C (galena, cotunnite PbCl2, laurionite PbOHCl, phosgenite, cerussite, "
     "hydrocerussite, anglesite)? Under what Pb, chloride, carbonate and pH conditions do chloride or "
     "carbonate lead phases form instead of, or alongside, PbS?"),
    ("F2a", "decisive flaw 2",
     "Precipitation onset within hours does not mark equilibrium solubility.",
     "Does the onset of FeS or PbS precipitation detected within minutes to hours of mixing correspond "
     "to equilibrium solubility? What do studies report on nucleation supersaturation thresholds, "
     "induction times, and the time needed to reach solubility equilibrium for iron and lead sulfides, "
     "and how have sulfide solubility studies shown equilibrium, for example by approaching it from "
     "both undersaturation and supersaturation?"),
    ("F2b", "decisive flaw 2",
     "FeS ages, so its apparent solubility drifts with time.",
     "How does the apparent solubility of freshly precipitated FeS change as disordered or "
     "nanocrystalline mackinawite ages or transforms, and what solubility constants have been reported "
     "for amorphous FeS versus crystalline mackinawite, troilite and pyrrhotite?"),
    ("F3", "decisive flaw 3",
     "Pitzer's design aims at a minimal parameter set; not every parameter needs fitting.",
     "What was the original rationale for how Pitzer ion-interaction model parameters should be "
     "obtained: binary parameters (beta0, beta1, Cphi) from single-salt solution data and mixing "
     "parameters (theta, psi) from two-salt common-ion mixtures, using as few adjustable parameters as "
     "possible? Which papers by Pitzer and coworkers set this out, and when are mixing terms omitted?"),
    ("P0", "opening",
     "Organic acids shift FeS/PbS solubility mostly through complexation, not activity coefficients.",
     "In NaCl brines, how much do acetate and other short-chain carboxylates change Fe(II) and Pb(II) "
     "speciation and the solubility of FeS and PbS? Is this effect usually modeled with aqueous "
     "complex-formation constants (for example FeOAc+, PbOAc+, Pb(OAc)2 aq) rather than with "
     "ion-interaction activity coefficients?"),
    ("P1a", "point 1",
     "The Debye-Hueckel limiting law holds to about I 0.1 for dissociated salts and below 0.01 for associating salts such as PbCl2.",
     "Up to what ionic strength does the Debye-Hueckel limiting law reproduce measured activity or "
     "osmotic coefficients within experimental accuracy, for fully dissociated 1:1 salts and for salts "
     "that hydrolyze or form ion pairs, such as PbCl2 or 2:1 transition-metal chlorides?"),
    ("P1b", "point 1",
     "FeS and PbS solubilities between pH 4 and 9 are millimolal or lower.",
     "What total dissolved Fe and Pb concentrations have been measured in equilibrium with mackinawite "
     "FeS and with galena PbS between pH 4 and 9 at 25 C, in water and in NaCl solutions? Are they "
     "millimolal or lower?"),
    ("P1c", "point 1",
     "FeS/PbS solubility can be reproduced with Ksp, complex constants, the limiting law and background-salt Pitzer terms alone.",
     "Have FeS or PbS solubilities in NaCl or other chloride brines been modeled successfully using only "
     "solubility products, aqueous complex constants (for example FeHS+, Pb(HS)2 aq, PbCl_n complexes) "
     "and activity coefficients of the background electrolyte, without any Fe-HS or Pb-HS "
     "ion-interaction (Pitzer) parameters?"),
    ("P1d", "point 1",
     "Na+-HS- interactions can be measured in NaHS solutions.",
     "What Pitzer parameters have been published for Na+-HS- and other major cation-bisulfide "
     "interactions, and from what data were they derived (NaHS solutions, H2S dissociation constants "
     "in ionic media, H2S solubility in salt solutions)?"),
    ("P1e", "point 1",
     "Others have published unjustified metal-bisulfide Pitzer terms; that does not justify repeating them.",
     "Have any researchers published Pitzer ion-interaction parameters (beta0, beta1, Cphi, theta, psi) "
     "for Fe2+-HS-, Pb2+-HS- or Zn2+-HS- interactions, for example in oilfield scale-prediction models? "
     "If so, what data were they fitted to, and have they been criticized?"),
    ("P2a", "point 2",
     "The design resembles the constant-ionic-medium method, which fits solubility and complex constants with no Pitzer terms.",
     "How has the constant ionic medium (swamping electrolyte) method been used to determine solubility "
     "products and complex formation constants of sparingly soluble metal sulfides, or of Fe(II) and "
     "Pb(II) with acetate? Which studies measured FeS or PbS solubility in NaCl or NaClO4 media with or "
     "without added acetate?"),
    ("P2b", "point 2",
     "Metal-acetate complex constants are the adjustable quantities in such a design.",
     "What stability constants, and what temperature dependence, have been reported for Pb(II)-acetate "
     "and Fe(II)-acetate complexes in aqueous solution, including at elevated temperature and in NaCl "
     "media?"),
    ("P3a", "point 3",
     "In a two-salt solubility experiment, one salt's parameters and the mixing terms must be known in advance.",
     "When Pitzer parameters are fitted to solubility data for a ternary system (for example a sparingly "
     "soluble salt in NaCl solutions), can the binary and mixing parameters be resolved separately, or "
     "must the background-salt and mixing parameters be fixed from independent data? Are there "
     "published discussions of parameter correlation in such fits?"),
    ("P3b", "point 3",
     "theta(Cl,OAc) and psi(Na,Cl,OAc) need NaCl-NaOAc-H2O data.",
     "Have the Pitzer mixing parameters theta(Cl-, acetate) and psi(Na+, Cl-, acetate) been determined "
     "from isopiestic, EMF, solubility or other data on NaCl-sodium acetate-water mixtures?"),
    ("P3c", "point 3",
     "Pitzer parameters for Fe(OAc)2 and Pb(OAc)2 are missing, and no isopiestic data exist for them.",
     "Are there isopiestic, vapor-pressure, osmotic-coefficient, freezing-point or EMF data for aqueous "
     "lead(II) acetate or iron(II) acetate solutions, and have Pitzer parameters been derived for "
     "Pb(OAc)2 or Fe(OAc)2?"),
    ("P3d", "point 3",
     "Freezing-point depression would work, and the platform could be adapted to measure it.",
     "How are freezing-point depression measurements used to derive osmotic coefficients and Pitzer "
     "parameters for electrolyte solutions, and have automated, small-volume or multi-well "
     "freezing-point or osmometry methods reached the accuracy needed for this?"),
    ("P4a", "point 4",
     "Millero and Byrne (1984) used ZnCl2 as a stand-in for PbCl2.",
     "What Pitzer parameters did Millero and Byrne (1984) use for Pb2+-Cl- interactions when modeling "
     "lead chloride complexation in seawater and NaCl solutions, and were these based on ZnCl2 or "
     "another analog salt?"),
    ("P4b", "points 4 and 8",
     "PbCl2 is below 0.05 mol/kg in water and appreciably more soluble in other chloride solutions.",
     "What is the solubility of PbCl2 in pure water at 25 C, and how does it change with NaCl, CaCl2 "
     "or other chloride concentration and with temperature?"),
    ("P4c", "point 4",
     "Felmy et al. (2000) rest on Kendall and Sloan (1925), whose solid was later shown to be misidentified.",
     "Is the 1925 Kendall and Sloan dataset on PbCl2 solubility in NaCl solutions considered reliable? "
     "Have later studies found that the solid phase in those experiments was not PbCl2 (for example a "
     "double salt or a basic lead chloride), and which later PbCl2-NaCl-H2O solubility studies exist?"),
    ("P4d", "point 4",
     "Felmy et al. added dependent parameters, including a C term for Na-PbCl4 with no matching B term.",
     "What Pitzer parameters did Felmy et al. (2000) include in their Pb-Na-K-Ca-Mg-H-Cl-SO4-H2O model, "
     "such as theta(Na,Pb), B(Na,PbCl3-) and C(Na,PbCl4 2-)? Is it considered physically justified to "
     "include a third virial coefficient for an ion pair without the corresponding second virial "
     "(beta0/beta1) terms?"),
    ("P4f", "point 4",
     "The Rice University group's Pb parameters share the same trace-ion problem.",
     "What Pitzer parameters for Pb2+, Zn2+ or Fe2+ interactions with HS-, Cl- and other ions have been "
     "published by the Rice University Brine Chemistry Consortium (Tomson, Kan, Zhang and coworkers) "
     "for sulfide scale prediction, and how were they determined?"),
    ("P5a", "point 5",
     "Mixing parameters should come from two-salt common-ion systems.",
     "From what kinds of experimental systems are Pitzer cation-cation mixing parameters (theta, psi) "
     "conventionally determined, such as two-salt common-ion mixtures like NaCl-KCl-H2O? Is it "
     "considered valid to derive theta for two cations when one or both are present only at trace "
     "concentrations?"),
    ("P5b", "point 5",
     "theta(Pb,Fe) cannot come from sulfide or sulfate systems; it would need something like Pb(OAc)2 + Fe(OAc)2 + H2O.",
     "Have Pitzer mixing parameters theta(Pb2+, Fe2+) or psi(Pb2+, Fe2+, anion) ever been determined, "
     "and if so from what systems?"),
    ("P6a", "point 6",
     "Pitzer and Mayorga (1973) used no C term below I of about 2 mol/kg.",
     "In Pitzer and Mayorga (1973), how were the third virial coefficients (Cphi) determined, and for "
     "which electrolytes or below what molality or ionic strength were Cphi terms omitted?"),
    ("P6b", "point 6",
     "PbSO4 solubility is below 1 mmol/kg and does not rise much in other salts.",
     "What is the solubility of PbSO4 (anglesite) in pure water at 25 C, and how much does it increase "
     "in NaCl and other salt solutions?"),
    ("P6c", "point 6",
     "Paige et al. (1992) used beta2 for PbSO4 to mimic the PbSO4 ion pair.",
     "How did Paige et al. (1992) represent lead sulfate in their Pitzer model, and did they use a "
     "beta(2) term to represent PbSO4 ion pairing instead of an explicit association constant?"),
    ("P6d", "point 6",
     "beta2 was a computational convenience; explicit ion-pair constants can match or beat it with fewer parameters.",
     "Why did Pitzer introduce the beta(2) parameter for 2:2 electrolytes, and how do Pitzer models that "
     "use beta(2) compare with models that use explicit ion-pair formation constants (for example "
     "CaSO4, MgSO4, BaSO4 or PbSO4 aqueous complexes) in accuracy and range?"),
    ("P6e", "point 6",
     "The Rice group fitted barite solubility with only beta2 for Ba-SO4.",
     "In the Rice University (Tomson, Kan and coworkers) Pitzer models for barite solubility in brines, "
     "which Ba2+-SO42- Pitzer parameters were used (for example only beta(2) without beta0 or beta1), "
     "and could an explicit BaSO4 association constant fit the same data?"),
    ("P6f", "point 6",
     "Na-Fe mixing terms should come from independent data where the ions are concentrated (Moog et al. 2004; Chou and Phan 1985).",
     "What Pitzer mixing parameters have been published for Na+-Fe2+ (theta(Na,Fe), psi(Na,Fe,Cl)) and "
     "from what data, for example NaCl-FeCl2-H2O solubility (Chou and Phan 1985) or isopiestic data "
     "for FeCl2 mixtures (Moog et al. 2004)?"),
    ("P7a", "point 7",
     "Complex-formation constants and B terms overlap, e.g. K(PbOAc+) against B(Pb,OAc).",
     "In Pitzer models that include explicit ion pairs or complexes, how strongly are the association "
     "constants (for example K for PbOAc+ or CaSO4 aq) correlated with the binary interaction "
     "parameters for the same ions, and how has this non-uniqueness been handled?"),
    ("P7b", "point 7",
     "Solubility data alone leave beta0 and beta1 poorly constrained, especially when both salts are very soluble.",
     "Can Pitzer binary parameters beta0 and beta1 be determined reliably from solid-solubility data "
     "alone, especially when both salts in the system are very soluble (above about 2 mol/kg)? Why did "
     "Pitzer and coworkers rely on osmotic, isopiestic and EMF data for homogeneous solutions instead?"),
    ("P8a", "point 8",
     "Enough thermal data exist for NaOAc and Na propanoate to build temperature-dependent models.",
     "Have temperature-dependent Pitzer parameters been published for aqueous sodium acetate and sodium "
     "propanoate, and what heat-capacity, enthalpy-of-dilution and vapor-pressure data support them?"),
    ("P8b", "point 8",
     "Enough thermal data exist for FeCl2 to build a temperature-dependent model.",
     "Have temperature-dependent Pitzer parameters for aqueous FeCl2 been published, and what heat "
     "capacity, enthalpy of dilution, vapor pressure and solubility data exist for FeCl2 solutions above "
     "25 C?"),
    ("P8c", "point 8",
     "A temperature-dependent PbCl2 model may not be possible from existing data.",
     "Are there temperature-dependent Pitzer models for PbCl2 or Pb(II)-chloride systems from 25 to 90 C "
     "or higher, and what PbCl2 solubility, heat capacity or enthalpy data support them?"),
    ("P8d", "point 8",
     "No temperature-dependent model exists for Pb(OAc)2, and Fe(OAc)2 has essentially no thermodynamic data.",
     "What thermodynamic data exist for aqueous lead(II) acetate and iron(II) acetate above 25 C, such "
     "as stability constants, heat capacities, enthalpies, solubilities or activity coefficients?"),
    ("P9a", "point 9",
     "PHREEQC has several Pitzer databases of uneven quality; adding entries is easy, consistency is the work.",
     "What Pitzer databases exist for PHREEQC (pitzer.dat, THEREDA, the Bozau gebo extension and "
     "others), how do they treat Fe(II) and Pb(II), and what internal-consistency problems have been "
     "reported when parameter sets from different sources are combined?"),
    ("P9b", "point 9",
     "theta(Na,Pb) from Na-Pb-NO3 data is far better constrained than one from Na-Pb-Cl data.",
     "Has the Pitzer mixing parameter theta(Na+, Pb2+) been determined from data for the NaNO3-Pb(NO3)2-"
     "H2O system (solubility or isopiestic), and how does it compare with values derived from Na-Pb-Cl "
     "systems?"),
    ("P10a", "point 10a",
     "Na-Ca mixing parameters have been measured (Holmes et al. 1981; Oakes et al. 1998).",
     "What Pitzer mixing parameters theta(Na,Ca) and psi(Na,Ca,Cl) were determined by Holmes, Baes and "
     "Mesmer (1981) and by Oakes, Pitzer and Sterner (1998), from what measurements and over what "
     "temperature range?"),
    ("P10b", "point 10b",
     "NaNO3 is fitted to about 11 mol/kg with only beta0 and beta1 (Marion 2002).",
     "Up to what molality can the Pitzer model reproduce osmotic and activity coefficients of aqueous "
     "NaNO3 at 25 C, and is a Cphi term needed? What parameters did Marion (2002) use for NaNO3?"),
    ("P10b2", "point 10b",
     "The Pitzer model does not generally fail above I of about 2 mol/kg.",
     "How accurate are Pitzer ion-interaction models for concentrated salt systems and natural brines "
     "above an ionic strength of 2 mol/kg, for example the Harvie-Moller-Weare model, and where do "
     "they break down?"),
    ("P10c", "point 10c",
     "FeS/PbS model misfits come from pH2S handling, model construction, equilibrium constants or bad data, not missing mixing terms.",
     "What explanations have been given for disagreement between modeled and measured solubilities of "
     "mackinawite or galena in brines, such as uncertainty in the second dissociation constant of H2S, "
     "uncontrolled H2S partial pressure, inaccurate bisulfide complex constants, or experimental error?"),
    ("P11", "point 11",
     "OLI is not Pitzer-based; its MSE databanks are proprietary and its aqueous model is Bromley's.",
     "What activity-coefficient models does the OLI Systems software use (its aqueous model and the "
     "mixed-solvent electrolyte MSE model), are they based on the Pitzer equations, and are their "
     "parameter databanks published or proprietary?"),
    ("P12", "point 12",
     "Sulfide solubility needs controlled pH2S; H2S escaping from the plate leaves an open, non-equilibrium system.",
     "How do FeS and PbS solubility studies control H2S partial pressure, and what errors arise when H2S "
     "degasses from open vessels or microplates during sulfide precipitation experiments?"),
    ("P13", "point 13",
     "ICP-OES is inaccurate for high-ionic-strength samples because of dilution errors.",
     "What are the main sources of inaccuracy when measuring dissolved Fe and Pb by ICP-OES in "
     "high-salinity brines (dilution error, matrix and easily ionized element effects), and what "
     "practices are recommended, such as gravimetric dilution, matrix matching, internal standards, "
     "standard addition or ICP-MS?"),
    ("P14", "point 14",
     "pH buffers complicate the experiment and add nothing; pH is not an independent variable.",
     "In thermodynamic solubility studies of metal sulfides or carbonates in brines, are pH buffers "
     "(Good's buffers such as MES and HEPES, or bicarbonate) used or avoided, and do these buffers "
     "complex Pb(II) or Fe(II)? Is pH treated as a controlled variable or as a measured quantity set by "
     "composition and gas partial pressure?"),
    ("P15a", "point 15",
     "Fitting Pitzer parameters through log(Q/Ksp) is a mistake; single-salt data resolve them better.",
     "Have Pitzer parameters been regressed successfully from saturation-index (log Q/Ksp) or "
     "precipitation-boundary data, and what pitfalls are known compared with fitting osmotic or "
     "activity coefficients of single-salt solutions?"),
    ("P15b", "point 15",
     "Taking water activity as 1 in Ksp expressions would be inconsistent at these conditions.",
     "How large is the error from assuming water activity equals 1 in solubility-product calculations "
     "for minerals in concentrated NaCl brines (for example 1-6 mol/kg), particularly for hydrated "
     "solids or dissolution reactions that involve water?"),
]


def _client() -> EdisonClient:
    key = (os.environ.get("EDISON_PLATFORM_API_KEY") or "").strip()
    if not key:
        raise SystemExit("EDISON_PLATFORM_API_KEY is not set")
    return EdisonClient(api_key=key)


def _load_ids() -> dict:
    return json.loads(TASK_IDS.read_text()) if TASK_IDS.exists() else {}


def _create(client: EdisonClient, query: str) -> str:
    """Submit one task, waiting out Edison's per-user rate limit (HTTP 429)."""
    start = time.time()
    while True:
        try:
            return str(client.create_task(TaskRequest(name=JobNames.LITERATURE, query=query)))
        except httpx.HTTPStatusError as e:
            if e.response.status_code != 429 or time.time() - start > MAX_WAIT_S:
                raise
            print("rate limited; retrying in 60 s", flush=True)
            time.sleep(60)


def submit() -> None:
    client = _client()
    OUT.mkdir(parents=True, exist_ok=True)
    ids = _load_ids()
    for cid, point, claim, query in CLAIMS:
        if cid in ids:
            continue
        task_id = _create(client, query)
        ids[cid] = {"task_id": task_id, "point": point, "claim": claim, "query": query,
                    "job": JobNames.LITERATURE.value,
                    "submitted": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        TASK_IDS.write_text(json.dumps(ids, indent=2))
        print("submitted", cid, task_id, flush=True)
    print(len(ids), "tasks recorded in", TASK_IDS)


def _status(client: EdisonClient, task_id: str) -> str:
    return str(client.get_task(task_id).status).lower()


def wait() -> None:
    client = _client()
    ids = _load_ids()
    start = time.time()
    while True:
        statuses = {cid: _status(client, v["task_id"]) for cid, v in ids.items()}
        done = [c for c, s in statuses.items() if s in TERMINAL]
        print(time.strftime("%H:%M:%S"), f"{len(done)}/{len(ids)} finished",
              {s: list(statuses.values()).count(s) for s in set(statuses.values())}, flush=True)
        if len(done) == len(ids) or time.time() - start > MAX_WAIT_S:
            break
        time.sleep(POLL_S)


def _answer(dump: dict) -> str:
    for key in ("formatted_answer", "answer"):
        if dump.get(key):
            return dump[key]
    try:
        state = dump["environment_frame"]["state"]["state"]
        return state.get("formatted_answer") or state.get("answer") or ""
    except (KeyError, TypeError, AttributeError):
        return ""


def fetch() -> None:
    client = _client()
    ids = _load_ids()
    for cid, v in ids.items():
        task = client.get_task(v["task_id"], verbose=True)
        dump = task.model_dump(mode="json")
        status = str(dump.get("status", "")).lower()
        (OUT / f"{cid}.json").write_text(json.dumps(dump, indent=2, default=str))
        answer = _answer(dump)
        header = (f"# {cid} ({v['point']})\n\n"
                  f"**Claim (paraphrased):** {v['claim']}\n\n"
                  f"**Query** (Edison `{v['job']}`, task `{v['task_id']}`, status `{status}`):\n\n"
                  f"> {v['query']}\n\n---\n\n")
        (OUT / f"{cid}.md").write_text(header + (answer or "_No answer returned._") + "\n")
        print(cid, status, len(answer), "chars", flush=True)


if __name__ == "__main__":
    {"submit": submit, "wait": wait, "fetch": fetch}[sys.argv[1]]()
