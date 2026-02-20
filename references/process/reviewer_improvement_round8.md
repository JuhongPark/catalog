# Reviewer Improvement Actions (Round 8)

Input:
- `references/process/grader_scorecard_round8.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

## What Changed This Round (vs Round 7)

- MIT 1996 extraction is simplified to statement-required outputs.
- Pipeline now performs and records numeric consistency checks.
- Dashboard structure audit is explicitly documented in scorecard notes.
- Static-HTML dashboard policy is clarified: lightweight client-side interactivity is allowed when metric traceability is preserved.

## Remaining Priority Actions

1. Department crosswalk hardening (`12_course_offerings.py`) - **P0**
- Goal: reduce false large-negative deltas caused by historical code evolution.
- DoD: top 10 reduction list includes per-dept reliability notes (high/medium/low).

2. Title-evolution robustness (`13_title_evolution.py`) - **P1**
- Goal: separate legacy-format residual terms from domain-topic declines with explicit buckets.
- DoD: summary report includes a short "likely-format-artifact" section.

3. Dashboard scan-speed polish (`extra_dashboard.py`) - **P1**
- Goal: keep same structure but improve immediate readability of key risk notes.
- DoD: critical cautions visible without reading full paragraphs.

4. Consistency guardrail coverage expansion (`09_pipeline.py`) - **P2**
- Goal: add at least one additional cross-file check for 13/14 report consistency.
- DoD: mismatch examples are surfaced with file-specific labels.
