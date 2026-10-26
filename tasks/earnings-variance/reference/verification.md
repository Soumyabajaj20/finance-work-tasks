# Verification log: earnings-variance

Process: run the strong model on the task, grade with `eval/judge.py`, then for **every failed rubric item**
label the cause. Fix task and rubric faults, re-run, up to 3 rounds.

| Round | Item ID | Result | Fault type (agent / task / rubric) | Evidence | Fix applied |
|---|---|---|---|---|---|
| 0 | n/a | reference self-check | n/a | Every variance in the reference memo computed in code from release figures and asserted; memo renders to exactly 1 page | none needed |
| 1 | | | | | |

Fault types:
- **agent**: model genuinely did the work wrong. Leave as is.
- **task**: request is ambiguous or the files lack needed information. Edit request/companions.
- **rubric**: item is unverifiable, wrong, or contradicts the reference. Edit rubric.

Sign-off: [ ] reference deliverable checked by hand   [ ] all task/rubric faults resolved   [ ] no overlap with GDPval gold tasks
