# Round 8 Plan

## Planner A

Focus:
1. Apply unresolved P0/P1/P2 feedback from Round 7 without widening scope.
2. Keep MIT 1996 extraction outputs simple and statement-aligned.
3. Add automatic numeric mismatch detection before grading.
4. Keep dashboard delivery as static HTML while explicitly allowing lightweight client-side interactivity.

Tasks:
1. Keep `10_extract_1996.py` focused on required output (`10_mit_1996.json`) and extraction report.
2. Add post-run consistency checks in `09_pipeline.py` and expose status in `pipeline_snapshot.json`.
3. Tighten legacy-format title cleanup in `13_title_evolution.py`.
4. Re-run full workflow (`09`, `10~15`, dashboard), then refresh `16_summary_reflection.txt`.
5. Document static-HTML interaction policy (toggles/sorting/filter chips allowed with statement-backed values).

DoD:
- `10_mit_1996.json` and `10_mit_1996_extraction_report.txt` are regenerated without runtime failure.
- `pipeline_snapshot.json` includes `consistency_checks.status = pass`.
- Summary reflects current run metrics.

## Reviewer Merged Execution Plan

1. Prioritize statement alignment and numeric evidence consistency.
2. Verify dashboard structure flow (overview -> analysis -> summary -> round evaluation).
3. Publish Round 8 scorecard with explicit dashboard-structure audit sign-off.
