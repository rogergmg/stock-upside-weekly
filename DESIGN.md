---
name: Stock Upside Weekly
description: A calm, precise research dashboard that ranks our 12-month price targets for large US stocks from the latest close, with the Wall St. average as a quiet, separate reference.
colors:
  canvas: "#f6f7f9"
  panel: "#ffffff"
  sunk: "#f8fafc"
  hover: "#f2f5f8"
  slate-ink: "#0f172a"
  slate-body: "#334155"
  slate-muted: "#556175"
  hairline: "#e3e8ee"
  hairline-strong: "#d3dae3"
  action-blue: "#2563eb"
  on-action: "#ffffff"
  action-wash: "#eef3ff"
  action-line: "#c7d7fe"
  range-band: "#c3d5fb"
  gain-green: "#137837"
  gain-wash: "#e6f4ea"
  loss-red: "#c2361f"
  loss-wash: "#fcebe7"
  caution-amber: "#965a00"
  caution-wash: "#fcf1dd"
  dark-canvas: "#0b0e14"
  dark-panel: "#12161f"
  dark-sunk: "#0f131b"
  dark-hover: "#181e29"
  dark-ink: "#e7eaf0"
  dark-body: "#c3cad6"
  dark-muted: "#98a2b3"
  dark-hairline: "#232a36"
  dark-hairline-strong: "#2f3846"
  dark-action-blue: "#6d9cff"
  dark-on-action: "#0b0e14"
  dark-action-wash: "#162140"
  dark-action-line: "#2b4278"
  dark-range-band: "#2a3f6e"
  dark-gain-green: "#4cc38a"
  dark-gain-wash: "rgba(76, 195, 138, .13)"
  dark-loss-red: "#ff8270"
  dark-loss-wash: "rgba(255, 130, 112, .13)"
  dark-caution-amber: "#e8a945"
  dark-caution-wash: "rgba(232, 169, 69, .13)"
typography:
  display:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "28px"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.025em"
    fontFeature: "tnum"
  headline:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.022em"
  figure:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    letterSpacing: "-0.015em"
    fontFeature: "tnum"
  ticker:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 600
    letterSpacing: "-0.012em"
  title:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
  subhead:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    letterSpacing: "-0.005em"
  caption:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.5
  chip:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "11.5px"
    fontWeight: 500
    lineHeight: "18px"
  kbd:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "11px"
    fontWeight: 500
    lineHeight: "16px"
rounded:
  keycap: "5px"
  badge: "6px"
  control: "8px"
  inner: "10px"
  panel: "12px"
  pill: "999px"
spacing:
  xxs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "20px"
  xl: "24px"
  xxl: "32px"
  xxxl: "48px"
components:
  top-bar:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.slate-ink}"
    height: "60px"
    padding: "0 24px"
  nav-link:
    textColor: "{colors.slate-muted}"
    rounded: "{rounded.control}"
    padding: "6px 10px"
  nav-link-hover:
    backgroundColor: "{colors.hover}"
    textColor: "{colors.slate-ink}"
  nav-link-current:
    backgroundColor: "{colors.action-wash}"
    textColor: "{colors.action-blue}"
  icon-button:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.slate-muted}"
    rounded: "{rounded.control}"
    size: "32px"
  panel:
    backgroundColor: "{colors.panel}"
    rounded: "{rounded.panel}"
  panel-head:
    typography: "{typography.title}"
    padding: "14px 16px"
  upside-card:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.slate-ink}"
    rounded: "{rounded.panel}"
    padding: "16px 16px 14px"
  case-card:
    backgroundColor: "{colors.panel}"
    rounded: "{rounded.inner}"
    padding: "14px"
  funnel-step:
    backgroundColor: "{colors.sunk}"
    rounded: "{rounded.inner}"
    padding: "10px 14px"
  input:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.slate-ink}"
    rounded: "{rounded.control}"
    height: "34px"
    padding: "6px 10px"
  table-header:
    backgroundColor: "{colors.sunk}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.label}"
    padding: "8px 12px"
  table-row:
    textColor: "{colors.slate-ink}"
    typography: "{typography.body}"
    padding: "10px 12px"
  table-row-hover:
    backgroundColor: "{colors.hover}"
  table-row-open:
    backgroundColor: "{colors.action-wash}"
  row-detail:
    backgroundColor: "{colors.sunk}"
    padding: "20px 16px 24px"
  phone-row:
    padding: "12px 16px"
  phone-row-open:
    backgroundColor: "{colors.action-wash}"
  week-row:
    typography: "{typography.body-sm}"
    height: "38px"
    padding: "7px 16px"
  pill-gain:
    backgroundColor: "{colors.gain-wash}"
    textColor: "{colors.gain-green}"
    rounded: "{rounded.pill}"
    padding: "2px 9px"
  pill-loss:
    backgroundColor: "{colors.loss-wash}"
    textColor: "{colors.loss-red}"
    rounded: "{rounded.pill}"
    padding: "2px 9px"
  chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.chip}"
    rounded: "{rounded.pill}"
    padding: "0 8px"
  chip-accent:
    backgroundColor: "{colors.action-wash}"
    textColor: "{colors.action-blue}"
    rounded: "{rounded.pill}"
  chip-caution:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-amber}"
    rounded: "{rounded.pill}"
  rank-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.badge}"
    padding: "0 7px"
  count-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 8px"
  kbd:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.kbd}"
    rounded: "{rounded.keycap}"
    padding: "0 5px"
---

# Design System: Stock Upside Weekly

## Overview

**Creative North Star: "The Quiet Research Desk"**

A calm, precise research dashboard in the category standard, executed at the craft bar of Linear and Stripe Dashboard. White panels sit on a cool grey canvas, hairline borders and soft shadows separate the layers, and one blue carries everything the reader can act on. The first screen ranks the best opportunities, and every number opens onto its reasoning. Alignment, tabular figures and restraint do the work; nothing on the page shouts.

Density is high but legible. One ranked list replaces tabs, and depth lives behind disclosure rather than being cut: a row expands into its cases, valuation, analyst evidence and sources. The page is desktop-first with a sticky "This week" rail; on a phone the table becomes a stacked list and the top cards become a sideways scroller. Light and dark themes are both first-class, following the system setting unless the reader picks one in the top bar.

The world rejects two things by name: the trading-app look (neon, hype, casino darkness, loud green and red fills) and the spreadsheet dump.

**Key Characteristics:**
- Cool grey canvas, white panels, 1px hairlines, 12px corners, soft two-layer shadows.
- Inter alone, semibold headings with tight negative tracking, tabular figures everywhere a number appears.
- One blue accent for action, selection, sort and the current place; green and red only for gain and loss.
- Our estimate and the Wall St. average always sit side by side, each labelled, never blended.
- Every range bar shares one scale, so rows compare at a glance.
- Keyboard-first list with visible kbd hints.

## Colors

A slate-and-paper neutral system with a single blue accent and three tinted state hues; every state colour has a soft wash partner so it can appear as tinted pill or text, never as a loud fill. Each light token has a `dark-` sibling that replaces it under `prefers-color-scheme: dark` (unless the reader chose light) and under `:root[data-theme="dark"]`.

### Primary
- **Action Blue** (`action-blue`; dark `dark-action-blue`): links, the brand mark, the active sort header, the current nav item, focus rings, disclosure summaries ("Show 179 more", "Weighting checks"), and the average marker on the analyst target strip.
- **Action Wash** (`action-wash`): the selected state. Open table rows, open phone rows, the current nav pill, the "Our estimate" chip, and the briefly highlighted row in "Not in the list".
- **Action Line** (`action-line`): the border of accent chips and the double hairline around the base-case card.
- **Range Band** (`range-band`): the pale blue bear-to-bull band on every range bar and its legend swatch.

### Secondary (state hues)
- **Gain Green** (`gain-green` on `gain-wash`): positive returns, Buy counts and segments, upgrades and raised targets, the high end of a target strip.
- **Loss Red** (`loss-red` on `loss-wash`): negative returns, Sell counts and segments, downgrades and cut targets, the low end of a target strip.
- **Caution Amber** (`caution-amber` on `caution-wash`): stale research, unverified market caps, split-adjusted notes, non-active analyst calls, and the footer disclaimer line.

### Neutral
- **Canvas** (`canvas`): the page ground; also the fill of chips, kbd keys, rank and count badges.
- **Panel** (`panel`): panels, cards, case cards, inputs, the top bar.
- **Sunk** (`sunk`): table headers, the expanded row-detail well, funnel steps, timeline dividers.
- **Hover** (`hover`): row, nav and button hover fill.
- **Slate Ink** (`slate-ink`): primary text and figures.
- **Slate Body** (`slate-body`): reasoning prose, case drivers, key-value answers.
- **Slate Muted** (`slate-muted`): labels, secondary lines, table headers, the ghost ring.
- **Hairline** (`hairline`) and **Hairline Strong** (`hairline-strong`): 1px borders and row rules; the strong step for input borders, hover borders, the zero tick and Hold segments.

### Named Rules
**The Two Bases Rule.** Our estimate and the Wall St. average are never blended into one number. Each has its own labelled column and its own sort, and `#` always shows our rank, even when the list is sorted by something else (a sort note says so).

**The Our-View-Leads Rule.** The page is about three numbers: the close, our 12-month target and the upside between them. They get the weight (semibold target, coloured pill, card headline). Wall St. is a reference: muted grey, the last column, absent from the cards, its weekly moves listed last.

**The Dated Close Rule.** Prices are named by when they were set: "Close · Nov 20", "Prices at the Nov 20, 2026 close", "from the Nov 13 close of $110.63". Never "now", "today" or "current".

**The Meaningful Colour Rule.** Green and red mean gain and loss, and their direct analogues (Buy and Sell, upgrade and downgrade, a target strip's high and low). Amber means caution. Blue means you can act here, or this is selected, sorted or current. No hue is ever decorative.

**The Wash Not Fill Rule.** State colour appears as text, or as text on its own 13%-strength wash. There are no solid green or red blocks.

## Typography

**Display Font:** Inter (with system-ui, -apple-system, Segoe UI, sans-serif)
**Body Font:** Inter
**Label/Mono Font:** Inter, with `font-variant-numeric: tabular-nums` on every number

**Character:** One neutral face carried at four weights (400, 500, 600, 700 loaded; 400 to 600 used), with semibold headings and tight negative tracking that grows as size grows. Hierarchy comes from size, weight and the ink/body/muted steps, never from a second family or from all-caps.

### Hierarchy
- **Display** (600, 28px, 1.15, -0.025em, tabular): the base-case return on each top-upside card, coloured as gain or loss.
- **Headline** (600, 24px, 1.25, -0.022em; 21px on phones): the page's one h1, "Top upside".
- **Figure** (600, 20px, -0.015em, tabular): case-card price targets. The funnel counts use the same treatment at 18px.
- **Ticker** (600, 17px, -0.012em): the ticker on each top-upside card.
- **Title** (600, 15px, 1.35, -0.01em): panel headings (h2) and the brand name.
- **Body** (400, 14px, 1.5): base text and table cells.
- **Body small** (400, 13 to 13.5px): reasoning prose, key-value lists, week rows, controls. Prose caps at 72 to 80ch.
- **Subhead** (600, 13px): detail section headings (h3); analyst block headings use 600 at 12.5px.
- **Caption** (400, 12.5px): company names under tickers, sub-lines, card secondary lines, footer.
- **Label** (500, 12px): table headers, legends, rank badges, counts.
- **Chip / kbd** (500, 11.5px / 11px): chips and key hints.

### Named Rules
**The Tabular Figures Rule.** Every number that can sit above another number uses tabular figures, so columns align without monospace.

**The Sentence Case Rule.** Headings, headers and labels are sentence case at their natural size. No uppercase tracking, no eyebrow labels above headings.

## Layout

A single centred column, max 1400px wide, with 24px side gutters (16px on phones) and 24px between major blocks; page padding is 32px top, 48px bottom. The order is fixed: "Top upside" heading and lede, a row of five top-upside cards (14px gaps), then a work area of the stocks panel beside a 360px "This week" rail (20px gap), then the Methodology panel and the footer.

The top bar is sticky at 60px (56px on phones) and respects the safe-area inset. Its three-column grid puts the brand left, the section nav centred, and "Prices as of" right. There is no theme switch: the page follows the artifact viewer's theme (system, or an explicit light/dark choice the viewer sets on the root). Sticky offsets for the table header, the week rail and scroll anchors all derive from the bar height.

Panels share one inner rhythm: 16px horizontal inset, 14px head padding, 8px meta strips, 10px by 12px table cells.

**Responsive steps** (desktop first):
- Down to 1080px the five cards stay in one row; at 1080px they become a horizontal snap scroller (240px cards), so no row is ever left half empty.
- At 1180px the rail stacks below the stocks panel, becomes a two-column grid of groups, loses its stickiness, and a "This week" jump link appears under the cards.
- At 1040px the table scrolls horizontally, its header stops sticking, and the range text beside each bar hides.
- At 900px the nav hides, and detail and methodology columns stack.
- At 720px the table is replaced by the phone list, the card scroller widens each card to 78%, a sort select (our upside, Wall St. avg, company) appears beside the sector filter because the table header is gone, inputs grow to 16px text and 42px height, the week groups go single-column, and kbd hints hide.
- At 380px the "Prices as of" stamp hides.

### Named Rules
**The Desktop First Rule.** The desktop layout is the reference. Phones get a purpose-built stacked list and a sideways card scroller, not a squeezed table.

## Elevation & Depth

A hybrid: tonal layering (canvas, panel, sunk) does most of the work, and soft two-layer shadows lift panels just off the canvas. Shadows are ambient, slate-tinted in light and pure black in dark, and they only grow on hover for cards that open something.

### Shadow Vocabulary
- **Rest** (`box-shadow: 0 1px 2px rgba(15, 23, 42, .04), 0 2px 6px -2px rgba(15, 23, 42, .06)`; dark `0 1px 2px rgba(0, 0, 0, .35)`): every panel and top-upside card.
- **Lift** (`box-shadow: 0 2px 4px rgba(15, 23, 42, .05), 0 14px 28px -10px rgba(15, 23, 42, .18)`; dark `0 2px 4px rgba(0, 0, 0, .4), 0 14px 28px -10px rgba(0, 0, 0, .7)`): top-upside card hover, paired with a 2px rise.
- **Base-case ring** (`box-shadow: inset 0 0 0 1px` action line): doubles the base-case card's border so it reads as the selected estimate without a fill.

### Named Rules
**The Lift Means Open Rule.** Only elements that open something rise on hover. Static panels never move.

## Shapes

Gently rounded rectangles in four nested steps: 12px for panels and top-upside cards, 10px for cards inside a panel (case cards, funnel steps, the timeline and "Not in the list" frames), 8px for controls (inputs, select, icon buttons), and fully round pills and chips. Small fixed badges (rank, timeline action icons) use 6px, kbd keys 5px. Borders are always 1px hairlines; the one exception is the kbd key's 2px bottom edge, which reads as a keycap.

Data marks are round: 4px stroke caps on range bars, a 5px base-case dot with a panel-coloured halo, a hollow 4px ghost ring for last week, 6px rating segments with 2px corners.

### Named Rules
**The Shared Scale Rule.** Every range bar on the page uses one scale, computed from the whole ranked list, with a dashed zero tick. A hollow ghost ring marks last week's base case whenever it moved by half a point or more.

## Components

### Top bar
Quiet, always present. Panel-white with a hairline bottom border, sticky under the safe area. The brand mark is a 24px blue rounded tile with a white rising line. Nav links are 13.5px medium muted text in 6px by 10px pills; hover fills with the hover tone, and the current section (scrollspy) turns blue on the action wash.

### Top-upside cards
The first thing read. Five equal cards, each a button that opens its stock in the list. Top line: ticker and a `#rank` badge. Then the company name (ellipsised), the "Our 12-month upside" label, the display-size base-case return in gain or loss colour, and the price pair: "Close · Nov 20" over the closing price, an arrow, then "Our target" over our base-case price (target in semibold ink, close in body tone). A "from X last week" line follows, then a full-width range bar with bear and bull end labels. Wall St. does not appear on the cards. Hover lifts 2px with the lift shadow and a stronger border (0.2s, standard ease, motion-gated).

### Stocks table
The reference list. A panel head with title, count line, search (with a `/` kbd hint inside the field) and a sector select. Under it, a meta strip carries the legend (range band, base-case dot, ghost ring) on the left and the kbd row (↑ ↓ move, Enter open, Esc close) on the right. Columns: `#`, Company (ticker, optional stale chip, muted name), Close, Our target (semibold ink), Upside (return pill, the default sort), Bear to bull (range bar plus range text), Wall St. avg (13px muted grey price and return, last, a quiet reference), and a chevron. Headers are 12px muted on the sunk tone and stick under the top bar; sortable headers are buttons that turn blue and semibold with an arrow when active. Rows hover to the hover tone; the open row takes the action wash and its chevron rotates 90 degrees and turns blue. Pending rows are muted with a "Research pending" chip.

### Phone list rows
Each row is a full-width button: rank, ticker and name, and on the right the upside pill over "$close → **$target**". A second line holds the range bar and "Bear X% · Bull Y%". Wall St. lives in the row detail on phones. The open row takes the action wash and its detail opens beneath on the sunk tone.

### Row detail
Opens in a sunk well under the row with a 0.24s fade-and-drop reveal (motion-gated).
- **Split note:** an amber "Split-adjusted" chip with a one-line explanation, above the cases.
- **Case cards:** three 10px cards (bear, base, bull) with the price target in figure type, the return beside it, the driver in body text and the assumption in muted caption. The base case carries the "Our estimate" accent chip and a doubled blue hairline.
- **Valuation:** a key-value list with a 150px muted key column (method, what the close implies, sensitivity, what to watch, next report, dividends, researched, market cap). Market cap comes last.
- **Analysts:** stacked blocks split by hairlines. The Wall St. average block names its source and fetch date and draws the target strip (red low, green high, blue-ringed average, ink tick for the close). The Named analysts block shows the recency-weighted target with its own strip and an optional "Weighting checks" disclosure.
- **Analyst ratings:** a full-width section that is always open, never behind a disclosure (Roger, 2026-11-23: ratings and their changes must be visible on every stock, as on the old page). Two columns on top: "Current ratings" (Sell, Hold, Buy counts over a row of 6px segments, plus the recency-weighted split) and "Changes recorded" (only non-zero counts of upgrades, downgrades, targets raised and targets cut, in gain or loss colour; reiterations and first sightings are not counted as changes). Below them is every analyst action, newest first, in a compact table inside a 10px frame: action, rating (prior → new), analyst and firm, target (prior → new), change, date and source. Action icons sit in 20px tinted tiles (green for a raise or upgrade, red for a cut or downgrade, neutral otherwise), with a sunk divider row at the last earnings release. On phones each action stacks into a small card: action and date, analyst and source, then rating with target and change. With no data, a single muted line replaces the section body.
- **Sources:** a numbered list of links with muted notes on what each one supports.

### This week panel
The change log. Sticky beside the list on desktop and scrolls inside itself. Groups (Estimate moves, Analyst calls, Crossed $50B, Fresh research, Street targets last) each have a subhead with a count badge, a muted hint, three rows and a "Show N more" disclosure. Rows are 38px buttons (44px on phones): ticker, a two-line muted description with the new value in ink, and a pill on the right. Fresh research uses chips, blue for a first research and grey for a refresh. Below 1180px, where the rail stacks under the list, a full-width jump link under the cards ("This week: N estimate moves · N analyst calls · N crossed $50B", with a down arrow) takes readers straight to it.

### Methodology panel
A funnel of 10px sunk steps (big tabular count over a muted caption), two prose columns, and a "Not in the list" disclosure holding a framed table of stocks outside the cutoff with amber "unverified" or grey "below $XB" chips. Jumping to one of those names flashes its row with the action wash for 2.6s.

### Pills, chips and kbd
- **Pill:** the return badge. 999px, 600 weight, 13px tabular (12px in week rows), gain or loss text on its wash.
- **Chip:** the status tag. 999px, 11.5px medium, canvas fill with a hairline; accent variant in blue on the wash, caution variant in amber on the amber wash with no border. Chips that act as buttons darken border and text on hover.
- **Kbd:** a 5px keycap with a 2px bottom border, 11px medium muted text, shown only where a keyboard is likely.

### Inputs
8px corners, strong hairline border, 34px minimum height. Hover darkens the border to muted; focus turns the border blue with a 3px action-wash halo. On phones they grow to 16px text and 42px height.

### Keyboard model
`/` focuses search from anywhere. The list holds one roving tab stop; arrow keys move between rows (and carry an open detail to the next row), Enter opens, Esc closes. Every interactive element shows a 2px blue focus ring with a 2px offset (inset on rows).

## Do's and Don'ts

### Do:
- **Do** keep our estimate and the Wall St. average in separate, labelled columns with separate sorts, and keep `#` as our rank.
- **Do** put our base-case price target ahead of market cap wherever both appear; market cap is supporting detail.
- **Do** draw every range bar on the one shared scale, with the ghost ring for last week's base case.
- **Do** use tabular figures for every number and Inter for every word.
- **Do** keep panels at 12px corners, inner cards at 10px, controls at 8px and pills at 999px, with 1px hairlines and the rest shadow.
- **Do** show the disclaimer ("Research output, not investment advice") in both the lede and the footer.
- **Do** put depth behind disclosure (row detail, "Show N more", "Weighting checks") instead of removing it.
- **Do** gate every movement behind `prefers-reduced-motion: no-preference`.

### Don't:
- **Don't** use green or red for anything but gain and loss and their direct analogues, and never as a solid fill.
- **Don't** use blue for decoration; it marks action, selection, sort and the current place.
- **Don't** blend our estimate and the Street into one number or one sort.
- **Don't** add neon colour, glowing effects or a dark casino mood; dark mode is a near-black canvas with raised panels and the same restraint.
- **Don't** add a second typeface, uppercase eyebrow labels or kicker text above headings.
- **Don't** squeeze the desktop table onto a phone; use the stacked list.
