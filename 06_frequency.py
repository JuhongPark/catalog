# -----------------------------------------------
#  6. Word Frequency Analysis:
# 
#  Objective: Perform a word frequency count 
#  on the course titles.
# 
#  Tools/Resources: You can use a “map reduce” 
#  style word counting approach.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import INTERIM_DIR, OUTPUT_DIR, ensure_directories, word_counts, write_csv

SOURCE = "ne"


def main() -> None:
    ensure_directories()
    in_file = INTERIM_DIR / f"{SOURCE}_titles.txt"
    out_file = OUTPUT_DIR / f"{SOURCE}_title_freq.csv"

    if not in_file.exists():
        raise SystemExit(f"Missing {in_file}. Run 05_extract.py first.")

    titles = [line.strip() for line in in_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    counts = word_counts(titles)

    rows = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    write_csv(out_file, ["word", "count"], rows)
    print(f"Computed {len(rows)} word frequencies -> {out_file}")


if __name__ == "__main__":
    main()
