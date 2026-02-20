# Round 7 Plan

## Planner A

Focus:
1. Enforce statement-grounded accuracy checks before publishing any metric.
2. Apply confidence-comparison evidence for 1996 extraction quality decisions.
3. Improve dashboard readability and review traceability while keeping dashboard-only visualization policy.

Tasks:
1. Add confidence comparison artifact in `10_extract_1996.py` (full set vs >=0.45 threshold).
2. Add visualization policy drift warning in `09_pipeline.py`.
3. Improve `extra_dashboard.py` with round-change keywords and panel source timestamps.
4. Re-run `09`, `10~15`, and dashboard generation.
5. Refresh `16_summary_reflection.txt` with round-change summary.

DoD:
- All required scripts complete without runtime failure.
- Metrics in text outputs match current generated files.
- Dashboard shows concise round-change keywords and panel source traceability.

## Planner B

Alternative emphasis:
1. Keep improvements narrow and evidence-driven.
2. Avoid non-statement expansion; focus on quality and verification.

Tasks:
1. Preserve dashboard-only visualization governance.
2. Validate policy drift signal from `pipeline_snapshot.json`.
3. Keep round documentation explicit about what changed this round.

DoD:
- No non-required standalone visualization outputs created.
- Round artifacts include concise change summary.

## Reviewer Merged Execution Plan

1. Implement P0/P1/P2 feedback items with strict accuracy checks.
2. Re-run full workflow and validate output consistency.
3. Publish round scorecard and improvement actions with explicit round-change summary.

Execution evidence (this run):
1. `09_pipeline.py`: all `01~08` succeeded; `pipeline_snapshot.json` updated.
2. `10_extract_1996.py --force-ocr`: extraction report plus confidence-comparison report generated.
3. `11~15` regenerated and dashboard rebuilt with change keywords + source timestamps.
