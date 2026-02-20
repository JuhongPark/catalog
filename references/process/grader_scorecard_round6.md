# Grader Scorecard (Round 6)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high reliability)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Round 6)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **5/5**
- Evidence: `01~08` pipeline execution and machine-readable snapshot artifact available (`data/output/pipeline_snapshot.json`).
10. Extract MIT 1996 (`10_extract_1996.py`): **4/5**
- Evidence: OCR runtime active (`ocr_runtime_available: True`), 2625 records, description non-empty 68.80%, avg reliability 0.614.
- Remaining gap: low-reliability rows still sizable (959 records under 0.45 reliability).
11. Extract MIT 2024 (`11_extract_2024.py`): **5/5**
- Evidence: parser coverage improved to 1543 records with strong Course 6 capture.
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
- Evidence: crosswalk normalization and interpretation notes maintained; outputs regenerated.
13. Title Evolution (`13_title_evolution.py`): **4/5**
- Evidence: metadata and connector-token suppression improved interpretability.
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
- Evidence: raw and normalized change counts both reported.
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**
- Evidence: summary refreshed with OCR-enabled extraction metrics.

## Overall Evaluation

- Total score: **67 / 80**
- Average score: **4.19 / 5.00**
- Round 5 -> Round 6: **+1 point**

Top improvements achieved:
- OCR runtime actually activated and integrated into 1996 extraction run.
- MIT 2024 extraction coverage improved materially (notably Course 6 family).
- Visualization governance clarified: non-required standalone visual files removed; dashboard-centric display policy documented.

Remaining highest-impact gap:
- Confidence quality in 1996 extraction still has a substantial low-reliability tail; next-round value is in precision filtering and parser refinement rather than broader scope expansion.
- Next-round scoring should enforce two non-negotiables: statement-grounded numeric accuracy first, and materially improved dashboard visual quality second.
- Next-round deliverables should also include (a) a concise per-round change summary and (b) dashboard-visible short change keywords for quick review.
