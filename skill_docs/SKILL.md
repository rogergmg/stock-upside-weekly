---
name: stock-upside-analysis
description: Research stock upside for a company, watchlist, or defined market of public companies with verified equity market capitalization strictly above US$20 billion. Compare sector-appropriate valuation scenarios with analyst ratings, individual target revisions, and recency-weighted consensus. Use for equity upside, analyst-disagreement, and ranked opportunity screens.
---

# Stock upside analysis

Answer how much the share price could change, what the current price implies, and which observable results would change the investment case. Default to a 12-month price horizon and the latest completed regular-session close. Keep negative conclusions. Accept international listings.

## Verify eligibility before valuation

1. Identify the issuer, share class, listing, price currency and share unit. Use one row per issuer in discovery. Use the user's chosen listing for returns. Resolve ambiguous tickers from exchange or company evidence.
2. Admit only a company with verified whole-company common equity market value **strictly above US$20,000,000,000** at the reference close. Exactly $20 billion is excluded. If a rounded figure, conflicting sources or missing data straddles the boundary, obtain better evidence or mark eligibility unverified. Return only the eligibility finding for that name.
3. Use a dated issuer-level cap or sum each distinct class's closing price × actual outstanding shares, converting to USD with dated FX. Exclude treasury shares. Avoid adding depositary receipts or secondary listings to their underlying shares. Distinguish the market value of all shares from free float, enterprise value and diluted weighted-average shares. Identify the shares date when different from the price date. Reconcile material issuance, buybacks or splits. For rounding rules and data acquisition see [data and coverage](references/data.md).

## Value eligible companies

- Establish one information cutoff, currency and horizon for each comparison. A filing or call released after the reference close belongs in a subsequent-events note or a later run. Record the actual close date per listing on holidays. For an historical request, use the public information and share units as of that date.
- Build independent bear, base and bull cases from filings and operating assumptions. Read [valuation methods](references/valuation.md) for sector choice, worked arithmetic and how to handle enterprise value or discounted cash flow. Show the driver, the valuation assumption, the target price and signed price return for every case. Expected cash dividends have their own line. If the data cannot support a target, identify the missing input and leave the company unranked.
- Quantify what would justify today's price and the analyst target using the same operating forecast. Show how a plausible change to the most influential assumption changes the result. Name a specific metric and next disclosure that would support or weaken the base case.

## Reconstruct analyst views

Obtain dated individual calls and their sources using [data and coverage](references/data.md). Read [analyst records and calculator](references/analysts.md) before preparing inputs. Run the bundled Python 3 calculator from the installed skill directory. It computes independent rating and target weights, histories, coverage, sensitivity and price upside from verified inputs.

- Track one active rating and target per identifiable analyst for each stock. Use only explicitly issued or reaffirmed fields. Keep previous calls in the person's timeline. Close the former coverage when a broker hands it to a successor. Label uncovered periods and firm-only reports.
- Default to 90 calendar days for the weight to halve. Show raw Buy/Hold/Sell counts and the normalized weighted distribution. Show the source's original rating and its benchmark when a relative label has been mapped. These percentages represent coverage weight.
- Compare equal-weight and recency-weighted targets. Report each sample size, target range, latest dates and updates after the last earnings release. Surface concentration, old targets and differences between the sample and published consensus. With only a provider aggregate, report it as published with its date/methodology. Leave individual-weight and timeline fields unavailable.
- Show how each identifiable analyst's view evolved. Include dated previous/current ratings and targets, target changes in percent, and reaffirmations. In a large screen summarize changes and preserve access to each researched name's underlying rows. A target cut and a Buy can coexist. Distinguish an actual revision from higher implied upside caused by a falling stock price.

## Produce the result

For one stock, lead with the listing, close, date, USD market cap, 12-month base and bear price returns, and analyst-implied return. Follow with scenario math, analyst evolution and the measurable reason the views differ. Put source links adjacent to the numbers they support. Differentiate reported results, company guidance, analyst estimates and your model assumptions.

For a watchlist or screen, use the user's universe and filters. For open-ended discovery, choose a reproducible universe with an accessible constituent list, state it prominently, and cover it or report the exact subset evaluated. Collect all pages of constituents and collapse duplicate issuers. Record distinct issuers checked, below cutoff, ambiguous, eligible, valued, with usable analyst histories and matching the filters. Explain material omissions. Apply user filters before taking the top N. Rank by unrounded independent base-case price return by default. Keep negative estimates and missing analyst coverage visible. If the user asks for analyst-led ranking, identify the target basis, coverage quality and any exclusions. Never mix provider aggregate upside and calculated named-analyst upside into one unlabeled sort.

Use the bundled watchlist calculator in [valuation methods](references/valuation.md) to apply the cap rule, calculate signed returns, filter and sort the researched universe. A compact comparison uses issuer, cap, close, bear/base/bull price returns, weighted analyst upside, target contributor count and recent revisions. State the percentage-point gap as analyst upside minus base-case upside. Where evidence allows, translate the gap into implied EPS, growth, margin or multiple. Identify where analyst assumptions are unknown.

## Evaluate the weighting

Use [historical evaluation](references/evaluation.md) for a weight comparison or calibration request. The helper compares equal weighting and 45-, 90- and 180-day half-lives on identical observations. Treat 90 days as the working preference. Changing the default requires evidence on held-out issuers and dates. Historical test scores and current investment conclusions answer different questions.
