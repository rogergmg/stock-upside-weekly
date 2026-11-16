#!/usr/bin/env python3
"""Score matched 12-month historical forecasts against realized price-only returns."""
import argparse
import json
import statistics
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from consensus import amount, analyze, anniversary, timestamp


def evaluate(cases):
    methods = ("equal", "45", "90", "180")
    observations, skipped = [], []
    seen = set()
    for case in cases:
        snap = case["snapshot"]
        result = analyze(snap)
        day = timestamp(snap["as_of"]).astimezone(ZoneInfo(snap["exchange_tz"])).date()
        key = (snap["symbol"], day)
        if key in seen:
            raise ValueError(f"duplicate company/listing date: {key}")
        seen.add(key)
        label = {"symbol": key[0], "date": str(day)}
        reason = None
        if result["eligibility"] != "eligible":
            reason = result["eligibility"]
        elif result["horizon_months"] != 12:
            raise ValueError("evaluation expects 12-month snapshots")
        elif not result["targets"]["count"]:
            reason = "no comparable active target"
        elif case.get("outcome") is None:
            reason = "outcome unavailable"
        if reason:
            skipped.append(dict(label, reason=reason))
            continue
        outcome = case["outcome"]
        end_day = date.fromisoformat(outcome["date"])
        due = anniversary(day, 12)
        if not due <= end_day <= due + timedelta(days=7):
            raise ValueError(f"check target anniversary/trading calendar for {key}")
        if not outcome["source"].strip():
            raise ValueError("missing outcome source")
        end_value = float(amount(outcome["value_per_original_share"], "terminal value"))
        actual = 100 * (end_value / result["close"] - 1)
        predictions = {m: result["sensitivity"][m]["upside_pct"] for m in methods}
        observations.append(dict(label, targets=result["targets"]["count"], actual_pct=actual,
                                 forecast_pct=predictions,
                                 error_pp={m: predictions[m] - actual for m in methods}))
    scores = {}
    if observations:
        for method in methods:
            errors = [obs["error_pp"][method] for obs in observations]
            scores[method] = {"mean_absolute_error_pp": statistics.mean(map(abs, errors)),
                              "median_absolute_error_pp": statistics.median(map(abs, errors)),
                              "mean_signed_error_pp": statistics.mean(errors)}
    return dict(count=len(observations), skipped=skipped, scores=scores, observations=observations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(evaluate(json.loads(args.cases.read_text(), parse_float=str)), indent=2, allow_nan=False))
    except (ValueError, TypeError, KeyError, OSError, OverflowError) as exc:
        parser.exit(2, f"Cannot score observations: {exc}\n")
