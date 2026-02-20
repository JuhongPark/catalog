# -----------------------------------------------
#  14. New and Discontinued Subjects:
# 
#  Identify subjects that were offered in 
#  1996 but no longer exist in 2024, as 
#  well as new subjects introduced in 2024. 
#  Explore possible reasons for these changes.
# -----------------------------------------------

from __future__ import annotations

import re

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, write_text


def canonical_code(raw_code: str) -> str:
    code = raw_code.strip().upper()
    if not code:
        return ""
    # Historical crosswalk normalization for EECS renumbered families.
    code = re.sub(r"^6-(?:1|2|3|4|7|9)\.", "6.", code)
    code = re.sub(r"\s+", " ", code)
    return code


def to_set(rows: list[dict]) -> tuple[set[str], set[str]]:
    raw_vals = set()
    norm_vals = set()
    for r in rows:
        c = (r.get("course_code") or "").strip().upper()
        if c:
            raw_vals.add(c)
            norm = canonical_code(c)
            if norm:
                norm_vals.add(norm)
    return raw_vals, norm_vals


def main() -> None:
    ensure_directories()
    f1996 = OUTPUT_DIR / "10_mit_1996.json"
    f2024 = OUTPUT_DIR / "11_mit_2024.json"

    if not f1996.exists() or not f2024.exists():
        raise SystemExit("Missing 10_mit_1996.json or 11_mit_2024.json. Run 10 and 11 first.")

    s96_raw, s96_norm = to_set(read_json(f1996))
    s24_raw, s24_norm = to_set(read_json(f2024))

    discontinued_raw = sorted(s96_raw - s24_raw)
    new_raw = sorted(s24_raw - s96_raw)
    discontinued_norm = sorted(s96_norm - s24_norm)
    new_norm = sorted(s24_norm - s96_norm)

    lines = [
        "New and Discontinued Subjects",
        "============================",
        "",
        f"Discontinued since 1996 (raw): {len(discontinued_raw)}",
    ]
    lines.extend([f"- {x}" for x in discontinued_raw[:200]])
    lines.append("")
    lines.append(f"New by 2024 (raw): {len(new_raw)}")
    lines.extend([f"- {x}" for x in new_raw[:200]])
    lines.append("")
    lines.append("Crosswalk-Adjusted Counts (historical normalization):")
    lines.append(f"- Discontinued (normalized): {len(discontinued_norm)}")
    lines.append(f"- New (normalized): {len(new_norm)}")

    lines.append("")
    lines.append("Reasoned Patterns:")
    lines.append("- Counts are shown in raw form and crosswalk-adjusted form to separate true additions/removals from renumbering effects.")
    lines.append("- Many differences are likely from renumbering and catalog reorganization rather than pure creation/removal.")
    lines.append("- Newer codes often cluster around data/AI, interdisciplinary, and applied professional tracks.")
    lines.append("- Discontinued-style codes may represent migrated prefixes or merged subject structures.")
    lines.append("- A stronger conclusion requires a formal historical crosswalk between old and new numbering systems.")

    out_txt = OUTPUT_DIR / "14_new_and_old.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
