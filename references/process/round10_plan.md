# Round 10 Plan

## Planner A

Focus:
1. Complete remaining Round 9 feedback items without expanding scope.
2. Strengthen interpretation traceability for department and title-change analyses.
3. Improve report readability on smaller screens while preserving metric access.

Tasks:
1. Add explicit crosswalk evidence appendix in `12_course_offerings.py` output.
2. Add declining-term bucket classification to CSV in `13_title_evolution.py`.
3. Improve guardrail mismatch message specificity in `09_pipeline.py`.
4. Tune dashboard mobile compactness in `extra_dashboard.py`.
5. Re-run full workflow (`09`, `10~15`, dashboard) and refresh `16_summary_reflection.txt`.

DoD:
- `12_course_offerings_summary.txt` contains explicit crosswalk evidence appendix.
- `13_title_evolution.csv` includes decline bucket classification.
- `pipeline_snapshot.json` remains `consistency_checks.status = pass`.
- Dashboard remains sortable/filterable and readable on smaller screens.

## Reviewer Merged Execution Plan

1. Execute all remaining P0/P1/P2 actions from Round 9.
2. Validate regenerated outputs and consistency checks.
3. Publish Round 10 scorecard and next-round improvement actions.
