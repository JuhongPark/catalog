# -----------------------------------------------
#  9. Data pipeline:
# 
#  Write a program that automates the 
#  sequential execution of previously created 
#  script files, ensuring that each script 
#  runs to completion before the next begins. 
#  This program aims to streamline the 
#  generation of outputs from all your 
#  previous files, consolidating the 
#  results into one sequence.
# -----------------------------------------------

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from catalog_utils import LOG_DIR, OUTPUT_DIR, ensure_directories, read_json


STEPS = [
    "01_pull.py",
    "02_combine.py",
    "03_parse.py",
    "04_clean.py",
    "05_extract.py",
    "06_frequency.py",
    "07_visualization.py",
    "08_export.py",
]


def run_step(step: str, py_exe: str, log_file: Path) -> int:
    cmd = [py_exe, step]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"$ {' '.join(cmd)}\n")
        if proc.stdout:
            f.write(proc.stdout)
        if proc.stderr:
            f.write(proc.stderr)
        f.write(f"[exit={proc.returncode}]\n\n")
    return proc.returncode


def collect_snapshot(step_results: list[tuple[str, int]]) -> dict:
    snapshot = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "step_results": [{"step": step, "exit_code": code} for step, code in step_results],
        "all_success": all(code == 0 for _, code in step_results),
        "outputs": {},
    }

    for path in sorted(OUTPUT_DIR.glob("*")):
        if path.is_file():
            snapshot["outputs"][path.name] = {"bytes": path.stat().st_size}

    p1996 = OUTPUT_DIR / "10_mit_1996.json"
    p2024 = OUTPUT_DIR / "11_mit_2024.json"
    if p1996.exists():
        rows = read_json(p1996)
        desc_non_empty = sum(1 for r in rows if str(r.get("description", "")).strip())
        snapshot["mit_1996"] = {
            "records": len(rows),
            "description_non_empty": desc_non_empty,
            "description_coverage_pct": round((desc_non_empty / max(len(rows), 1)) * 100, 2),
        }
    if p2024.exists():
        rows = read_json(p2024)
        snapshot["mit_2024"] = {"records": len(rows)}

    return snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Run catalog pipeline scripts sequentially.")
    parser.add_argument("--from", dest="from_step", default="01_pull.py", help="Start from this script file")
    args = parser.parse_args()

    ensure_directories()
    log_file = LOG_DIR / "pipeline.log"
    start = args.from_step

    if start not in STEPS:
        raise SystemExit(f"Invalid --from value: {start}. Choose one of: {', '.join(STEPS)}")

    start_idx = STEPS.index(start)
    py_exe = sys.executable
    step_results: list[tuple[str, int]] = []

    for step in STEPS[start_idx:]:
        code = run_step(step, py_exe=py_exe, log_file=log_file)
        step_results.append((step, code))
        print(f"[{step}] exit={code}")
        if code != 0:
            raise SystemExit(f"Pipeline failed at {step}. See {log_file}")

    snapshot = collect_snapshot(step_results)
    snapshot_path = OUTPUT_DIR / "pipeline_snapshot.json"
    snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote snapshot: {snapshot_path}")
    print(f"Pipeline completed successfully. Log: {log_file}")


if __name__ == "__main__":
    main()
