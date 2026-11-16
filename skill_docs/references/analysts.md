# Analyst records and calculator

Run `python3 scripts/consensus.py snapshot.json` from the skill directory or call the script by its absolute path. Requires Python 3.9+ and standard IANA time zones. Use a scratch JSON file per issuer. The helper works offline after research. Its eligibility decision depends on the verified USD bounds you supply. It does not retrieve market data or authenticate sources.

## Prepare the snapshot

The example is synthetic. At a $100 close the two targets yield an equal-weight target of $120 and a 90-day weighted target of $102. The table of named ratings is empty because these example events are target-only.

```json
{
  "symbol": "EXAMPLE:TEST", "currency": "USD", "close": 100,
  "exchange_tz": "America/New_York", "as_of": "2026-11-12T16:00:00-05:00",
  "market_cap_usd": {"low": "25000000000", "high": "25000000000"},
  "coverage": "partial", "earnings_at": "2026-10-29T16:05:00-04:00",
  "horizon_months": 12,
  "events": [
    {"analyst": "Analyst A", "firm": "Broker A", "field": "target", "value": 90,
     "issued_at": "2026-11-12", "public_at": "2026-11-12T09:00:00-05:00",
     "horizon_months": 12, "source": "Synthetic case A"},
    {"analyst": "Analyst B", "firm": "Broker B", "field": "target", "value": 150,
     "issued_at": "2026-05-16", "public_at": "2026-05-16T09:00:00-04:00",
     "horizon_months": 12, "source": "Synthetic case B"}
  ]
}
```

- `symbol` identifies one listing/class. `close` and every numeric target must already be on that listing's currency and share basis. Keep conversion evidence with the raw input. `market_cap_usd` has lower and upper dollar bounds or is null for unknown. Use matching bounds for a verified exact figure.
- `coverage` is complete, partial, aggregate_only or unavailable. Complete means the documented source population across the requested window has been reviewed. Use an empty event list for aggregate-only coverage. Report the published aggregate outside the helper.
- For each explicitly issued or reaffirmed field, create one row with its own time and source locator. Supply `source_prior` when the source states a comparable prior value on the same basis. The calculator uses it for target revisions, including the first observed call. Retain original action wording as needed. Reconcile any mismatch with the last observed value and disclose a missing intervening call. For a rating use e.g. `"field":"rating","value":"Outperform","bucket":"Buy"` only when the source's scale supports that mapping. Buy/strong buy, hold and sell/strong sell usually map directly. Retain an ambiguous original label with bucket null. A value of null means an explicit withdrawal for that field. An omitted field has no event. When coverage ends, submit a withdrawal for both active fields.
- Use a stable analyst identity (source ID or disambiguated name), a readable display name and the brokerage at the time. Reconcile duplicated notes before entry. Treat a coauthored brokerage call as one coverage seat. A named successor starts their own history. Retire the predecessor's seat on a documented handover. If the author is anonymous or a change cannot be resolved, use a separately labeled firm history and omit it from the individual calculation.
- `issued_at` is the call's actual date or offset-aware timestamp. `public_at` is a verified time the evidence was publicly knowable. For a date-only publication use end of day in the publisher's timezone unless an earlier public record proves availability. A later newspaper recap may establish availability by the recap time, but age is based on the original issue date. Unknown intra-day earnings order is counted separately. For historical replay use only the version accessible by the cutoff. Treat a subsequent correction as a later public version when building separate snapshots.
- For targets, record the documented original horizon in months. A provider's explicit methodology may establish it. Leave an unknown horizon null. Use `expires_on` for a specific end date, first day it no longer applies. By default a 12-month target expires on its first anniversary. A reaffirmation restarts age but extends the life of a fixed-date target only if the analyst extends it. Keep the absolute expiry otherwise. Ratings without stated expiry use a disclosed trailing 12-month window. An explicit expiry can shorten that window. New, withdrawn, unmapped or incompatible calls supersede the older field even when the replacement cannot be averaged.
- Normalize splits using actions effective by the cutoff and apply the same share basis to both sides of a revision. Some vendors' “adjusted” targets also reflect dividends. If the original listing, unit, currency, expiry or action cannot be verified, omit the affected numeric comparison and explain it. When a newer target clearly supersedes a former one but its value or units are unresolved, clear the former target from the input and annotate the exclusion. Preserve both source observations in the research notes. [Massive field definitions](https://massive.com/docs/rest/partners/benzinga/analyst-ratings)

## Interpret the output

For each active field give each analyst one vote before age adjustment. Raw weight = 2^(−calendar days since issue / half-life). Normalize weights within ratings and targets separately. Weighted target = sum(weight × target). The weighted rating mix is the sum of rating weights in each bucket. The 90-day raw weights at 0, 90 and 180 days are 1, 0.5 and 0.25. The sensitivity output uses the same analyst set for all four methods. Missing contributors yield null estimates. [Half-life definition](https://pandas.pydata.org/docs/user_guide/window.html#exponentially-weighted-window)

Report the number and median age of active contributors, target range, largest individual weight and how many updated each field after the last earnings release. If every target predates earnings, say so. A single analyst has 100% normalized weight whatever their age. A stale 12-month target also has less remaining time than a new one. Treat the group as outstanding broker targets with mixed remaining lives. Avoid describing it as synchronized forecasts for the base-case target date.

Use the returned history to display each analyst's dated path. Compare an updated target to the person's previous comparable target, including a prior value explicitly quoted in the initial source. Do not invent its issue date. A first observation without a known prior is an initiation only when the source says so. A target reaffirmation is a 0% revision. A coverage break interrupts consecutive cuts/raises. Separate upgrades/downgrades, raises/cuts and unchanged calls. If books of business or raw share units change, compare only after reconciliation. For a post-earnings filter, use a genuine positive revision after release. Reaffirming an old raise does not create a new one. Assess historical analyst accuracy separately only when the user asks and enough matured, dated calls exist.
