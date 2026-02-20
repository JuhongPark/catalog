# Reviewer Improvement Actions (Round 2)

Input:
- `references/process/grader_scorecard_round2.md`

## Remaining Priority Actions

1. MIT 1996 OCR pipeline (`10_extract_1996.py`) - **P0**
- Add OCR fallback for hard pages (e.g., image-based text) and reliability-based post-filtering.
- Done when description coverage and parse precision improve measurably.

2. Historical crosswalk for subject-code evolution (`12`, `14`) - **P1**
- Introduce mapping table for old/new MIT numbering systems.
- Done when large deltas are normalized for known renumbering cases.

3. Visualization polish (`07`) - **P1**
- Add trend annotations and downloadable chart images.
- Done when dashboard includes at least one annotated insight callout per panel.

4. Semantic text normalization (`06`, `13`, `15`) - **P2**
- Optional lemmatization/stemming to improve term aggregation.
- Done when equivalent inflections are merged in frequency outputs.

## Note
- Follow the global planning/grading guardrails defined in `references/process/project_plan.md` and role rules in `references/process/personas.md`.
