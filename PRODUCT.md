# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Roger, for his own investing. He opens the page once a week, after the Saturday refresh, to catch up on the US large-cap universe. It is a private, single-reader tool, not a team or client product.

## Product Purpose
Stock Upside Weekly estimates the 12-month price upside of every US-listed stock with a whole-company market cap above US$50B, using the `stock-upside-analysis` skill's method. Each weekly visit should show **what changed this week**:
- names newly researched;
- moves in base-case returns;
- rating and target changes by named analysts;
- names that crossed the $50B line.

The visit succeeds when Roger can see those changes quickly and open the reasoning behind any number.

## Positioning
Two separate views of upside that are never blended:
- **Independent valuation:** bear, base and bull targets built from filings and stated assumptions.
- **Street consensus:** the provider's aggregate analyst target, shown as published.

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
- **Rankings:** the independent ranking sorts by unrounded base-case 12-month price return. Provider aggregate upside has its own ranking. The two are never merged into one unlabelled sort. Negative returns stay visible, and unresearched names stay listed as pending.
- **Refresh:** weekly, on Saturday after Friday's close. There is one information cutoff per run (the reference session), and research dates are shown.
- **Disclaimer:** the page always says it is research output, not investment advice.
- **Sources:** source links sit next to the numbers they support.

Known gaps:
- **Week-over-week view is new.** `pipeline/changes.py` compares each snapshot with the previous one in `data/weekly/` and the page leads with a "Since last week" section (base-case moves, named-analyst calls, Street target changes, $50B crossings, research added). The first real comparison arrives with the 2026-11-20 run; until then only analyst calls and research are shown.
- **Thin named-analyst coverage.** Few calls have a documented 12-month horizon, so the analyst-weighted column is mostly empty.

## Evidence on Hand
- Weekly snapshots are in `data/weekly/<date>.json`; research files are in `research/*.json`.
- There are no testimonials, users or performance track record, and future work must not invent them.
- The skill's own two-case backtest is a calculator check, not evidence of accuracy.

## Product Principles
- Change first. A weekly visit leads with what moved since last week.
- Show the basis of every number: label every figure with where it came from (our model, named analysts, or the provider aggregate).
- Show negatives, gaps and stale research plainly rather than hiding them.
- Every number links to its scenario maths, analyst timeline and dated sources.
- Readable at a glance on a phone and scannable as a dense table on desktop.
