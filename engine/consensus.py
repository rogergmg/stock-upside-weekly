#!/usr/bin/env python3
"""Reconstruct a stock's as-of analyst coverage from field-level public events."""
import argparse
import calendar
import json
import math
import statistics
from collections import Counter
from datetime import date, datetime, time
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

CUTOFF = Decimal("20000000000")
BUCKETS = ("Buy", "Hold", "Sell")


def amount(value, label):
    try:
        number = Decimal(str(value))
    except InvalidOperation:
        raise ValueError(f"{label} must be a number") from None
    if not number.is_finite() or number < 0:
        raise ValueError(f"{label} must be finite and nonnegative")
    return number


def eligibility(cap):
    if cap is None:
        return "unverified"
    if not isinstance(cap, dict) or set(cap) != {"low", "high"}:
        raise ValueError("market_cap_usd needs low and high bounds")
    low = amount(cap["low"], "low cap")
    high = amount(cap["high"], "high cap")
    if high < low:
        raise ValueError("cap bounds are reversed")
    if low > CUTOFF:
        return "eligible"
    return "excluded" if high <= CUTOFF else "unverified"


def timestamp(text):
    value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    if value.utcoffset() is None:
        raise ValueError("time must include a UTC offset")
    return value


def anniversary(day, months):
    year, month = divmod(day.year * 12 + day.month - 1 + months, 12)
    month += 1
    return date(year, month, min(day.day, calendar.monthrange(year, month)[1]))


def event_rows(data, cutoff, zone):
    """Sort by actual issue time after screening for first public availability."""
    seen = {}
    fields = {}
    for event in data["events"]:
        raw_date = event["issued_at"]
        if len(raw_date) == 10:
            issued = datetime.combine(date.fromisoformat(raw_date), time.min, zone)
        else:
            issued = timestamp(raw_date)
        available = timestamp(event["public_at"])
        if available < issued:
            raise ValueError("public_at precedes issued_at")
        if available > cutoff:
            continue
        identity = event["analyst"].strip()
        field = event["field"]
        if field not in ("rating", "target") or not identity or not event["firm"].strip():
            raise ValueError("each event needs a named analyst, firm and rating/target field")
        if not event["source"].strip():
            raise ValueError("missing event source")
        key = (identity, field, issued)
        value = event["value"]
        bucket = event.get("bucket")
        horizon = event.get("horizon_months")
        if field == "target" and value is not None:
            value = float(amount(value, "target"))
            if horizon is not None and (type(horizon) is not int or horizon <= 0):
                raise ValueError("invalid target horizon")
        if field == "rating" and value is not None:
            if not isinstance(value, str) or not value.strip() or bucket not in (*BUCKETS, None):
                raise ValueError("invalid rating label or normalized rating bucket")
        expiry = event.get("expires_on")
        if expiry and date.fromisoformat(expiry) < issued.astimezone(zone).date():
            raise ValueError("expiry precedes issue date")
        signature = (event["firm"], value, bucket, horizon, expiry)
        if key in seen:
            if seen[key] != signature:
                raise ValueError(f"conflicting same-time {field} for {identity}: reconcile source records")
            continue
        seen[key] = signature
        row = dict(event, value=value)
        fields.setdefault((identity, field), []).append((issued, row))
    for history in fields.values():
        history.sort(key=lambda item: item[0])
        for (before, prev), (after, curr) in zip(history, history[1:]):
            if before.astimezone(zone).date() == after.astimezone(zone).date():
                if len(prev["issued_at"]) == 10 or len(curr["issued_at"]) == 10:
                    raise ValueError("same-day events with unknown order: reconcile records")
    return fields


def expiration(day, event):
    months = event.get("horizon_months") if event["field"] == "target" else 12
    derived = anniversary(day, months) if months else None
    if not event.get("expires_on"):
        return derived
    explicit = date.fromisoformat(event["expires_on"])
    return min(derived, explicit) if event["field"] == "rating" else explicit


def reconstruct(data, cutoff, zone, horizon):
    today = cutoff.astimezone(zone).date()
    earnings = timestamp(data["earnings_at"]) if data.get("earnings_at") else None
    if earnings and earnings > cutoff:
        raise ValueError("earnings_at must be the last public release by the cutoff")
    active = {"rating": [], "target": []}
    history = []
    for (analyst, field), entries in sorted(event_rows(data, cutoff, zone).items()):
        prior = None
        previous_firm, previous_expiry, previous_horizon = None, None, None
        for issued, event in entries:
            value = event["value"]
            issue_day = issued.astimezone(zone).date()
            same_basis = event.get("horizon_months") == previous_horizon
            continuous = event["firm"] == previous_firm and same_basis
            if previous_expiry is not None and issue_day >= previous_expiry:
                continuous = False
            observed = prior if continuous else None
            row = dict(event, prior_observed=observed)
            baseline = event.get("source_prior")
            if baseline is None:
                baseline = observed
            if field == "target" and value is not None and baseline is not None:
                baseline = float(amount(baseline, "prior target"))
                if baseline > 0:
                    row["revision_pct"] = 100 * (value / baseline - 1)
                row["direction"] = "raise" if value > baseline else "cut" if value < baseline else "unchanged"
            history.append(row)
            prior = value
            previous_firm = event["firm"]
            previous_horizon = event.get("horizon_months")
            previous_expiry = expiration(issue_day, event)
        day = issued.astimezone(zone).date()
        age = (today - day).days
        reason = None
        if value is None:
            reason = "withdrawn"
        elif field == "rating" and not event.get("bucket"):
            reason = "unmapped rating"
        elif field == "target" and event.get("horizon_months") != horizon:
            reason = "unknown or different horizon"
        else:
            if today >= expiration(day, event):
                reason = "expired or outside rating window"
        row["status_at_cutoff"] = reason or "active"
        if reason is None:
            after_release = None
            if earnings:
                release_day = earnings.astimezone(zone).date()
                if len(event["issued_at"]) != 10 or day != release_day:
                    after_release = issued > earnings
            active[field].append(dict(analyst=analyst, firm=event["firm"], value=value,
                                      bucket=event.get("bucket"), issued_at=event["issued_at"],
                                      age_days=age, after_earnings=after_release,
                                      source=event["source"]))
    return active, history


def weighted(rows, half_life):
    if not rows:
        return []
    # Removing a common age offset leaves normalized shares unchanged.
    youngest = min(r["age_days"] for r in rows)
    weights = [1.0 if half_life is None else 2 ** (-(r["age_days"] - youngest) / half_life)
               for r in rows]
    total = math.fsum(weights)
    return [dict(r, weight=w / total) for r, w in zip(rows, weights)]


def coverage(rows, earnings_known):
    return {"count": len(rows), "post_earnings": sum(r["after_earnings"] is True for r in rows) if earnings_known else None,
            "earnings_order_unknown": sum(r["after_earnings"] is None for r in rows) if earnings_known else None,
            "median_age_days": statistics.median(r["age_days"] for r in rows) if rows else None,
            "max_weight_pct": 100 * max((r["weight"] for r in rows), default=0) if rows else None,
            "contributors": rows}


def target_summary(rows, close, half_life):
    updated = weighted(rows, half_life)
    if not updated:
        return {"target": None, "upside_pct": None}
    target = math.fsum(r["value"] * r["weight"] for r in updated)
    return {"target": target, "upside_pct": 100 * (target / close - 1)}


def analyze(data, half_life=90):
    if not math.isfinite(half_life) or half_life <= 0:
        raise ValueError("half-life must be positive and finite")
    cutoff = timestamp(data["as_of"])
    result = {k: data[k] for k in ("symbol", "as_of", "market_cap_usd")}
    result["eligibility"] = eligibility(data["market_cap_usd"])
    if result["eligibility"] != "eligible":
        return result
    zone = ZoneInfo(data["exchange_tz"])
    close = float(amount(data["close"], "close"))
    horizon = data.get("horizon_months", 12)
    if not close or type(horizon) is not int or horizon < 1:
        raise ValueError("close and horizon must be positive")
    if data["coverage"] not in ("complete", "partial", "aggregate_only", "unavailable"):
        raise ValueError("identify the observed coverage")
    if data["coverage"] in ("aggregate_only", "unavailable") and data["events"]:
        raise ValueError("named event rows conflict with the coverage label")
    active, history = reconstruct(data, cutoff, zone, horizon)
    ratings = weighted(active["rating"], half_life)
    targets = weighted(active["target"], half_life)
    earnings_known = bool(data.get("earnings_at"))
    rating = coverage(ratings, earnings_known)
    counts = Counter(r["bucket"] for r in ratings)
    rating["counts"] = {b: counts[b] for b in BUCKETS}
    rating["weighted_pct"] = {b: 100 * math.fsum(r["weight"] for r in ratings if r["bucket"] == b)
                              for b in BUCKETS} if ratings else None
    target = coverage(targets, earnings_known)
    target.update(target_summary(targets, close, half_life))
    values = [r["value"] for r in targets]
    target["range"] = [min(values), max(values)] if values else None
    target["median"] = statistics.median(values) if values else None
    sensitivity = {str(h): target_summary(targets, close, h) for h in (45, 90, 180)}
    sensitivity["equal"] = target_summary(targets, close, None)
    result.update(close=close, currency=data["currency"], coverage=data["coverage"],
                  horizon_months=horizon, half_life_days=half_life, ratings=rating, targets=target,
                  sensitivity=sensitivity, history=history)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--half-life", type=float, default=90)
    args = parser.parse_args()
    try:
        data = json.loads(args.snapshot.read_text(), parse_float=Decimal)
        result = analyze(data, args.half_life)
        print(json.dumps(result, indent=2, allow_nan=False, default=str))
    except (ValueError, TypeError, KeyError, OSError, OverflowError) as exc:
        parser.exit(2, f"Cannot calculate consensus: {exc}\n")


if __name__ == "__main__":
    main()
