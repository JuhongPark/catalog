# -----------------------------------------------
#  17. Extra Dashboard (Non-statement extension)
#
#  Note:
#  - This file is an extra artifact for visual review.
#  - It is not part of the original 01~16 statement files.
#  - Core statement visualization remains in 07_visualization.py.
# -----------------------------------------------

from __future__ import annotations

import csv
import re
from html import escape

from catalog_utils import BASE_DIR, OUTPUT_DIR, ensure_directories, write_text

RESULTS_DIR = BASE_DIR / "results"
PROCESS_DIR = BASE_DIR / "references" / "process"
SOURCE = "ne"


def read_word_freq(path, top_n: int = 25) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row["word"], int(row["count"])))
    return rows[:top_n]


def read_delta_csv(path, key: str, top_n: int = 12) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row[key], int(row["delta"])))
    rows.sort(key=lambda x: x[1], reverse=True)
    return rows[:top_n]


def read_round_scores() -> list[tuple[str, float]]:
    scores: list[tuple[str, float]] = []
    files = sorted(PROCESS_DIR.glob("grader_scorecard_round*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        round_match = re.search(r"round(\d+)\.md$", path.name, flags=re.IGNORECASE)
        avg_match = re.search(r"Average score:\s*\*\*([0-9]+(?:\.[0-9]+)?)\s*/\s*5", text, flags=re.IGNORECASE)
        if not round_match or not avg_match:
            continue
        scores.append((f"Round {int(round_match.group(1))}", float(avg_match.group(1))))
    return scores


def read_scorecard_summary() -> tuple[str, str, list[str], str]:
    files = sorted(PROCESS_DIR.glob("grader_scorecard_round*.md"))
    if not files:
        return ("N/A", "N/A", [], "N/A")
    path = files[-1]
    if not path.exists():
        return ("N/A", "N/A", [], "N/A")
    round_match = re.search(r"round(\d+)\.md$", path.name, flags=re.IGNORECASE)
    round_label = f"Round {round_match.group(1)}" if round_match else "Latest Round"
    text = path.read_text(encoding="utf-8", errors="replace")
    total_match = re.search(r"Total score:\s*\*\*([0-9]+\s*/\s*[0-9]+)\*\*", text, flags=re.IGNORECASE)
    avg_match = re.search(r"Average score:\s*\*\*([0-9]+(?:\.[0-9]+)?\s*/\s*5(?:\.00)?)\*\*", text, flags=re.IGNORECASE)
    top_match = re.search(r"Top improvements achieved:\s*(.*?)(?:\n\n|\Z)", text, flags=re.IGNORECASE | re.DOTALL)
    total = total_match.group(1) if total_match else "N/A"
    avg = avg_match.group(1) if avg_match else "N/A"
    tops: list[str] = []
    if top_match:
        for line in top_match.group(1).splitlines():
            line = line.strip()
            if line.startswith("-"):
                tops.append(line[1:].strip())
    return (total, avg, tops, round_label)


def read_reviewer_priorities() -> list[str]:
    files = sorted(PROCESS_DIR.glob("reviewer_improvement_round*.md"))
    if not files:
        return []
    path = files[-1]
    if not path.exists():
        return []
    out: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if re.match(r"^\d+\.\s", line):
            out.append(line)
    return out


def render_bar_list(rows: list[tuple[str, int]], color: str) -> str:
    if not rows:
        return "<p>No data</p>"
    max_val = max(v for _, v in rows) or 1
    out = []
    for label, value in rows:
        width = int((value / max_val) * 100)
        out.append(
            f"<div class='bar-row'><span class='label'>{escape(label)}</span>"
            f"<div class='bar-wrap'><div class='bar' style='width:{width}%;background:{color}'></div></div>"
            f"<span class='value'>{value}</span></div>"
        )
    return "\n".join(out)


def render_score_trend(rows: list[tuple[str, float]]) -> str:
    if not rows:
        return "<p>No round score data available.</p>"
    out = []
    prev = None
    for label, score in rows:
        width = int((score / 5.0) * 100)
        delta = ""
        if prev is not None:
            delta = f" ({score - prev:+.2f})"
        out.append(
            f"<div class='bar-row'><span class='label'>{escape(label)}</span>"
            f"<div class='bar-wrap'><div class='bar' style='width:{width}%;background:#6a4c93'></div></div>"
            f"<span class='value'>{score:.2f}/5{delta}</span></div>"
        )
        prev = score
    return "\n".join(out)


def build_html(
    freq_rows,
    offering_rows,
    title_rows,
    breadth_summary,
    score_rows,
    total_score: str,
    avg_score: str,
    top_improvements: list[str],
    reviewer_priorities: list[str],
    score_round_label: str,
) -> str:
    top_html = "".join(f"<li>{escape(item)}</li>" for item in top_improvements) or "<li>N/A</li>"
    pri_html = "".join(f"<li>{escape(item)}</li>" for item in reviewer_priorities[:4]) or "<li>N/A</li>"
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1' />
  <title>Catalog Analysis Dashboard</title>
  <style>
    :root {{ --bg:#f7f4ed; --card:#fffdf8; --ink:#1f2933; --muted:#5f6c72; --line:#dfd8c8; }}
    body {{ margin:0; font-family: 'Trebuchet MS', Verdana, sans-serif; background: linear-gradient(180deg, #f7f4ed 0%, #efe9db 100%); color:var(--ink); }}
    .wrap {{ max-width:1100px; margin:0 auto; padding:24px; }}
    h1 {{ margin:0 0 12px; font-size:28px; }}
    .sub {{ color:var(--muted); margin-bottom:20px; }}
    .grid {{ display:grid; grid-template-columns: 1fr; gap:14px; }}
    @media (min-width: 900px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
    .card {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px; box-shadow: 0 6px 20px rgba(40,40,40,.05); }}
    .supplemental {{ margin-top:14px; }}
    h2 {{ margin:0 0 12px; font-size:18px; }}
    .bar-row {{ display:grid; grid-template-columns: 160px 1fr 66px; gap:8px; align-items:center; margin:6px 0; }}
    .label {{ font-size:13px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
    .bar-wrap {{ height:10px; background:#ece4d5; border-radius:999px; overflow:hidden; }}
    .bar {{ height:100%; border-radius:999px; }}
    .value {{ text-align:right; font-size:12px; color:var(--muted); }}
    pre {{ white-space:pre-wrap; font-size:12px; background:#f6f2e7; border:1px solid var(--line); padding:10px; border-radius:8px; }}
  </style>
</head>
<body>
  <div class='wrap'>
    <h1>Catalog Analysis Dashboard</h1>
    <div class='sub'>Generated by `extra_dashboard.py` from outputs of 06, 12, 13, 15 and round scorecards.</div>
    <div class='grid'>
      <section class='card'>
        <h2>Top Words in Course Titles (NE)</h2>
        {render_bar_list(freq_rows, '#2a6f8f')}
      </section>
      <section class='card'>
        <h2>Top Department Growth (MIT 1996→2024)</h2>
        {render_bar_list(offering_rows, '#b85c38')}
      </section>
      <section class='card'>
        <h2>Top Rising Title Terms (MIT)</h2>
        {render_bar_list(title_rows, '#3f7d20')}
      </section>
      <section class='card'>
        <h2>Curriculum Breadth Summary</h2>
        <pre>{escape(breadth_summary)}</pre>
      </section>
      <section class='card'>
        <h2>{escape(score_round_label)} Grading & Evaluation</h2>
        <p><b>Total score:</b> {escape(total_score)}<br/><b>Average score:</b> {escape(avg_score)}</p>
        <p><b>Top improvements achieved</b></p>
        <ul>{top_html}</ul>
        <p><b>Next priorities</b></p>
        <ul>{pri_html}</ul>
      </section>
    </div>
    <section class='card supplemental'>
      <h2>Supplemental: Quality Score Trend by Round</h2>
      {render_score_trend(score_rows)}
    </section>
  </div>
</body>
</html>
"""


def main() -> None:
    ensure_directories()
    freq_rows = read_word_freq(OUTPUT_DIR / f"{SOURCE}_title_freq.csv", top_n=25)
    offering_rows = [x for x in read_delta_csv(OUTPUT_DIR / "12_course_offerings_delta.csv", "dept", top_n=12) if x[1] > 0]
    title_rows = [x for x in read_delta_csv(OUTPUT_DIR / "13_title_evolution.csv", "word", top_n=14) if x[1] > 0]
    score_rows = read_round_scores()
    total_score, avg_score, top_improvements, score_round_label = read_scorecard_summary()
    reviewer_priorities = read_reviewer_priorities()
    breadth_path = OUTPUT_DIR / "15_curriculum_breadth.txt"
    breadth_summary = breadth_path.read_text(encoding="utf-8") if breadth_path.exists() else "No breadth summary yet."

    html = build_html(
        freq_rows,
        offering_rows,
        title_rows,
        breadth_summary,
        score_rows,
        total_score,
        avg_score,
        top_improvements,
        reviewer_priorities,
        score_round_label,
    )

    runtime_file = OUTPUT_DIR / "analysis_dashboard.html"
    artifact_file = RESULTS_DIR / "analysis_dashboard.html"
    write_text(runtime_file, html)
    write_text(artifact_file, html)

    print(f"Saved dashboard -> {runtime_file}")
    print(f"Saved shareable dashboard -> {artifact_file}")


if __name__ == "__main__":
    main()
