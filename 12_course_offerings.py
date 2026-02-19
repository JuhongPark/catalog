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

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, write_csv, write_text


def counts_by_dept(rows: list[dict]) -> Counter:
    c = Counter()
    for r in rows:
        dept = (r.get("dept") or "UNK").strip().upper()
        if dept:
            c[dept] += 1
    return c


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

    top_up = rows[:10]
    top_down = sorted(rows, key=lambda x: x[3])[:10]
    lines = ["Course Offerings Over Time", "==========================", "", "Top Expanded Departments:"]
    lines.extend([f"- {d}: {n96} -> {n24} (delta {delta:+d})" for d, n96, n24, delta in top_up])
    lines.append("")
    lines.append("Top Reduced Departments:")
    lines.extend([f"- {d}: {n96} -> {n24} (delta {delta:+d})" for d, n96, n24, delta in top_down])

    out_txt = OUTPUT_DIR / "12_course_offerings_summary.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
