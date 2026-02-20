# Project Plan (1-Round)

## Goal
- Improve work quality and requirement coverage through role-based collaboration in a single round.

## Fixed Round Flow (Single Round)
1. Planner writes Plan A
2. Planner writes Plan B (same persona, second pass)
3. Reviewer (Plan) merges A/B into one final execution plan
4. Builder implements based on the final plan
5. Grader scores using only the statement criteria
6. Reviewer (Improvement) proposes improvements based on grading results
7. End

## Operating Rules
- Run only one round.
- Start another round only when explicitly instructed by the user.
- Grader must not evaluate based on personal preference or style taste outside the statement.
- Reviewer feedback must be actionable and specific.
- Before executing any plan item, run a mandatory goal-alignment check: if the work does not directly support the statement goal or grading criteria, do not execute it.
- Enforce strict scope control: avoid side tasks, unrelated refactors, and non-required enhancements.
- Run a grading-risk check before completion: verify evidence, output integrity, and reproducibility to prevent point deductions.
- Mark tasks complete only when Definition of Done is objectively met; otherwise mark as partial with explicit remaining gaps.
- Run a pre-submit sanity check against statement requirements, rubric constraints, and required output format.
- Never create a git commit without explicit user approval in the current conversation.

## Deliverable Format
- Planner: task checklist, priorities, and Definition of Done (DoD)
- Reviewer (Plan): one merged execution plan
- Builder: code/document changes
- Grader: itemized scorecard + missing items
- Reviewer (Improvement): prioritized improvement action list
