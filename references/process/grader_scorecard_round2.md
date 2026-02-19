# Grader Scorecard (Round 2)

Grading basis: quality-first evaluation against statement expectations.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high confidence)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Quality-first)

1. Data Acquisition (`01_pull.py`): **4/5**
- Stable NE crawl and reproducible raw snapshots.

2. Data Preparation (`02_combine.py`): **4/5**
- Deterministic merge and source trace comments.

3. Data Parsing (`03_parse.py`): **4/5**
- Improved NE parsing: title/code + description + source URL coverage.

4. Data Cleaning (`04_clean.py`): **4/5**
- Consistent normalization/dedup.

5. Data Extraction (`05_extract.py`): **4/5**
- Reliable title extraction.

6. Word Frequency (`06_frequency.py`): **4/5**
- Domain stopwords added, significantly cleaner top terms.

7. Data Visualization (`07_visualization.py`): **5/5**
- Upgraded from ASCII output to integrated HTML dashboard (`analysis_dashboard.html`) with multi-output visuals.

8. Export Clean Dataset (`08_export.py`): **4/5**
- Export now includes field completeness metrics; NE description coverage is high.

9. Data Pipeline (`09_pipeline.py`): **4/5**
- Sequential orchestration and restart support remain solid.

10. Extract MIT 1996 (`10_extract_1996.py`): **2/5**
- Still weakest area; no OCR fallback and description quality remains limited.

11. Extract MIT 2024 (`11_extract_2024.py`): **4/5**
- Improved with description/prereq extraction and full URL coverage.

12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
- Added reasoned explanation notes with caveat handling for renumbering effects.

13. Title Evolution (`13_title_evolution.py`): **4/5**
- Strong comparative outputs with improved token signal quality.

14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
- Added reasoned pattern interpretation beyond raw list output.

15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
- Clear metric + interpretation; still single-metric bias risk.

16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**
- Good synthesis with explicit data-quality limitations.

## Overall Evaluation

- Total score: **63 / 80**
- Average score: **3.94 / 5.00**
- Round 1 -> Round 2: **+8 points** (from 55 to 63)

Top improvements achieved:
- Visualization quality (7)
- Parsing/export richness (3,8)
- MIT 2024 richness (11)
- Analysis explanation depth (12,14)

Remaining high-impact gap:
- MIT 1996 OCR-grade extraction quality (10)
