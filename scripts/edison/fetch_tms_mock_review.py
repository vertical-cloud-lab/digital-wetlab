#!/usr/bin/env python3
"""Poll and fetch the Edison ANALYSIS mock-review task, writing the answer and
full task dump (plus any notebook figures) into edison-trajectories/tms-mock-review/.

Per repo guidance, waits 10 minutes before the first poll (override with
EDISON_INITIAL_WAIT_S=0 for an immediate check), then polls every 5 minutes.

Usage:
    EDISON_PLATFORM_API_KEY=... python scripts/edison/fetch_tms_mock_review.py [--once]
"""
from __future__ import annotations

import base64
import json
import os
import sys
import time
from pathlib import Path

from edison_client import EdisonClient

HERE = Path(__file__).resolve().parents[2]
TRAJ = HERE / "edison-trajectories" / "tms-mock-review"
SUBMITTED = TRAJ / "tms-mock-review-SUBMITTED.json"

TERMINAL = {"success", "fail", "failed", "cancelled", "error", "crashed", "truncated"}
INITIAL_WAIT_S = int(os.environ.get("EDISON_INITIAL_WAIT_S", "600"))
POLL_S = int(os.environ.get("EDISON_POLL_S", "300"))


def _extract_answer(dump: dict) -> str:
    if dump.get("answer"):
        return dump["answer"]
    try:
        return dump["environment_frame"]["state"]["state"]["answer"] or ""
    except (KeyError, TypeError):
        return ""


def main() -> None:
    api_key = (os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY") or "").strip()
    if not api_key:
        raise SystemExit("No EDISON_PLATFORM_API_KEY / EDISON_API_KEY in environment")
    once = "--once" in sys.argv
    task_id = json.loads(SUBMITTED.read_text())["task_id"]
    client = EdisonClient(api_key=api_key)

    if not once and INITIAL_WAIT_S:
        print(f"initial wait {INITIAL_WAIT_S}s before first poll", flush=True)
        time.sleep(INITIAL_WAIT_S)

    while True:
        resp = client.get_task(task_id)
        dump = resp.model_dump()
        status = str(dump.get("status", "")).lower()
        print("status:", status, flush=True)
        if status in TERMINAL:
            break
        if once:
            return
        time.sleep(POLL_S)

    answer = _extract_answer(dump)
    (TRAJ / f"tms-mock-review-{task_id}.md").write_text(answer)
    (TRAJ / f"tms-mock-review-{task_id}.json").write_text(json.dumps(dump, indent=2, default=str))
    print("wrote", TRAJ / f"tms-mock-review-{task_id}.md", len(answer), "chars")

    nb = dump.get("notebook")
    if isinstance(nb, dict):
        n = 0
        for cell in nb.get("cells", []):
            for out in cell.get("outputs", []):
                img = (out.get("data") or {}).get("image/png")
                if img:
                    (TRAJ / f"figure_{n:02d}.png").write_bytes(base64.b64decode(img))
                    n += 1
        if n:
            print("wrote", n, "figures")


if __name__ == "__main__":
    main()
