# -----------------------------------------------
#   4. Data Cleaning:
# 
#   Objective: Clean and preprocess the 
#   extracted data for analysis.
# 
#   Tools/Resources: Use Regular Expressions 
#   or string manipulation functions in 
#   your programming language.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import INTERIM_DIR, ensure_directories, normalize_whitespace, read_json, write_json

SOURCE = "ne"


def clean_record(rec: dict) -> dict:
    out = dict(rec)
    out["title"] = normalize_whitespace(str(out.get("title", "")))
    out["description"] = normalize_whitespace(str(out.get("description", "")))
    out["dept"] = normalize_whitespace(str(out.get("dept", ""))).upper()
    out["course_code"] = normalize_whitespace(str(out.get("course_code", ""))).upper()
    out["url"] = normalize_whitespace(str(out.get("url", "")))
    return out


def main() -> None:
    ensure_directories()
    in_file = INTERIM_DIR / f"{SOURCE}_parsed.json"
    out_file = INTERIM_DIR / f"{SOURCE}_clean.json"

    if not in_file.exists():
        raise SystemExit(f"Missing {in_file}. Run 03_parse.py first.")

    rows = read_json(in_file)
    cleaned = []
    seen = set()
    for row in rows:
        item = clean_record(row)
        if not item["course_code"] or not item["title"]:
            continue
        key = (item["course_code"], item["title"].lower())
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(item)

    write_json(out_file, cleaned)
    print(f"Cleaned {len(cleaned)} records -> {out_file}")


if __name__ == "__main__":
    main()
