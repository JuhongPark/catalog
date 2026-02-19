# -----------------------------------------------
#  13. Title Evolution:
# 
#  Conduct a word frequency analysis 
#  on course titles from 1996 and 2024 
#  to explore shifts in academic 
#  terminology and focus areas.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, word_counts, write_csv, write_text


def top_words(rows: list[dict]) -> dict[str, int]:
    titles = [r.get("title", "") for r in rows if r.get("title")]
    return dict(word_counts(titles))


def main() -> None:
    ensure_directories()
    f1996 = OUTPUT_DIR / "10_mit_1996.json"
    f2024 = OUTPUT_DIR / "11_mit_2024.json"

    if not f1996.exists() or not f2024.exists():
        raise SystemExit("Missing 10_mit_1996.json or 11_mit_2024.json. Run 10 and 11 first.")

    d96 = top_words(read_json(f1996))
    d24 = top_words(read_json(f2024))
    words = sorted(set(d96) | set(d24))

    rows = []
    for w in words:
        c96 = d96.get(w, 0)
        c24 = d24.get(w, 0)
        rows.append((w, c96, c24, c24 - c96))

    rows.sort(key=lambda x: x[3], reverse=True)
    out_csv = OUTPUT_DIR / "13_title_evolution.csv"
    write_csv(out_csv, ["word", "count_1996", "count_2024", "delta"], rows)

    top_gain = rows[:20]
    top_loss = sorted(rows, key=lambda x: x[3])[:20]
    lines = ["Title Evolution", "===============", "", "Top Rising Terms:"]
    lines.extend([f"- {w}: {a} -> {b} ({d:+d})" for w, a, b, d in top_gain])
    lines.append("")
    lines.append("Top Declining Terms:")
    lines.extend([f"- {w}: {a} -> {b} ({d:+d})" for w, a, b, d in top_loss])

    out_txt = OUTPUT_DIR / "13_title_evolution_summary.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
