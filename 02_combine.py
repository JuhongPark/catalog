# -----------------------------------------------
#  2. Data Preparation:
# 
#  Objective: Combine multiple HTML files into 
#  a single document.
# 
#  Tools/Resources: Concatenate HTML text using 
#  python or javascript.
# -----------------------------------------------

from __future__ import annotations

from pathlib import Path

from catalog_utils import INTERIM_DIR, RAW_DIR, ensure_directories, write_text


SOURCE = "ne"
HEADER = "<!doctype html><html><head><meta charset='utf-8'><title>Northeastern Catalog Combined</title></head><body>"
FOOTER = "</body></html>"


def main() -> None:
    ensure_directories()
    src_dir = RAW_DIR / SOURCE
    out_file = INTERIM_DIR / f"{SOURCE}_combined.html"

    html_files = sorted(src_dir.glob("*.html"))
    if not html_files:
        raise SystemExit(f"No HTML files found in {src_dir}. Run 01_pull.py first.")

    chunks = [HEADER]
    for path in html_files:
        content = path.read_text(encoding="utf-8", errors="replace")
        chunks.append(f"\n<!-- SOURCE: {path.name} -->\n")
        chunks.append(content)
    chunks.append(FOOTER)

    write_text(out_file, "\n".join(chunks))
    print(f"Combined {len(html_files)} files -> {out_file}")


if __name__ == "__main__":
    main()
