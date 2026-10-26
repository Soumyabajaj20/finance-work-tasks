"""LLM judge: score one output item-by-item against rubric.json. Each item is judged independently (pass/fail),
score = sum of weights of passed items. Env: JUDGE_BASE_URL, JUDGE_API_KEY, JUDGE_MODEL.
Usage: python judge.py --task dcf-valuation --tag qwen3-8b
"""
import argparse, os, pathlib, json
from openai import OpenAI

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--task", required=True); ap.add_argument("--tag", required=True)
    a = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parent.parent
    rubric = json.loads((root / "tasks" / a.task / "rubric.json").read_text(encoding="utf-8"))
    request = (root / "tasks" / a.task / "request.md").read_text(encoding="utf-8")
    output = (root / "eval" / "results" / a.tag / f"{a.task}.txt").read_text(encoding="utf-8")
    client = OpenAI(base_url=os.environ["JUDGE_BASE_URL"], api_key=os.environ["JUDGE_API_KEY"])
    results, score = [], 0
    for it in rubric["items"]:
        prompt = (f"TASK REQUEST:\n{request}\n\nMODEL OUTPUT:\n{output}\n\nCRITERION: {it['criterion']}\n"
                  'Does the output satisfy this criterion? Reply JSON only: {"pass": true|false, "reason": "..."}')
        r = client.chat.completions.create(model=os.environ["JUDGE_MODEL"], temperature=0,
            messages=[{"role": "user", "content": prompt}], response_format={"type": "json_object"})
        v = json.loads(r.choices[0].message.content)
        score += it["weight"] if v.get("pass") else 0
        results.append({"id": it["id"], "weight": it["weight"], **v})
    out = root / "eval" / "results" / a.tag / f"{a.task}.score.json"
    out.write_text(json.dumps({"task": a.task, "tag": a.tag, "score": score, "items": results}, indent=2), encoding="utf-8")
    print(a.task, a.tag, "score", score, "/ 100")

if __name__ == "__main__":
    main()
