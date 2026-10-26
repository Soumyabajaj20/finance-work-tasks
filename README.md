# finance-work-tasks

Research project with Prof. Pengtao Xie (UCSD): building realistic finance-analyst work tasks
(GDPval / WorkGenesis direction) and post-training a small open model on them.

**Research question:** Can a small open model learn real financial-analyst work from automatically
built, verified finance tasks, and does using the task rubrics as a reward beat plain SFT?

## Layout
- `tasks/<task>/anchor/` real public file (SEC EDGAR 10-K, earnings release, FRED data)
- `tasks/<task>/companions/` synthetic gap-filling files (manager notes, consensus sheet)
- `tasks/<task>/request.md` the manager-style request
- `tasks/<task>/rubric.json` 20-40 weighted, checkable items (weights sum to 100)
- `tasks/<task>/reference/` checked solution + `verification.md` log
- `eval/` `run_models.py`, `judge.py`, `results/`
- `docs/weekly-updates/` Monday emails

## Rules
1. Training tasks never overlap the GDPval finance gold tasks (held out for final evaluation only).
2. Every failed rubric item is labelled agent / task / rubric fault in `verification.md`; task and
   rubric faults are fixed, up to 3 rounds.
3. No API keys in the repo. Use environment variables (see `eval/`).

## Status
| Phase | Due | State |
|---|---|---|
| 1 | 3 Nov | both tasks built with reference solutions (DCF: Apple FY2025 10-K; memo: P&G FQ1 FY27). Pending: download anchor files, agent verification rounds, baseline runs once GPU/API access is given (Prof. Xie, 23 Oct) |
| 2 | 30 Nov | not started |
| 3 | 13 Dec | not started |
| 4 | 27 Dec | not started |
