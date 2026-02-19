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
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from catalog_utils import RAW_DIR, ensure_directories, parse_course_code, strip_html, write_json


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


def extract_courses_from_text(text: str) -> list[dict]:
    records = []
    seen = set()
    for line in text.splitlines():
        line = line.strip()
        if len(line) < 8:
            continue
        code = parse_course_code(line)
        if not code:
            continue
        title = re.sub(r"\s+", " ", line)
        key = (code, title.lower())
        if key in seen:
            continue
        seen.add(key)
        records.append(
            {
                "source": "mit",
                "year": 1996,
                "dept": code.split()[0] if " " in code else code.split(".")[0],
                "course_code": code,
                "title": title,
                "description": "",
                "url": "",
            }
        )
    return records


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract MIT 1996 course records")
    parser.add_argument("--index-url", default=INDEX_URL)
    args = parser.parse_args()

    ensure_directories()
    raw_dir = RAW_DIR / "mit_1996"
    raw_dir.mkdir(parents=True, exist_ok=True)

    index_html = fetch(args.index_url)
    (raw_dir / "index.html").write_text(index_html, encoding="utf-8")

    pdf_links = extract_pdf_links(index_html)
    text_blob = [strip_html(index_html)]
    text_blob.extend(pdf_links)

    for i, pdf_url in enumerate(pdf_links, start=1):
        pdf_path = raw_dir / f"catalog_{i:02d}.pdf"
        try:
            download_binary(pdf_url, str(pdf_path))
            pdf_text = extract_text_from_pdf(str(pdf_path))
            if pdf_text:
                text_blob.append(pdf_text)
        except Exception:
            continue

    # Minimal baseline extraction from available index text/links.
    courses = extract_courses_from_text("\n".join(text_blob))

    out_file = RAW_DIR.parent / "output" / "10_mit_1996.json"
    write_json(out_file, courses)
    print(f"Index parsed: {len(pdf_links)} PDF links")
    print(f"Extracted {len(courses)} course-like records -> {out_file}")


if __name__ == "__main__":
    main()
