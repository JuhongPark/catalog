# -----------------------------------------------
#  14. New and Discontinued Subjects:
# 
#  Identify subjects that were offered in 
#  1996 but no longer exist in 2024, as 
#  well as new subjects introduced in 2024. 
#  Explore possible reasons for these changes.
# -----------------------------------------------

from __future__ import annotations

from catalog_utils import OUTPUT_DIR, ensure_directories, read_json, write_text


def to_set(rows: list[dict]) -> set[str]:
    vals = set()
    for r in rows:
        c = (r.get("course_code") or "").strip().upper()
        if c:
            vals.add(c)
    return vals


def main() -> None:
    ensure_directories()
    f1996 = OUTPUT_DIR / "10_mit_1996.json"
    f2024 = OUTPUT_DIR / "11_mit_2024.json"

    if not f1996.exists() or not f2024.exists():
        raise SystemExit("Missing 10_mit_1996.json or 11_mit_2024.json. Run 10 and 11 first.")

    s96 = to_set(read_json(f1996))
    s24 = to_set(read_json(f2024))

    discontinued = sorted(s96 - s24)
    new = sorted(s24 - s96)

    lines = [
        "New and Discontinued Subjects",
        "============================",
        "",
        f"Discontinued since 1996: {len(discontinued)}",
    ]
    lines.extend([f"- {x}" for x in discontinued[:200]])
    lines.append("")
    lines.append(f"New by 2024: {len(new)}")
    lines.extend([f"- {x}" for x in new[:200]])

    out_txt = OUTPUT_DIR / "14_new_and_old.txt"
    write_text(out_txt, "\n".join(lines) + "\n")
    print(f"Wrote {out_txt}")


if __name__ == "__main__":
    main()
