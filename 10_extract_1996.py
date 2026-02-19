# -----------------------------------------------
#  10. Catalog 1996
# 
#  Extract course data from the scanned 
#  1996 MIT course catalog. After extracting 
#  the text, create a data model and save the 
#  processed data. This task emphasizes 
#  working with raw, scanned documents 
#  and aims to teach you how to extract 
#  information from non-digitized sources.
# -----------------------------------------------

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from catalog_utils import OUTPUT_DIR, RAW_DIR, ensure_directories, normalize_whitespace, parse_course_code, strip_html, write_json, write_text


INDEX_URL = "https://onexi.org/catalog/pdf/index.html"


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; catalog-bot/1.0)"})
    with urlopen(req, timeout=25) as res:
        charset = res.headers.get_content_charset() or "utf-8"
        return res.read().decode(charset, errors="replace")


def download_binary(url: str, out_path: str) -> None:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; catalog-bot/1.0)"})
    with urlopen(req, timeout=30) as res:
        data = res.read()
    with open(out_path, "wb") as f:
        f.write(data)


def extract_pdf_links(index_html: str) -> list[str]:
    links = re.findall(r'href=["\']([^"\']+\.pdf)["\']', index_html, flags=re.IGNORECASE)
    out = []
    seen = set()
    for link in links:
        full = urljoin(INDEX_URL, link)
        if full not in seen:
            seen.add(full)
            out.append(full)
    return out


def extract_text_from_pdf(pdf_path: str) -> str:
    txt_path = f"{pdf_path}.txt"
    try:
        subprocess.run(["pdftotext", "-layout", pdf_path, txt_path], check=True, capture_output=True, text=True)
    except Exception:
        return ""
    if not os.path.exists(txt_path):
        return ""
    with open(txt_path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def looks_like_metadata(line: str) -> bool:
    lower = line.lower()
    blockers = [
        "prereq",
        "acad year",
        "u (",
        "g (",
        "iap",
        "same subject as",
        "meets with",
        "hass",
        "rest",
        "h-level",
        "credit cannot",
        "units",
    ]
    return any(x in lower for x in blockers)


def is_probable_title(text: str, code: str) -> bool:
    if len(text) < 8:
        return False
    lower = text.lower()
    if lower.startswith("course "):
        return False
    if lower.startswith("chapter "):
        return False
    if "guide to" in lower:
        return False
    # Title should contain additional words after course code.
    compact_code = code.replace(" ", "")
    compact_text = text.replace(" ", "")
    return len(compact_text) > len(compact_code) + 4


def split_line_into_course_segments(line: str) -> list[str]:
    pattern = re.compile(r"(?<![A-Za-z0-9])(?:\d{1,2}\.\d{2,3}[A-ZJ]?|[A-Z]{2,4}\s*\d{3,4}[A-Z]?)\s+")
    matches = list(pattern.finditer(line))
    if not matches:
        return []
    out = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
        seg = normalize_whitespace(line[start:end])
        if seg:
            out.append(seg)
    return out


def extract_courses_from_text(text: str) -> list[dict]:
    lines = [normalize_whitespace(x) for x in text.replace("\f", "\n").splitlines()]

    entries: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue

        segments = split_line_into_course_segments(line)
        for seg in segments:
            code = parse_course_code(seg)
            if not code:
                continue

            title = normalize_whitespace(seg)
            if not is_probable_title(title, code):
                continue

            # Collect nearby descriptive lines until next strong course header block.
            desc_parts: list[str] = []
            j = i + 1
            steps = 0
            while j < len(lines) and steps < 28:
                candidate = lines[j]
                steps += 1
                if not candidate:
                    j += 1
                    continue

                next_segments = split_line_into_course_segments(candidate)
                if next_segments:
                    # Another course header starts here.
                    break

                if looks_like_metadata(candidate):
                    j += 1
                    continue

                if len(candidate) < 20:
                    j += 1
                    continue

                desc_parts.append(candidate)
                j += 1

            description = normalize_whitespace(" ".join(desc_parts))

            entries.append(
                {
                    "source": "mit",
                    "year": 1996,
                    "dept": code.split()[0] if " " in code else code.split(".")[0],
                    "course_code": code,
                    "title": title,
                    "description": description,
                    "url": "",
                }
            )

        i += 1

    # Deduplicate by (code,title), keep longest description.
    best: dict[tuple[str, str], dict] = {}
    for rec in entries:
        key = (rec["course_code"], rec["title"].lower())
        prev = best.get(key)
        if prev is None or len(rec["description"]) > len(prev["description"]):
            best[key] = rec

    return list(best.values())


def generate_report(rows: list[dict], pdf_count: int) -> str:
    total = len(rows)
    desc_non_empty = sum(1 for r in rows if str(r.get("description", "")).strip())
    desc_pct = (desc_non_empty / total * 100) if total else 0.0
    avg_desc_len = (sum(len(str(r.get("description", ""))) for r in rows) / total) if total else 0.0
    return (
        "MIT 1996 Extraction Report\n"
        "==========================\n"
        f"PDF files processed: {pdf_count}\n"
        f"records: {total}\n"
        f"description_non_empty: {desc_non_empty} ({desc_pct:.2f}%)\n"
        f"avg_description_length: {avg_desc_len:.1f}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract MIT 1996 course records")
    parser.add_argument("--index-url", default=INDEX_URL)
    parser.add_argument("--use-local", action="store_true", help="Use already-downloaded local PDFs when available")
    args = parser.parse_args()

    ensure_directories()
    raw_dir = RAW_DIR / "mit_1996"
    raw_dir.mkdir(parents=True, exist_ok=True)

    index_html = ""
    pdf_links: list[str] = []

    if args.use_local and (raw_dir / "index.html").exists():
        index_html = (raw_dir / "index.html").read_text(encoding="utf-8", errors="replace")
        pdf_links = extract_pdf_links(index_html)
    else:
        index_html = fetch(args.index_url)
        (raw_dir / "index.html").write_text(index_html, encoding="utf-8")
        pdf_links = extract_pdf_links(index_html)

    text_blob = [strip_html(index_html)]
    text_blob.extend(pdf_links)

    pdf_paths: list[Path] = []
    for i, pdf_url in enumerate(pdf_links, start=1):
        pdf_path = raw_dir / f"catalog_{i:02d}.pdf"
        pdf_paths.append(pdf_path)
        if not pdf_path.exists() or not args.use_local:
            try:
                download_binary(pdf_url, str(pdf_path))
            except Exception:
                continue

        pdf_text = extract_text_from_pdf(str(pdf_path))
        if pdf_text:
            text_blob.append(pdf_text)

    courses = extract_courses_from_text("\n".join(text_blob))

    out_file = OUTPUT_DIR / "10_mit_1996.json"
    write_json(out_file, courses)

    report = generate_report(courses, pdf_count=len([p for p in pdf_paths if p.exists()]))
    report_path = OUTPUT_DIR / "10_mit_1996_extraction_report.txt"
    write_text(report_path, report)

    print(f"Index parsed: {len(pdf_links)} PDF links")
    print(f"Extracted {len(courses)} course-like records -> {out_file}")
    print(f"Wrote extraction report -> {report_path}")


if __name__ == "__main__":
    main()
