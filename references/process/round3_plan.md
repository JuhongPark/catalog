# Round 3 Plan

## Planner A

Focus:
1. Resolve the largest remaining quality gap: MIT 1996 extraction depth.
2. Improve reliability/reproducibility by adding extraction quality reporting.
3. Re-evaluate complete pipeline quality after fixes.

Tasks:
1. Rework `10_extract_1996.py` parser to extract course title + description chunks.
2. Add optional local-file mode to avoid unnecessary network dependency during reruns.
3. Emit extraction quality report (`10_mit_1996_extraction_report.txt`).
4. Regenerate downstream analyses (12~15) and dashboard.

DoD:
- 1996 description non-empty rate is materially above Round 2 baseline (0%).
- Round 3 scorecard reflects quality increase.

## Planner B

Alternative emphasis:
1. Keep parser conservative to avoid noisy over-extraction.
2. Prioritize precision over recall for description extraction.

Tasks:
1. Strict course-header detection and controlled description window.
2. Filter metadata-heavy lines (Prereq/Units/term markers) from description body.
3. Keep existing files stable; improve only weakest node (item 10).

DoD:
- Improved descriptions with manageable noise.
- No regression in downstream scripts.

## Reviewer Merged Execution Plan

1. Implement focused upgrade in `10_extract_1996.py` (description extraction + report).
2. Re-run 10 -> 12~15 -> dashboard.
3. Produce Round 3 grading and improvement docs.

Execution order:
1. `10_extract_1996.py`
2. `12_course_offerings.py`
3. `13_title_evolution.py`
4. `14_new_and_old.py`
5. `15_curriculum_breadth.py`
6. `extra_dashboard.py`
7. `grader_scorecard_round3.md`
8. `reviewer_improvement_round3.md`
