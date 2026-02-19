# Reviewer Improvement Actions (Round 3)

Input:
- `references/process/grader_scorecard_round3.md`

## Remaining Priority Actions

1. OCR-backed 1996 extraction refinement (`10_extract_1996.py`) - **P0**
- Add OCR fallback path (when text layer quality is poor) and confidence-based filtering.
- Add de-columnization cleanup for multi-column scan artifacts.
- Done when description relevance and precision improve on sampled validation set.

2. Crosswalk-based longitudinal normalization (`12`, `14`) - **P1**
- Build mapping table for MIT numbering/department structural changes.
- Done when major deltas are adjusted for known renumbering cases.

3. Description quality scoring (`10`, `11`) - **P1**
- Add per-record quality flags (low/medium/high confidence).
- Done when downstream analyses can optionally filter low-confidence records.

4. Dashboard insight annotations (`extra_dashboard.py`) - **P2**
- Add short “what changed and why” callouts driven by score and metric deltas.
- Done when dashboard includes concise narrative annotations for each panel.
