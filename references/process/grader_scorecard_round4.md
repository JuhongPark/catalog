# Grader Scorecard (Round 4)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high reliability)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Round 4)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **4/5**
- Evidence: full `01~08` run completed with all `exit=0`.
10. Extract MIT 1996 (`10_extract_1996.py`): **3/5**
- Evidence: 3381 records and 64.42% non-empty descriptions in extraction report.
- Remaining gap: OCR-backed cleanup and precision filtering for scanned artifacts.
11. Extract MIT 2024 (`11_extract_2024.py`): **4/5**
- Evidence: 1449 records extracted successfully.
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
13. Title Evolution (`13_title_evolution.py`): **4/5**
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**
- Improvement: stale counts were corrected to match current outputs.

## Overall Evaluation

- Total score: **64 / 80**
- Average score: **4.00 / 5.00**
- Round 3 -> Round 4: **0 point change** (quality sustained; consistency improved).

Strengths:
- End-to-end reproducibility remains stable.
- Statement-required artifacts are regenerated and consistent.

Remaining highest-impact gap:
- Item 10 extraction quality for noisy scanned pages (OCR/de-columnization/reliability scoring).
