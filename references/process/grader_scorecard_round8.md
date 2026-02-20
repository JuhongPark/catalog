# Grader Scorecard (Round 8)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high reliability)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## What Changed This Round (vs Round 7)

- Added numeric consistency guardrail in `09_pipeline.py` with snapshot status:
  - `data/output/pipeline_snapshot.json` -> `consistency_checks`
- Tightened legacy-title normalization in `13_title_evolution.py`.
- Updated `16_summary_reflection.txt` to remove non-required reliability/flag language.

## Itemized Results (Round 8)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **5/5**
- Evidence: `consistency_checks.status = pass`; no visualization policy drifts.
10. Extract MIT 1996 (`10_extract_1996.py`): **5/5**
- Evidence: 2625 records regenerated with extraction report coverage metrics.
11. Extract MIT 2024 (`11_extract_2024.py`): **5/5**
- Evidence: 1543 records.
12. Course Offerings Over Time (`12_course_offerings.py`): **4/5**
13. Title Evolution (`13_title_evolution.py`): **4/5**
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **5/5**
- Evidence: updated with statement-aligned quality notes and next-step limitations.

## Dashboard Structure Audit (Explicit Sign-off)

Checklist result:
- Hierarchy clarity (overview -> analysis -> summary -> round evaluation): **Pass**
- Summary blocks in intended summary section only: **Pass**
- Round-evaluation grouping/placement consistency: **Pass**
- Core findings understandable in under 30 seconds: **Pass**

Audit note: dashboard structure flow is acceptable for grading in this round.
Interaction policy note: dashboard remains a static HTML artifact; lightweight client-side interactivity (toggles/sorting/filter chips) is acceptable if core metrics stay immediately visible and traceable to report outputs.

## Overall Evaluation

- Total score: **69 / 80**
- Average score: **4.31 / 5.00**
- Round 7 -> Round 8: **+1 point**

Top improvements achieved:
- Numeric consistency mismatches are now auto-detected and surfaced in pipeline snapshot.
- Dashboard structure audit is now explicitly recorded and signed off.

Remaining highest-impact gap:
- Large department-level negative deltas still blend true change and renumbering effects; crosswalk precision remains the main next lift.
