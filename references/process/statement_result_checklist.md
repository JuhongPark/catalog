# Statement Result Checklist

Purpose:
- Keep outputs strictly aligned with statement requirements.
- Ensure each item leaves enough evidence for grading.

## Item-by-item output expectations

1. `01_pull.py`
- Save raw source data.
- Leave fetch scope and source choice explicit in logs/output.

2. `02_combine.py`
- Combine pulled artifacts into one parse-ready structure.
- Keep combined-output path explicit.

3. `03_parse.py`
- Parse target entities consistently.
- Leave parse output with fields needed downstream.

4. `04_clean.py`
- Normalize/clean parsed data.
- Keep cleaning rules deterministic and reproducible.

5. `05_extract.py`
- Extract course titles/records robustly.
- Leave extraction output in structured format.

6. `06_frequency.py`
- Word frequency from titles.
- Keep preprocessing assumptions visible (case/punctuation/stopwords).

7. `07_visualization.py`
- Produce visualization of frequency results.
- Ensure chart is readable and directly tied to `06` output.

8. `08_export.py`
- Export clean dataset format and schema notes.

9. `09_pipeline.py`
- Sequentially run required scripts and stop on failure.
- Leave machine-readable run evidence when possible.

10. `10_extract_1996.py`
- Extract 1996 course records from scanned catalog.
- Leave extraction-quality evidence (coverage/reliability/report).

11. `11_extract_2024.py`
- Extract current MIT catalog records.
- Leave record count and structure consistency evidence.

12. `12_course_offerings.py`
- Analyze department-level offering deltas.
- Leave top growth/reduction lists plus interpretation notes.
- If visualization is used, numbers must match exported deltas.

13. `13_title_evolution.py`
- Compare 1996 vs current title-term frequencies.
- Leave top rising/declining terms and interpretation.

14. `14_new_and_old.py`
- Report discontinued/new subjects with clear counting basis.
- Leave pattern/trend commentary.

15. `15_curriculum_breadth.py`
- Compare breadth/diversity metrics with clear method summary.

16. `16_summary_reflection.txt`
- Summarize most significant changes across items 10~15.
- Tie findings to broader education/industry trends.
- Include limitations and next-step recommendations.

## Quality gates for every round

- Accuracy first: all claims must be traceable to generated outputs.
- Consistency: counts in summary/report/dashboard must match source files.
- Dashboard policy: keep visualization consolidated in dashboard unless statement explicitly requires a separate artifact.
- Summary-to-visual mapping rule: when a dashboard visualization directly corresponds to summary/reflection content, place that summary content near the related visualization (or in the related evaluation block) instead of isolating it in a disconnected dump.
