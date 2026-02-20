# Round 5 Plan

## Planner A

Focus:
1. Apply P0 extraction-quality improvements to `10_extract_1996.py`.
2. Add reproducibility snapshot artifacts for grading evidence.
3. Normalize known numbering drift in comparative analyses.

Tasks:
1. Upgrade `10_extract_1996.py` with optional OCR fallback path, de-columnization, and per-record reliability flags.
2. Add reliability-aware extraction report metrics and filtering option.
3. Add department/code crosswalk normalization to `12_course_offerings.py` and `14_new_and_old.py`.
4. Suppress metadata-heavy legacy tokens in `13_title_evolution.py`.
5. Emit machine-readable run snapshot from `09_pipeline.py`.
6. Re-run `09`, `10~15`, and refresh dashboard artifacts.

DoD:
- `09_pipeline.py` completes with all `exit=0` and writes `data/output/pipeline_snapshot.json`.
- `10_mit_1996_extraction_report.txt` includes reliability and coverage metrics.
- `12~14` outputs include crosswalk-aware interpretation notes.

## Planner B

Alternative emphasis:
1. Keep scope within feedback priorities and statement alignment.
2. Improve evidence quality without broad refactor risk.

Tasks:
1. Implement only measurable quality controls tied to Round 4 feedback.
2. Prefer additive metadata fields over schema-breaking changes.
3. Re-score with run-evidence only.

DoD:
- Round 5 artifacts are reproducible from current outputs.
- Scorecard references concrete metrics from this run.

## Reviewer Merged Execution Plan

1. Implement P0 extraction controls and quality scoring in `10_extract_1996.py`.
2. Implement P1/P2 analytic controls (`12`, `13`, `14`, `09`).
3. Run full workflow and verify all generated outputs.
4. Publish Round 5 scorecard and next-round improvements.

Execution evidence (this run):
1. `09_pipeline.py` succeeded for `01~08` and wrote `data/output/pipeline_snapshot.json`.
2. `10_extract_1996.py --use-local`: 2560 records, description non-empty 67.93%, avg reliability 0.611.
3. `11_extract_2024.py`: 1449 records.
4. `12~15` outputs regenerated in `data/output/`.
