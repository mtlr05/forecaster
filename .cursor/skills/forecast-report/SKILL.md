---
name: forecast-report
description: >-
  Use after producing a company revenue/EBITDA forecast (e.g. with the
  forecaster skill) to write the accompanying analyst-style company update
  report (markdown + PDF) in a fixed structure, number format and citation
  style, including a valuation section when a collaborative run has produced one.
---
# Forecast report

Write this report every time a forecast is produced, next to the forecast files (e.g. `forecasts/<TICKER>/report.md` and `report.pdf`). The forecast file stays the audit record; the report is the reader's document. Never change a forecast number in the report; any new arithmetic is marked "(derived)" and gets its own calculation tag.

## Voice
Sell-side analyst prose: professional and precise, but clear. Front-load the conclusion, lead with numbers, use active voice ("We forecast..."), write "vs." not "versus", be objective and acknowledge risks. No internal method shorthand in the body (no coefficient names, ladder, step numbers, scale factors as decimals); explain judgments in words. The Estimate comparison section may use the names bottom-up, top-down, calibrated top-down, and Consensus. Every table and figure is introduced by a sentence saying what to take from it.

## Structure (in this order)
Title: `<Company> (<Exchange>: <Ticker>)`, subtitle `Company Update: FY<x>E–FY<y>E Revenue and EBITDA Forecast`, then an italic note with the date, currency and units, "forecast only: no rating, price target or valuation" unless a collaborative valuation exists (then say it includes a valuation but carries no rating), and a pointer to the forecast file and the numbered-sources appendix.

1. **Estimate comparison.** **Figure 1 – Estimate comparison**, for revenue and EBITDA across the explicit years: bottom-up, top-down low and high (or the single point), calibrated top-down, Consensus, and the base for revenue and the base for EBITDA, which may differ. Show each other view divided by that metric's base, bottom-up divided by calibrated top-down, and bottom-up divided by Consensus. Ratios in the prose are words ("about 10% below Consensus"); the table may show them as 1-decimal percentages or factors. A missing view is "n/a" plus the short reason (no range, no estimate, guidance left). The numbers come only from `views` in the forecast file. Do not recompute them, except a displayed ratio already stored as `[C]`.
2. **Summary.** A `FORECAST UPDATE` header, then 3–4 `■` bullets, each a bold one-sentence conclusion that leads with the number, followed by 3–5 sentences of support. Point back to Figure 1 for which view is the base of revenue and which is the base of EBITDA. Then **Figure 2 – Financial summary**: revenue, growth, gross margin, EBITDA, EBITDA growth and margin for 2 actual years plus the forecast years.
3. **Business Description and Reporting Lines.** What the company does, then each reporting line and its key products: what each one is, where it's sold, how the company earns from it (direct sales, royalty, licence), and its share of revenue. **Figure 3** shows revenue by line for the last full year. Discuss a royalty, license, earn-out, or similar contingent payment whenever the filing or the call states an amount, a formula, or a trigger and the item is large enough to discuss. That discussion is a subsection of the line that holds the dollars, or its own section when the item is reported separately or a line subsection would bury it. Cover what it is, who pays, what triggers it, the term, how it is earned, its share of revenue when known, and whether the base case includes the dollars. Name the line that holds the dollars. Discuss each product still in development that management names, as a subsection of the line that will hold it, or as its own section when a subsection would bury it. Cover what it is, the stated timing, any stated amount, and whether the explicit years already include it.
4. **Management.** The CEO's background, tenure and title, prior roles, ownership, and track record on capital allocation, deals and execution. Say plainly where the record is thin.
5. **Key Developments.** Dated recent events (deals, launches, approvals, guidance, financing, buybacks, legal) in **Figure 4**, plus a short commentary on what matters.
6. **Business Drivers by Line.** Volume vs. price where possible. A contingent payment, and a product still in development, use the same placement as in Business Description: a subsection of the line that holds the dollars, or its own section.
7. **Risks.** Company-specific, then industry and regulatory, 2–3 sentences each, sized where possible.
8. **Forecast.** First *How the evidence becomes the numbers*: prose plus **Figure 5 – Evidence → assumption → forecast impact**, mapping each development, driver and risk to the assumption it sets and its effect on the numbers. Point back to Figure 1 for the four views, which view is the base of each metric, and any gap between the bottom-up build and that base. Name a one-time adjustment, or an incremental-margin or next-period-growth judgment, that rests on the history window. Name M&A costs treated as one-time, and say whether integration costs remain in the short-term cost base and when they come out. Say whether the explicit window was extended because an unlaunched product's impact is well enough understood, and name the effect on next-period growth (gsnext) and incremental margin (mc), or say the pipeline was considered and did not move them. Then *Base case*: **Figure 6 – Base case by line**, with revenue by line, the total, growth, EBITDA and margin for the actual years (including the latest partial period if it's used) and each forecast year.
9. **Valuation (only for a collaborative run).** Skip this section, and keep the "no valuation" note in the title block, when no collaborative result exists. When one does, use only numbers from `valuation_result`. Do not recompute a value. Mark any arithmetic of your own "(derived)" with a C tag. Open the section with the raw value per share, the adjusted value only when the request has a post-run factor (raw and adjusted side by side, tagged `[P]` with the user's date), every prompt input tagged `[P]` with its date, the defaults that were filled, sanity flags and validation warnings in the result's own words, the fetched market inputs, and the Finagle commit. Then cover, in this order:
   - **Method.** In prose: Finagle discounts free cash flow to equity at the cost of equity, takes the explicit revenue and EBITDA as given, extends them to its horizon using the starting margin, incremental margin (mc) and next-period growth (gsnext) fading to terminal growth, and adds a terminal value. Say how many years are explicit and how many Finagle extends, that terminal growth is Finagle's default (never set by us), and how negative cash flow is treated.
   - **Figure 8 – Valuation inputs.** One column per case: cost of equity, cost of debt, tax rate, terminal growth, shares, price, debt and cash, starting margin, mc, gsnext, and Finagle's terminal WACC. Each row says whether it's a Finagle default, a forecast-file input or a judgment, and gets tags. Explain in prose how each judgment input was chosen.
   - **Figure 9 – Value bridge.** Per case: the present value of explicit-period cash flows, the terminal value and its share of the total, firm value, less debt, plus cash, equity value, and value per share vs. the current price (% upside or downside).
   - **Figure 10 – Finagle valuation table, base case.** Mirror the "report" sheet of Finagle's Excel template (`company_template.xlsx`): a header block (ticker, price, shares, rates, terminal growth), then one column per year from the last actual year to the end of Finagle's horizon, with rows for revenue, EBITDA, SBC, interest, pre-tax income, NOL, cash taxes, capex, M&A, working capital, debt change, FCF, FCFE, FCFF, firm value, debt, EV, equity, cash, FCF per share, dividend, WACC and value per share. Add discount-factor and PV rows only if marked derived. Print Finagle's values as output; flag oddities (e.g. a sign flip) in a note instead of correcting them. **Figure 11** gives the key rows for bull and bear.
   - **Figure 12 – Sensitivity.** Include this figure only when the user asks for another run. Value per share when one input moves at a time (e.g. cost of equity ±1 pt, mc ±10 pts, gsnext ±5 pts). The numbers come from that run's result file.
   - **Figure 13 – Scenarios vs. price.** Bull, base and bear values per share against the price, with one sentence on what drives the spread.
   - **Caveats.** Name what the valuation leaves out or overstates: unmodelled dilution or funding when cash goes negative, unweighted approval or event assumptions, dependence on the terminal value, financing terms not modelled, and anything else specific. Draw no rating or price target unless asked.
   Use landscape pages in the PDF if the year-by-year tables don't fit in portrait.

Appendices:
- **A – Bull and Bear Cases.** **Figure 7** shows the scenarios from the forecast file only. Explain what differs and why, and label any story the forecast file doesn't support as qualitative.
- **B – Numbered sources** (citation style below).
- **C – Method.** A short plain description of how the forecast was built (the forecaster skill's method). State that bottom-up, top-down, calibrated top-down, and Consensus are recorded and that revenue and EBITDA each have their own base, which may differ. State the history window in one or two sentences: at least nine reported quarters and their transcripts, where the documents exist, used for one-time items and for the inputs past the explicit years. When a quarter has no call, the earnings press release is the call material, and the window is not short for that reason alone. M&A-related costs are one-time unless the company says they continue. Integration costs stay only while the integration work is unfinished. An unlaunched product extends the explicit years when its impact is well enough understood, and otherwise sits in the years after that window. It is not added on top of a near-term total that already includes it.

## Numbers
- Tables: US$M (or the reporting currency) to 1 decimal, whole numbers at $100M and above. Growth and margins to 1 decimal.
- When a converted display currency is shown (e.g. CPH in USD while consensus is in CAD), use the same cited conversion rate as the forecast file.
- Prose: about 3 significant figures for dollar amounts, whole percentages, margin changes in bps.
- Per share to 2 decimals, multiples to 1 decimal with an x.
- Years marked A or E (FY2025A, H2 2026E).
- Ratios and factors go in words ("about 10% below Consensus").
- Use the same figure in prose and tables. Add "May not sum due to rounding" under any table whose rounded parts don't add up.
- Full precision lives only in Appendix B and the forecast file.
- Every figure has a caption `**Figure N – Title**` and an italic `*Source: ...*` line with its tags.

## Citations
- **Inline:** every factual or numeric claim ends with bracketed tags placed just before the full stop, e.g. `... converted from CAD [G1][E1][C3].` No footnotes.
- **Tag letters:** A = actuals, G = guidance and management statements, E = estimates (consensus), S = assumptions and judgments, C = calculations, P = figures or instructions supplied in the prompt, D = documents. Reuse the forecast file's tags verbatim, and number new ones after them.
- **Appendix B, "Numbered sources":** grouped Documents → Actuals → Guidance and management statements → Estimates → Assumptions → Calculations → Not verified.
  - Document entries: **D#**, then publisher, title (contents), date, then a colon and the raw URL, with a note such as "(HTML; no page numbers)". URLs appear only here.
  - Fact entries: bold tag, the quoted source text, then the document and page (e.g. "D2, p.8"). Calculation entries give the formula with the input tags.
  - Anything without a verified link, page or date is marked "link unverified", "page unverified" or "date unknown" and listed under Not verified.

## PDF layout: no table breaks across pages
- Keep every table on one page together with its Figure caption, any sub-label and its Source line: wrap caption + table + Source in a block (e.g. `div.fig`) styled `break-inside: avoid; page-break-inside: avoid`, with `break-after: avoid` on the caption, `thead {display: table-header-group}` and `tr {break-inside: avoid}`.
- For tables too long for one page, split them into logical blocks (e.g. year ranges), each with its own label, and use a smaller font (about 6pt) for tables over about 24 rows, rather than letting a table break mid-way.
- After rendering, check page by page that no table appears on two pages, and fix it before delivering.

## Finish
Render a PDF beside the markdown (e.g. with weasyprint, applying the layout rules above). Check that every forecast number matches the forecast file, that every valuation number matches the result file, that every claim has a tag, that every tag resolves in Appendix B, and that no table breaks across pages. Then report the path and anything you couldn't source.
