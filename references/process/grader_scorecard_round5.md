# Grader Scorecard (Round 5)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high confidence)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Round 5)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **5/5**
- Evidence: `01~08` all `exit=0` and `data/output/pipeline_snapshot.json` generated.
10. Extract MIT 1996 (`10_extract_1996.py`): **4/5**
- Evidence: 2560 records, description non-empty 67.93%, avg confidence 0.611 with per-record quality flags.
- Improvement: de-columnization, confidence scoring, optional OCR fallback path, confidence filter support.
11. Extract MIT 2024 (`11_extract_2024.py`): **4/5**
- Evidence: 1449 records extracted successfully.
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
- Improvement: alias crosswalk normalization added (for example, `6` and `6-*` grouped).
13. Title Evolution (`13_title_evolution.py`): **4/5**
- Improvement: metadata-token suppression expanded; topic terms dominate top rising list.
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
- Improvement: raw vs crosswalk-adjusted counts both reported.
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**
- Improvement: key values refreshed to current run outputs.

## Overall Evaluation

- Total score: **66 / 80**
- Average score: **4.13 / 5.00**
- Round 4 -> Round 5: **+2 points**

Top improvements achieved:
- Added reproducibility snapshot artifact (`pipeline_snapshot.json`) for grading evidence.
- Upgraded 1996 extraction quality controls with confidence and filtering signals.
- Added crosswalk-aware interpretation in comparative analyses (items 12 and 14).

Remaining highest-impact gap:
- OCR execution path is runtime-dependent and currently inactive in this environment (`tesseract` unavailable), so low-confidence legacy rows still remain.
