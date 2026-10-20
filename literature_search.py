"""Initial literature search using Edison Scientific platform.

Performs a literature search on LLM-based agents for qualitative
inorganic chemistry automation, relevant to the Digital Wetlab project.

Usage:
    export EDISON_API_KEY='your_api_key'
    python literature_search.py
"""

import os
import sys

from edison_client import EdisonClient, JobNames

EDISON_API_KEY = os.environ.get("EDISON_API_KEY")
if not EDISON_API_KEY:
    print("Error: EDISON_API_KEY environment variable is not set.")
    sys.exit(1)

QUERY = (
    "What are the recent advances in using large language model (LLM) based agents "
    "for automating qualitative inorganic chemical analysis, including systematic "
    "cation and anion identification schemes, and how have robotic liquid handling "
    "platforms such as Opentrons been integrated with AI-driven experimental planning "
    "in chemistry laboratories?"
)

OUTPUT_FILE = "literature_search_results.md"


def main():
    client = EdisonClient(api_key=EDISON_API_KEY)

    print(f"Submitting literature search query to Edison Scientific...")
    print(f"Query: {QUERY}")
    print("This may take up to 10 minutes. Please wait...")

    task_data = {
        "name": JobNames.LITERATURE,
        "query": QUERY,
    }

    responses = client.run_tasks_until_done(task_data)
    response = responses[0] if isinstance(responses, list) else responses

    answer = response.formatted_answer or response.answer

    with open(OUTPUT_FILE, "w") as f:
        f.write("# Literature Search Results\n\n")
        f.write("## Query\n\n")
        f.write(f"{QUERY}\n\n")
        f.write("## Results\n\n")
        f.write(answer)
        f.write("\n")

    print(f"\nResults saved to {OUTPUT_FILE}")
    print("\n--- Answer ---\n")
    print(answer)


if __name__ == "__main__":
    main()
