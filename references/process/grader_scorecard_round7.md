# Grader Scorecard (Round 7)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high confidence)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## What Changed This Round (vs Round 6)

- Added confidence tradeoff artifact: `data/output/10_mit_1996_confidence_comparison.txt`.
- Added pipeline visualization-policy drift signal: `visualization_policy_drifts` in `data/output/pipeline_snapshot.json`.
- Upgraded dashboard with short round-change keywords and per-panel source timestamps.
- Added explicit round-change summary in `16_summary_reflection.txt`.

## Itemized Results (Round 7)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **5/5**
- Evidence: full `01~08` success and policy-drift metadata captured in snapshot.
10. Extract MIT 1996 (`10_extract_1996.py`): **4/5**
- Evidence: OCR active, 2625 records, 68.80% non-empty descriptions, avg confidence 0.614.
- Added evidence: threshold comparison shows `>=0.45` subset improves avg confidence to 0.752.
11. Extract MIT 2024 (`11_extract_2024.py`): **5/5**
- Evidence: 1543 records with improved code coverage.
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
13. Title Evolution (`13_title_evolution.py`): **4/5**
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **5/5**
- Evidence: updated with current metrics and explicit round-change summary.

## Overall Evaluation

- Total score: **68 / 80**
- Average score: **4.25 / 5.00**
- Round 6 -> Round 7: **+1 point**

Top improvements achieved:
- Accuracy evidence strengthened through confidence-threshold comparison outputs.
- Dashboard readability/traceability improved with clear update labels and source timestamps.
- Governance checks added to prevent visualization policy drift.

Remaining highest-impact gap:
- 1996 low-confidence tail remains meaningful; next-round gains depend on precision filtering defaults and additional title/description cleanup.
- Dashboard can be further strengthened with lightweight interactivity (filters/toggles/sorting) as long as statement-grounded metric accuracy is preserved.
- Scoring guardrail: interactivity should improve discoverability, not complexity; if interactions obscure or delay access to core metrics, apply a visualization-quality deduction.
- Evaluator responsibility: include an explicit dashboard-structure audit note in grading output (hierarchy, section placement, summary mapping, and scan-speed clarity).
