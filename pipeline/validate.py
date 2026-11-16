#!/usr/bin/env python3
"""Check every research file against this week's listing data; move unusable files to research/rejected/."""
import json
import shutil
import sys

from common import DATA, RESEARCH, latest, read, write
from snapshot import problems


def main():
    agg = read(latest(DATA / "aggregate"))
    rows = {r["symbol"]: r for r in agg["issuers"]}
    log, bad = [], 0
    for path in sorted(RESEARCH.glob("*.json")):
        try:
            research = json.loads(path.read_text())
            row = rows.get(research.get("symbol"))
            errs = problems(research, row) if row else ["listing not in this week's universe"]
        except json.JSONDecodeError as exc:
            errs = [f"invalid JSON: {exc}"]
        if errs:
            bad += 1
            dest = RESEARCH / "rejected" / path.name
            dest.parent.mkdir(exist_ok=True)
            shutil.move(str(path), dest)
            log.append(dict(file=path.name, errors=errs))
            print(f"REJECTED {path.name}: {'; '.join(errs)}", file=sys.stderr)
    write(DATA / "validation.json", dict(reference_session=agg["reference_session"], rejected=log))
    print(f"validated research; {bad} rejected")


if __name__ == "__main__":
    main()
