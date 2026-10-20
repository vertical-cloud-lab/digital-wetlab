"""Evaluate whether organic-organic Pitzer interaction parameters should be
included in the ACS PRF proposal, addressing reviewer feedback from
Barry Bickmore.

Uses Edison Scientific literature search to assess whether omitting
organic-organic parameters (e.g., theta(OAc-Prop), psi(OAc-Prop-Na))
is scientifically justified or represents a significant gap.

Usage:
    export EDISON_API_KEY='your_api_key'
    python organic_organic_evaluation.py
"""

import os
import sys

from edison_client import EdisonClient, JobNames

EDISON_API_KEY = os.environ.get("EDISON_API_KEY")
if not EDISON_API_KEY:
    print("Error: EDISON_API_KEY environment variable is not set.")
    sys.exit(1)

QUERY = (
    "In the Pitzer ion-interaction model for electrolyte solutions, when a system "
    "contains multiple organic acid anions (e.g., acetate and propionate) alongside "
    "inorganic ions (Na+, Ca2+, Cl-, HS-) at high ionic strength (1-5 molal), how "
    "significant are the organic-organic anion interaction parameters? Specifically: "
    "(1) Are the like-charge mixing parameters theta(acetate-propionate) and ternary "
    "parameters psi(acetate-propionate-Na+) typically important for predicting mineral "
    "solubility and precipitation in concentrated brines? "
    "(2) What is the typical magnitude of organic acid concentrations (acetate, "
    "propionate) in petroleum produced waters relative to the dominant inorganic anions "
    "(Cl-, SO4^2-, HS-)? Are organic acids ever at concentrations where organic-organic "
    "interactions would meaningfully affect activity coefficients? "
    "(3) In the Pitzer framework, when minor anions (organic acids at millimolar "
    "concentrations) are present alongside dominant anions (Cl- at molar "
    "concentrations), do the minor-minor anion mixing parameters contribute "
    "significantly to activity coefficient calculations, or are they typically "
    "negligible compared to the dominant anion interactions? "
    "(4) Have any studies measured or estimated Pitzer theta or psi parameters for "
    "acetate-propionate or similar organic-organic anion pairs? If so, what are their "
    "magnitudes? "
    "(5) In produced-water geochemistry, is it standard practice to include or exclude "
    "organic-organic Pitzer interaction parameters when modeling mineral scale "
    "precipitation? What justification is typically given? "
    "Please cite specific papers and provide quantitative assessments where possible."
)

OUTPUT_FILE = "grants/acs-prf/ORGANIC_ORGANIC_EVALUATION.md"


def main():
    client = EdisonClient(api_key=EDISON_API_KEY)

    literature_job_name = getattr(JobNames, "LITERATURE_HIGH", JobNames.LITERATURE)
    job_label = str(
        literature_job_name.value
        if hasattr(literature_job_name, "value")
        else literature_job_name
    )

    print("Submitting organic-organic parameter evaluation query to Edison Scientific...")
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

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Organic–Organic Pitzer Parameter Evaluation — Edison Scientific\n\n")
        f.write(
            "> Generated via [Edison Scientific](https://edisonscientific.com/platform) "
            f"`{job_label}` search.\n"
        )
        f.write(
            "> Addresses reviewer feedback (Barry Bickmore, BYU) on the omission of "
            "organic–organic interaction parameters from the ACS PRF proposal.\n\n"
        )
        f.write("## Question Evaluated\n\n")
        f.write(
            "> Is the omission of organic–organic Pitzer interaction parameters "
            "(e.g., θ(OAc⁻–Prop⁻), ψ(OAc⁻–Prop⁻–Na⁺)) scientifically justified "
            "in a proposal focused on metal–sulfide and metal–organic acid interactions "
            "in produced-water brines?\n\n"
        )
        f.write("## Full Query\n\n")
        f.write(f"{QUERY}\n\n")
        f.write("## Edison Scientific Assessment\n\n")
        f.write(answer)
        f.write("\n")

    print(f"\nResults saved to {OUTPUT_FILE}")
    print("\n--- Answer ---\n")
    print(answer)


if __name__ == "__main__":
    main()
