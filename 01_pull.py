# -----------------------------------------------
#  1. Data Acquisition:
# 
#  Objective: Download all the public course 
#  catalog data in raw HTML format from a 
#  university website.
# 
#  Tools/Resources: Extract all the course 
#  catalog data from one of the follow 
#  three universities:
#     Harvard: https://courses.my.harvard.edu
#     BU: https://www.bu.edu/academics/cas/courses
#     NE: https://catalog.northeastern.edu/course-descriptions
# -----------------------------------------------

from __future__ import annotations

import argparse
import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from catalog_utils import RAW_DIR, ensure_directories, write_json


SOURCE = "ne"
DEFAULT_START_URLS = [
    "https://catalog.northeastern.edu/course-descriptions/",
]


def fetch(url: str, timeout: int = 20) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; catalog-bot/1.0)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urlopen(req, timeout=timeout) as res:
        charset = res.headers.get_content_charset() or "utf-8"
        return res.read().decode(charset, errors="replace")


def extract_links(base_url: str, html: str, domain: str) -> list[str]:
    links = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    out: list[str] = []
    seen = set()
    for link in links:
        if link.startswith("javascript:") or link.startswith("mailto:"):
            continue
        full = urljoin(base_url, link)
        parsed = urlparse(full)
        if parsed.scheme not in {"http", "https"}:
            continue
        if domain not in (parsed.netloc or ""):
            continue
        cleaned = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if parsed.query:
            cleaned += f"?{parsed.query}"
        if cleaned not in seen:
            seen.add(cleaned)
            out.append(cleaned)
    return out


def should_keep(url: str) -> bool:
    lower = url.lower()
    if "catalog.northeastern.edu" not in lower:
        return False
    if "/course-descriptions/" not in lower:
        return False
    keywords = ["course-descriptions", "search/?p=", "courseblock"]
    return any(k in lower for k in keywords)


def crawl(start_urls: list[str], max_pages: int, delay: float) -> list[dict]:
    domain = "catalog.northeastern.edu"
    queue = deque(start_urls)
    visited = set()
    results: list[dict] = []

    while queue and len(results) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            html = fetch(url)
        except Exception as exc:
            results.append({"url": url, "status": "error", "error": str(exc)})
            continue

        results.append({"url": url, "status": "ok", "html": html})
        for nxt in extract_links(url, html, domain=domain):
            if nxt not in visited and should_keep(nxt):
                queue.append(nxt)
        if delay > 0:
            time.sleep(delay)

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Pull Northeastern catalog HTML pages")
    parser.add_argument("--max-pages", type=int, default=80)
    parser.add_argument("--delay", type=float, default=0.2)
    args = parser.parse_args()

    ensure_directories()
    out_dir = RAW_DIR / SOURCE
    out_dir.mkdir(parents=True, exist_ok=True)

    pages = crawl(DEFAULT_START_URLS, max_pages=args.max_pages, delay=args.delay)
    index = []
    for i, item in enumerate(pages, start=1):
        if item.get("status") != "ok":
            index.append(item)
            continue
        fname = out_dir / f"page_{i:04d}.html"
        fname.write_text(item["html"], encoding="utf-8")
        index.append({"url": item["url"], "status": "ok", "file": str(fname.relative_to(Path.cwd()))})

    write_json(out_dir / "index.json", index)
    ok_count = sum(1 for x in index if x.get("status") == "ok")
    err_count = sum(1 for x in index if x.get("status") != "ok")
    print(f"Saved {ok_count} HTML pages to {out_dir}")
    print(f"Errors: {err_count}")


if __name__ == "__main__":
    main()
