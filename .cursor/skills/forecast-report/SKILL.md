---
name: forecast-report
description: >-
  Use after producing a company revenue/EBITDA forecast (e.g. with the
  forecaster skill) to write the accompanying analyst-style company update
  report (markdown + PDF) in a fixed structure, number format and citation
  style, including a Finagle valuation section when Finagle has been run.
---
# Forecast report

Write this report every time a forecast is produced, next to the forecast files (e.g. `forecasts/<TICKER>/report.md` and `report.pdf`). The forecast file stays the audit record; the report is the reader's document. Never change a forecast number in the report; any new arithmetic is marked "(derived)" and gets its own calculation tag.

## Voice
Sell-side analyst prose: professional and precise, but clear. Front-load the conclusion, lead with numbers, use active voice ("We forecast..."), write "vs." not "versus", be objective and acknowledge risks. No internal method shorthand in the body (no coefficient names, ladder, step numbers, scale factors as decimals); explain judgments in words. Every table and figure is introduced by a sentence saying what to take from it.

## Structure (in this order)
Title: `<Company> (<Exchange>: <Ticker>)`, subtitle `Company Update: FY<x>E–FY<y>E Revenue and EBITDA Forecast`, then an italic note with the date, currency and units, "forecast only: no rating, price target or valuation" unless a Finagle valuation exists (then say it includes a Finagle valuation but carries no rating), and a pointer to the forecast file and the numbered-sources appendix.

1. **Summary.** A `FORECAST UPDATE` header, then 3–4 `■` bullets, each a bold one-sentence conclusion that leads with the number, followed by 3–5 sentences of support. Then **Figure 1 – Financial summary**: revenue, growth, gross margin, EBITDA, EBITDA growth and margin for 2 actual years plus the forecast years.
2. **Business Description and Reporting Lines.** What the company does, then each reporting line and its key products: what each one is, where it's sold, how the company earns from it (direct sales, royalty, licence), and its share of revenue. **Figure 2** shows revenue by line for the last full year.
3. **Management.** The CEO's background, tenure and title, prior roles, ownership, and track record on capital allocation, deals and execution. Say plainly where the record is thin.
4. **Key Developments.** Dated recent events (deals, launches, approvals, guidance, financing, buybacks, legal) in **Figure 3**, plus a short commentary on what matters.
5. **Business Drivers by Line.** Volume vs. price where possible.
6. **Risks.** Company-specific, then industry and regulatory, 2–3 sentences each, sized where possible.
7. **Forecast.** First *How the evidence becomes the numbers*: prose plus **Figure 4 – Evidence → assumption → forecast impact**, mapping each development, driver and risk to the assumption it sets and its effect on the numbers, including where totals come from (guidance, consensus or the line build) and any gap between the line build and the totals. Then *Base case*: **Figure 5 – Base case by line**, with revenue by line, the total, growth, EBITDA and margin for the actual years (including the latest partial period if it's used) and each forecast year.
8. **Valuation (only when Finagle has been run).** Skip this section, and keep the "no valuation" note in the title block, when no Finagle run exists. When one does, use only Finagle's output (`run_case` results, its notebook code and its filled template); never revalue by hand. Mark any arithmetic of your own "(derived)" with a C tag. Cover, in this order:
   - **Method.** In prose: Finagle discounts free cash flow to equity at the cost of equity, takes the explicit revenue and EBITDA as given, extends them to its horizon using the starting margin, incremental margin (mc) and next-period growth (gsnext) fading to terminal growth, and adds a terminal value. Say how many years are explicit and how many Finagle extends, that terminal growth is Finagle's default (never set by us), and how negative cash flow is treated.
   - **Figure 7 – Valuation inputs.** One column per case: cost of equity, cost of debt, tax rate, terminal growth, shares, price, debt and cash, starting margin, mc, gsnext, and Finagle's terminal WACC. Each row says whether it's a Finagle default, a forecast-file input or a judgment, and gets tags. Explain in prose how each judgment input was chosen.
   - **Figure 8 – Value bridge.** Per case: the present value of explicit-period cash flows, the terminal value and its share of the total, firm value, less debt, plus cash, equity value, and value per share vs. the current price (% upside or downside).
   - **Figure 9 – Finagle valuation table, base case.** Mirror the "report" sheet of Finagle's Excel template (`company_template.xlsx`): a header block (ticker, price, shares, rates, terminal growth), then one column per year from the last actual year to the end of Finagle's horizon, with rows for revenue, EBITDA, SBC, interest, pre-tax income, NOL, cash taxes, capex, M&A, working capital, debt change, FCF, FCFE, FCFF, firm value, debt, EV, equity, cash, FCF per share, dividend, WACC and value per share. Add discount-factor and PV rows only if marked derived. Print Finagle's values as output; flag oddities (e.g. a sign flip) in a note instead of correcting them. **Figure 10** gives the key rows for bull and bear.
   - **Figure 11 – Sensitivity.** Value per share when one input moves at a time (e.g. cost of equity ±1 pt, mc ±10 pts, gsnext ±5 pts), using Finagle reruns only.
   - **Figure 12 – Scenarios vs. price.** Bull, base and bear values per share against the price, with one sentence on what drives the spread.
   - **Caveats.** Name what the valuation leaves out or overstates: unmodelled dilution or funding when cash goes negative, unweighted approval or event assumptions, dependence on the terminal value, financing terms not modelled, and anything else specific. Draw no rating or price target unless asked.
   Use landscape pages in the PDF if the year-by-year tables don't fit in portrait.

Appendices:
- **A – Bull and Bear Cases.** **Figure 6** shows the scenarios from the forecast file only. Explain what differs and why, and label any story the forecast file doesn't support as qualitative.
- **B – Numbered sources** (citation style below).
- **C – Method.** A short plain description of how the forecast was built (the forecaster skill's method).

## Numbers
- Tables: US$M (or the reporting currency) to 1 decimal, whole numbers at $100M and above. Growth and margins to 1 decimal.
- Prose: about 3 significant figures for dollar amounts, whole percentages, margin changes in bps.
- Per share to 2 decimals, multiples to 1 decimal with an x.
- Years marked A or E (FY2025A, H2 2026E).
- Ratios and factors go in words ("about 10% below consensus").
- Use the same figure in prose and tables. Add "May not sum due to rounding" under any table whose rounded parts don't add up.
- Full precision lives only in Appendix B and the forecast file.
- Every figure has a caption `**Figure N – Title**` and an italic `*Source: ...*` line with its tags.

## Citations
- **Inline:** every factual or numeric claim ends with bracketed tags placed just before the full stop, e.g. `... converted from CAD [G1][E1][C3].` No footnotes.
- **Tag letters:** A = actuals, G = guidance and management statements, E = estimates (consensus), S = assumptions and judgments, C = calculations, D = documents. Reuse the forecast file's tags verbatim, and number new ones after them.
- **Appendix B, "Numbered sources":** grouped Documents → Actuals → Guidance and management statements → Estimates → Assumptions → Calculations → Not verified.
  - Document entries: **D#**, then publisher, title (contents), date, then a colon and the raw URL, with a note such as "(HTML; no page numbers)". URLs appear only here.
  - Fact entries: bold tag, the quoted source text, then the document and page (e.g. "D2, p.8"). Calculation entries give the formula with the input tags.
  - Anything without a verified link, page or date is marked "link unverified", "page unverified" or "date unknown" and listed under Not verified.

## PDF layout: no table breaks across pages
- Keep every table on one page together with its Figure caption, any sub-label and its Source line: wrap caption + table + Source in a block (e.g. `div.fig`) styled `break-inside: avoid; page-break-inside: avoid`, with `break-after: avoid` on the caption, `thead {display: table-header-group}` and `tr {break-inside: avoid}`.
- For tables too long for one page, split them into logical blocks (e.g. year ranges), each with its own label, and use a smaller font (about 6pt) for tables over about 24 rows, rather than letting a table break mid-way.
- After rendering, check page by page that no table appears on two pages, and fix it before delivering.

## Finish
Render a PDF beside the markdown (e.g. with weasyprint, applying the layout rules above). Check that every forecast number matches the forecast file, that every valuation number matches Finagle's output, that every claim has a tag, that every tag resolves in Appendix B, and that no table breaks across pages. Then report the path and anything you couldn't source.
