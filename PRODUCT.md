# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Roger, for his own investing. He opens the page once a week, after the Saturday refresh, to catch up on the US large-cap universe. It is a private, single-reader tool, not a team or client product.

## Product Purpose
Stock Upside estimates the 12-month price upside of every US-listed stock with a whole-company market cap above US$50B, using the `stock-upside-analysis` skill's method. Each weekly visit should show **what changed this week**:
- names newly researched;
- moves in base-case returns;
- rating and target changes by named analysts;
- names that crossed the $50B line.

The visit succeeds when Roger can see those changes quickly and open the reasoning behind any number.

## Positioning
Two separate views of upside that are never blended:
- **Independent valuation (the headline):** bear, base and bull targets built from filings and stated assumptions. The page leads with the close, our 12-month target and the upside between them.
- **Street consensus (a reference):** the provider's aggregate analyst target, shown as published, quietly and after ours.

Named-analyst targets are weighted by recency with a 90-day half-life, and only calls with a documented 12-month horizon count. Every number traces to a dated source.

## Operating Context
- **Weekly pipeline:** a cloud routine runs every Saturday at 15:00 UTC on Haiku, in the `stock-upside-weekly` environment. It:
  1. refreshes all issuers;
  2. has Sonnet subagents research about 15 more names;
  3. validates the files;
  4. builds the page;
  5. commits to the `rogergmg/stock-upside-weekly` repo;
  6. republishes the claude.ai Artifact (https://claude.ai/artifact/BVzpV1DvRwdpRDqhhVa8wW).
- **Data:** universe from the Nasdaq screener; closes, shares and aggregate targets from Yahoo Finance via yfinance; deep research files in `research/`.
- **Page build:** `pipeline/build.py` inlines the week's snapshot into `site/template.html` to produce `site/index.html`.
- **Read on:** desktop and phone.

## Capabilities and Constraints
Binding rules:
- **Scope:** US-listed issuers whose verified market cap is strictly above $50B. That is a stricter filter than the skill's $20B floor. Each issuer gets one row; extra share classes fold into it. Names whose cap interval straddles $50B are shown as unverified, never guessed.
- **Rankings:** one list of every eligible issuer, ranked by default by unrounded base-case 12-month price return. Provider aggregate upside sits in its own labelled column and can be sorted on its own. The two are never combined into one number or one unlabelled sort, and the rank column always shows the base-case rank. Negative returns stay visible, and unresearched names stay listed as pending.
- **Refresh:** weekly, on Saturday after Friday's close. There is one information cutoff per run (the reference session), and research dates are shown.
- **Disclaimer:** the page always says it is research output, not investment advice.
- **Sources:** source links sit next to the numbers they support.

Known gaps:
- **Week-over-week view.** `pipeline/changes.py` compares each snapshot with the previous one in `data/weekly/`. The page shows a "This week" panel beside the list: base-case moves, named-analyst calls, Street target changes, $50B crossings and research added. On a first snapshot, only analyst calls and research are shown.
- **Thin named-analyst coverage.** Few calls have a documented 12-month horizon, so the analyst-weighted column is mostly empty.

## Evidence on Hand
- Weekly snapshots are in `data/weekly/<date>.json`; research files are in `research/*.json`.
- There are no testimonials, users or performance track record, and future work must not invent them.
- The skill's own two-case backtest is a calculator check, not evidence of accuracy.

## Product Principles
- Opportunities first, then change. The first screen ranks the best opportunities now; what moved since last week sits beside the full list.
- Show the basis of every number: label every figure with where it came from (our model, named analysts, or the provider aggregate).
- Show negatives, gaps and stale research plainly rather than hiding them.
- Every number links to its scenario maths, analyst timeline and dated sources.
- Desktop first: a scannable table on desktop, still comfortable on a phone.

## Brand Commitments
- **Look:** the category standard for research dashboards, executed at the craft level of Linear and Stripe Dashboard. Roger chose this on 2026-11-23 over more expressive directions.
- **Never trading-app hype:** no neon, no casino energy, no loud green and red fills. It should feel calm and trustworthy.
- **Our view leads:** our estimate, the closing price and our 12-month target carry the design; Wall St. is a muted reference.
- **Dated prices:** prices are described by their close date ("at the Nov 20 close"), never as "now" or "today".
- **Better, not barer:** when the page needs to be easier to read, improve hierarchy and disclosure rather than deleting content.
