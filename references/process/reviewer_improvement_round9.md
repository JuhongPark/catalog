# Reviewer Improvement Actions (Round 9)

Input:
- `references/process/grader_scorecard_round9.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

## What Changed This Round (vs Round 8)

- Reduced-department interpretation now includes explicit reliability notes.
- Title-evolution output now explicitly separates likely format-artifact terms.
- Pipeline consistency checks now cover a 13/14 signal-coherence condition.
- Dashboard highlights critical cautions in a concise, visible block.

## Remaining Priority Actions

1. Department crosswalk evidence depth (`12_course_offerings.py`) - **P0**
- Goal: improve reliability-note grounding with explicit mapping references.
- DoD: include a short crosswalk-evidence appendix or reference table for top high-impact departments.

2. Title-evolution interpretability (`13_title_evolution.py`) - **P1**
- Goal: split declining terms into two explicit buckets (format-artifact vs domain-content) in CSV output as well.
- DoD: summary and CSV both expose the bucket classification.

3. Dashboard compactness (`extra_dashboard.py`) - **P1**
- Goal: keep caution visibility while preventing card sprawl on smaller screens.
- DoD: analysis section remains readable with minimal scrolling on standard laptop viewport.

4. Guardrail message quality (`09_pipeline.py`) - **P2**
- Goal: improve mismatch message specificity with file/metric labels.
- DoD: each guardrail failure message names exact source fields and expected relationship.
