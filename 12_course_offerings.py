# -----------------------------------------------
#  12. Course Offerings Over Time
# 
#  After extracting the course data from 
#  both the 1996 and present catalogs, 
#  analyze the number of courses offered 
#  in various departments. Are there any 
#  departments that have significantly 
#  expanded or reduced their course offerings? 
#  If so, identify them and discuss possible 
#  reasons for these changes.
# -----------------------------------------------

from __future__ import annotations

from collections import Counter
import re

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, write_csv, write_text


DEPT_ALIASES = {
    "6-1": "6",
    "6-2": "6",
    "6-3": "6",
    "6-4": "6",
    "6-7": "6",
    "6-9": "6",
    "6": "6",
}


def canonical_dept(row: dict) -> str:
    dept = (row.get("dept") or "").strip().upper()
    code = (row.get("course_code") or "").strip().upper()

    if re.match(r"^6(?:[-.])", code):
        return "6"
    if dept in DEPT_ALIASES:
        return DEPT_ALIASES[dept]
    return dept or "UNK"


def counts_by_dept(rows: list[dict]) -> Counter:
    c = Counter()
    for r in rows:
        dept = canonical_dept(r)
        if dept:
            c[dept] += 1
    return c


def reason_for_delta(dept: str, delta: int) -> str:
    if dept == "6" and delta < 0:
        return "Likely affected by MIT EECS renumbering/split plus extraction coverage differences."
    if delta > 40:
        return "Strong growth likely tied to newer interdisciplinary/program tracks and catalog expansion."
    if delta < -20:
        return "Large decrease may reflect renumbering, restructuring, or extraction coverage differences."
    if delta > 0:
        return "Moderate increase; likely incremental curriculum growth."
    if delta < 0:
        return "Moderate decrease; may indicate consolidation or catalog maintenance changes."
    return "Relatively stable between the two snapshots."


def reliability_note(dept: str, delta: int) -> str:
    if dept == "6" and delta < 0:
        return "low (major renumbering/split effects likely)"
    if abs(delta) >= 120:
        return "low (very large shift, likely mixed with structural effects)"
    if abs(delta) >= 60:
        return "medium (possible mixed effect of true change + code evolution)"
    return "high (smaller shift, more likely stable department mapping)"


def main() -> None:
    ensure_directories()
    f1996 = OUTPUT_DIR / "10_mit_1996.json"
    f2024 = OUTPUT_DIR / "11_mit_2024.json"

    if not f1996.exists() or not f2024.exists():
        raise SystemExit("Missing 10_mit_1996.json or 11_mit_2024.json. Run 10 and 11 first.")

    a = read_json(f1996)
    b = read_json(f2024)
    c96 = counts_by_dept(a)
    c24 = counts_by_dept(b)

    all_depts = sorted(set(c96) | set(c24))
    rows = []
    for d in all_depts:
        n96 = c96.get(d, 0)
        n24 = c24.get(d, 0)
        rows.append((d, n96, n24, n24 - n96))

    rows.sort(key=lambda x: x[3], reverse=True)
    out_csv = OUTPUT_DIR / "12_course_offerings_delta.csv"
    write_csv(out_csv, ["dept", "count_1996", "count_2024", "delta"], rows)

    top_up = [r for r in rows if r[3] > 0][:10]
    top_down = [r for r in sorted(rows, key=lambda x: x[3]) if r[3] < 0][:10]
    lines = [
        "Course Offerings Over Time",
        "==========================",
        "",
        "Top Expanded Departments:",
    ]
    lines.extend([f"- {d}: {n96} -> {n24} (delta {delta:+d}) | {reason_for_delta(d, delta)}" for d, n96, n24, delta in top_up])
    lines.append("")
    lines.append("Top Reduced Departments:")
    lines.extend(
        [
            f"- {d}: {n96} -> {n24} (delta {delta:+d}) | {reason_for_delta(d, delta)} "
            f"| reliability: {reliability_note(d, delta)}"
            for d, n96, n24, delta in top_down
        ]
    )

    lines.append("")
    lines.append("Interpretation Notes:")
    lines.append("- Department values are normalized with a historical alias crosswalk (for example, 6 and 6-* -> 6).")
    lines.append("- Differences mix true curriculum change with catalog formatting/numbering evolution.")
    lines.append("- Extreme deltas should be interpreted with caution unless cross-validated with historical departmental metadata.")

    out_txt = OUTPUT_DIR / "12_course_offerings_summary.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
