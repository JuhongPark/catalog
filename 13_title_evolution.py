# -----------------------------------------------
#  13. Title Evolution:
# 
#  Conduct a word frequency analysis 
#  on course titles from 1996 and 2024 
#  to explore shifts in academic 
#  terminology and focus areas.
# -----------------------------------------------

from __future__ import annotations

import re

from catalog_utils import DEFAULT_STOPWORDS, OUTPUT_DIR, ensure_directories, read_json, word_counts, write_csv, write_text


EXTRA_STOPWORDS = {
    "in",
    "of",
    "or",
    "the",
    "and",
    "is",
    "for",
    "to",
    "with",
    "prereq",
    "units",
    "permission",
    "credit",
    "instructor",
    "subject",
    "same",
    "acad",
    "year",
    "spring",
    "fall",
    "h-level",
    "u-level",
    "g-level",
    "special",
    "level",
    "catalog",
    "undergraduate",
    "graduate",
    "arranged",
    "consent",
    "staff",
}

LIKELY_FORMAT_ARTIFACTS = {
    "seminar",
    "topics",
    "advanced",
    "problems",
    "equivalent",
    "studies",
}

def decline_bucket(word: str, delta: int) -> str:
    if delta < 0 and word in LIKELY_FORMAT_ARTIFACTS:
        return "format_artifact"
    if delta < 0:
        return "domain_content"
    return "rising_or_neutral"


def normalize_title(raw_title: str) -> str:
    title = raw_title.strip()
    title = re.sub(r"^\s*[A-Z]{2,5}\s*\d{1,4}[A-Z]?\s*[:.-]?\s*", "", title)
    title = re.sub(r"^\s*\d{1,2}\.\d{1,3}[A-Z]?\s*[:.-]?\s*", "", title)
    title = re.sub(r"\b(?:Prereq|Units|Acad Year|HASS|REST)\b.*$", "", title, flags=re.IGNORECASE)
    title = re.sub(
        r"\b(?:h[\s-]?level|u[\s-]?level|g[\s-]?level|undergraduate level|graduate level)\b",
        " ",
        title,
        flags=re.IGNORECASE,
    )
    title = re.sub(r"\b(?:permission of instructor|consent of instructor|arranged)\b", " ", title, flags=re.IGNORECASE)
    title = re.sub(r"\b(?:same subject as|meets with|credit cannot also be received for)\b.*$", "", title, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", title).strip()


def top_words(rows: list[dict]) -> dict[str, int]:
    titles = [normalize_title(r.get("title", "")) for r in rows if r.get("title")]
    titles = [x for x in titles if x]
    stopwords = set(DEFAULT_STOPWORDS) | EXTRA_STOPWORDS
    return dict(word_counts(titles, stopwords=stopwords))


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
        delta = c24 - c96
        rows.append((w, c96, c24, delta, decline_bucket(w, delta)))

    rows.sort(key=lambda x: x[3], reverse=True)
    out_csv = OUTPUT_DIR / "13_title_evolution.csv"
    write_csv(out_csv, ["word", "count_1996", "count_2024", "delta", "decline_bucket"], rows)

    top_gain = rows[:20]
    top_loss = sorted(rows, key=lambda x: x[3])[:20]
    lines = ["Title Evolution", "===============", "", "Top Rising Terms:"]
    lines.extend([f"- {w}: {a} -> {b} ({d:+d})" for w, a, b, d, _ in top_gain])
    lines.append("")
    lines.append("Top Declining Terms:")
    lines.extend([f"- {w}: {a} -> {b} ({d:+d})" for w, a, b, d, _ in top_loss])
    lines.append("")
    lines.append("Likely Format-Artifact Terms (from declining list):")
    artifacts = [r for r in top_loss if r[4] == "format_artifact"]
    if artifacts:
        lines.extend([f"- {w}: {a} -> {b} ({d:+d})" for w, a, b, d, _ in artifacts])
    else:
        lines.append("- none detected in current top declining terms")

    out_txt = OUTPUT_DIR / "13_title_evolution_summary.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
