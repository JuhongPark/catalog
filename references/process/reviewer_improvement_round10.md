# Reviewer Improvement Actions (Round 10)

Input:
- `references/process/grader_scorecard_round10.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

## What Changed This Round (vs Round 9)

- Department crosswalk assumptions are now exposed in a dedicated appendix.
- Title-evolution CSV now includes explicit decline bucket classification.
- Pipeline guardrail mismatch messages now include clearer file/metric labels.
- Dashboard compactness improved for smaller screens.

## Remaining Priority Actions

1. Crosswalk maintainability (`12_course_offerings.py`) - **P0**
- Goal: move alias rules into a small versioned reference file for easier audit.
- DoD: crosswalk table is loaded from a dedicated data file with fallback validation.

2. Title-evolution analysis depth (`13_title_evolution.py`) - **P1**
- Goal: add a short aggregate bucket summary (counts/percentages) in text report.
- DoD: summary includes distribution of `format_artifact` vs `domain_content` in declining terms.

3. Dashboard signal density (`extra_dashboard.py`) - **P1**
- Goal: reduce visual clutter in round-change keywords when lines are too long.
- DoD: keyword chips are concise and non-truncated in common viewport widths.

4. Guardrail coverage (`09_pipeline.py`) - **P2**
- Goal: add one more cross-file rule tying 12 and 15 high-level trend direction checks.
- DoD: mismatch messages remain explicit and field-labeled.
