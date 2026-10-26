# Weekly progress log: Week 1 (19 to 26 Oct 2026)

**Final goal:** a research paper (write-up due 27 Dec 2026) on whether a small open model can learn real financial-analyst work from automatically built, verified finance tasks, and whether rubric-as-reward training beats plain SFT.

## Done this week
- Read GDPval and WorkGenesis and fixed the task format: anchor file, companion files, manager-style request, weighted rubric, reference deliverable, verification log.
- Set up this private repository with the agreed layout.
- **Task 1, `dcf-valuation`:** DCF of Apple from its FY2025 10-K (EDGAR accession 0000320193-25-000079).
  - Request, 22-item rubric (weights sum to 100) and manager notes written.
  - Reference Excel model built with live formulas, WACC build and sensitivity table. It recalculates with no errors and gives $131.44 per share at a WACC of 9.0%.
- **Task 2, `earnings-variance`:** earnings variance memo on P&G's fiscal Q1 FY2027 release (8-K filed 22 Oct 2026).
  - Request, 21-item rubric, synthetic consensus sheet and a one-page reference memo written. All variances are computed in code from the release figures.
- Wrote the evaluation code in `eval/`: `run_models.py` (runs a model on a task) and `judge.py` (LLM judge that scores each rubric item). Tested end to end on a mock endpoint.

## Remaining in Phase 1 (due 3 Nov)
| Item | Status |
|---|---|
| Agent verification rounds (up to 3 per task), labelling each failed item as agent, task or rubric fault | Not started; needs a model |
| Baseline runs: Qwen3 (4B or 8B) and one strong model on both tasks | Waiting on GPU and LLM API access |
| Score the reference solutions with the judge to check the judge agrees with the rubric | Not started |
| Harness so models can produce real `.xlsx` and `.docx` outputs (the runner is text-only) | Not started |
| Trim the Apple 10-K to the financial statements so it fits a small model's context | Not started |
| Confirm neither company appears in the GDPval gold tasks (held out for final evaluation) | Not started |
| Phase 1 results table and short report to Prof. Xie | Due 3 Nov |

## Open items
- GPU and LLM API access details from Prof. Xie.
- Add Prof. Xie as a collaborator once his GitHub username is received.
- Main claim of the paper (finance dataset, rubric-reward training, or both) to settle with him.
- Authorship and target venue to ask about once Phase 1 results are in.
- Exams run 9 to 21 Nov, which is why Phase 2 is stretched to 30 Nov.
