# Grader Scorecard (Round 3)

Grading basis: quality-first evaluation against statement expectations.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high confidence)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Quality-first)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **4/5**
10. Extract MIT 1996 (`10_extract_1996.py`): **3/5**
- Round 3 improvement: description extraction/report added and non-empty description coverage increased from 0% to 64.42%.
- Remaining gap: OCR-level cleanup and precision filtering still needed.
11. Extract MIT 2024 (`11_extract_2024.py`): **4/5**
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
13. Title Evolution (`13_title_evolution.py`): **4/5**
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**

## Overall Evaluation

- Total score: **64 / 80**
- Average score: **4.00 / 5.00**
- Round 2 -> Round 3: **+1 point** (from 63 to 64)

Top improvements achieved:
- MIT 1996 extraction depth improved (item 10).
- End-to-end outputs now include 1996 extraction quality report.

Remaining high-impact gaps:
- OCR-backed 1996 cleanup and precision control.
- historical course-code crosswalk for stronger longitudinal comparability.
