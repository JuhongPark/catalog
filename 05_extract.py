# -----------------------------------------------
#  5. Data Extraction:
# 
#  Objective: Extract course titles from 
#  the data you cleaned.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import INTERIM_DIR, ensure_directories, read_json, write_text

SOURCE = "ne"


def main() -> None:
    ensure_directories()
    in_file = INTERIM_DIR / f"{SOURCE}_clean.json"
    out_file = INTERIM_DIR / f"{SOURCE}_titles.txt"

    if not in_file.exists():
        raise SystemExit(f"Missing {in_file}. Run 04_clean.py first.")

    rows = read_json(in_file)
    titles = sorted({r.get("title", "").strip() for r in rows if r.get("title")})
    write_text(out_file, "\n".join(titles) + ("\n" if titles else ""))
    print(f"Extracted {len(titles)} titles -> {out_file}")


if __name__ == "__main__":
    main()
