# -----------------------------------------------
#  7. Data Visualization:
#  Objective: Visualize the word frequencies
#  using a visualization library.
# 
#  Tools/Resources: Examples of visualization 
#  libraries D3, Plotly, and Chart.JS.
#     D3, https://d3js.org/
#     Plotly, https://plotly.com/
#     Chart.JS, https://www.chartjs.org/
#     Google Charts, https://developers.google.com/chart/
# -----------------------------------------------

from __future__ import annotations

import csv
from pathlib import Path

from catalog_utils import OUTPUT_DIR, ensure_directories, write_text

SOURCE = "ne"


def write_ascii_chart(rows: list[tuple[str, int]], path: Path, width: int = 40) -> None:
    if not rows:
        write_text(path, "No data.\n")
        return

    max_count = max(c for _, c in rows)
    lines = ["Word Frequency (Top 30)", "======================="]
    for word, count in rows:
        bar_len = int((count / max_count) * width) if max_count else 0
        lines.append(f"{word:20} | {'#' * bar_len} {count}")
    write_text(path, "\n".join(lines) + "\n")


def main() -> None:
    ensure_directories()
    in_file = OUTPUT_DIR / f"{SOURCE}_title_freq.csv"
    out_file = OUTPUT_DIR / f"{SOURCE}_freq_top30.txt"

    if not in_file.exists():
        raise SystemExit(f"Missing {in_file}. Run 06_frequency.py first.")

    rows: list[tuple[str, int]] = []
    with in_file.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row["word"], int(row["count"])))

    top = rows[:30]
    write_ascii_chart(top, out_file)
    print(f"Saved visualization artifact -> {out_file}")


if __name__ == "__main__":
    main()
