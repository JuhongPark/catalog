# Reviewer Improvement Actions (Round 6)

Input:
- `references/process/grader_scorecard_round6.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

Mandatory execution gate for next round:
- Accuracy-first rule: every analysis/metric/claim must be derived directly from statement-scoped outputs and checked for numeric consistency before publishing.
- Visualization quality rule: keep dashboard-only policy, but materially improve visual polish (layout hierarchy, readability, contrast, spacing, and chart clarity) without weakening accuracy.
- Round-change summary rule: every round output must include a concise “what changed this round” section versus the previous round.
- Dashboard change-note rule: add a short keyword-style change note panel in the dashboard describing round-level updates.
- Compliance rule: if either rule is not satisfied, do not mark the round as complete.

## Remaining Priority Actions

1. Confidence-driven filtering for 1996 extraction (`10_extract_1996.py`) - **P0**
- Add default reporting slices by reliability band and an optional production threshold mode (for example, `--min-reliability 0.45`).
- Compare quality metrics between full-set and filtered-set outputs.
- Done when low-reliability impact is quantifiably reduced with transparent tradeoff reporting.

2. 1996 title precision cleanup for analysis tasks (`10_extract_1996.py`, `13_title_evolution.py`) - **P1**
- Tighten title sanitization to reduce residual legacy label noise without suppressing true academic terms.
- Done when top declining terms are less dominated by format-era artifacts.

3. Dashboard evidence traceability improvements (`extra_dashboard.py`) - **P1**
- Add explicit “data timestamps + source output filenames” blocks for each panel.
- Improve information design for readability (clear section hierarchy, chart labeling, spacing, and visual balance).
- Add a compact “Round Change Keywords” block (short bullets/keywords) summarizing what changed from prior round.
- Done when grader can map every panel to a concrete generated artifact without opening code, dashboard readability is clearly improved, and round change notes are visible at a glance.

4. Policy compliance guard in pipeline (`09_pipeline.py`) - **P2**
- Add a lightweight warning check for non-required standalone visualization files under `data/output/`.
- Done when runs surface policy drift early and keep visualization consolidated in dashboard outputs.
