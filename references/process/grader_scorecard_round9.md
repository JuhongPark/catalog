# Grader Scorecard (Round 9)

Grading basis: statement-first evaluation using current run outputs only.

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high reliability)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## What Changed This Round (vs Round 8)

- Added per-department reliability notes to top reduced departments in `12_course_offerings_summary.txt`.
- Added explicit "Likely Format-Artifact Terms" section to `13_title_evolution_summary.txt`.
- Added 13/14 cross-file guardrail checks in `09_pipeline.py`.
- Added concise "Critical Cautions" block in dashboard analysis section.
- Updated `16_summary_reflection.txt` with reliability-note and artifact-section implications.

## Itemized Results (Round 9)

1. Data Acquisition (`01_pull.py`): **4/5**
2. Data Preparation (`02_combine.py`): **4/5**
3. Data Parsing (`03_parse.py`): **4/5**
4. Data Cleaning (`04_clean.py`): **4/5**
5. Data Extraction (`05_extract.py`): **4/5**
6. Word Frequency (`06_frequency.py`): **4/5**
7. Data Visualization (`07_visualization.py`): **5/5**
8. Export Clean Dataset (`08_export.py`): **4/5**
9. Data Pipeline (`09_pipeline.py`): **5/5**
- Evidence: `consistency_checks.status = pass`; no policy drifts; added 13/14 cross-check logic.
10. Extract MIT 1996 (`10_extract_1996.py`): **5/5**
- Evidence: 2625 records with stable extraction report coverage.
11. Extract MIT 2024 (`11_extract_2024.py`): **5/5**
- Evidence: 1543 records.
12. Course Offerings Over Time (`12_course_offerings.py`): **5/5**
- Evidence: top reduced departments now include reliability notes.
13. Title Evolution (`13_title_evolution.py`): **5/5**
- Evidence: summary now distinguishes likely format-artifact declines.
14. New/Discontinued Subjects (`14_new_and_old.py`): **4/5**
15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
16. Summary and Reflection (`16_summary_reflection.txt`): **5/5**
- Evidence: updated to reflect reliability-aware and artifact-aware interpretation.

## Dashboard Structure Audit (Explicit Sign-off)

Checklist result:
- Hierarchy clarity (overview -> analysis -> summary -> round evaluation): **Pass**
- Summary blocks in intended summary section only: **Pass**
- Round-evaluation grouping/placement consistency: **Pass**
- Core findings understandable in under 30 seconds: **Pass**

Audit note: Round 9 dashboard improves risk visibility with concise caution block while preserving scan speed.

## Overall Evaluation

- Total score: **71 / 80**
- Average score: **4.44 / 5.00**
- Round 8 -> Round 9: **+2 points**

Top improvements achieved:
- Department-level interpretation is now reliability-tagged for high-delta reductions.
- Title-evolution report now separates likely format artifacts from domain-term signals.
- Pipeline consistency guardrail coverage expanded to include 13/14 relationship checks.

Remaining highest-impact gap:
- Department crosswalk evidence is still heuristic and can be strengthened with richer historical mapping references.
