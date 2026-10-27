#!/usr/bin/env python3
"""Edison LITERATURE queries on how long deionized water keeps, and what open
containers do to it (issue 80, 2026-10-27).

Three queries run in parallel:

  q1  purity loss in storage: CO2 uptake, leaching from containers, airborne
      contamination, and what ISO 3696 / ASTM D1193 / CLSI / USP say
  q2  bacterial growth in stored distilled or deionized water
  q3  what dissolved O2 and CO2 in the water do to lead nitrate and sulfide
      stock solutions

`submit` writes the task ids to _task_ids.json so fetching can resume in a
later session. `wait` polls until every task is done (one blocking call, per
CLAUDE.md), then writes each answer and full task dump next to the task ids.

Usage:
    EDISON_PLATFORM_API_KEY=... python scripts/edison/di_water_storage.py submit
    EDISON_PLATFORM_API_KEY=... python scripts/edison/di_water_storage.py wait
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from edison_client import EdisonClient, JobNames, TaskRequest

HERE = Path(__file__).resolve().parents[2]
TRAJ = HERE / "edison-trajectories" / "di-water-storage"
SUBMITTED = TRAJ / "_task_ids.json"

TERMINAL = {"success", "fail", "failed", "cancelled", "error", "crashed", "truncated"}
POLL_S = int(os.environ.get("EDISON_POLL_S", "120"))

QUERIES = {
    "q1-storage-purity": """\
How quickly does the purity of laboratory deionized (DI) or ultrapure water
degrade after it leaves the purification system, and does it have a shelf
life? Report quantitative data from peer-reviewed studies and from the
standards, on:
(a) uptake of atmospheric CO2: how fast resistivity falls from 18.2 MOhm-cm
    (conductivity rises from 0.055 uS/cm) and pH falls toward about 5.6, in
    open versus closed containers;
(b) leaching of ions, silica, boron, metals and organic carbon (TOC) from
    storage containers (borosilicate glass, LDPE, HDPE, polypropylene,
    PTFE/PFA) over days to weeks;
(c) uptake of airborne contaminants (ammonia, acid vapours, dust, volatile
    organics) by open containers of water in a laboratory;
(d) what ISO 3696, ASTM D1193, CLSI GP40 and USP <645> say about storing
    reagent water of each grade, e.g. whether grade 1 / Type I water may be
    stored at all, for how long, and in what containers.
Distinguish water kept in sealed, completely filled containers from water
kept in open or partly filled containers for several days to several weeks.
""",
    "q2-bacteria-in-stored-water": """\
Do bacteria grow in deionized or distilled water stored at room temperature,
and how fast? Summarize peer-reviewed evidence on the growth of oligotrophic
bacteria (for example Pseudomonas aeruginosa, Burkholderia cepacia, Ralstonia
pickettii, Sphingomonas, Methylobacterium) in distilled, deionized or
ultrapure water: the cell densities reached over days to weeks, the effect of
container type and of leaving containers open or partly full, biofilm in
carboys, wash bottles and reservoirs, and recommendations on how long
purified water can be kept before use and how often storage containers should
be cleaned or replaced.
""",
    "q3-o2-co2-and-lead-sulfide-stocks": """\
When millimolar stock solutions of lead(II) nitrate and of ammonium sulfide
(or sodium hydrosulfide) are made up in deionized water for lead sulfide
precipitation experiments, how much do the dissolved oxygen and dissolved CO2
of air-equilibrated water matter? Summarize kinetic studies of the oxidation
of aqueous sulfide by dissolved O2 (rate laws, half-lives at micromolar to
millimolar sulfide and pH 7 to 10, catalysis by trace metals), loss of H2S
from open containers, formation of polysulfide and thiosulfate, and any
evidence that CO2 from air forms lead carbonate or basic lead carbonate in
dilute lead solutions. Include recommended practice from the literature, such
as deoxygenating water by N2 sparging or boiling, making sulfide stocks fresh
each day, and storing them in sealed, completely filled containers.
""",
}


def _client() -> EdisonClient:
    api_key = (os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY") or "").strip()
    if not api_key:
        raise SystemExit("No EDISON_PLATFORM_API_KEY / EDISON_API_KEY in environment")
    return EdisonClient(api_key=api_key)


def _extract_answer(dump: dict) -> str:
    if dump.get("formatted_answer"):
        return dump["formatted_answer"]
    if dump.get("answer"):
        return dump["answer"]
    try:
        return dump["environment_frame"]["state"]["state"]["answer"] or ""
    except (KeyError, TypeError):
        return ""


def submit() -> None:
    client = _client()
    ids = {}
    for key, query in QUERIES.items():
        task_id = str(client.create_task(TaskRequest(name=JobNames.LITERATURE, query=query)))
        print("submitted", key, task_id, flush=True)
        ids[key] = task_id
    TRAJ.mkdir(parents=True, exist_ok=True)
    SUBMITTED.write_text(json.dumps(ids, indent=2) + "\n")
    print("wrote", SUBMITTED)


def wait() -> None:
    client = _client()
    ids = json.loads(SUBMITTED.read_text())
    pending = dict(ids)
    while pending:
        for key, task_id in list(pending.items()):
            dump = client.get_task(task_id=task_id, verbose=True).model_dump(mode="json")
            status = str(dump.get("status", "")).lower()
            print(time.strftime("%H:%M:%S"), key, "status:", status, flush=True)
            if status not in TERMINAL:
                continue
            answer = _extract_answer(dump)
            (TRAJ / f"{key}-answer.md").write_text(answer + "\n")
            (TRAJ / f"{key}.json").write_text(json.dumps(dump, indent=2, default=str) + "\n")
            print("wrote", key, len(answer), "chars", flush=True)
            del pending[key]
        if pending:
            time.sleep(POLL_S)


if __name__ == "__main__":
    {"submit": submit, "wait": wait}[sys.argv[1]]()
