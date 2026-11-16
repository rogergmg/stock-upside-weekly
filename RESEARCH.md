# Deep research brief (one issuer per agent)

You are researching ONE company for the weekly Stock Upside site. Follow the method in
`skill_docs/SKILL.md` and its `skill_docs/references/*.md` (valuation.md and analysts.md matter most).
Use web search and open the original sources. Do not invent numbers. If an input can't be sourced, say so in the notes.

## Inputs (from data/batch.json)
symbol, issuer name, listing currency, the reference close and close date, exchange time zone, sector.
The valuation targets MUST be per share of THIS US listing, in its currency (USD). For an ADR, convert
ordinary-share values with the ADR ratio and a dated FX rate, and state both in `valuation.method`.

## Output: write exactly one JSON file at the path given (research/<SYMBOL>.json, "/" in a symbol becomes "-")

```json
{
  "issuer_id": "<issuer name as given>",
  "symbol": "<listing symbol as given, e.g. BRK/B>",
  "researched_at": "YYYY-MM-DD",
  "research_close": {"close": 0.0, "close_date": "YYYY-MM-DD"},
  "currency": "USD",
  "earnings_at": "<offset-aware ISO time of the last earnings release before the reference close, or null>",
  "coverage": "partial",
  "events": [
    {"analyst": "Jane Doe", "firm": "Broker", "field": "target", "value": 250, "source_prior": 240,
     "issued_at": "YYYY-MM-DD", "public_at": "YYYY-MM-DDTHH:MM:SS-05:00", "horizon_months": 12,
     "source": "https://..."},
    {"analyst": "Jane Doe", "firm": "Broker", "field": "rating", "value": "Overweight", "bucket": "Buy",
     "issued_at": "YYYY-MM-DD", "public_at": "YYYY-MM-DDTHH:MM:SS-05:00", "source": "https://..."}
  ],
  "valuation": {
    "method": "Forward EPS x P/E (FY2027 EPS viewed at the 12-month target date) ...",
    "bear": 0.0, "base": 0.0, "bull": 0.0,
    "cases": {
      "bear": {"driver": "...", "assumption": "EPS $x at y x", "target": 0.0},
      "base": {"driver": "...", "assumption": "...", "target": 0.0},
      "bull": {"driver": "...", "assumption": "...", "target": 0.0}
    },
    "implied_by_close": "At base EPS the close implies N x; the analyst-weighted target implies M x or EPS $z",
    "sensitivity": "One turn of P/E moves the base target by $x (y pp)",
    "watch_metric": "The specific metric that would confirm or break the base case",
    "next_disclosure": "Next earnings date or filing where that metric appears"
  },
  "dividend_per_share": null,
  "analyst_notes": "2-4 sentences: how named views moved since last earnings, why they differ from the base case (pp gap translated into EPS/multiple where possible), concentration or stale targets.",
  "sources": [{"label": "10-Q Q3 FY2026", "url": "https://...", "supports": "EPS, share count"}]
}
```

Rules (from the skill, enforced by pipeline/validate.py):
- Targets ordered bear <= base <= bull, all > 0, 12-month horizon, built from filings and stated operating assumptions. Don't anchor to the analyst targets.
- Analyst events: aim for 6-12 named analysts with dated calls from the last 12 months, one row per explicitly issued or reaffirmed field.
  - `public_at` must not be after the reference close. Use end of day in the publisher's time zone for date-only sources.
  - Use `bucket` only when Buy/Hold/Sell mapping is clear; otherwise set it to null.
  - Use `horizon_months: 12` only when the 12-month horizon is documented: either in the source, or in the broker's published research-disclosure page saying its price targets are 12-month. Add that disclosure page to `sources` with `supports: "<Firm> 12-month target horizon"`. Otherwise use null. A null horizon keeps the call in the timeline but out of the weighted target.
  - `coverage` is "partial" for a found subset. If no named calls are found, use "unavailable" with an empty events list.
- At least 3 sources with working http(s) URLs. Put source URLs on every event.
- Write valid JSON only, then stop. Don't edit any other file.
