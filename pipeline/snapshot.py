"""Merge a weekly aggregate row with an issuer's research file into an engine snapshot."""
from datetime import datetime, time

from common import NY

REQUIRED = ("issuer_id", "symbol", "researched_at", "currency", "coverage", "events", "valuation", "sources")
CASE_KEYS = ("driver", "assumption", "target")


def as_of(row):
    day = datetime.fromisoformat(row["close_date"]).date()
    return datetime.combine(day, time(16, 0), NY).isoformat()


def engine_input(row, research=None):
    """Calculator snapshot (consensus.py format) on this week's close; research supplies events + valuation."""
    snap = dict(issuer_id=row["issuer_id"], symbol=row["symbol"], currency=row["currency"], close=row["close"],
                exchange_tz=row["exchange_tz"], as_of=as_of(row), market_cap_usd=row["market_cap_usd"],
                horizon_months=12, coverage="aggregate_only", events=[], earnings_at=None)
    if research:
        snap.update(coverage=research["coverage"], events=research["events"],
                    earnings_at=research.get("earnings_at"))
        v = research["valuation"]
        snap["valuation"] = {k: v[k] for k in ("bear", "base", "bull")}
        if research.get("dividend_per_share") is not None:
            snap["dividend_per_share"] = research["dividend_per_share"]
    return snap


def problems(research, row):
    """Return a list of reasons a research file can't be used (empty = ok)."""
    errs = [f"missing {k}" for k in REQUIRED if k not in research]
    if errs:
        return errs
    if research["symbol"] != row["symbol"]:
        errs.append(f"symbol {research['symbol']} != listing {row['symbol']}")
    if research["currency"] != row["currency"]:
        errs.append("valuation currency differs from listing currency")
    v = research["valuation"]
    try:
        trio = [float(v[k]) for k in ("bear", "base", "bull")]
        if trio != sorted(trio) or trio[0] <= 0:
            errs.append("scenario targets must be positive and ordered bear <= base <= bull")
    except (KeyError, TypeError, ValueError):
        errs.append("valuation needs numeric bear/base/bull")
    for k in ("bear", "base", "bull"):
        case = v.get("cases", {}).get(k, {})
        if not all(case.get(c) not in (None, "") for c in CASE_KEYS):
            errs.append(f"valuation.cases.{k} needs driver/assumption/target")
    if not v.get("method"):
        errs.append("valuation.method missing")
    if len([s for s in research["sources"] if str(s.get("url", "")).startswith("http")]) < 3:
        errs.append("need at least 3 linked sources")
    if research["coverage"] in ("aggregate_only", "unavailable") and research["events"]:
        errs.append("events conflict with coverage label")
    try:
        datetime.fromisoformat(research["researched_at"])
    except ValueError:
        errs.append("researched_at must be ISO date")
    if not errs:
        import consensus
        try:
            consensus.analyze(engine_input(row, research))
        except (ValueError, TypeError, KeyError, OverflowError) as exc:
            errs.append(f"engine rejected events: {exc}")
    return errs
