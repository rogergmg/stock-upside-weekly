#!/usr/bin/env python3
"""Pick this week's deep-research batch: never researched first (largest cap first), then stalest research."""
import argparse
import json

from common import DATA, RESEARCH, latest, read, write


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-n", type=int, default=15)
    args = ap.parse_args()
    agg = read(latest(DATA / "aggregate"))
    done = {}
    for p in RESEARCH.glob("*.json"):
        try:
            r = json.loads(p.read_text())
            done[r["symbol"]] = r["researched_at"]
        except (ValueError, KeyError):
            pass
    eligible = [r for r in agg["issuers"] if r["status"] == "eligible"]

    def key(r):
        move = abs(r["close"] / r["week_ago_close"] - 1) if r.get("week_ago_close") else 0
        seen = done.get(r["symbol"])
        return (seen is not None, seen or "", -r["market_cap_usd"]["low"] if seen is None else -move)

    batch = [dict(symbol=r["symbol"], yf_symbol=r["yf_symbol"], issuer_id=r["issuer_id"], name=r["name"],
                  currency=r["currency"], financial_currency=r["financial_currency"], close=r["close"],
                  close_date=r["close_date"], exchange_tz=r["exchange_tz"], sector=r["sector"],
                  last_researched=done.get(r["symbol"]),
                  file=f"research/{r['symbol'].replace('/', '-')}.json")
             for r in sorted(eligible, key=key)[:args.n]]
    write(DATA / "batch.json", dict(reference_session=agg["reference_session"], batch=batch))
    for b in batch:
        print(b["symbol"], b["last_researched"] or "new")


if __name__ == "__main__":
    main()
