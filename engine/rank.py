#!/usr/bin/env python3
"""Rank a researched universe by independent base-case or named-analyst upside."""
import argparse
import json
from collections import Counter
from datetime import date
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

from consensus import amount, analyze, timestamp


def compare(batch, order="base", limit=None, minimum_base=None):
    if not batch["universe"].strip():
        raise ValueError("name the market, watchlist or researched subset")
    report_day = date.fromisoformat(batch["date"])
    counts = Counter(dict(checked=0, eligible=0, excluded=0, unverified=0, valued=0,
                          with_named_targets=0, matched=0))
    rows, omitted, seen = [], [], set()
    for case in batch["companies"]:
        issuer = case["issuer_id"].strip()
        if not issuer or issuer in seen:
            raise ValueError("select one listing per issuer and give it a unique issuer_id")
        seen.add(issuer)
        result = analyze(case)
        state = result["eligibility"]
        counts["checked"] += 1
        counts[state] += 1
        symbol = result["symbol"]
        close_day = timestamp(result["as_of"]).astimezone(ZoneInfo(case["exchange_tz"])).date()
        if close_day > report_day:
            raise ValueError(f"future close relative to screen date: {symbol}")
        if state != "eligible":
            omitted.append(dict(symbol=symbol, reason=state))
            continue
        if result["horizon_months"] != batch.get("horizon_months", 12):
            raise ValueError("rank comparable valuation horizons")
        targets = result["targets"]
        analyst = targets["upside_pct"]
        counts["with_named_targets"] += int(analyst is not None)
        valuation = case.get("valuation")
        scenarios = {}
        base_exact = None
        close = amount(case["close"], "close")
        if valuation is not None:
            targets_by_case = [amount(valuation[k], k) for k in ("bear", "base", "bull")]
            if targets_by_case != sorted(targets_by_case):
                raise ValueError(f"inspect reversed scenario targets for {symbol}")
            for k, target in zip(("bear", "base", "bull"), targets_by_case):
                scenarios[k] = float(100 * (target - close) / close)
            base_exact = 100 * (targets_by_case[1] - close) / close
            counts["valued"] += 1
        base = scenarios.get("base")
        if order == "base" and base is None:
            reason = "independent valuation unavailable"
        elif order == "analyst" and analyst is None:
            reason = "named-analyst targets unavailable"
        elif minimum_base is not None and (base_exact is None or base_exact < Decimal(str(minimum_base))):
            reason = "base return filter not met or unavailable"
        else:
            reason = None
        if reason:
            omitted.append(dict(symbol=symbol, reason=reason))
            continue
        total_base = None
        if base is not None and case.get("dividend_per_share") is not None:
            dividends = float(amount(case["dividend_per_share"], "expected dividends"))
            total_base = base + 100 * dividends / result["close"]
        rows.append(dict(symbol=symbol, issuer_id=issuer, close=result["close"], close_date=str(close_day),
                         currency=result["currency"], market_cap_usd=result["market_cap_usd"],
                         scenarios_pct=scenarios, base_total_return_pct=total_base,
                         analyst_upside_pct=analyst, target_count=targets["count"], coverage=result["coverage"],
                         analyst_minus_base_pp=analyst-base if base is not None and analyst is not None else None))
    metric = (lambda r: r["scenarios_pct"]["base"]) if order == "base" else (lambda r: r["analyst_upside_pct"])
    rows.sort(key=lambda r: (-metric(r), r["symbol"]))
    counts["matched"] = len(rows)
    return dict(universe=batch["universe"], date=batch["date"], order=order, counts=counts,
                ranked=rows[:limit], omitted=omitted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("universe", type=Path)
    parser.add_argument("--order", choices=["base", "analyst"], default="base")
    parser.add_argument("--min-base-pct", type=Decimal)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    try:
        data = json.loads(args.universe.read_text(), parse_float=str)
        print(json.dumps(compare(data, args.order, args.limit, args.min_base_pct), indent=2, allow_nan=False))
    except (ValueError, TypeError, KeyError, OSError, OverflowError) as exc:
        parser.exit(2, f"Cannot rank universe: {exc}\n")
