# Data and coverage

## Retrieval path

| Need | Where to look | Check before use |
|---|---|---|
| Universe | Index administrator's constituent download, exchange issuer list or user's watchlist | Effective date, number of pages, security type and distinct issuers. For a historical screen recover constituents at that date, including later delistings. |
| Price, cap, FX | Primary listing's official close, issuer share disclosures, a dated market-data quote and a dated public FX fixing | Trading currency and units, regular session, shares effective date, FX direction and security identifier. Convert GBp to GBP before any USD conversion. For same-day releases resolve time zones. |
| Accounts and guidance | Issuer investor relations, home regulator's interim/annual filings and earnings release | Distinguish fiscal periods, reported currency, continuing operations and per-share units. For SEC data use the filing accession and acceptance time. Company Facts has multiple observations for the same period and subsequent amendments. [SEC data documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) |
| Individual calls | Dated original brokerage note or investor-relations analyst table, followed by an accessible event feed or public coverage quoting the analyst | Verify analyst, firm, action date, exact field reaffirmed, rating label, target currency, horizon and first availability. Search company + broker/analyst + target + date. Look backward from the most recent earnings release for prior calls and forward to the cutoff for replacements. Reconcile with the broker's latest identifiable call. |
| Aggregate consensus | Provider's instrument-specific forecast page and its own methodology | Record collection window, price horizon, mean/median, last update, separate rating and target counts, range and underlying close. Recompute upside on the chosen close. Identify provider or coverage changes across issuers. [TipRanks methodology](https://www.tipranks.com/glossary/f/faq) |

Open the source behind a search result. If a feed is available, paginate until the requested window is covered. No subscription is necessary to use the skill. Access to complete analyst history varies by issuer and provider. Public articles may expose only an explicitly selected subset. Label it “weighted target of the N named analysts found,” identify its selection rule and keep it distinct from broad consensus. Use a provided export or authorized data connection if available. A source's latest ingestion timestamp alone cannot establish the issue date. [Benzinga event fields](https://www.benzinga.com/apis/cloud-product/analyst-ratings) · [Massive event dates, fields and pagination](https://massive.com/docs/rest/partners/benzinga/analyst-ratings)

## Threshold decisions

Use the highest defensible precision available. For a cap rounded to the nearest $0.1B, displayed $20.0B implies a range of roughly $19.95B–$20.05B. Treat that range as unresolved. A displayed $23.1B clearly qualifies. When the rounding convention is unknown near the boundary, find the underlying figure. The calculator accepts either an exact verified amount or a conservative inclusive interval. Bounds must encompass uncertainty from conversion or share counts if that uncertainty could change eligibility.

For a foreign issuer, sum each distinct economic class using its own price and shares, with a sourced conversion or value proxy for an unlisted class when defensible. An ADR representing two ordinary shares describes a unit conversion, not extra equity. Translate an ordinary-share target to the ADR using that ratio, the correct FX direction and a disclosed FX date/assumption. Keep the eligibility calculation on the issuer and the return calculation on the chosen listing. [SEC market cap definition](https://www.investor.gov/introduction-investing/investing-basics/glossary/market-capitalization)

## Evidence to retain

Retain one link or source document locator per material input, in scratch notes or a user-requested workbook. Distinguish price date, release time, filing period, event date and retrieval date. Record whether data are complete, partial, aggregate only or unavailable. If historical outcomes involve a takeover, delisting, split, spin-off or change of share class, reconcile consideration and units explicitly. Never silently drop failed companies or use a dividend-adjusted close against a price-only target.
