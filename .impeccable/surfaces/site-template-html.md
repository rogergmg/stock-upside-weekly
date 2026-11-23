---
version: 1
slug: "site-template-html"
primary_target: "site/template.html"
related_targets: ["site/index.html"]
---

# Surface brief: Stock Upside Weekly page (site/template.html)

**Scope and mode.** The single weekly page built into `site/index.html`. Mode: **Operate**. Desktop-first; it must also work well on a phone.

**Audience and job.** Roger reads it once a week after the Saturday refresh.
- First he wants to see **the best opportunities now**.
- Then what changed this week.
- Then the reasoning behind any number.

**Constraints.**
- PRODUCT.md binding rules.
- Our estimate and Wall St. are never combined into one number. Each is labelled and each sorts on its own column.
- Nothing is removed for the sake of simplicity. Depth goes behind disclosure instead.

**What would feel wrong:**
- trading-app hype: neon colour, a casino feel, loud green and red fills.

**Decisions made with Roger (2026-11-23).**
- Roger rejected the "strip it down" plan: "I don't want simple but better design."
- There is one list with two labelled columns, and the old tabs are gone.
- Look: the category standard, executed at the craft of **Linear** and **Stripe Dashboard**.

## Direction contract

**THESIS.** A calm, precise research dashboard. The first screen ranks the best opportunities, and every number opens its reasoning. It refuses two things: the trading-app look (neon, hype, dark casino) and the spreadsheet dump. Craft does the work: alignment, type and restraint.

**OWN-WORLD.**
- **Surfaces:** a cool grey canvas (#f6f7f9) under white panels, with 1px #e3e8ee borders, 12px radii and soft two-layer shadows.
- **Ink and accent:** slate ink (#0f172a) with a single blue accent (#2563eb) for actions, selection and sort.
- **State colours:** green and red appear only as gain and loss, as tinted pills or text.
- **Type:** Inter with tabular figures. Headings are semibold with tight tracking.
- **Controls:** keyboard affordances (`/` to search, arrows to move, Esc to close) are shown as small kbd chips.
- **Dark theme:** a near-black canvas (#0b0e14) with raised panels.

**STORY.**
1. Roger sees the five highest-upside names at a glance, each with its range and Wall St.'s view.
2. He scans the whole ranked list, with this week's changes beside it.
3. He opens any row to read the bear, base and bull reasoning, the analyst evidence and the sources.

**FIRST VIEWPORT.**
- **Top bar (sticky, 64px):** brand mark and name on the left; in-page nav (Top upside, All stocks, This week, Methodology) in the centre; "Prices as of …" on the right (theme follows the artifact viewer; no page-level switch).
- **Header:** "Top upside" at 24px semibold, with a one-line basis and disclaimer under it.
- **Cards:** a row of five top-upside cards. Each holds the ticker and rank, the name, the big base-case figure, "from X last week", and a range bar on the shared scale with a ghost ring for last week. Wall St. sits on a ruled footer row.
- **Below the cards:**
  - the "All 294 stocks" table panel on the left: search with a `/` hint, a sector filter, and a sticky sortable header;
  - a sticky "This week" panel on the right.

**FORM.** The canon (category standard), chosen over the dealt Share Certificate direction. Its craft bar is Linear and Stripe Dashboard. seed: seed:79118e55235bf58e

**FINISH.** unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
