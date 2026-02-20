# Grader Scorecard (Round 1)

Grading basis: statement requirements in `references/google-docs/1kxmwf7e-cLBEEC92QaNUIOeIYWupwPOSnFPnGZrKHfI/document.md`

## 5-Point Quality Scale

- 5: excellent quality (robust, clear, high reliability)
- 4: good quality (solid implementation with minor limitations)
- 3: acceptable quality (works but notable quality gaps)
- 2: weak quality (limited depth/robustness)
- 1: poor quality (insufficient)

## Itemized Results (Quality-first)

1. Data Acquisition (`01_pull.py`): **4/5**
- Strength: stable NE collection workflow with reproducible raw snapshots.
- Limitation: source flexibility is manual and extraction quality depends on URL heuristics.

2. Data Preparation (`02_combine.py`): **4/5**
- Strength: deterministic merge and traceable source comments.
- Limitation: minimal structural validation during merge.

3. Data Parsing (`03_parse.py`): **3/5**
- Strength: NE-specific parsing now extracts large record volume.
- Limitation: description/url fidelity remains low; regex-centric parsing is brittle to markup changes.

4. Data Cleaning (`04_clean.py`): **4/5**
- Strength: normalization and deduplication are clear and consistent.
- Limitation: no advanced canonicalization for edge-case course code variants.

5. Data Extraction (`05_extract.py`): **4/5**
- Strength: title extraction is simple and reliable.
- Limitation: no reliability filtering for noisy/generated titles.

6. Word Frequency (`06_frequency.py`): **4/5**
- Strength: reproducible tokenization/counting pipeline.
- Limitation: domain-specific stopword tuning is limited (e.g., "hours", "elective").

7. Data Visualization (`07_visualization.py`): **2/5**
- Strength: output is generated consistently.
- Limitation: ASCII chart is low analytical/communication quality versus proper chart library output.

8. Export Clean Dataset (`08_export.py`): **3/5**
- Strength: export + schema doc delivered.
- Limitation: many records lack rich fields (`description`, `url`), reducing downstream value.

9. Data Pipeline (`09_pipeline.py`): **4/5**
- Strength: sequential orchestration, failure stop, restart point, and logs.
- Limitation: no retry policy or structured logging format.

10. Extract MIT 1996 (`10_extract_1996.py`): **2/5**
- Strength: automated fetch + PDF text extraction achieved at scale.
- Limitation: no OCR robustness and limited semantic parsing quality for scanned-source noise.

11. Extract MIT 2024 (`11_extract_2024.py`): **3/5**
- Strength: broad crawl and high record count.
- Limitation: description-level richness and deeper normalization are limited.

12. Course Offerings Over Time (`12_course_offerings.py`): **3/5**
- Strength: clear quantitative deltas by department.
- Limitation: explanatory reasoning is shallow and sensitive to code-system changes.

13. Title Evolution (`13_title_evolution.py`): **4/5**
- Strength: clear comparative term-delta outputs.
- Limitation: lexical noise control could be stronger.

14. New/Discontinued Subjects (`14_new_and_old.py`): **3/5**
- Strength: direct set-based comparison is clear and reproducible.
- Limitation: interpretation layer is minimal.

15. Curriculum Breadth (`15_curriculum_breadth.py`): **4/5**
- Strength: coherent breadth proxy (unique terms + entropy) with interpretable summary.
- Limitation: single-metric interpretation may oversimplify curriculum complexity.

16. Summary and Reflection (`16_summary_reflection.txt`): **4/5**
- Strength: concise synthesis with explicit quality caveat.
- Limitation: evidence linking to individual output files can be more explicit.

## Overall Evaluation (Quality-first)

- Total score: **55 / 80**
- Average score: **3.44 / 5.00**

Interpretation:
- The project is functionally complete and reproducible, with good engineering structure.
- Quality ceiling is constrained by extraction depth (especially 1996 OCR/semantic parsing) and visualization richness.
- Highest-impact improvements: **10, 7, 3, 8, 11**.
