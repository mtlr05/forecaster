# CLPT / Parkinson's analysis — handoff note

**Purpose.** ClearPoint Neuro (CLPT) forecast and Finagle valuation, driven mainly by procedure revenue from one-time CED-delivered gene and cell therapies (Parkinson's class, Huntington's AMT-130), with a partner-program appendix and a Parkinson's (PD) patient-pool model.

**Status (2026-10-25, v10).** Value per share (Finagle `run_case`): **base $54.29, bull $72.68, bear $16.72** vs. a $9.25 price. Scenario values, not a target. Nothing here has been confirmed as final; see open items.

## Agreed base-case decisions
| Decision | Setting | Rationale / tag |
|---|---|---|
| PD eligible pool | ~180k = 1.104M US PD × 0.45 (≥4 yrs duration) × 0.50 (motor complications) × 0.806 (levodopa-responsive idiopathic proxy: clinical-diagnosis accuracy) × 0.90 (fit for surgery) | Label-style eligibility, following the DBS label. Already-DBS patients stay eligible (DBS and one-time therapy are not mutually exclusive). David's decision. |
| Bear pool | ~138k, trial-style exclusion of prior-DBS patients | Trial criteria are the bear case only. |
| Treated share | 6% of pool, one-time therapy alone; DBS modelled separately | David's judgment: ~2.9% (2.2% alt. measure) get DBS today, and many more would favour a disease-modifying gene therapy. |
| Lumping | Demand and valuation at PD class level, not bemdaneprocel alone | David's decision. |
| ClearPoint platform share | 100% | David's assumption: sponsors will not risk a multi-billion-dollar therapy to save on a cannula not used in the trial. Note: ClearPoint's 10-K names Brainlab and Renishaw offerings as competitive. |
| Ramp | 1/3, 2/3, full demand over FY2029E–FY2031E | David's reasoning: gives time for other therapies to be approved. Other PD launches (FY2033–34E) fall after the ramp ends, so this is a judgment. Implies ~74 centres (~94 incl. AMT-130) — flagged aggressive vs. management's 20–30. |
| Base volume | 3,919 / 7,594 / 11,126 procedures FY29–31E; revenue $231M / $320M / $410M | Class demand ~11.8k/yr at launch, drifting to ~11k. |
| Bull | 8% of pool, same ramp (~14k/yr) | **Not yet confirmed** (earlier request was a bull reaching 10k/yr). |
| Bear | Exclusion pool ~138k (demand ~8.4k/yr), capped at 4,500/yr capacity | |
| Huntington's | AMT-130 3,000/yr steady state [S30] | Unchanged; no HD revision agreed. |
| Perpetuity yardstick | +$20M/yr procedure revenue adds $2.69/share from FY2030E ($2.29 from FY2032E) | Finagle run (`finagle_perpetuity.*`). |
| Finagle artifact | gsnext fades from the last explicit growth, so one-year volume steps near the window end inflate value | Keep volumes at steady state by the last explicit year. |

## Process rules
Single base case first; no sensitivity until the base is agreed. Lean models, nested funnels, anchored on published statistics. Tag (A/G/E/S/C/D) and cite every number with a linked sources appendix. Value only through Finagle `run_case`; never set terminal growth (gt). Prompt estimates override defaults. Reports self-contained (no version references); tables never split across pages. Plan review before larger analysis changes. **finagle and ceochat are read-only inputs.**

## Open items
1. Confirm bull at 8% of pool.
2. Rerun valuation at 12–13% cost of equity.
3. Sources list: A41–A43 and D71–D76 out of order.
4. `partners/partners_v4.md` has no PDF/Word version.
5. Epilepsy, FTD and glioblastoma funnels not rebuilt with the pool method.
6. Platform-share sensitivity: each 1,000 procedures/yr ≈ $2.58/share.
7. Motor-complication 50% and fitness 90% are judgments; a published share of PD patients with motor complications at 5–10 yrs would firm up the 50%.

## File map
- `report.md/.pdf/.docx` — current company report (PDF via `render_report.py`, Word via `tools/md2docx.py`).
- `build_forecast.py` → `forecast.md/.json`, `CLPT_base/bull/bear.xlsx`; `run_finagle.py`, `finagle_*.py/.json` — valuation runs.
- `revision_log.md` — every line change with reason.
- `partners/pd_simple4_*` — current PD model (`pd_simple4_model.py`, explanation md/pdf/docx, xlsx, chart).
- `partners/partners_v4_*` — current partner table (`partners_v4_model.py`).
- `partners/ce_delivery_notes.md`, `dbs_exclusivity_notes.md`, `pd_research_notes.md` — research notes.
- Older versions (`pd_simple*`, `pd_pool_*`, `partners_v2/v3`) kept for history only.

## How to resume
From `forecasts/CLPT/`: `python partners/pd_simple4_model.py` → `python partners/partners_v4_model.py` → `python build_forecast.py` → `python run_finagle.py` → `python render_report.py` (PDF) and `python ../../tools/md2docx.py report.md report.docx` (Word). Requires a local finagle checkout (read-only).
