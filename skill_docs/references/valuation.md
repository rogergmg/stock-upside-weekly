# Independent valuation

Start with the latest annual and interim results available at the cutoff. Present key inputs at the same accounting basis and horizon in all scenarios. Select the driver that explains the business. Read management's outlook and reconcile it to the model. A sector label alone does not justify a multiple.

| Business | Possible primary method | Inputs that can reverse the conclusion |
|---|---|---|
| Profitable operating company | Forward EPS × justified P/E at the horizon | Revenue, operating margin, tax, dilution and buybacks. Specify which earnings period an investor at the target date is pricing. |
| Capital-intensive or leveraged business | Enterprise value from forward EBITDA or unlevered cash flow | Reinvestment, working capital, net debt, leases, preferred claims and minority interests. Match lease and pension treatment to the peers. |
| Bank or insurer | Tangible book value per common share × P/TBV or residual income | Sustainable return on tangible equity, cost of equity, capital distribution constraints, credit losses or reserve development. For a steady-state check, P/TBV ≈ (ROTE − growth)/(cost of equity − growth) only with consistent book, payout and growth assumptions. |
| REIT or property company | FFO/AFFO per share multiple or asset NAV less senior claims | Maintenance capex, occupancy, cap rates, debt resets and definition of AFFO. |
| Cyclical or commodity producer | Mid-cycle earnings/cash flow or asset NAV | Product price, volume, sustaining capex and net debt across the cycle. Stress the balance sheet in the bear case. |
| Loss-making growth company or conglomerate | Explicit revenue-to-margin-to-cash-flow path, or sum of segment values | Cash burn, financing/dilution and corporate costs. For binary assets, source milestone probabilities or show an unweighted range. |

For a forward enterprise value, add projected non-operating cash and investments and subtract projected gross debt, preferred equity, non-controlling interests and other senior claims as applicable. Divide by projected diluted common shares. Avoid counting the same cash or debt twice. With a DCF, value remaining cash flows **at the target date** using a discount rate consistent with their currency and risk, then bridge to equity at that date. Today's DCF fair value and a future price target have different valuation dates. For perpetual growth, justify a discount rate above terminal growth. Explain any material divergence from a peer or historical multiple.

## A reproducible stock case

Illustration only. Close $100. The earnings inputs below are diluted EPS for the same forward period as viewed at the 12-month target date.

| Case | EPS | P/E | Target | Price return |
|---|---:|---:|---:|---:|
| Bear | $5.00 | 16× | $80.00 | −20.0% |
| Base | $6.00 | 18× | $108.00 | +8.0% |
| Bull | $6.50 | 21× | $136.50 | +36.5% |

At $6.00 EPS, the close corresponds to 16.7×, and an analyst target of $125 corresponds to 20.8×. At a constant 18×, $125 requires $6.94 EPS, about 15.7% above the model. These are alternative explanations for the gap. Attribute neither explanation to a brokerage without evidence. A two-turn reduction from the base P/E cuts the target to $96 and flips the price return to −4%.

Price return = target / close − 1. Simple gross total return = (target + expected cash dividends over the horizon) / close − 1. Label the dividend assumption, tax basis and any reinvestment convention. Keep distributions out of a price-only backtest. Present price returns at a precision the inputs support. Show no probability-weighted expected value unless the probabilities are sourced or explicitly hypothetical.

## Apply the comparison to a watchlist

Run `python3 scripts/rank.py universe.json` after researching the universe. The top-level fields are `universe` (name of the list), `date` (ISO analysis date), optional `horizon_months` (default 12) and `companies` (array). Each company is a [calculator snapshot](analysts.md) plus `issuer_id` and optional `valuation` with numeric `bear`, `base`, `bull` target prices on the same per-share/currency basis as the close. Add `dividend_per_share` if a defensible gross dividend estimate exists. For an ineligible name, only issuer ID, listing symbol, time zone, as-of timestamp and USD cap bounds are needed. Keep the derivation of scenario targets and the data sources with each company's research.

The default sort uses the independent base-case price return. For an analyst-led screen choose `--order analyst`. `--min-base-pct 15 --limit 10` applies a 15% independent base-case threshold and returns at most ten names after sorting. For a user-requested revision or sector filter, apply the additional criterion to the complete matched set before truncation and report that count. Preserve partial coverage labels on every row in an analyst-led screen. Exclude partial panels from a screen for broad Street consensus unless the requested comparison explicitly admits samples. A single analyst is one opinion. Negative base returns rank below positive returns. Prices for different exchanges may have different most-recent closing dates.
