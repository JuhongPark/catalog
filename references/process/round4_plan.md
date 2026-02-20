# Round 4 Plan

## Planner A

Focus:
1. Re-run full workflow to refresh all outputs from current codebase.
2. Remove statement-risk from stale or inconsistent summary values.
3. Produce evidence-backed grading artifacts only from current run outputs.

Tasks:
1. Run `09_pipeline.py` and verify 01~08 all exit successfully.
2. Run `10_extract_1996.py` and `11_extract_2024.py`; record extraction metrics.
3. Run `12_course_offerings.py`, `13_title_evolution.py`, `14_new_and_old.py`, `15_curriculum_breadth.py`.
4. Regenerate dashboard via `extra_dashboard.py`.
5. Refresh `16_summary_reflection.txt` to match current output metrics.
6. Publish Round 4 scorecard and improvement actions.

DoD:
- All required scripts complete without runtime failure (except non-script text files).
- `16_summary_reflection.txt` numerics match current output files.
- Grading references concrete evidence from this run only.

## Planner B

Alternative emphasis:
1. Preserve scope: no speculative refactors outside statement requirements.
2. Prioritize grading-risk controls (evidence, reproducibility, consistency).

Tasks:
1. Keep implementation fixed; execute and validate outputs first.
2. Correct only mismatches that affect statement compliance (for example, stale counts in item 16).
3. Keep reviewer feedback focused on highest-impact remaining gap (`10_extract_1996.py` quality).

DoD:
- No out-of-scope code changes.
- Statement-facing outputs are internally consistent.

## Reviewer Merged Execution Plan

1. Execute full baseline (`09`) and Part II (`10~15`) + dashboard.
2. Apply narrow fix for item 16 consistency.
3. Grade all items against statement expectations using run evidence.
4. Produce next-round prioritized improvements.

Execution evidence (this run):
1. `09_pipeline.py` succeeded for `01~08` (all `exit=0`).
2. `10_extract_1996.py`: 3381 records, description non-empty 64.42%.
3. `11_extract_2024.py`: 1449 records.
4. `12~15` outputs regenerated in `data/output/`.
5. `extra_dashboard.py` regenerated `results/analysis_dashboard.html`.
