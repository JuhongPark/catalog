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
import json
import re
from datetime import datetime, timezone
from html import escape

from catalog_utils import BASE_DIR, OUTPUT_DIR, ensure_directories, write_text

RESULTS_DIR = BASE_DIR / "results"
PROCESS_DIR = BASE_DIR / "references" / "process"
SOURCE = "ne"
SPOTLIGHT_TITLE = "1.001: Engineering Computation and Data Science"
SPOTLIGHT_INSTRUCTORS = "Instructors: Abel Sanchez and John R. Williams"


def read_word_freq(path, top_n: int = 25) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row["word"], int(row["count"])))
    return rows[:top_n]


def read_delta_rows(path, key: str) -> list[tuple[str, int]]:
    rows: list[tuple[str, int]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row[key], int(row["delta"])))
    return rows


def clean_markdown_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "")
    return text.strip()


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
    if not top_match:
        top_match = re.search(r"Strengths:\s*(.*?)(?:\n\n|\Z)", text, flags=re.IGNORECASE | re.DOTALL)
    total = total_match.group(1) if total_match else "N/A"
    avg = avg_match.group(1) if avg_match else "N/A"
    tops: list[str] = []
    if top_match:
        for line in top_match.group(1).splitlines():
            line = line.strip()
            if line.startswith("-"):
                tops.append(clean_markdown_text(line[1:].strip()))
    return (total, avg, tops, round_label)


def read_reviewer_priorities() -> list[str]:
    files = sorted(PROCESS_DIR.glob("reviewer_improvement_round*.md"))
    if not files:
        return []
    path = files[-1]
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    block_match = re.search(
        r"##\s*Remaining Priority Actions\s*(.*?)(?:\n##|\Z)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    block = block_match.group(1) if block_match else text

    out: list[str] = []
    for line in block.splitlines():
        line = line.strip()
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if not m:
            continue
        item = clean_markdown_text(m.group(2).strip())
        if item:
            out.append(item)
    return out


def file_stamp(name: str) -> str:
    path = OUTPUT_DIR / name
    if not path.exists():
        return f"{name} (missing)"
    ts = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"{name} ({ts})"


def read_round_change_keywords() -> list[str]:
    # Round keywords must reflect latest round results documents first.
    keywords: list[str] = []

    score_files = sorted(PROCESS_DIR.glob("grader_scorecard_round*.md"))
    if score_files:
        latest = score_files[-1]
        text = latest.read_text(encoding="utf-8", errors="replace")
        m_round = re.search(r"round(\d+)\.md$", latest.name, flags=re.IGNORECASE)
        if m_round:
            keywords.append(f"Round {m_round.group(1)}")
        m_total = re.search(r"Total score:\s*\*\*([0-9]+\s*/\s*[0-9]+)\*\*", text, flags=re.IGNORECASE)
        if m_total:
            keywords.append(f"Score {m_total.group(1)}")
        m_delta = re.search(r"Round\s+\d+\s*->\s*Round\s+\d+:\s*\*\*([^\*]+)\*\*", text, flags=re.IGNORECASE)
        if m_delta:
            keywords.append(f"Delta {m_delta.group(1).strip()}")

        changed_block = re.search(
            r"##\s*What Changed This Round.*?(?=\n##|\Z)",
            text,
            flags=re.IGNORECASE | re.DOTALL,
        )
        def to_keyword(line: str) -> str:
            low = line.lower()
            if "policy drift" in low or "visualization-policy drift" in low:
                return "Policy Drift Check Added"
            if "source timestamps" in low:
                return "Source Trace Added"
            if "round-change keywords" in low:
                return "Round Keywords Added"
            if "summary" in low and "reflection" in low:
                return "Round Summary Updated"
            line = re.sub(r"`[^`]+`", "", line)
            line = re.sub(r"[A-Za-z0-9_./-]+\.(txt|json|md|html|csv)", "", line, flags=re.IGNORECASE)
            line = re.sub(r"\s+", " ", line).strip(" .:-")
            words = line.split()
            return " ".join(words[:4]) if words else ""

        if changed_block:
            for line in changed_block.group(0).splitlines():
                line = line.strip()
                if line.startswith("-"):
                    clean = clean_markdown_text(line[1:].strip())
                    if clean:
                        short = to_keyword(clean)
                        if short:
                            keywords.append(short)

    if len(keywords) < 8:
        report_path = OUTPUT_DIR / "10_mit_1996_extraction_report.txt"
        if report_path.exists():
            text = report_path.read_text(encoding="utf-8", errors="replace")
            if "ocr_runtime_available: True" in text:
                keywords.append("OCR Active")
            m = re.search(r"records:\s*([0-9]+)", text)
            if m:
                keywords.append(f"MIT1996 {m.group(1)} rows")

    # Deduplicate while preserving order.
    deduped: list[str] = []
    seen = set()
    for item in keywords:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped[:8]


def render_source_trace() -> str:
    traces = [
        ("Word Frequency", [file_stamp(f"{SOURCE}_title_freq.csv")]),
        ("Offerings Delta", [file_stamp("12_course_offerings_delta.csv"), file_stamp("12_course_offerings_summary.txt")]),
        ("Title Evolution", [file_stamp("13_title_evolution.csv")]),
        ("New/Discontinued", [file_stamp("14_new_and_old.txt")]),
        ("Breadth", [file_stamp("15_curriculum_breadth.txt")]),
        ("Extraction", [file_stamp("10_mit_1996.json"), file_stamp("10_mit_1996_extraction_report.txt")]),
        ("Run Snapshot", [file_stamp("pipeline_snapshot.json")]),
    ]
    rows = []
    for label, files in traces:
        joined = ", ".join(files)
        rows.append(f"<div class='trace-row'><span class='trace-k'>{escape(label)}</span><span class='trace-v'>{escape(joined)}</span></div>")
    return "\n".join(rows)


def split_summary_sections(summary_text: str) -> dict[str, str]:
    sections = {
        "major": "",
        "terminology": "",
        "new_old": "",
        "breadth": "",
        "quality": "",
        "limitations": "",
    }
    if not summary_text.strip():
        return sections

    blocks: dict[str, list[str]] = {}
    current = "intro"
    blocks[current] = []
    for line in summary_text.splitlines():
        m = re.match(r"^\s*([1-5])\.\s+", line)
        if m:
            current = m.group(1)
            blocks[current] = [line]
        else:
            blocks.setdefault(current, []).append(line)

    sections["major"] = "\n".join(blocks.get("1", [])).strip()
    sections["terminology"] = "\n".join(blocks.get("2", [])).strip()
    sections["new_old"] = "\n".join(blocks.get("3", [])).strip()
    sections["breadth"] = "\n".join(blocks.get("4", [])).strip()
    quality_block = "\n".join(blocks.get("5", [])).strip()
    # Keep section 5 focused on metrics; move trailing note/limitations separately.
    q_lower = quality_block.lower()
    q_idx = q_lower.find("data quality note")
    if q_idx >= 0:
        sections["quality"] = quality_block[:q_idx].strip()
    else:
        sections["quality"] = quality_block

    lower = summary_text.lower()
    idx = lower.find("data quality note")
    if idx >= 0:
        limit_text = summary_text[idx:]
        # Evidence source list is metadata; keep it out of summary-mapping blocks.
        ev_idx = limit_text.lower().find("evidence sources used for this summary")
        if ev_idx >= 0:
            before = limit_text[:ev_idx].strip()
            after = limit_text[ev_idx:]
            # Keep recommendation part if present after evidence list.
            rec_idx = after.lower().find("limitations and next-step recommendation")
            if rec_idx >= 0:
                sections["limitations"] = (before + "\n\n" + after[rec_idx:]).strip()
            else:
                sections["limitations"] = before
        else:
            sections["limitations"] = limit_text.strip()
    return sections


def render_summary_points(title: str, text: str) -> str:
    if not text.strip():
        return f"<div class='sblock'><h3>{escape(title)}</h3><p class='snote'>No summary text available.</p></div>"
    lines = [x.rstrip() for x in text.splitlines() if x.strip()]
    points: list[str] = []
    current = ""
    for raw in lines:
        line = raw.strip()
        if line.lower() in {
            "data quality note",
            "evidence sources used for this summary",
            "limitations and next-step recommendation",
        }:
            continue
        if re.match(r"^\d+\.\s+", line):
            continue
        if line.startswith("-"):
            if current:
                points.append(current.strip())
            current = line[1:].strip()
            continue
        if current:
            current += " " + line
    if current:
        points.append(current.strip())
    if not points:
        body = "<p class='snote'>" + escape(" ".join(lines[:3])) + "</p>"
    else:
        body = "<ul>" + "".join(f"<li>{escape(p)}</li>" for p in points[:8]) + "</ul>"
    return f"<div class='sblock'><h3>{escape(title)}</h3>{body}</div>"


def render_bar_list(rows: list[tuple[str, int]], color: str, use_abs: bool = False) -> str:
    if not rows:
        return "<p>No data</p>"
    if use_abs:
        max_val = max(abs(v) for _, v in rows) or 1
    else:
        max_val = max(v for _, v in rows) or 1
    out = []
    for label, value in rows:
        basis = abs(value) if use_abs else value
        width = int((basis / max_val) * 100)
        if value != 0:
            width = max(width, 2)
        out.append(
            f"<div class='bar-row' data-sort-value='{value}' data-sort-abs='{abs(value)}'><span class='label'>{escape(label)}</span>"
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
            f"<div class='bar-row' data-sort-value='{score:.4f}'><span class='label'>{escape(label)}</span>"
            f"<div class='bar-wrap'><div class='bar' style='width:{width}%;background:#6a4c93'></div></div>"
            f"<span class='value'>{score:.2f}/5{delta}</span></div>"
        )
        prev = score
    return "\n".join(out)


def normalize_display_label(label: str) -> str:
    if label == "6_EECS":
        return "6"
    return label


def build_html(
    freq_rows,
    offering_up_rows,
    offering_down_rows,
    title_up_rows,
    title_down_rows,
    breadth_summary,
    score_rows,
    total_score: str,
    avg_score: str,
    top_improvements: list[str],
    reviewer_priorities: list[str],
    score_round_label: str,
    change_keywords: list[str],
    generated_at: str,
    summary_sections: dict[str, str],
) -> str:
    top_html = "".join(f"<li>{escape(item)}</li>" for item in top_improvements) or "<li>N/A</li>"
    pri_html = "".join(f"<li>{escape(item)}</li>" for item in reviewer_priorities[:4]) or "<li>N/A</li>"
    change_html = "".join(f"<li>{escape(item)}</li>" for item in change_keywords) or "<li>N/A</li>"
    source_trace_html = render_source_trace()
    snapshot_year = generated_at[:4] if len(generated_at) >= 4 else "N/A"
    kpi_mit = "MIT 1996 records: N/A | MIT 2024 records: N/A"
    kpi_ne = f"NE {snapshot_year} records: N/A"
    p1996 = OUTPUT_DIR / "10_mit_1996.json"
    p2024 = OUTPUT_DIR / "11_mit_2024.json"
    mit_1996_count = None
    mit_2024_count = None
    if p1996.exists():
        try:
            mit_1996_count = len(json.loads(p1996.read_text(encoding="utf-8")))
        except Exception:
            pass
    if p2024.exists():
        try:
            mit_2024_count = len(json.loads(p2024.read_text(encoding="utf-8")))
        except Exception:
            pass
    pne = OUTPUT_DIR / "ne_catalog.json"
    if pne.exists():
        try:
            kpi_ne = f"NE {snapshot_year} records: {len(json.loads(pne.read_text(encoding='utf-8')))}"
        except Exception:
            pass
    if mit_1996_count is not None or mit_2024_count is not None:
        kpi_mit = (
            f"MIT 1996 records: {mit_1996_count if mit_1996_count is not None else 'N/A'} | "
            f"MIT 2024 records: {mit_2024_count if mit_2024_count is not None else 'N/A'}"
        )
    summary_major = render_summary_points("Major Departmental Shifts", summary_sections.get("major", ""))
    summary_term = render_summary_points("Terminology Changes", summary_sections.get("terminology", ""))
    summary_new_old = render_summary_points("New/Discontinued Subjects", summary_sections.get("new_old", ""))
    summary_breadth = render_summary_points("Curriculum Breadth", summary_sections.get("breadth", ""))
    summary_quality = render_summary_points("Data Quality", summary_sections.get("quality", ""))
    summary_limit = render_summary_points("Limitations", summary_sections.get("limitations", ""))
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1' />
  <title>Catalog Analysis Dashboard</title>
  <style>
    :root {{
      --bg:#eff1f3;
      --bg2:#e6e9ed;
      --card:#f6f7f9;
      --card2:#eef1f4;
      --ink:#2c333a;
      --line:#d7dce1;
      --track:#dde2e8;
    }}
    body {{ margin:0; font-family: 'Avenir Next', 'Segoe UI', sans-serif; background: linear-gradient(180deg,var(--bg) 0%, var(--bg2) 100%); color:var(--ink); }}
    .wrap {{ max-width:1200px; margin:0 auto; padding:30px 26px 36px; }}
    h1 {{ margin:0 0 8px; font-size:36px; letter-spacing:.1px; color:#13202b; }}
    .sub {{ color:var(--muted); margin-bottom:14px; font-size:15px; }}
    .controls {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin:0 0 14px; }}
    .chip {{ border:1px solid #cfd6de; background:#edf1f5; color:#40505d; border-radius:999px; padding:6px 10px; font-size:12px; cursor:pointer; }}
    .chip.active {{ background:#dce7f2; border-color:#a9bfd6; color:#1f3950; }}
    .btn {{ border:1px solid #c5ced7; background:#f3f6f9; color:#394b5a; border-radius:8px; padding:6px 10px; font-size:12px; cursor:pointer; }}
    .sort-btn {{ flex: 0 0 78px; min-width:78px; text-align:center; }}
    .panel-head {{ display:flex; justify-content:space-between; gap:8px; align-items:center; }}
    .panel-head h2 {{ margin-bottom:0; }}
    .panel-actions {{ display:flex; gap:6px; }}
    .bar-list.collapsed {{ display:none; }}
    .panel.hidden {{ display:none; }}
    .kpis {{ display:grid; grid-template-columns:1fr; gap:10px; margin:0 0 14px; }}
    @media (min-width: 900px) {{ .kpis {{ grid-template-columns: 1fr 1fr 1fr; }} }}
    .kpi {{ background:#f4f6f8; border:1px solid var(--line); border-radius:12px; padding:10px 12px; box-shadow:0 4px 12px rgba(31,43,56,.06); }}
    .kpi .k {{ color:#7a8490; font-size:12px; text-transform:uppercase; letter-spacing:.7px; }}
    .kpi .v {{ margin-top:4px; font-size:16px; color:#26323d; }}
    .grid {{ display:grid; grid-template-columns: 1fr; gap:14px; }}
    @media (min-width: 1000px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
    .card {{ background:linear-gradient(180deg, var(--card) 0%, var(--card2) 100%); border:1px solid var(--line); border-radius:14px; padding:16px; box-shadow:0 8px 20px rgba(31,43,56,.06); }}
    .section-divider {{ grid-column: 1 / -1; font-size:13px; font-weight:700; letter-spacing:.6px; color:#435668; text-transform:uppercase; border-top:1px solid #cfd6de; padding-top:8px; }}
    .spotlight {{ margin-bottom:14px; background:linear-gradient(180deg, #f1f3f6 0%, #e8edf2 100%); border-color:#cfd6dd; }}
    .spotlight h2 {{ color:#6e7782; margin-bottom:8px; font-size:13px; text-transform:uppercase; letter-spacing:.8px; }}
    .spotlight .title {{ font-size:30px; font-weight:700; margin:0 0 4px; line-height:1.25; color:#2f3740; }}
    .spotlight .inst {{ font-size:16px; color:#6f7780; margin:0; }}
    .supplemental {{ margin-top:14px; }}
    h2 {{ margin:0 0 12px; font-size:22px; color:#1f2a37; }}
    .bar-row {{ display:grid; grid-template-columns: 170px 1fr 66px; gap:8px; align-items:center; margin:6px 0; }}
    .label {{ font-size:15px; color:#2e3e49; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
    .bar-wrap {{ height:10px; background:var(--track); border-radius:999px; overflow:hidden; }}
    .bar {{ height:100%; border-radius:999px; }}
    .value {{ text-align:right; font-size:14px; color:#4f5c66; }}
    .note {{ font-size:14px; color:var(--muted); margin-top:10px; line-height:1.45; }}
    .keyword-list {{ display:flex; flex-wrap:wrap; gap:8px; padding-left:0; list-style:none; margin:0 0 10px; }}
    .keyword-list li {{ margin:0; color:#4b5b68; border:1px solid #cfd6de; background:#edf1f5; border-radius:999px; padding:6px 12px; font-size:13px; font-weight:600; }}
    .trace {{ margin-top:10px; border-top:1px dashed var(--line); padding-top:10px; }}
    .trace-row {{ display:grid; grid-template-columns: 150px 1fr; gap:8px; margin:6px 0; }}
    .trace-k {{ color:#2e4250; font-size:13px; font-weight:600; }}
    .trace-v {{ color:#4f6070; font-size:13px; }}
    .summary-box {{ margin-top:10px; }}
    .summary-links a {{ color:#4d6d8f; text-decoration:none; margin-right:10px; font-size:13px; }}
    .summary-links a:hover {{ text-decoration:underline; }}
    .summary-map {{ margin-top:10px; border-top:1px dashed var(--line); padding-top:10px; }}
    .sblock {{ background:#f3f6f9; border:1px solid #d5dde5; border-radius:10px; padding:10px; margin:8px 0; }}
    .sblock h3 {{ margin:0 0 6px; font-size:15px; color:#4a5561; }}
    .sblock ul {{ margin:0; padding-left:18px; }}
    .sblock li {{ margin:4px 0; color:#3f4f5d; font-size:14px; }}
    .snote {{ margin:0; color:#495b68; font-size:14px; }}
    .wide {{ grid-column: 1 / -1; }}
    .round-sub {{ margin-top:14px; padding-top:10px; border-top:1px dashed var(--line); }}
    pre {{ white-space:pre-wrap; font-size:14px; background:#f2f5f8; border:1px solid var(--line); padding:12px; border-radius:8px; color:#3c4b59; line-height:1.5; }}
  </style>
</head>
<body>
  <div class='wrap'>
    <section class='card spotlight'>
      <h2>Course Analysis</h2>
      <p class='title'>{escape(SPOTLIGHT_TITLE)}</p>
      <p class='inst'>{escape(SPOTLIGHT_INSTRUCTORS)}</p>
    </section>
    <h1>Catalog Analysis Dashboard</h1>
    <div class='sub'>Generated by `extra_dashboard.py` from outputs of 06, 10, 12, 13, 14, 15 and round scorecards. Updated: {escape(generated_at)}. Static HTML view (no server required); lightweight client-side interactivity (for example toggles, sorting, filter chips) is allowed when metric traceability is preserved.</div>
    <div class='controls'>
      <button class='chip active' data-filter='all'>All</button>
      <button class='chip' data-filter='analysis'>Analysis</button>
      <button class='chip' data-filter='summary'>Summary</button>
      <button class='chip' data-filter='evaluation'>Evaluation</button>
    </div>
    <section class='kpis'>
      <div class='kpi'><div class='k'>Round Snapshot</div><div class='v'>{escape(score_round_label)} | Total {escape(total_score)} | Avg {escape(avg_score)}</div></div>
      <div class='kpi'><div class='k'>NE</div><div class='v'>{escape(kpi_ne)}</div></div>
      <div class='kpi'><div class='k'>MIT</div><div class='v'>{escape(kpi_mit)}</div></div>
    </section>
    <div class='grid'>
      <div class='section-divider panel' data-group='analysis'>NE Information</div>
      <section class='card panel' data-group='analysis'>
        <div class='panel-head'>
          <h2>Words in Course Titles (NE)</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='freq-bars'>Sort: Desc</button>
          </div>
        </div>
        <div id='freq-bars' class='bar-list'>{render_bar_list(freq_rows, '#6b8fbe')}</div>
      </section>
      <div class='section-divider panel' data-group='analysis'>MIT Information</div>
      <section class='card panel' data-group='analysis'>
        <div class='panel-head'>
          <h2>Department Growth (MIT 1996→Catalog Snapshot)</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='dept-growth-bars'>Sort: Desc</button>
          </div>
        </div>
        <div id='dept-growth-bars' class='bar-list'>{render_bar_list(offering_up_rows, '#7eaf73')}</div>
      </section>
      <section class='card panel' data-group='analysis'>
        <div class='panel-head'>
          <h2>Department Reduction (MIT 1996→Catalog Snapshot)</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='dept-reduction-bars' data-sort-mode='abs'>Sort: Desc</button>
          </div>
        </div>
        <div id='dept-reduction-bars' class='bar-list'>{render_bar_list(offering_down_rows, '#d96a72', use_abs=True)}</div>
        <div class='note'>Note: raw deltas may include renumbering/restructuring effects, not only true curriculum growth/reduction.</div>
      </section>
      <section class='card panel' data-group='analysis'>
        <div class='panel-head'>
          <h2>Rising Title Terms (MIT)</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='title-rise-bars'>Sort: Desc</button>
          </div>
        </div>
        <div id='title-rise-bars' class='bar-list'>{render_bar_list(title_up_rows, '#7eaf73')}</div>
      </section>
      <section class='card panel' data-group='analysis'>
        <div class='panel-head'>
          <h2>Declining Title Terms (MIT)</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='title-down-bars' data-sort-mode='abs'>Sort: Desc</button>
          </div>
        </div>
        <div id='title-down-bars' class='bar-list'>{render_bar_list(title_down_rows, '#d96a72', use_abs=True)}</div>
        <div class='note'>Interpretation caution: declining terms can include legacy metadata tokens from older catalog formatting.</div>
      </section>
      <section class='card panel' data-group='analysis'>
        <h2>Curriculum Breadth Summary</h2>
        <pre>{escape(breadth_summary)}</pre>
      </section>
    </div>
    <section class='card supplemental panel' data-group='summary'>
      <div class='summary-box'>
        <h2 style='margin-top:2px'>Summary & Reflection</h2>
        <div class='summary-links'>
          <a href='../16_summary_reflection.txt'>Open Summary (results path)</a>
          <a href='../../16_summary_reflection.txt'>Open Summary (data/output path)</a>
        </div>
        <div class='note'>Summary content is organized here as structured blocks for quick review.</div>
        <div class='summary-map'>
          {summary_major}
          {summary_term}
          {summary_new_old}
          {summary_breadth}
          {summary_quality}
          {summary_limit}
        </div>
      </div>
      <div class='trace'>
        <h2 style='margin-top:2px'>Panel Sources & Timestamps</h2>
        {source_trace_html}
      </div>
    </section>
    <section class='card supplemental panel' data-group='evaluation'>
      <h2>{escape(score_round_label)} Grading & Evaluation</h2>
      <p><b>Total score:</b> {escape(total_score)}<br/><b>Average score:</b> {escape(avg_score)}</p>
      <p><b>Top improvements achieved</b></p>
      <ul>{top_html}</ul>
      <p><b>Next priorities</b></p>
      <ul>{pri_html}</ul>
      <div class='round-sub'>
        <div class='panel-head'>
          <h2>Supplemental: Quality Score Trend by Round</h2>
          <div class='panel-actions'>
            <button class='btn sort-btn' data-target='score-trend-bars'>Sort: Desc</button>
          </div>
        </div>
        <ul class='keyword-list'>{change_html}</ul>
        <div id='score-trend-bars' class='bar-list'>{render_score_trend(score_rows)}</div>
      </div>
    </section>
  </div>
  <script>
    (function() {{
      const chips = Array.from(document.querySelectorAll('.chip'));
      const panels = Array.from(document.querySelectorAll('.panel'));

      chips.forEach((chip) => {{
        chip.addEventListener('click', () => {{
          const filter = chip.getAttribute('data-filter');
          chips.forEach((c) => c.classList.remove('active'));
          chip.classList.add('active');
          panels.forEach((panel) => {{
            if (filter === 'all') {{
              panel.classList.remove('hidden');
              return;
            }}
            const match = panel.getAttribute('data-group') === filter;
            panel.classList.toggle('hidden', !match);
          }});
        }});
      }});

      document.querySelectorAll('.sort-btn').forEach((btn) => {{
        btn.dataset.order = 'desc';
        btn.addEventListener('click', () => {{
          const target = document.getElementById(btn.getAttribute('data-target'));
          if (!target) return;
          const rows = Array.from(target.querySelectorAll('.bar-row'));
          const order = btn.dataset.order === 'desc' ? 'asc' : 'desc';
          const mode = btn.getAttribute('data-sort-mode') || 'value';
          rows.sort((a, b) => {{
            const av = Number(mode === 'abs' ? (a.getAttribute('data-sort-abs') || '0') : (a.getAttribute('data-sort-value') || '0')) || 0;
            const bv = Number(mode === 'abs' ? (b.getAttribute('data-sort-abs') || '0') : (b.getAttribute('data-sort-value') || '0')) || 0;
            return order === 'asc' ? av - bv : bv - av;
          }});
          rows.forEach((row) => target.appendChild(row));
          btn.dataset.order = order;
          btn.textContent = `Sort: ${{order === 'asc' ? 'Asc' : 'Desc'}}`;
        }});
      }});
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    ensure_directories()
    freq_rows = read_word_freq(OUTPUT_DIR / f"{SOURCE}_title_freq.csv", top_n=25)
    deltas = read_delta_rows(OUTPUT_DIR / "12_course_offerings_delta.csv", "dept")
    offering_up_rows = [(normalize_display_label(k), v) for k, v in [x for x in deltas if x[1] > 0][:8]]
    offering_down_rows = [(normalize_display_label(k), v) for k, v in sorted([x for x in deltas if x[1] < 0], key=lambda x: x[1])[:8]]
    title_deltas = read_delta_rows(OUTPUT_DIR / "13_title_evolution.csv", "word")
    title_up_rows = sorted([x for x in title_deltas if x[1] > 0], key=lambda x: x[1], reverse=True)[:14]
    title_down_rows = sorted([x for x in title_deltas if x[1] < 0], key=lambda x: x[1])[:14]
    score_rows = read_round_scores()
    total_score, avg_score, top_improvements, score_round_label = read_scorecard_summary()
    reviewer_priorities = read_reviewer_priorities()
    change_keywords = read_round_change_keywords()
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    summary_path = BASE_DIR / "16_summary_reflection.txt"
    summary_reflection_text = summary_path.read_text(encoding="utf-8", errors="replace") if summary_path.exists() else ""
    summary_sections = split_summary_sections(summary_reflection_text)
    breadth_path = OUTPUT_DIR / "15_curriculum_breadth.txt"
    breadth_summary = breadth_path.read_text(encoding="utf-8") if breadth_path.exists() else "No breadth summary yet."

    html = build_html(
        freq_rows,
        offering_up_rows,
        offering_down_rows,
        title_up_rows,
        title_down_rows,
        breadth_summary,
        score_rows,
        total_score,
        avg_score,
        top_improvements,
        reviewer_priorities,
        score_round_label,
        change_keywords,
        generated_at,
        summary_sections,
    )

    runtime_file = OUTPUT_DIR / "analysis_dashboard.html"
    artifact_file = RESULTS_DIR / "analysis_dashboard.html"
    write_text(runtime_file, html)
    write_text(artifact_file, html)

    print(f"Saved dashboard -> {runtime_file}")
    print(f"Saved shareable dashboard -> {artifact_file}")


if __name__ == "__main__":
    main()
