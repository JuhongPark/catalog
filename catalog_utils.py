from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = BASE_DIR / "logs"


DEFAULT_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
    "i",
    "ii",
    "iii",
}


def ensure_directories() -> None:
    for path in (DATA_DIR, RAW_DIR, INTERIM_DIR, OUTPUT_DIR, LOG_DIR):
        path.mkdir(parents=True, exist_ok=True)


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data, indent: int = 2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def strip_html(html: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str, stopwords: Iterable[str] | None = None) -> list[str]:
    sw = set(DEFAULT_STOPWORDS if stopwords is None else stopwords)
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9\-']*", text.lower())
    return [w for w in words if w not in sw and len(w) > 1]


def word_counts(lines: Iterable[str], stopwords: Iterable[str] | None = None) -> Counter:
    counter: Counter = Counter()
    for line in lines:
        counter.update(tokenize(line, stopwords=stopwords))
    return counter


def write_csv(path: Path, headers: list[str], rows: Iterable[Iterable]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_course_code(text: str) -> str:
    match = re.match(r"^([A-Z]{2,5}\s*\d{1,4}[A-Z]?)\b", text)
    if match:
        return normalize_whitespace(match.group(1))
    match = re.match(r"^(\d{1,2}\.\d{1,3}[A-Z]?)\b", text)
    if match:
        return normalize_whitespace(match.group(1))
    return ""
