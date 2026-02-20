# Reviewer Improvement Actions (Round 5)

Input:
- `references/process/grader_scorecard_round5.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

Review notes and proposed actions must explicitly protect these three areas.

## Remaining Priority Actions

1. Activate OCR runtime for 1996 extraction (`10_extract_1996.py`) - **P0**
- Install and enable `tesseract` in the execution environment.
- Re-run extraction with OCR enabled and compare confidence/coverage deltas.
- Done when low-confidence share decreases with no major precision regression.

2. Improve MIT 2024 Course 6 coverage (`11_extract_2024.py`) - **P1**
- Expand parser patterns to capture `6-*` style/alternate heading variants.
- Done when department-level undercount for EECS is reduced with traceable evidence.

3. Refine title-token filtering (`13_title_evolution.py`) - **P1**
- Suppress additional connector tokens (for example, prepositions/articles) while preserving semantic signal.
- Done when top declining terms are less dominated by grammatical fillers.

4. Add dashboard section for confidence diagnostics (`extra_dashboard.py`) - **P2**
- Visualize confidence distribution and top quality flags from `10_mit_1996.json`.
- Done when graders can inspect extraction quality risk visually without opening raw JSON.
