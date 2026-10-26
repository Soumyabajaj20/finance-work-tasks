# Research project with Prof. Pengtao Xie
building a realistic finance-analyst work tasks and post-training a small open model on them.

**Research question:** Can a small open model learn real financial-analyst work from automatically
built, verified finance tasks, and does using the task rubrics as a reward beat plain SFT?

**Final goal:** a research paper with Prof. Xie, written by 27 Dec 2026, showing whether a small open
model can learn real financial-analyst work from automatically built, verified finance tasks, and
whether using the task rubrics as a reward beats plain SFT. A rebuilt, reusable finance task pipeline
is a second contribution. The paper's main claim (dataset, rubric-reward training, or both) is still
to be settled with Prof. Xie.

## Layout
- `tasks/<task>/anchor/` real public file (SEC EDGAR 10-K, earnings release, FRED data)
- `tasks/<task>/companions/` synthetic gap-filling files (manager notes, consensus sheet)
- `tasks/<task>/request.md` the manager-style request
- `tasks/<task>/rubric.json` 20-40 weighted, checkable items (weights sum to 100)
- `tasks/<task>/reference/` checked solution + `verification.md` log
- `eval/` `run_models.py`, `judge.py`, `results/`

## Rules
1. Training tasks never overlap the GDPval finance gold tasks (held out for final evaluation only).
2. Every failed rubric item is labelled agent / task / rubric fault in `verification.md`; task and
   rubric faults are fixed, up to 3 rounds.
3. No API keys in the repo. Use environment variables (see `eval/`).
