# -----------------------------------------------
#  15. Curriculum Breadth:
# 
#  Compare the breadth of topics in the 
#  1996 and 2024 catalogs to assess whether 
#  the curriculum has become more 
#  interdisciplinary or specialized.
# -----------------------------------------------

from __future__ import annotations

import math
from collections import Counter

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, tokenize, write_text


def entropy(counter: Counter) -> float:
    total = sum(counter.values())
    if total == 0:
        return 0.0
    h = 0.0
    for c in counter.values():
        p = c / total
        h -= p * math.log2(p)
    return h


def title_word_counter(rows: list[dict]) -> Counter:
    c = Counter()
    for r in rows:
        c.update(tokenize(r.get("title", "")))
    return c


def main() -> None:
    ensure_directories()
    f1996 = OUTPUT_DIR / "10_mit_1996.json"
    f2024 = OUTPUT_DIR / "11_mit_2024.json"

    if not f1996.exists() or not f2024.exists():
        raise SystemExit("Missing 10_mit_1996.json or 11_mit_2024.json. Run 10 and 11 first.")

    rows96 = read_json(f1996)
    rows24 = read_json(f2024)

    c96 = title_word_counter(rows96)
    c24 = title_word_counter(rows24)

    metrics = {
        "1996_unique_terms": len(c96),
        "2024_unique_terms": len(c24),
        "1996_entropy": round(entropy(c96), 4),
        "2024_entropy": round(entropy(c24), 4),
    }

    interp = "more interdisciplinary" if metrics["2024_entropy"] > metrics["1996_entropy"] else "more specialized"

    lines = [
        "Curriculum Breadth",
        "==================",
        "",
        f"Unique terms (1996): {metrics['1996_unique_terms']}",
        f"Unique terms (2024): {metrics['2024_unique_terms']}",
        f"Entropy (1996): {metrics['1996_entropy']}",
        f"Entropy (2024): {metrics['2024_entropy']}",
        "",
        f"Interpretation: 2024 appears {interp} than 1996 (token-distribution based).",
    ]

    out_txt = OUTPUT_DIR / "15_curriculum_breadth.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
