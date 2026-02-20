# Reviewer Improvement Actions (Round 7)

Input:
- `references/process/grader_scorecard_round7.md`

## Attention Priorities (Must Apply in This Round)

Use the following order for all planning, scoring, and feedback decisions:
1. Statement alignment (most important)
2. Result correctness and evidence validity
3. Visual quality and readability

## What Changed This Round (vs Round 6)

- Confidence comparison artifact added for 1996 extraction quality tradeoff.
- Pipeline now reports visualization-policy drift metadata.
- Dashboard now includes round-change keywords and panel source timestamps.

## Remaining Priority Actions

0. Explicit evaluator assignment: dashboard structure audit (`extra_dashboard.py`) - **P0**
- Owner: Grader + Reviewer (Improvement).
- Task: review dashboard layout end-to-end before final scoring and request/verify structure fixes when readability flow is weak.
- Required checklist:
  - Is information hierarchy clear (overview -> analysis -> summary -> round evaluation)?
  - Are summary blocks placed in the intended summary section (not mixed into unrelated sections)?
  - Is round-evaluation content grouped and positioned consistently?
  - Can core findings be understood in under 30 seconds without scrolling confusion?
- DoD: evaluator signs off dashboard structure explicitly in scorecard notes; if not passed, round is not complete.

1. Production threshold mode for 1996 extraction (`10_extract_1996.py`) - **P0**
- Add an explicit dual-output mode: full set + filtered set files (for example `10_mit_1996_filtered.json`).
- Keep threshold configurable but enforce one default benchmark (0.45) for grading reproducibility.
- Done when graders can compare both sets directly without rerunning extraction.

2. Precision cleanup for legacy title noise (`10_extract_1996.py`, `13_title_evolution.py`) - **P1**
- Reduce residual format-era descriptors in extracted titles while preserving true topic terms.
- Done when declining-term list further shifts toward domain semantics.

3. Dashboard visual polish pass (`extra_dashboard.py`) - **P1**
- Tighten visual hierarchy and spacing consistency across cards, labels, and notes.
- Keep current traceability blocks and round keywords while improving scan speed.
- Interactivity is allowed, but only in lightweight forms (for example, panel toggles, sortable views, filter chips) and only when values remain strictly report-backed.
- Do not overdo interactions: avoid heavy animation, hidden default states, excessive controls, or any behavior that makes core metrics harder to read in under 30 seconds.
- Done when dashboard communicates key changes/risks in under 30 seconds of reading.

4. Accuracy guardrail automation (`09_pipeline.py`) - **P2**
- Add a lightweight post-run numeric consistency check between key reports and JSON outputs.
- Done when common stale-metric mismatches are surfaced automatically before grading.
