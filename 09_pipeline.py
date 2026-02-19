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
import subprocess
import sys
from pathlib import Path

from catalog_utils import LOG_DIR, ensure_directories


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

    for step in STEPS[start_idx:]:
        code = run_step(step, py_exe=py_exe, log_file=log_file)
        print(f"[{step}] exit={code}")
        if code != 0:
            raise SystemExit(f"Pipeline failed at {step}. See {log_file}")

    print(f"Pipeline completed successfully. Log: {log_file}")


if __name__ == "__main__":
    main()
