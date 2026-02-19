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

from catalog_utils import INTERIM_DIR, ensure_directories, parse_course_code, strip_html, write_json

SOURCE = "ne"

TITLE_PATTERNS = [
    re.compile(
        r'<p[^>]*class="courseblocktitle[^"]*"[^>]*>\s*<strong>(.*?)</strong>\s*</p>',
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(r"<h[1-4][^>]*>(.*?)</h[1-4]>", re.IGNORECASE | re.DOTALL),
    re.compile(r"<a[^>]*>([A-Z]{2,5}\s*\d{1,4}[A-Z]?\s+[^<]{5,})</a>", re.IGNORECASE),
    re.compile(r">\s*(\d{1,2}\.\d{1,3}[A-Z]?\s+[^<]{5,})\s*<"),
]


def parse_courses(html: str) -> list[dict]:
    records: list[dict] = []
    seen = set()

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
