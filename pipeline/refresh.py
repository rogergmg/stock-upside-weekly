#!/usr/bin/env python3
"""Weekly mechanical tier: reference close, USD cap bounds, eligibility and provider aggregate target."""
import argparse
import time as _time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone

import yfinance as yf

from common import CAP_BAND, DATA, NY, USER_CUTOFF_USD, read, reference_session, write

INFO_KEYS = ("longName", "currency", "financialCurrency", "sharesOutstanding", "impliedSharesOutstanding",
             "marketCap", "targetMeanPrice", "targetMedianPrice", "targetHighPrice", "targetLowPrice",
             "numberOfAnalystOpinions", "recommendationKey", "recommendationMean", "sector", "industry",
             "averageVolume", "quoteType", "exchange", "exchangeTimezoneName", "dividendRate",
             "earningsTimestamp", "website", "lastSplitFactor", "lastSplitDate")


def info(symbol):
    for attempt in range(3):
        try:
            data = yf.Ticker(symbol).info or {}
            if data.get("quoteType"):
                return {k: data.get(k) for k in INFO_KEYS}
        except Exception:  # network / rate limit
            pass
        _time.sleep(2 * (attempt + 1))
    return None


def closes(symbols, ref_day):
    hist = yf.download(symbols, period="1mo", interval="1d", auto_adjust=False, actions=False,
                       group_by="ticker", progress=False, threads=True)
    out = {}
    for s in symbols:
        try:
            series = hist[s]["Close"].dropna()
        except KeyError:
            continue
        series = series[[d.date() <= ref_day for d in series.index]]
        if len(series):
            prev = float(series.iloc[-6]) if len(series) >= 6 else None
            out[s] = dict(close=round(float(series.iloc[-1]), 4), close_date=str(series.index[-1].date()),
                          week_ago_close=prev)
    return out


def last_split(i):
    """Most recent split as {date, factor}; factor = new shares per old share (8:1 -> 8.0)."""
    f, ts = i.get("lastSplitFactor"), i.get("lastSplitDate")
    try:
        a, b = (float(x) for x in str(f).split(":"))
        return dict(date=datetime.fromtimestamp(int(ts), timezone.utc).date().isoformat(), factor=a / b) if a > 0 and b > 0 and ts else None
    except (TypeError, ValueError):
        return None

def bounds(close, shares, screener_cap):
    """Conservative interval: +/-band around close x shares, widened to include the screener's figure."""
    caps = [c for c in (close * shares if shares else None, screener_cap) if c]
    return dict(low=round(min(caps) * (1 - CAP_BAND)), high=round(max(caps) * (1 + CAP_BAND)))


def status(cap):
    if cap["low"] > USER_CUTOFF_USD:
        return "eligible"
    return "below_cutoff" if cap["high"] <= USER_CUTOFF_USD else "unverified"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="reference session YYYY-MM-DD (default: latest completed)")
    ap.add_argument("--only", nargs="*", help="limit to these Nasdaq symbols (testing)")
    args = ap.parse_args()
    ref_day = date.fromisoformat(args.date) if args.date else reference_session()
    uni = read(DATA / "universe.json")
    cands = [c for c in uni["candidates"] if not args.only or c["symbol"] in args.only]
    symbols = [c["yf_symbol"] for c in cands]
    px = closes(symbols, ref_day)
    with ThreadPoolExecutor(8) as pool:
        infos = dict(zip(symbols, pool.map(info, symbols)))

    issuers, failures = {}, []
    for c in cands:
        s, i, p = c["yf_symbol"], infos.get(c["yf_symbol"]), px.get(c["yf_symbol"])
        if not i or not p or i.get("quoteType") != "EQUITY":
            failures.append(dict(symbol=c["symbol"], reason="no quote/info" if not (i and p) else i.get("quoteType")))
            continue
        shares = i.get("impliedSharesOutstanding") or i.get("sharesOutstanding")
        cap = bounds(p["close"], shares, c["screener_cap_usd"])
        mean = i.get("targetMeanPrice")
        row = dict(issuer_id=(i.get("longName") or c["name"]).strip(), symbol=c["symbol"], yf_symbol=s,
                   name=i.get("longName") or c["name"], country=c["country"],
                   sector=i.get("sector") or c["sector"], industry=i.get("industry") or c["industry"],
                   currency=i.get("currency"), financial_currency=i.get("financialCurrency"),
                   exchange_tz=i.get("exchangeTimezoneName") or "America/New_York",
                   close=p["close"], close_date=p["close_date"], week_ago_close=p["week_ago_close"],
                   shares_used=shares, market_cap_usd=cap, screener_cap_usd=c["screener_cap_usd"],
                   status=status(cap), avg_volume=i.get("averageVolume") or 0, dividend_rate=i.get("dividendRate"),
                   earnings_ts=i.get("earningsTimestamp"), last_split=last_split(i),
                   aggregate=dict(provider="Yahoo Finance (via yfinance)", mean=mean,
                                  median=i.get("targetMedianPrice"), high=i.get("targetHighPrice"),
                                  low=i.get("targetLowPrice"), analysts=i.get("numberOfAnalystOpinions"),
                                  recommendation=i.get("recommendationKey"),
                                  recommendation_mean=i.get("recommendationMean"),
                                  upside_pct=(100 * (mean / p["close"] - 1)) if mean and i.get("currency") == "USD" else None))
        prev = issuers.get(row["issuer_id"])
        if prev:   # one row per issuer: keep the most traded class, remember the others
            keep, other = (row, prev) if row["avg_volume"] > prev["avg_volume"] else (prev, row)
            keep.setdefault("other_classes", []).extend([other["symbol"]] + other.get("other_classes", []))
            issuers[row["issuer_id"]] = keep
        else:
            issuers[row["issuer_id"]] = row

    rows = sorted(issuers.values(), key=lambda r: -r["market_cap_usd"]["low"])
    counts = dict(listings_checked=len(cands), issuers=len(rows), failures=len(failures))
    for st in ("eligible", "below_cutoff", "unverified"):
        counts[st] = sum(r["status"] == st for r in rows)
    out = dict(universe_source=uni["source"], universe_retrieved_at=uni["retrieved_at"],
               reference_session=str(ref_day), fetched_at=datetime.now(timezone.utc).isoformat(),
               cutoff_usd=USER_CUTOFF_USD, counts=counts, issuers=rows, failures=failures)
    write(DATA / "aggregate" / f"{ref_day}.json", out)
    print(counts)


if __name__ == "__main__":
    main()
