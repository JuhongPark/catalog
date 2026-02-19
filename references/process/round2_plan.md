# Round 2 Plan

## Planner A

Priority order:
1. Improve extraction richness for core datasets (NE + MIT 2024)
2. Replace low-fidelity visualization with chart/dashboard outputs
3. Improve analysis explainability and signal quality
4. Re-run outputs and update quality scorecard

Tasks:
1. `03_parse.py`: parse NE courseblock description and source URL where possible.
2. `08_export.py`: include field completeness report in schema output.
3. `11_extract_2024.py`: capture description snippets from course blocks.
4. `06_frequency.py`: add domain stopwords to reduce metadata-heavy terms.
5. `07_visualization.py`: generate HTML chart + integrated dashboard from 12/13/15 outputs.
6. `12_course_offerings.py`, `14_new_and_old.py`: add reasoned interpretation sections.

DoD:
- `description` field coverage increases for NE and MIT 2024 exports.
- visualization output includes non-text chart artifact (`.html`).
- analysis summaries include explicit explanation blocks.

Risks:
- HTML structure drift; mitigate by regex fallbacks and graceful defaults.

## Planner B

Alternative emphasis:
1. Visualization and communication first
2. Then parsing depth and data quality

Tasks:
1. Build dashboard skeleton and chart rendering early to validate usability.
2. Backfill extraction richness for 03/11 and update exports.
3. Tune token filtering to improve top-word relevance.
4. Regenerate all affected outputs and rescore.

DoD:
- One-click review path via dashboard output.
- measurable reduction of low-value tokens in top frequency lists.

Risks:
- Overfitting stopwords; mitigate with conservative curated list.

## Reviewer Merged Execution Plan

1. Implement extraction richness first (`03`, `11`, `08`) to improve data basis.
2. Implement visualization/dashboard (`07`) and token tuning (`06`).
3. Strengthen reasoning outputs (`12`, `14`).
4. Re-run affected scripts and verify outputs.
5. Update grader scorecard for Round 2 quality view.

Execution order:
1. `03_parse.py`
2. `08_export.py`
3. `11_extract_2024.py`
4. `06_frequency.py`
5. `07_visualization.py`
6. `12_course_offerings.py`
7. `14_new_and_old.py`
8. rerun + validate outputs + scorecard update
