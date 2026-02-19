# -----------------------------------------------
#   3. Data Parsing:
# 
#   Objective: Parse course data leveraging
#   HTML elements structure.
# 
#   Tools/Resources: Use resources like the 
#   DOMParser, BeautifulSoup, or Regular Expressions.
#       Beautiful Soup:
#           https://www.crummy.com/software/BeautifulSoup/
#       DOMParser:
#           https://developer.mozilla.org/en-US/docs/Web/API/DOMParser
#       RegEx:
#           https://regexr.com 
#           https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
# -----------------------------------------------

from __future__ import annotations

import re

from catalog_utils import INTERIM_DIR, ensure_directories, normalize_whitespace, parse_course_code, strip_html, write_json

SOURCE = "ne"
BASE_URL = "https://catalog.northeastern.edu"

TITLE_PATTERNS = [
    re.compile(
        r'<p[^>]*class="courseblocktitle[^"]*"[^>]*>\s*<strong>(.*?)</strong>\s*</p>',
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(r"<h[1-4][^>]*>(.*?)</h[1-4]>", re.IGNORECASE | re.DOTALL),
    re.compile(r"<a[^>]*>([A-Z]{2,5}\s*\d{1,4}[A-Z]?\s+[^<]{5,})</a>", re.IGNORECASE),
    re.compile(r">\s*(\d{1,2}\.\d{1,3}[A-Z]?\s+[^<]{5,})\s*<"),
]


def absolutize_url(url: str) -> str:
    if not url:
        return ""
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/"):
        return f"{BASE_URL}{url}"
    return f"{BASE_URL}/{url}"


def parse_from_courseblocks(html: str) -> list[dict]:
    records: list[dict] = []
    seen = set()

    block_pattern = re.compile(
        r'<div\s+class="courseblock"[^>]*>(.*?)</div>\s*(?=<div\s+class="courseblock"|$)',
        re.IGNORECASE | re.DOTALL,
    )

    for m in block_pattern.finditer(html):
        block = m.group(1)

        title_match = re.search(
            r'<p[^>]*class="courseblocktitle[^"]*"[^>]*>\s*<strong>(.*?)</strong>\s*</p>',
            block,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if not title_match:
            continue

        raw_title = strip_html(title_match.group(1))
        title = normalize_whitespace(raw_title)
        code = parse_course_code(title)
        if not code:
            continue

        desc_match = re.search(r'<p[^>]*class="cb_desc"[^>]*>(.*?)</p>', block, flags=re.IGNORECASE | re.DOTALL)
        description = normalize_whitespace(strip_html(desc_match.group(1))) if desc_match else ""

        if not description:
            # Fallback: remove title/extra blocks and keep residual text.
            residual = re.sub(r'<p[^>]*class="courseblocktitle[^"]*"[^>]*>.*?</p>', ' ', block, flags=re.IGNORECASE | re.DOTALL)
            residual = re.sub(r'<p[^>]*class="courseblockextra[^"]*"[^>]*>.*?</p>', ' ', residual, flags=re.IGNORECASE | re.DOTALL)
            description = normalize_whitespace(strip_html(residual))

        link_match = re.search(r'href=["\']([^"\']+)["\']', block, flags=re.IGNORECASE)
        url = absolutize_url(link_match.group(1)) if link_match else ""

        key = (code, title.lower())
        if key in seen:
            continue
        seen.add(key)

        records.append(
            {
                "source": SOURCE,
                "year": None,
                "dept": code.split()[0] if " " in code else code.split(".")[0],
                "course_code": code,
                "title": title,
                "description": description,
                "url": url,
            }
        )

    return records


def parse_with_fallback_patterns(html: str, seen: set[tuple[str, str]]) -> list[dict]:
    records: list[dict] = []
    for pattern in TITLE_PATTERNS:
        for m in pattern.finditer(html):
            raw = strip_html(m.group(1))
            title = re.sub(r"\s+", " ", raw).strip(" -|\t\n\r")
            if len(title) < 8:
                continue
            code = parse_course_code(title)
            if not code:
                continue
            key = (code, title.lower())
            if key in seen:
                continue
            seen.add(key)
            records.append(
                {
                    "source": SOURCE,
                    "year": None,
                    "dept": code.split()[0] if " " in code else code.split(".")[0],
                    "course_code": code,
                    "title": title,
                    "description": "",
                    "url": "",
                }
            )
    return records


def parse_courses(html: str) -> list[dict]:
    block_records = parse_from_courseblocks(html)
    seen = {(r["course_code"], r["title"].lower()) for r in block_records}
    fallback_records = parse_with_fallback_patterns(html, seen=seen)
    return block_records + fallback_records


def main() -> None:
    ensure_directories()
    combined = INTERIM_DIR / f"{SOURCE}_combined.html"
    out_file = INTERIM_DIR / f"{SOURCE}_parsed.json"

    if not combined.exists():
        raise SystemExit(f"Missing {combined}. Run 02_combine.py first.")

    html = combined.read_text(encoding="utf-8", errors="replace")
    courses = parse_courses(html)

    write_json(out_file, courses)
    print(f"Parsed {len(courses)} candidate courses -> {out_file}")


if __name__ == "__main__":
    main()
