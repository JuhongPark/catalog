# -----------------------------------------------
#  8. Export a Clean Formatted Dataset
#  of the Entire University Catalog:
# 
#  Export a Clean Formatted Dataset of 
#  the Entire University Catalog: The 
#  dataset you would have liked when you 
#  started. Prepare and export a clean, 
#  well-formatted dataset encompassing 
#  the entire university catalog. This 
#  dataset should be in a form that is 
#  readily usable for analysis and 
#  visualization, reflecting the cleaned 
#  and consolidated data you've worked 
#  with throughout the project. Document 
#  the structure of your dataset, including 
#  a description of columns, data types, and 
#  any assumptions or decisions made during 
#  the data preparation process.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import INTERIM_DIR, OUTPUT_DIR, ensure_directories, read_json, write_json, write_text

SOURCE = "ne"

SCHEMA_DOC = """Dataset: ne_catalog.json

Fields:
- source (str): data source identifier
- year (int|null): year label if available
- dept (str): department code prefix
- course_code (str): normalized course code
- title (str): course title
- description (str): course description text
- url (str): source url when known
"""


def main() -> None:
    ensure_directories()
    in_file = INTERIM_DIR / f"{SOURCE}_clean.json"
    out_json = OUTPUT_DIR / f"{SOURCE}_catalog.json"
    out_doc = OUTPUT_DIR / f"{SOURCE}_catalog_schema.txt"

    if not in_file.exists():
        raise SystemExit(f"Missing {in_file}. Run 04_clean.py first.")

    rows = read_json(in_file)
    write_json(out_json, rows)
    write_text(out_doc, SCHEMA_DOC)
    print(f"Exported {len(rows)} records -> {out_json}")
    print(f"Wrote schema doc -> {out_doc}")


if __name__ == "__main__":
    main()
