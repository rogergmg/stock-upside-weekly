#!/usr/bin/env python3
"""Rank researched names with the skill engine, merge the aggregate tier, write the weekly snapshot and page."""
import json
from datetime import datetime, timezone

from common import DATA, RESEARCH, SITE, UNIVERSE_NAME, latest, read, write  # sets engine path
import consensus
import rank
from snapshot import engine_input, problems, split_adjust
import changes


def main():
    agg = read(latest(DATA / "aggregate"))
    ref = agg["reference_session"]
    research = {}
    for p in RESEARCH.glob("*.json"):
        r = json.loads(p.read_text())
        research[r["symbol"]] = r

    eligible = [r for r in agg["issuers"] if r["status"] == "eligible"]
    companies, details, skipped = [], {}, []
    for row in eligible:
        res = research.get(row["symbol"])
        if res and problems(res, row):
            skipped.append(row["symbol"])
            res = None
        snap = engine_input(row, res)
        companies.append(snap)
        if res:
            out = consensus.analyze(snap)
            res = split_adjust(res, row)
            details[row["symbol"]] = dict(
                researched_at=res["researched_at"], research_close=res.get("research_close"),
                valuation=res["valuation"], dividend_per_share=res.get("dividend_per_share"),
                analyst_notes=res.get("analyst_notes"), sources=res["sources"], coverage=res["coverage"],
                earnings_at=res.get("earnings_at"), split_adjusted=res.get("split_adjusted"), ratings=out["ratings"], targets=out["targets"],
                sensitivity=out["sensitivity"], history=out["history"])

    batch = dict(universe=UNIVERSE_NAME, date=ref, horizon_months=12, companies=companies)
    write(DATA / "weekly" / f"{ref}.input.json", batch)
    ranked = rank.compare(json.loads(json.dumps(batch), parse_float=str), order="base")

    def brief(r):
        return {k: r.get(k) for k in ("symbol", "issuer_id", "name", "sector", "industry", "country", "currency",
                                       "close", "close_date", "market_cap_usd", "status", "aggregate",
                                       "other_classes", "financial_currency", "last_split")}

    counts = dict(agg["counts"], **{f"rank_{k}": v for k, v in ranked["counts"].items()},
                  researched=len(details))
    snapshot = dict(
        universe=UNIVERSE_NAME, reference_session=ref, cutoff_usd=agg["cutoff_usd"],
        built_at=datetime.now(timezone.utc).isoformat(), fetched_at=agg["fetched_at"],
        universe_source=agg["universe_source"], counts=counts,
        ranked=ranked["ranked"], omitted=ranked["omitted"],
        issuers=[brief(r) for r in agg["issuers"]], details=details,
        failures=agg["failures"], rejected=read(DATA / "validation.json")["rejected"]
        if (DATA / "validation.json").exists() else [])
    snapshot["changes"] = changes.compute(snapshot, changes.previous_snapshot(ref))
    write(DATA / "weekly" / f"{ref}.json", snapshot)

    template = (SITE / "template.html").read_text()
    payload = json.dumps(snapshot, allow_nan=False, default=str, separators=(",", ":")).replace("</", "<\\/")
    (SITE / "index.html").write_text(template.replace("__DATA__", payload))
    print(f"{ref}: {counts['eligible']} eligible, {len(details)} researched, {len(ranked['ranked'])} ranked "
          f"-> site/index.html ({(SITE / 'index.html').stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
