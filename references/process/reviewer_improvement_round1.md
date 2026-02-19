# Reviewer Improvement Actions (Round 1)

Input:
- `references/process/grader_scorecard_round1.md`

Goal:
- Improve output quality in the next round, prioritizing highest impact per effort.

## Priority Action List

1. Upgrade MIT 1996 extraction quality (`10_extract_1996.py`) - **P0**
- Why: Lowest quality score and biggest downstream impact on 12~16 reliability.
- Action:
  - Add OCR fallback path for low-quality scanned pages.
  - Separate title/code extraction from body description extraction.
  - Add extraction quality report (parse success rate, empty-description rate).
- Done when:
  - `10_mit_1996.json` has materially higher description coverage.
  - Extraction report is generated under `data/output/`.

2. Replace ASCII visualization with real chart output (`07_visualization.py`) - **P0**
- Why: Visualization quality is currently weak and below expectation.
- Action:
  - Generate actual chart artifact (e.g., matplotlib PNG or HTML chart).
  - Keep top-N configurable and include labels.
  - Add a consolidated visual result view (dashboard-style HTML or multi-chart report) for quick review.
- Done when:
  - A rendered chart file is produced in `data/output/`.
  - Chart is readable without opening raw text.
  - At least one integrated visual summary artifact is generated from key outputs (12, 13, 15).

3. Improve parser depth for Part I (`03_parse.py`, `08_export.py`) - **P1**
- Why: Export quality is limited by sparse fields (`description`, `url`).
- Action:
  - Parse NE course descriptions from courseblock body sections.
  - Preserve source URL per record.
  - Add field-level completeness checks before export.
- Done when:
  - Description coverage exceeds a defined threshold (e.g., >=80% non-empty).
  - Export schema doc reflects real populated fields.

4. Improve MIT 2024 record richness (`11_extract_2024.py`) - **P1**
- Why: Current output is mostly code/title, reducing analysis depth.
- Action:
  - Extract description and prerequisite snippets where available.
  - Normalize department/course code mapping consistently.
- Done when:
  - `11_mit_2024.json` includes non-empty descriptions for most records.

5. Strengthen analysis narratives (`12_course_offerings.py`, `14_new_and_old.py`) - **P2**
- Why: Current outputs show counts/lists but shallow reasoned interpretation.
- Action:
  - Add rule-based interpretation notes (renumbering, new programs, interdisciplinary growth).
  - Emit summary text with explicit explanation sections.
- Done when:
  - Outputs include both quantitative result and reasoned commentary blocks.

6. Improve token quality for frequency analyses (`06_frequency.py`, `13_title_evolution.py`, `15_curriculum_breadth.py`) - **P2**
- Why: Generic tokens (e.g., hours/elective) dominate signal.
- Action:
  - Add domain stopword list and optional stemming/lemmatization toggle.
  - Export top terms excluding structural catalog words.
- Done when:
  - Top-frequency outputs are topic-relevant and less metadata-heavy.

## Execution Order (Next Round)

1. `10_extract_1996.py` quality upgrade (OCR + parsing split)
2. `03_parse.py` + `08_export.py` field completeness upgrade
3. `11_extract_2024.py` richness upgrade
4. `07_visualization.py` chart rendering upgrade
5. `12`/`14` narrative enhancement
6. `06`/`13`/`15` token-quality tuning

## Expected Outcome

- Quality-first average score target:
  - from **3.44 / 5.00** to **>=4.2 / 5.00**
- Most likely score lift sources:
  - Items 10, 7, 3, 8, 11
