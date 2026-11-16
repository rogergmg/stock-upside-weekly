# Weekly routine (runs Saturdays 10:00 America/New_York)

Artifact URL: https://claude.ai/artifact/BVzpV1DvRwdpRDqhhVa8wW

Steps, run from the repo root. Stop and report if a step fails; never publish a partial page over a good one.

1. Install: `python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt`
2. Universe: `cd pipeline && ../.venv/bin/python -W ignore universe.py`
3. Mechanical tier: `../.venv/bin/python -W ignore refresh.py`. It prints counts; if failures exceed 10% of listings, stop.
4. Pick the batch: `../.venv/bin/python rotate.py -n 15`. This writes `data/batch.json`.
5. Deep research: for each entry in `data/batch.json`, launch a subagent (Agent tool, `model: "sonnet"`, up to 5 at a time). Give it this prompt, filled in:
   > Work in the repo root. Read RESEARCH.md and follow it exactly, along with skill_docs/SKILL.md and skill_docs/references/valuation.md and analysts.md. Your issuer: {name}, listing symbol {symbol}, currency {currency}, reference close {close} on {close_date} ({exchange_tz}). Today is {today}. Write {file} and nothing else. When finished, check it with: `cd pipeline && ../.venv/bin/python -c "import json,sys; sys.path.insert(0,'.'); from common import *; from snapshot import problems; a=read(latest(DATA/'aggregate')); row=[r for r in a['issuers'] if r['symbol']=='{symbol}'][0]; print(problems(json.load(open('../{file}')), row))"`. Fix the file until that prints [].
6. Validate and build: `../.venv/bin/python -W ignore validate.py && ../.venv/bin/python -W ignore build.py`
7. Commit and push: `git add -A && git commit -m "Weekly update <reference_session>" && git push`
8. Publish:
   - Read the artifact first (Artifact tool, `action: "read"`, the URL above).
   - Then publish `site/index.html` with `url` set to the URL above.
   - Don't pass `icon`.
9. Report: the reference session, the counts line from build.py, the names researched, and any rejected files from `data/validation.json`.
