"""Evaluate the quality of the ACS PRF DNI hypothesis using Edison Scientific.

Uses a high-effort literature search to assess the scientific validity,
novelty, and testability of the core hypothesis about Pitzer-model
predictions for sulfide-scale precipitation in produced-water brines.

Based on the updated draft proposal: "Systematic Experimental Validation
of Pitzer Activity-Coefficient Models for Sulfide-Scale Precipitation in
Produced-Water Brines" (Baird, BYU).

Usage:
    export EDISON_API_KEY='your_api_key'
    python hypothesis_evaluation.py
"""

import os
import sys

from edison_client import EdisonClient, JobNames

EDISON_API_KEY = os.environ.get("EDISON_API_KEY")
if not EDISON_API_KEY:
    print("Error: EDISON_API_KEY environment variable is not set.")
    sys.exit(1)

QUERY = (
    "Evaluate the following research hypothesis from a proposal titled "
    "'Systematic Experimental Validation of Pitzer Activity-Coefficient Models "
    "for Sulfide-Scale Precipitation in Produced-Water Brines': "
    "The hypothesis states that existing Pitzer models will accurately predict "
    "FeS (mackinawite) and PbS (galena) precipitation at low ionic strengths "
    "(I < 1 molal) but will systematically deviate at ionic strengths above ~2 molal. "
    "The proposed resolution is to fit a total of 34 target Pitzer parameters: "
    "6 binary (beta-0, beta-1, C-phi for Fe2+-HS- and Pb2+-HS-), "
    "8 mixing (theta_ij, psi_ijk for Fe2+/Pb2+ with Na+, Ca2+, Cl-), "
    "8 neutral-species (lambda_n,Na, lambda_n,Cl, zeta_n,Na,Cl, zeta_n,Ca,Cl "
    "for both FeSaq and PbSaq), 3 temperature-dependent Pb2+-Cl- coefficients, "
    "2 metal-hydroxide corrections, 3 Pb2+-SO4(2-) binary parameters "
    "(beta-0, beta-1, C-phi), and 4 PbCl2(0) neutral-species parameters "
    "(lambda_n,Na, lambda_n,Cl, zeta_n,Na,Cl, zeta_n,Ca,Cl). "
    "The experimental approach uses an Opentrons OT-2 robot with Latin hypercube "
    "sampling across 5 dimensions ([metal], [sulfide], ionic strength 0.5-5 molal, "
    "pH 4-9, temperature 25-90C) to generate ~30,000 experiments (initial LHS + "
    "Bayesian-optimization-guided follow-up) in 96-well plates, "
    "with tiered off-line detection (visual scoring, camera imaging, microplate reader). "
    "Results are compared to PHREEQC pitzer.dat predictions, and new parameters "
    "regressed where deviations exceed +/-0.2 SI units, validated via 5-fold CV "
    "and extrapolatory challenge splits. "
    "The proposal notes that PHREEQC pitzer.dat has Fe2+ parameters only for Cl- "
    "and SO4(2-) (no Fe2+-HS- or Fe2+-S2-), and zero Pb2+ parameters for any anion. "
    "Evaluate: (1) Are the 34 target parameters the right set, or are additional "
    "parameters still needed? "
    "(2) Is the proposed experimental design (~30,000 points with LHS + Bayesian "
    "optimization, 5D space, tiered detection) adequate to constrain 34 parameters? "
    "(3) What are the key risks — can Fe2+ oxidation be controlled in 96-well plates "
    "inside a glovebox, and is binary precipitation scoring sufficient for continuous "
    "Ksp regression? "
    "(4) Does the literature support the claim that mackinawite Ksp values vary by "
    "over an order of magnitude, and what is the current best estimate?"
)

OUTPUT_FILE = "grants/acs-prf/HYPOTHESIS_EVALUATION.md"


def main():
    client = EdisonClient(api_key=EDISON_API_KEY)

    literature_job_name = getattr(JobNames, "LITERATURE_HIGH", JobNames.LITERATURE)
    job_label = str(
        literature_job_name.value
        if hasattr(literature_job_name, "value")
        else literature_job_name
    )

    print("Submitting hypothesis evaluation query to Edison Scientific...")
    print(f"Query: {QUERY[:100]}...")
    print(f"Using {job_label} search mode.")
    print("This may take up to 10 minutes. Please wait...")

    task_data = {
        "name": literature_job_name,
        "query": QUERY,
    }

    responses = client.run_tasks_until_done(task_data)
    response = responses[0] if isinstance(responses, list) else responses

    answer = response.formatted_answer or response.answer

    hypothesis_text = (
        "Existing Pitzer models will accurately predict FeS and PbS precipitation "
        "at low ionic strengths (I < 1 molal) but will systematically deviate at "
        "ionic strengths above ~2 molal. The resolution is to fit a total of 34 "
        "target Pitzer parameters (6 binary, 8 mixing, 8 neutral-species for "
        "FeS⁰ₐq/PbS⁰ₐq, 3 temperature-dependent Pb²⁺–Cl⁻, 2 metal–hydroxide, "
        "3 Pb²⁺–SO₄²⁻ binary, and 4 PbCl₂⁰ neutral-species). Experimental "
        "validation via ~30,000 Opentrons OT-2 experiments using Latin hypercube "
        "sampling plus Bayesian-optimization-guided follow-up across "
        "[metal] × [sulfide] × ionic strength × pH × temperature, "
        "with PHREEQC pitzer.dat as the baseline model."
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Hypothesis Quality Evaluation — Edison Scientific\n\n")
        f.write(
            "> Generated via [Edison Scientific](https://edisonscientific.com/platform) "
            f"`{job_label}` search.\n"
        )
        f.write(
            "> Based on the updated draft proposal: *Systematic Experimental "
            "Validation of Pitzer Activity-Coefficient Models for Sulfide-Scale "
            "Precipitation in Produced-Water Brines* (Baird, BYU).\n\n"
        )
        f.write("## Hypothesis Evaluated\n\n")
        f.write(f"> {hypothesis_text}\n\n")
        f.write("## Evaluation Query\n\n")
        f.write(f"{QUERY}\n\n")
        f.write("## Edison Scientific Assessment\n\n")
        f.write(answer)
        f.write("\n")

    print(f"\nResults saved to {OUTPUT_FILE}")
    print("\n--- Answer ---\n")
    print(answer)


if __name__ == "__main__":
    main()
