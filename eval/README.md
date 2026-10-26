# Running the evaluation

1. `pip install -r requirements.txt`
2. Serve the small model on a GPU with an OpenAI-compatible endpoint (vLLM):
   `vllm serve Qwen/Qwen3-8B --port 8000`
   then `export MODEL_BASE_URL=http://localhost:8000/v1 MODEL_API_KEY=none MODEL_NAME=Qwen/Qwen3-8B`
3. For the strong model and the judge, set `MODEL_*` / `JUDGE_*` to the provided API (never commit keys).
4. `python run_models.py --task dcf-valuation --tag qwen3-8b`
   `python judge.py --task dcf-valuation --tag qwen3-8b`
5. Scores land in `results/<tag>/<task>.score.json` (0-100).

Tested locally against a mock OpenAI-compatible server (pipeline only; the mock always passes every item).
Known gap: text-only. Producing .xlsx/.docx needs an agent harness with file tools.
