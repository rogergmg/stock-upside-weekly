---
name: Stock Upside Weekly
description: A weekly ledger of 12-month upside for US stocks above $50B, independent and Street views kept apart.
colors:
  ledger-cobalt: "#1d5bbf"
  cobalt-wash: "#e3ecfa"
  gain-green: "#11805b"
  loss-red: "#c0392b"
  caution-ochre: "#9a6300"
  caution-wash: "#fbf0d9"
  ink: "#13202c"
  slate-muted: "#5a6a7b"
  rule-line: "#d9e0e8"
  paper: "#f4f6f9"
  sheet: "#ffffff"
  sunk: "#eaeef3"
  dark-ledger-cobalt: "#74a6ff"
  dark-cobalt-wash: "#1b2a42"
  dark-gain-green: "#3fcf8e"
  dark-loss-red: "#ff7b6c"
  dark-caution-ochre: "#e2a63c"
  dark-caution-wash: "#2e2512"
  dark-ink: "#e5ecf3"
  dark-slate-muted: "#93a3b4"
  dark-rule-line: "#26323f"
  dark-paper: "#0d131a"
  dark-sheet: "#141c25"
  dark-sunk: "#1a2430"
typography:
  display:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(26px, 4vw, 36px)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.2
  title:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  label:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    letterSpacing: "0.05em"
rounded:
  xs: "3px"
  sm: "5px"
  md: "6px"
  lg: "8px"
  full: "99px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "22px"
components:
  pill-gain:
    backgroundColor: "color-mix(in srgb, {colors.gain-green} 14%, transparent)"
    textColor: "{colors.gain-green}"
    rounded: "{rounded.sm}"
    padding: "2px 7px"
  pill-loss:
    backgroundColor: "color-mix(in srgb, {colors.loss-red} 14%, transparent)"
    textColor: "{colors.loss-red}"
    rounded: "{rounded.sm}"
    padding: "2px 7px"
  chip:
    backgroundColor: "{colors.sunk}"
    textColor: "{colors.slate-muted}"
    rounded: "{rounded.full}"
    padding: "1px 7px"
  chip-accent:
    backgroundColor: "{colors.cobalt-wash}"
    textColor: "{colors.ledger-cobalt}"
    rounded: "{rounded.full}"
    padding: "1px 7px"
  chip-caution:
    backgroundColor: "{colors.caution-wash}"
    textColor: "{colors.caution-ochre}"
    rounded: "{rounded.full}"
    padding: "1px 7px"
  highlight-card:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "12px 14px"
  table-box:
    backgroundColor: "{colors.sheet}"
    rounded: "{rounded.lg}"
  table-header:
    backgroundColor: "{colors.sunk}"
    textColor: "{colors.slate-muted}"
    typography: "{typography.label}"
    padding: "8px 10px"
  input-field:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "7px 9px"
  tab:
    textColor: "{colors.slate-muted}"
    padding: "10px 12px"
  tab-selected:
    textColor: "{colors.ink}"
---

# Design System: Stock Upside Weekly

## Overview

**Creative North Star: "The Weekly Ledger"**

The page is a ledger of names you scan line by line once a week. Numbers come first and decoration hardly appears. Hairline rules separate the rows, tabular figures line up the columns, and change is marked in the margin with small coloured pills, not loud fills. The ledger is dense on desktop: an eleven-column table of sortable, ruled rows. On a phone it becomes a stack of entries, each with a ticker, the company name, one pill and one small to-scale drawing.

Calm and sourced is the attitude. Every figure carries its basis (our model, named analysts or the provider aggregate), and the design makes those bases look different so they're never blended. Colour means something here: green and red mean gain and loss, ochre means caution, and cobalt marks what you can act on or what is selected. Anything else stays a cool neutral.

**Key Characteristics:**
- Dense, ruled and tabular: the page is the table.
- Cool slate neutrals tinted toward the cobalt accent; no pure greys.
- Semantic colour only: gain, loss, caution and an action or selection accent.
- Every chart is drawn to one shared scale per row type, so rows compare.
- Both light and dark themes, defined as tokens; dark is a separate palette, not an inversion.

## Colors

A cool ledger palette: blue-tinted slate paper, ink text, and one cobalt accent that marks action and selection.

### Primary
- **Ledger Cobalt** (`ledger-cobalt`): the selected tab underline, the sorted column header, links, focus rings, the weighted-target marker on target strips, hover borders on highlight cards and the "as of" chip. **Cobalt Wash** (`cobalt-wash`) is its tint, used behind the selected row, accent chips and the scenario-range band.

### Semantic
- **Gain Green** (`gain-green`): positive returns, target raises, upgrades and the bull-case end of a strip.
- **Loss Red** (`loss-red`): negative returns, target cuts, downgrades and the bear-case end of a strip.
- **Caution Ochre** (`caution-ochre`) on **Caution Wash** (`caution-wash`): the disclaimer, "stale" and "unverified" chips, and calls kept out of the weighted target.

### Neutral
- **Ink** (`ink`): primary text and figures.
- **Slate Muted** (`slate-muted`): secondary text, column labels and footnotes.
- **Rule Line** (`rule-line`): hairline borders and row dividers.
- **Paper** (`paper`): the page background.
- **Sheet** (`sheet`): tables, cards and inputs.
- **Sunk** (`sunk`): table headers, row hover and neutral chips.

Each token has a `dark-` counterpart for the dark theme. Tokens are defined on `:root`, then redefined under `prefers-color-scheme: dark` (guarded by `:not([data-theme="light"])`) and again under `[data-theme="dark"]`.

### Named Rules
**The Meaning-Only Colour Rule.** Green and red only ever mean gain and loss, and ochre only ever means caution. Never use them as decoration or for a category.

**The Two Bases Rule.** Independent-valuation figures and provider-aggregate figures never share a sort, and every place they appear (column header, card tag or basis line) names which one it is.

## Typography

**Display Font:** Schibsted Grotesk (falling back to Helvetica Neue, Arial)
**Body Font:** Inter (falling back to system-ui)

**Character:** Schibsted Grotesk appears in only a few places: the page title, card headline figures and section titles. Inter does everything else, with tabular numerals so columns align.

### Hierarchy
- **Display** (800, clamp 26–36px, −0.02em): the page title only.
- **Headline** (700, 20px): the ticker or figure on highlight cards and scenario case targets.
- **Title** (700, 14px): section titles in the detail panel ("Analyst timeline", "Sources").
- **Body** (400, 14px, 1.5): running text, table cells and list rows. Prose lines stay at 72–90 characters.
- **Label** (600, 11px, +0.05em, uppercase): table column headers only.

### Named Rules
**The Tabular Rule.** Any column, pill or stat that holds digits uses tabular numerals (`font-variant-numeric: tabular-nums`).

**The No-Eyebrow Rule.** No small uppercase label sits above a heading. Headings carry their own weight, and context goes in a chip beside the heading or a sentence below it.

## Layout

There is one centred column, up to 1240px wide. The side gutter is `max(16px, safe-area inset)`, with 28px of padding above and 56px below. Sections stack on a 22px gap in this order:
1. header (title row with the "as of" chip, then the description and the disclaimer);
2. a one-line count strip ruled top and bottom;
3. four highlight cards;
4. tabs;
5. filters;
6. the active panel;
7. the footer.

- **Responsive:** highlight cards drop from 4 columns to 2 below 900px. Below 720px, each ranking table becomes a stacked list, the filters become a two-column grid with search spanning both, and the detail panel's two key-value columns collapse to one.
- **Overflow:** grid containers use `minmax(0, 1fr)` columns and `min-width: 0` children, so a wide table scrolls inside its own box and the page never scrolls sideways.
- **Expanded rows:** on desktop, the expanded detail is pinned to the visible width of the table's scroll box.

## Elevation & Depth

Flat and ruled. Depth comes from tone (paper, then sheet, then sunk) and 1px rule lines, not shadows. The one shadow appears in response to state: a soft cobalt-tinted lift under a highlight card on hover.

### Shadow Vocabulary
- **Hover lift** (`0 2px 10px -4px` of cobalt at 35%): highlight cards on hover only.

### Named Rules
**The Flat-at-Rest Rule.** Nothing is lifted at rest. If an element needs separation, give it a rule line or a tone step.

## Shapes

Corners are gently rounded and stay small:
- 8px on containers (table boxes, highlight cards, the phone list);
- 6px on inputs;
- 5px on pills and timeline action icons;
- full round on chips.

Borders are 1px rule lines. Scenario bars and target strips use round-capped lines and dots on a dashed zero line. Never use a coloured border thicker than 1px.

## Components

### Return pills
Short, tinted and unmissable. They show signed percentages with a typographic minus, one decimal, and never wrap. The tint is 14% of the gain or loss colour, with text in the full colour.

### Chips
Small rounded tags for status and counts: neutral (`chip`), accent for coverage or research labels (`chip-accent`) and caution for stale or unverified (`chip-caution`).

### Highlight cards
Four clickable summaries above the tabs. Each shows the card's label, the ticker in headline type, a pill, the company name truncated with an ellipsis, and a basis tag. On hover the border turns cobalt and the card lifts. Clicking one opens that row or filters the other tab to it.

### Tables
Tables sit in a sheet-coloured box with a sticky sunk header row. Sortable headers show an arrow and turn cobalt on the active sort. Rows highlight on hover; an expanded row gets the cobalt wash. The leftmost # column always shows the official rank, even after a re-sort.

### Phone list rows
Each row has three columns: rank, then ticker and name, then the pill. A second line shows the scenario bar or target strip with its caption. Tapping toggles the row's detail open and closed.

### Scenario bar (signature)
A 170px SVG drawn on one shared −60% to +100% scale: a dashed zero line, a cobalt-wash band from bear to bull, and a gain- or loss-coloured dot at the base case. Because every row uses the same scale, rows can be compared.

### Target strip (signature)
A round-capped line from the low target to the high target, with a red dot at the low end, a green dot at the high end, a hollow cobalt ring at the average and an ink tick at the close. A wide version labels the low and high values.

### Analyst timeline
Each row is one action per analyst and date. Action icons are drawn SVG arrows or dots in a tinted 20px square. Ratings show as "prior → new" and targets as "$prior → **$new**" with the % change. A sunk divider row marks the last earnings release.

### Inputs and tabs
Inputs are sheet-coloured with a 1px rule border and 6px radius, with a cobalt focus ring. Tabs are text buttons with a 2px cobalt underline on the selected tab and show their count in parentheses.

## Do's and Don'ts

### Do:
- **Do** label every number's basis (our model, named analysts or the provider aggregate) in its header, tag or basis line.
- **Do** keep negative returns, unresearched names and unverified caps visible, with a chip for their status.
- **Do** draw every row of a given chart type on one shared scale.
- **Do** style the browser's own details: text selection in cobalt wash, `accent-color` in cobalt, scrollbars in rule-line colour, and a 2px cobalt focus ring.
- **Do** switch tables to stacked lists below 720px rather than letting the page scroll sideways.

### Don't:
- **Don't** merge independent and provider-aggregate upside into one unlabelled sort.
- **Don't** use green, red or ochre for decoration.
- **Don't** add small uppercase labels above headings, numbered section markers, or Unicode or emoji glyphs as icons. Use drawn SVG.
- **Don't** lift elements with shadows at rest.
- **Don't** put display type in labels, buttons or table data.
