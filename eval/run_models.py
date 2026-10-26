"""Run a model on each task and save its output text.
Both models are called through an OpenAI-compatible endpoint (vLLM for Qwen3, hosted API for the strong model).
Env: MODEL_BASE_URL, MODEL_API_KEY, MODEL_NAME.   Usage: python run_models.py --task dcf-valuation --tag qwen3-8b
NOTE: this sends request.md and text of companions only. File-producing tasks need an agent harness
(tool use for xlsx/docx); this skeleton gets a text-only baseline first.
"""
import argparse, os, pathlib, json
from openai import OpenAI

import html.parser, re

class _Text(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.out = []
    def handle_data(self, d): self.out.append(d)

def read_text(f: pathlib.Path, max_chars: int) -> str:
    raw = f.read_text(encoding="utf-8", errors="ignore")
    if f.suffix in {".htm", ".html"}:
        p = _Text(); p.feed(raw); raw = re.sub(r"\s+", " ", " ".join(p.out))
    if len(raw) > max_chars:
        print(f"WARNING: {f.name} truncated from {len(raw)} to {max_chars} chars")
        raw = raw[:max_chars]
    return raw

def load_context(task_dir: pathlib.Path, max_chars: int = 120000) -> str:
    parts = [(task_dir / "request.md").read_text(encoding="utf-8")]
    for sub in ("anchor", "companions"):
        for f in sorted((task_dir / sub).glob("*")):
            if f.suffix in {".md", ".txt", ".csv", ".htm", ".html"} and f.name != "SOURCE.md":
                parts.append(f"\n--- {sub}/{f.name} ---\n" + read_text(f, max_chars))
            elif f.suffix == ".xlsx":
                import openpyxl
                wb = openpyxl.load_workbook(f, data_only=True)
                rows = [" | ".join("" if c is None else str(c) for c in r) for ws in wb for r in ws.iter_rows(values_only=True)]
                parts.append(f"\n--- {sub}/{f.name} (as text) ---\n" + "\n".join(rows))
    return "\n".join(parts)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--task", required=True); ap.add_argument("--tag", required=True)
    a = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parent.parent
    task_dir = root / "tasks" / a.task
    client = OpenAI(base_url=os.environ["MODEL_BASE_URL"], api_key=os.environ["MODEL_API_KEY"])
    r = client.chat.completions.create(model=os.environ["MODEL_NAME"], temperature=0,
        messages=[{"role": "system", "content": "You are a financial analyst. Do the task fully."},
                  {"role": "user", "content": load_context(task_dir)}])
    out = root / "eval" / "results" / a.tag; out.mkdir(parents=True, exist_ok=True)
    (out / f"{a.task}.txt").write_text(r.choices[0].message.content, encoding="utf-8")
    print("saved", out / f"{a.task}.txt")

if __name__ == "__main__":
    main()
