# Stock Upside Weekly

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)

Weekly 12-month upside estimates for every US-listed company with a verified market cap above **US$50B** — combining independent, filing-based **bear / base / bull** valuations with a structured week-over-week change feed, rendered into a single self-contained HTML dashboard.

---

## Why This Exists

Most stock screeners blend analyst consensus, momentum, and opaque scores into a single number. **Stock Upside Weekly** separates independent valuation from Wall Street consensus and traces every figure back to a dated source:

- **Independent valuation leads** — Bear, base, and bull 12-month targets are built from SEC filings and stated operating assumptions, ranked by unrounded base-case 12-month price return.
- **Street consensus stays separate** — Provider aggregate targets are displayed quietly in their own column and never blended with the base-case model.
- **Recency-weighted named analysts** — Individual analyst calls are tracked with dated sources and weighted using a 90-day half-life; only calls with a documented 12-month horizon count toward the weighted target.
- **Week-over-week diff** — Each weekly snapshot highlights what actually changed: newly researched names, base-case return moves, rating and target changes by named analysts, Street target shifts, and companies crossing the $50B threshold.
- **Nothing hidden** — Negative upside, stale research, missing coverage, and issuers straddling the $50B boundary are surfaced plainly rather than filtered out or guessed.

---

## How the Pipeline Works

Every week after Friday's close, the pipeline refreshes market data, rotates a batch of issuers through deep research, validates every research file against strict schema and math rules, and builds a static, zero-dependency dashboard:

```text
Nasdaq Screener ──▶ universe.py   ──▶ data/universe.json
Yahoo Finance   ──▶ refresh.py    ──▶ data/aggregate/<date>.json
Batch Selector  ──▶ rotate.py     ──▶ data/batch.json
Deep Research   ──▶ research/*.json (300+ US large-cap issuers)
Validation      ──▶ validate.py   ──▶ data/validation.json
Diff + Build    ──▶ changes.py + build.py ──▶ data/weekly/<date>.json + site/index.html
```

1. **`pipeline/universe.py`** — Pulls the US-listed universe from the Nasdaq screener and consolidates multiple share classes per issuer.
2. **`pipeline/refresh.py`** — Fetches reference close prices, share counts, and aggregate analyst targets via `yfinance`.
3. **`pipeline/rotate.py`** — Selects the next batch of issuers to research or refresh.
4. **Deep research (`research/<SYMBOL>.json`)** — Structured JSON per issuer containing bear/base/bull scenarios, sensitivities, watch metrics, dated named-analyst events, and primary source URLs (see [`RESEARCH.md`](RESEARCH.md)).
5. **`pipeline/validate.py`** — Enforces target ordering (`bear <= base <= bull`), timestamp cutoffs, horizon rules, and source requirements.
6. **`pipeline/build.py`** — Runs the valuation/consensus/ranking engine (`engine/`), computes week-over-week changes (`pipeline/changes.py`), writes the weekly snapshot (`data/weekly/<date>.json`), and inlines it into `site/template.html` to produce `site/index.html`.

---

## Repository Structure

```text
.
├── engine/         # Core math: consensus weighting (90d half-life), evaluation, and ranking
├── pipeline/       # End-to-end weekly data, validation, diffing, and HTML build scripts
├── research/       # Per-issuer deep research JSON files (300+ $50B+ US-listed issuers)
├── data/           # Universe lists, aggregate market snapshots, and weekly ranked snapshots
├── site/           # Dashboard template (template.html) and built single-file output (index.html)
├── skill_docs/     # Valuation and analyst-tracking methodology specifications
├── PRODUCT.md      # Product scope, rules, and principles
├── RESEARCH.md     # Schema and rules for per-issuer research files
├── ROUTINE.md      # Weekly refresh runbook
└── DESIGN.md       # Dashboard design system and layout specification
```

---

## Quick Start

### 1. Set up Python environment

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 2. View the latest built dashboard

Open `site/index.html` directly in any browser — it is completely self-contained and requires no backend server.

### 3. Run the data & build pipeline

```bash
cd pipeline
../.venv/bin/python -W ignore universe.py
../.venv/bin/python -W ignore refresh.py
../.venv/bin/python -W ignore validate.py
../.venv/bin/python -W ignore build.py
```

To select a batch of issuers for new or refreshed deep research:

```bash
../.venv/bin/python rotate.py -n 15
```

See [`ROUTINE.md`](ROUTINE.md) for the full weekly operating runbook and [`RESEARCH.md`](RESEARCH.md) for the research JSON specification.

---

## Disclaimer

This repository and its generated dashboards are **research output for informational purposes only**, not investment advice or a recommendation to buy or sell any security. Valuations depend on stated assumptions and publicly available filings as of each snapshot's reference close date, and this project makes no claim of historical performance or accuracy.

---

## License

Released under the [MIT License](LICENSE).
