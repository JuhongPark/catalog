# -----------------------------------------------
#  11. Catalog 2024
# 
#  Extract course data from the current 
#  MIT course catalog. After extracting the 
#  text, create a data model and save the 
#  processed data.
# -----------------------------------------------

from __future__ import annotations

import re
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from catalog_utils import OUTPUT_DIR, ensure_directories, normalize_whitespace, parse_course_code, strip_html, write_json


BASE_URL = "https://student.mit.edu/catalog/index.cgi"


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; catalog-bot/1.0)"})
    with urlopen(req, timeout=25) as res:
        charset = res.headers.get_content_charset() or "utf-8"
        return res.read().decode(charset, errors="replace")


def extract_subject_urls(html: str) -> list[str]:
    links = re.findall(r'href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    out = []
    seen = set()
    for href in links:
        if not re.search(r"/?m[0-9A-Za-z]+\.html$", href):
            continue
        full = urljoin(BASE_URL, href)
        if full not in seen:
            seen.add(full)
            out.append(full)
    return out


def parse_courses(html: str, url: str) -> list[dict]:
    courses = []
    seen = set()

    section_pattern = re.compile(
        r"<h3[^>]*>(.*?)</h3>(.*?)(?=(?:<a\s+name=|<h2>|<h3|</body>|$))",
        flags=re.IGNORECASE | re.DOTALL,
    )

    for m in section_pattern.finditer(html):
        raw_title = strip_html(m.group(1))
        title = normalize_whitespace(raw_title)
        if not title:
            continue

        code = parse_course_code(title)
        if not code or len(title) < 8:
            continue

        body_html = m.group(2)

        prereq_match = re.search(r"<br>\s*Prereq:\s*(.*?)(?:<br>|$)", body_html, flags=re.IGNORECASE | re.DOTALL)
        prereq = normalize_whitespace(strip_html(prereq_match.group(1))) if prereq_match else ""

        body_text = normalize_whitespace(strip_html(body_html))
        body_text = re.sub(r"\bPrereq:\b.*", "", body_text, flags=re.IGNORECASE)
        body_text = re.sub(r"\bUnits:\b.*", "", body_text, flags=re.IGNORECASE)
        body_text = normalize_whitespace(body_text)

        description = body_text[:1400]
        if prereq:
            description = f"Prereq: {prereq}. {description}" if description else f"Prereq: {prereq}."

        key = (code, title.lower())
        if key in seen:
            continue
        seen.add(key)

        courses.append(
            {
                "source": "mit",
                "year": 2024,
                "dept": code.split()[0] if " " in code else code.split(".")[0],
                "course_code": code,
                "title": title,
                "description": description,
                "url": url,
            }
        )
    return courses


def main() -> None:
    ensure_directories()

    index_html = fetch(BASE_URL)
    urls = extract_subject_urls(index_html)
    if not urls:
        urls = [BASE_URL]

    all_rows = []
    seen = set()
    for url in urls:
        try:
            html = fetch(url)
        except Exception:
            continue
        for rec in parse_courses(html, url=url):
            key = (rec["course_code"], rec["title"].lower())
            if key in seen:
                continue
            seen.add(key)
            all_rows.append(rec)

    out_file = OUTPUT_DIR / "11_mit_2024.json"
    write_json(out_file, all_rows)
    print(f"Extracted {len(all_rows)} records -> {out_file}")


if __name__ == "__main__":
    main()
