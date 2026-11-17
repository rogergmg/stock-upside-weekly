#!/usr/bin/env python3
"""Week-over-week changes: compare this week's snapshot with the previous one in data/weekly/."""
from datetime import date, timedelta

from common import DATA, read

STREET_TARGET_MOVE = 2.0   # % change in the provider's mean target worth reporting
BASE_MOVE_PP = 0.05        # base-case moves smaller than this are noise from rounding


def previous_snapshot(ref):
    files = sorted(p for p in (DATA / "weekly").glob("????-??-??.json") if p.stem < ref)
    return read(files[-1]) if files else None


def _base(rows):
    return {r["symbol"]: r for r in rows}


def analyst_calls(details, since, until):
    """Named-analyst actions issued in (since, until], one row per analyst per day (rating and target merged)."""
    calls = {}
    for sym, d in details.items():
        for e in d.get("history") or []:
            day = (e.get("issued_at") or "")[:10]
            if not (since < day <= until):
                continue
            k = (sym, e.get("firm"), e.get("analyst"), day)
            c = calls.setdefault(k, dict(symbol=sym, firm=e.get("firm"), analyst=e.get("analyst"), issued_at=day,
                                         source=e.get("source"), currency=None))
            if e["field"] == "rating":
                c.update(rating=e.get("value"), bucket=e.get("bucket"), prior_rating=e.get("prior_observed"))
            else:
                c.update(target=e.get("value"), prior_target=e.get("prior_observed") or e.get("source_prior"),
                         direction=e.get("direction"), revision_pct=e.get("revision_pct"),
                         horizon_months=e.get("horizon_months"))
    return sorted(calls.values(), key=lambda c: (c["issued_at"], c["symbol"]), reverse=True)


def compute(snap, prev):
    ref = snap["reference_session"]
    since = prev["reference_session"] if prev else (date.fromisoformat(ref) - timedelta(days=7)).isoformat()
    out = dict(previous_session=prev["reference_session"] if prev else None, window_start=since)

    pdet = prev["details"] if prev else {}
    out["research"] = sorted(
        [dict(symbol=s, researched_at=d["researched_at"], kind="refreshed" if s in pdet else "new")
         for s, d in snap["details"].items()
         if s not in pdet or d["researched_at"] != pdet[s]["researched_at"]],
        key=lambda r: r["symbol"])
    out["analyst_calls"] = analyst_calls(snap["details"], since, ref)

    if not prev:
        out.update(base_moves=None, street_moves=None, crossings=None)
        return out

    now, before = _base(snap["ranked"]), _base(prev["ranked"])
    moves = []
    for s, r in now.items():
        if s not in before:
            continue
        a, b = r["scenarios_pct"]["base"], before[s]["scenarios_pct"]["base"]
        if abs(a - b) < BASE_MOVE_PP:
            continue
        re = pdet.get(s, {}).get("researched_at") != snap["details"].get(s, {}).get("researched_at")
        pc, cc = before[s]["close"], r["close"]
        moves.append(dict(symbol=s, base=a, prev_base=b, delta_pp=a - b, re_researched=re,
                          price_change_pct=(cc / pc - 1) * 100 if pc else None))
    out["base_moves"] = sorted(moves, key=lambda m: -abs(m["delta_pp"]))

    pi, ni = _base(prev["issuers"]), _base(snap["issuers"])
    street = []
    for s, r in ni.items():
        o = pi.get(s)
        if not o or r["status"] != "eligible":
            continue
        a, b = r.get("aggregate") or {}, o.get("aggregate") or {}
        tchg = (a["mean"] / b["mean"] - 1) * 100 if a.get("mean") and b.get("mean") else None
        rec = a.get("recommendation") != b.get("recommendation") and a.get("recommendation") and b.get("recommendation")
        if (tchg is not None and abs(tchg) >= STREET_TARGET_MOVE) or rec:
            street.append(dict(symbol=s, mean=a.get("mean"), prev_mean=b.get("mean"), target_change_pct=tchg,
                               recommendation=a.get("recommendation"), prev_recommendation=b.get("recommendation"),
                               upside=a.get("upside_pct"), prev_upside=b.get("upside_pct"), currency=r.get("currency")))
    out["street_moves"] = sorted(street, key=lambda m: -abs(m["target_change_pct"] or 0))

    cross = []
    for s in sorted(set(pi) | set(ni)):
        a, b = (ni.get(s) or {}).get("status"), (pi.get(s) or {}).get("status")
        if a != b and "eligible" in (a, b):
            row = ni.get(s) or pi.get(s)
            cross.append(dict(symbol=s, name=row.get("name"), status=a or "dropped", prev_status=b or "new listing",
                              market_cap_usd=row.get("market_cap_usd")))
    out["crossings"] = cross
    return out
