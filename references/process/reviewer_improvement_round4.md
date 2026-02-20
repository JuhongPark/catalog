# Reviewer Improvement Actions (Round 4)

Input:
- `references/process/grader_scorecard_round4.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

Review notes and proposed actions must explicitly protect these three areas.

## Remaining Priority Actions

1. OCR/de-columnization upgrade for 1996 extraction (`10_extract_1996.py`) - **P0**
- Add OCR fallback for low-quality PDF text pages.
- Add de-columnization cleanup and reliability flags per extracted record.
- Done when sampled precision improves and low-reliability rows can be filtered.

2. Historical code crosswalk normalization (`12_course_offerings.py`, `14_new_and_old.py`) - **P1**
- Add mapping layer for known renumbering/restructuring changes.
- Done when extreme deltas are reduced for known renumbering cases.

3. Metadata-token suppression for title evolution (`13_title_evolution.py`) - **P1**
- Expand filtering for legacy catalog metadata artifacts.
- Done when top rising/declining terms are dominated by semantic course topics.

4. Metric snapshot artifact for grading reproducibility (`09_pipeline.py` + outputs) - **P2**
- Emit one machine-readable run summary (record counts, coverage, output paths).
- Done when grader evidence can be produced from a single snapshot file.
