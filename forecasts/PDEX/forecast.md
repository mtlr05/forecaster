# PDEX forecast audit summary — v4

# PDEX v3 → v4 revisions

7 November 2026, America/Toronto. All amounts US$M; full precision in JSON.

|Case|Year|Revenue before|After|EBITDA before|After|
|---|---|---|---|---|---|
|base|FY27E|82.700000|82.700000|15.621463|15.493111|
|base|FY28E|86.800000|86.800000|16.615498|16.513840|
|bull|FY27E|84.700000|85.047080|17.158500|17.122411|
|bull|FY28E|89.300000|92.117174|18.363020|19.783539|
|bear|FY27E|78.700000|78.292830|13.181000|12.918977|
|bear|FY28E|77.300000|70.723394|12.410520|10.165616|

Base revenue remains consensus; Monogram is now 0.307M/6.212M inside it, sized to the second-customer band. Own build 82.617170/89.278766M. High Monogram 1.054250/9.978780M, low 0.050000/0.085000M; Helios separate. Base EBITDA is the cost build, with the larger FY28 Monogram allocation inside consensus. No whole-robot or sourced-disposable gross bill counted as PDEX sales; no CVR operating revenue.

History, year zero, and capex method 1 are retained. Next-year growth is the FY29 continuation of the FY28 cohort. Finagle v02 is in `collab/valuation_result_v02.json`. See the report for the evidence, `robotics_model.csv` for the arithmetic, and `revision_log.md` for the earlier line changes.

The self-contained narrative and sources are report.md/report.pdf. Forecast.json is authoritative. David authorized reasoned robotics estimation; unverified pricing/volumes are explicit analyst assumptions, not optional unintegrated sensitivities. Validation results saved separately.

## Status and open items

Version 4, rank rebuild 8 November 2026. Base case: FY27E revenue 82.700 and EBITDA 15.493111; FY28E revenue 86.800 and EBITDA 16.513840. Revenue base is consensus; EBITDA base is the cost build. Bull FY28E revenue 92.117174 and EBITDA 19.783539; bear FY28E revenue 70.723394 and EBITDA 10.165616. Full precision is in `forecast.json`. The reader document is `report.md` and `report.pdf`. Line changes are in `revision_log.md`.

Finagle v02 is in `collab/valuation_result_v02.json`. Next-year sales growth is the FY29 continuation of the FY28 system cohort: about 0.9% base and 3.1% bull. Bear next-year growth stays −10% for the customer renewal. Incremental margin stays 25%. Unknown contract prices and customer identity remain risks.

Resume: `build_v4.py` applies the v4 robotics deltas to the retained `baseline_v3.json` beside it. It is not a from-scratch model. It writes `forecast.json`, `robotics_model.csv` and `model_results.json` in this directory. `render_report.py` renders the existing `report.md` to `report.pdf` and does not recompute forecast figures. `write_documents.py` and `check_v4.py` are not in this tree. Preserve `baseline_v3.json` unless the delta is being rerun on purpose. Numbered sources are in `report.md` Appendix B.

# Pro-Dex, Inc. (Nasdaq: PDEX)
## Company Update: FY27E–FY28E Revenue and EBITDA Forecast

*8 November 2026, America/Toronto (v4, rank rebuild). US$ millions except unit prices and operating volumes; fiscal year ends 30 June. Forecast only: no rating or price target. Finagle v02 is in `collab/valuation_result_v02.json`. Audit record: `forecast.json`; operating arithmetic: `robotics_model.csv` and `build_v4.py`. Numbered sources are in `report.md` Appendix B.*

## 1. Summary

**FORECAST UPDATE**

■ **Revenue remains $82.7M/$86.8M in FY27/FY28, and central Monogram is $0.307M/$6.21M inside those totals [E1][E2][S23].** The FY28 figure is the FY26 second-customer comparator. We keep the single-analyst revenue anchor and take the larger Monogram share out of residual core. Our own revenue build is $82.6M/$89.3M, above the FY28 anchor [C9][C10][C83][C85]. The prices are still analyst assumptions, not verified contract prices.

■ **Base EBITDA is $15.5M/$16.5M [C23][C24].** Hardware dominates the FY28 rank path, so the high-margin fee is a small part of the mix. Incremental launch support and the disclosed APM occupancy cost stay in the build [S24][S25][S26][G21].

■ **Bull FY28 revenue and EBITDA are $92.1M and $19.8M; bear is $70.7M and $10.2M [C52][C54][C71][C73].** The bull meets the annualized second-customer comparator. The bear is a missed launch, so it removes the central Monogram allocation that now sits inside the consensus base [S15][S16][S28]. The range is shipment, clearance, price, and utilization uncertainty.

■ **The contract supports both manufactured hardware and purchase-based fees, not a proven $50 royalty per surgery [G15][G16].** PDEX expects validation units in January–June 2027 and Zimmer targets a conditional launch in calendar H1 2027 [G10][G18]. Those dates can overlap only with a tight validation/clearance sequence. We therefore probability-weight central shipments, retain a no-commercial-launch bear, and exclude CVR proceeds from operating sales [S23][A38].

Figure 1 shows reported history and the revised base; historical EBITDA is not normalized.

<div class="fig" markdown="1">

**Figure 1 – Financial summary**

| US$M | FY25A | FY26A | FY27E | FY28E |
|---|---|---|---|---|
| Revenue | 66.6 [A16] | 77.5 [A17] | 82.7 [E1] | 86.8 [E2] |
| Revenue growth | 23.7% (derived) [D12] | 16.5% [C34] | 6.6% [C38] | 5.0% [C38] |
| Gross margin | 29.3% [C27] | 31.4% [C28] | 32.3% [C272] | 32.4% [C275] |
| EBITDA | 12.5 [C1] | 15.1 [C2] | 15.5 [C23] | 16.5 [C24] |
| EBITDA growth | 39.7% (derived) [D12] | 20.7% [C35] | 2.8% [C39] | 6.0% [C39] |
| EBITDA margin | 18.7% (derived) [C1][A16] | 19.4% (derived) [C2][A17] | 18.7% [C36] | 18.9% [C37] |

*Source: forecast.json; D1, D3, D12, D13. FY25 growth uses FY24 reported history. May not sum due to rounding.*
</div>
## 2. Business Description and Reporting Lines

Pro-Dex designs and manufactures autoclavable, battery-powered surgical drivers and shavers for orthopaedic, thoracic and craniomaxillofacial (CMF) device companies, mostly as a contract or co-development manufacturer, and since February 2026 also machines parts for aerospace and defence through Advanced Precision Machining (APM) [D1]. It reports one segment; we use its revenue-by-type disclosure as the lines. Figure 2 shows that medical devices are now four-fifths of sales and repairs have fallen to a sixth.

<div class="fig" markdown="1">

**Figure 2 – Revenue by line, FY26**

| Line | FY26A | Share | FY26 growth |
|---|---|---|---|
| Medical devices (orthopaedic 48.8, CMF 11.2, thoracic 2.1) | 62.1 [A6] | 80% | 30.1% [C29] |
| Industrial and scientific (incl. APM from Feb 2026) | 1.5 [A7] | 2% | 75.7% [C30] |
| NRE and prototype services | 1.7 [A8] | 2% | 136.4% [C31] |
| Repairs | 12.5 [A9] | 16% | −32.5% [C32] |
| Discounts and other (rebates) | −0.3 [A10] | 0% | n/m [C33] |
| **Total** | **77.5 [A17]** | 100% | 16.5% [C34] |

*Source: D1 p.19. May not sum due to rounding.*
</div>

**Medical devices.** Sold direct to OEMs under exclusive development and supply agreements. The largest customer's next-generation orthopaedic handpiece drove FY26 growth; the customer extended the contract through calendar 2028 with higher volumes and no volume rebates [G3][G6]. CMF drivers sell through distributors and rose 39% in Q1 FY27 [G7].

**Repairs.** Mostly repairs of the largest customer’s legacy handpiece, falling as it moves to the new model. Billable next-generation repairs start in FY27, but management does not know the volumes [G8]. The latest quarter’s repair margins are significantly lower because of expensive replacement components and labour under-utilisation; historical high margins are not a stable current annuity [G19].

**NRE and prototype services.** Billable engineering for customers, lumpy by quarter [G7].

**Industrial and scientific.** Air motors (de minimis) and APM's third-party machining [D3].

**Product pipeline.** Helios is already released for production, with interest but no guaranteed orders; commercial volumes remain uncertain; v4 now allocates a modest central sales path within the medical-device line [G9]. The June presentation also names an articulating attachment, spinal driver and shaver system, without annual revenue commitments [D20][D21]. Pipeline allocations are explicit inside the consensus total, not incremental to it [S28].

### Monogram / Zimmer Biomet: hardware, sourced-product fees and cash milestones

Zimmer completed its acquisition of Monogram on 7 October 2025; PDEX remains an independent supplier, not a Zimmer subsidiary [A37][D23][D18]. The operative 3 October 2023 supply contract, unlike the ineffective 2018 agreement, separates exclusive PDEX-manufactured end effectors and gearing from sourced burrs, saw blades and custom patient-specific implants [G16][G15]. Hardware uses cost-based pricing with a redacted target gross margin and annual adjustment; development services are time-and-materials [G16][D18]. The sourced-product fee is a redacted percentage of Monogram’s eligible purchases, payable on purchase/payment timing, not a disclosed fixed amount per completed operation; the robotic arm and navigation cameras are excluded from that basket [G15]. PDEX has no manufacturing responsibility for these sourced items, supporting a potentially capital-light fee stream, but neither a near-100% gross margin nor an EBITDA margin is disclosed [D18][S22].

The latest PDEX 10-Q expects validation units in the second half of FY27 (January–June 2027), not the article’s October–December 2026 start [G10][D17]. In June the CEO said Monogram “could definitely be customer number two” within a couple of years, but declined to quantify revenue [G17]. On 4 November, Zimmer’s CEO anticipated a surgeon-guided fully autonomous launch in calendar H1 2027, pending regulatory clearance; that statement is not a PDEX purchase order, and a 510(k) filing is not clearance [G18]. We do not map all ROSA installations or Zimmer robotic procedures into PDEX-eligible fee volumes [D23][G15].

Investment proceeds and CVRs are separate from product sales. PDEX received $8.9M for its Monogram equity and a $2.3M first milestone; the gains sit below operating income and are excluded from EBITDA [A37][A38]. Remaining contingent milestones are uncertain and cannot be added as recurring operating sales or counted again as cash already received [D1][D2].

The article’s “very likely Stryker” customer attribution is conjecture [D17]. PDEX’s own IFU index independently lists the Zimmer Biomet Atlas Pro Driver and accessories, corroborating a Zimmer product relationship, not the identity of the 78% customer [D26][A36]. The NIH record reviewed previously dates that product tie before the acquisition, but its v 3 re-fetch timed out [D19]. That concentration equals about $60.5M of FY26 revenue (derived) [C90]. Neither the supplier relationship nor discussion of Monogram separately proves or disproves whether Zimmer is the large OEM.

## 3. Management

Richard (Rick) Van Kirk is President and CEO; in June he described roughly eleven years as CEO and twenty years at PDEX, after an operations role [D21]. The capital-allocation record is long-dated: the Monogram stake returned $8.9M plus a $2.3M milestone [A37][A38]; buybacks were $3.4M in FY26 [A39]; APM was bought for vertical integration in February 2026 [D1]. The June public presentation confirms an actively staffed M&A effort [G11]. Beneficial ownership was not refreshed for this revision; no ownership-based forecast assumption is used. The record on diversification away from the largest customer is thin: that customer rose to 78% of sales [A36].

**Shareholder letters (qualitative evidence only).** We read the CEO letters at the front of the FY2022–FY2026 proxies. The FY2026 letter (filed 6 October 2026) confirms the three-year extension with the largest customer, counts "four projects in development" including Monogram/Zimmer Biomet with shipments expected this fiscal year, describes the Helios CMF driver as "ready for production" with "a number of potential customers", and says management is evaluating acquisitions [D14]. Earlier letters are short histories; the "strong year ahead" tone was followed by growth in each of the last four years, but every year in that sample was a growth year, and none flagged the later repair decline or customer concentration. The FY2025 letter cites $65M of sales against $66.6M filed; its own 24% growth matches the filed figure, so we treat $65M as loose rounding [D15][A16]. No forecast number rests on the letters.

## 4. Key Developments

Figure 3 aligns calendar launch targets with PDEX's fiscal-year recognition window; neither target is a firm purchase order.

<div class="fig" markdown="1">

**Figure 3 – Dated developments**

| Date | Evidence and relevance |
|---|---|
| 3 October 2023 | Executed exclusive supply contract: manufactured end effectors/gearing, engineering and separate eligible purchase fees [D18][D25] |
| 7 October 2025 | Zimmer acquires Monogram; PDEX remains an independent supplier [D23] |
| 17 June 2026 | PDEX CEO: Monogram “could definitely be customer number two” within a couple of years, but declines revenue expectations [G17][D21] |
| 29 October 2026 | PDEX: validation units in second half FY27 = January–June 2027; meaningful incremental sales have not yet occurred [G10][D2] |
| 30 October 2026 | New APM manufacturing space starts November 1; monthly rent $11,600 initially, then $12,064 from March 2028 [G21] |
| 4 November 2026 | Zimmer targets fully autonomous launch in H1 calendar 2027, conditional on clearance; no annual Monogram unit guidance [G18][D22] |

*Source: D18, D21, D22, D23, D28. May not sum due to rounding.*
</div>
## 5. Business Drivers by Line

**Core medical devices and repairs.** Before robotics, we retain the Q1 medical-device run rate and CMF growth assumptions. Repairs follow the existing decline; expensive replacement parts and labor under-utilization make old repair profitability an unreliable annuity [S2][S3][S8][S9][G19]. Industrial/APM stays unscaled; no intercompany manufacturing saving or acquisition speculation is added [S4][S5][A41]. Core gross-margin assumptions remain trailing experience in base, improved utilization in bull and adverse mix in bear [C4][S17][S19].

### Robotics: what is established, what we estimate

**Established rights are not volume commitments.** The 2023 contract covers autoclavable bone-milling end effectors and gearing for sagittal motion. Schedule 1 contains redacted quantity-price tiers, margin targets and cost markups; routine functional testing belongs inside hardware manufacturing cost, not a second NRE invoice [G16][D25]. The ten developed-and-validated units trigger the contract term; that clause is not a forecast minimum purchase. Requested lead time is at least 26 weeks and most forecast volumes are nonbinding [D18][D25]. We classify validation and commercial manufactured kits as medical-device hardware, engineering time as NRE, and the sourced-product fee provisionally in discounts/other operating revenue; ultimate company presentation is not disclosed [S24][S26][S28].

**Fees apply to purchases, not procedures.** Eligible purchases include burrs, saw blades and genuinely custom patient-specific implants; ordinary Persona implants do not automatically meet the custom criterion. Robotic arms, cameras, drapes and sterile packaging are excluded [G15][D25]. PDEX does not manufacture the sourced basket, so only its percentage fee—not the gross disposable purchase value—is sales. We model purchase inventory above contemporaneous utilization to allow stocking; royalty-like cash may precede use and collection need not equal revenue recognition [S25]. Full custom-implant adoption and CVRs are excluded, rather than silently adding a much larger basket [S25][A38].

**Timing: validation first, installed systems second, procedures later.** We assume first conditional commercial deliveries in April–June 2027, within FY27's final quarter, following validation during January–June. FY27 stays 10 conditional systems at 40% realization. FY28 is 348 conditional systems at 70%, the count that reaches the second-customer band at the existing kit price. The bull is 279 systems at full realization. The old 120 and 200 plans were not a company cap. The bear has no commercial delivery through June 2028 [S23]. FY27 procedures use half a quarter's average installed exposure; FY28 uses beginning systems plus half current deliveries, so equipment revenue can lead fee revenue [S23].

**An operational analog restrains utilization, not an OEM sales multiple.** MAKO's 2012 issuer results disclose 45 new RIO placements,156 installed systems,10,204 annual procedures, and 6.6 procedures per system per month in Q4. That last figure is about 79 annualized (derived); the system and procedures were from a different era and indication mix, not Monogram's modern TKA launch [D27][G20]. We choose central 120 and high 180 procedures per active system-year—modestly above the older run rate, not 30,000–60,000 cases assumed independently of the installed fleet [S23]. Central conditional 120 placements in the first full fiscal year already exceed the independent MAKO comparator; Zimmer's channel can accelerate rollout, but 225 suite-wide robotic sales specialists are not 225Monogram salespeople or a unit commitment [D22][S23]. ROSA's approximately 2,000 installations are not automatic conversions, and Zimmer ranks existing ROSA conversions behind nonrobotic and competitor accounts [D22][D23].

Figure 4b states the low/central/high operating choices. Every price, bundle count, shipment probability and fee percentage here is an analyst assumption; none is recovered from contract redactions [S23][S24][S25].

<div class="fig" markdown="1">

**Figure 4b – Operating bridge: shipments lead procedures**

| Case / year | Conditional new robots | Expected shipped | Validation kits | Kit price ($) | Procedure equivalents |
|---|---|---|---|---|---|
| Bear FY27E | 0 [S30] | 0 [C95] | 0 [S32] | 3500 [S34] | 0 [C105] |
| Bear FY28E | 0 [S46] | 0 [C124] | 10 [S48] | 3500 [S50] | 0 [C134] |
| Base FY27E | 10 [S62] | 4 [C153] | 10 [S64] | 6000 [S66] | 60 [C163] |
| Base FY28E | 120 [S78] | 84 [C182] | 0 [S80] | 6000 [S82] | 5520 [C192] |
| Bull FY27E | 25 [S94] | 25 [C211] | 10 [S96] | 7500 [S98] | 562 [C221] |
| Bull FY28E | 200 [S110] | 200 [C240] | 0 [S112] | 7500 [S114] | 22500 [C250] |

*Source: robotics_model.csv; S23–S25. Low/central/high denote bear/base/bull. May not sum due to rounding.*
</div>
**Hardware price is estimated from cost, not the value of the whole robot.** We assume four end-effector/gearing kits per new robot for working, backup and sterilization rotation. Central $6,000 per kit is supported only by an engineering cost sketch: $2,500 materials, ten direct hours at $70, and about$850 indirect/testing; the resulting margin approximates PDEX's trailing gross margin. Low/high prices of$3,500/$7,500 allow lower-complexity price pressure or more complex tooling, with 25%/35%hardware gross margins; the count and bill of materials are unverified [S24]. The initial validation lot uses the same price logic, not a special engineering multiple. Five-percent spares on beginning installed kits give a restrained replacement stream; a one-year warranty and multi-year handpiece lives argue against immediate annual replacement or billable repair annuities [D18][D21][S24].

**The fee basket matters more than an assumed fixed royalty.** Central purchases of$300 per case-equivalent at 5% imply$15of fee before inventory stocking; high$500at 8% implies$40(derived), not a verified$50. We allow central 5%direct processing cost plus 10%administration:95%fee gross margin and 85%incremental EBITDA margin before shared launch support [S25]. Engineering margins are 35%central,25%low,40%high; incremental support is kept separate so billable engineering labor is not charged twice [S26]. Hardware and engineering incremental contribution before shared launch support equals their modeled gross profit; we assume no extra variable overhead outside the kit cost sketch, but deduct program support separately. These are coherent cost and launch bands, not disclosed economics; prices, eligible baskets and the percentage could differ materially.

Figure 4c reconciles operating volumes to revenue and contribution. The fee is computed as eligible purchases times the assumed rate, not manufactured disposable revenue.

<div class="fig" markdown="1">

**Figure 4c – Stream economics, US$M**

| Case / year | Hardware | NRE | Fees | Monogram total | Monogram GP | Incremental EBITDA | Helios sales |
|---|---|---|---|---|---|---|---|
| Bear FY27E | 0.0 [C112] | 0.1 [S40] | 0.0 [C113] | 0.1 [C116] | 0.0 [C117] | 0.0 [C120] | 0.0 [S45] |
| Bear FY28E | 0.0 [C141] | 0.1 [S56] | 0.0 [C142] | 0.1 [C145] | 0.0 [C146] | 0.0 [C149] | 0.0 [S61] |
| Base FY27E | 0.2 [C170] | 0.2 [S72] | 0.0 [C171] | 0.3 [C174] | 0.1 [C175] | 0.1 [C178] | 0.2 [S77] |
| Base FY28E | 2.0 [C199] | 0.1 [S88] | 0.1 [C200] | 2.2 [C203] | 0.8 [C204] | 0.7 [C207] | 0.5 [S93] |
| Bull FY27E | 0.8 [C228] | 0.2 [S104] | 0.0 [C229] | 1.1 [C232] | 0.4 [C233] | 0.3 [C236] | 0.3 [S109] |
| Bull FY28E | 6.0 [C257] | 0.2 [S120] | 1.1 [C258] | 7.3 [C261] | 3.2 [C262] | 2.8 [C265] | 0.5 [S125] |

*Source: robotics_model.csv. Incremental EBITDA = stream GP less fee administration and incremental shared support; excludes company-wide APM rent step. May not sum due to rounding.*
</div>
**The June 2026 rank sets FY28.** “Within a couple of years,” said in June 2026, is the end of FY28. Second-largest customer sales were about $6.20M in FY26, and the latest quarter annualizes to about $9.95M [A43][A44][C267][C268]. Base FY28 Monogram revenue is $6.21M, from 348 conditional systems at 70% realization. Bull FY28 Monogram revenue is $9.98M, from 279 systems at full realization [S23]. The company total stays consensus. The comment does not identify the 78% customer [G17][A36].

**Helios is separate and modest.** Central sales of$0.150M/$0.450M are allocations within the existing CMF medical-device run rate/growth, not additions to it; high$0.250M/$0.500M and low zero create only the incremental differences between cases. The illustrative quantities and prices are judgments, not disclosed orders, and we do not use the article's 50–65%margin. Apply each case's ordinary core margin; setup engineering remains within the existing NRE budget [S27].

**APM occupancy and cash discipline.** The October 30 filing adds 5,800 square feet from November 1, beyond the Q1 cost run rate. We deduct$92,800/$141,056of incremental manufacturing occupancy in FY27/FY28 using contracted cash rent as a small expense proxy; actual straight-line lease expense and allocation can differ [G21]. Existing renewed-space escalations remain in ordinary inflation, not another blanket step [S1]. Capacity/outsourcing evidence supports small initial hardware volumes but does not guarantee zero incremental tooling, inventory or capex; capex method 1 and year-zero balance sheet remain unchanged [S21][D2].

## 6. Risks

**Concentration before robotics.** One customer represents 78%of FY26 sales and its contract runs through calendar 2028; robotics does not eliminate that near-term reliance. The largest customer's identity remains unverified: documented Zimmer/Monogram supplier relationships and investor guesses are not concentration disclosure [A36][G3][D26].

**Launch sequence and adoption.** Zimmer's calendar H1 2027 target and PDEX's validation window overlap. Clearance, sterilization/quality validation, training, surgeon learning, capital purchasing and reimbursement can delay deliveries and utilization; low assumes no commercial revenue through FY28 [G10][G18][S23]. Lead times, nonbinding forecasts and working-capital needs make purchase timing a substantial uncertainty [D18][D25].

**Price, kits and fee eligibility.** Four kits per robot, kit ASPs, procedure utilization and fee rates are all judgmental. Hardware dominates central revenue; a smaller kit count or negotiated transfer price can overwhelm a higher fee margin. Custom-implant economics are excluded unless the contractual eligibility is actually met [S24][S25].

**Costs and operating leverage.** Incremental program support and manufacturing space are not temporary acquisition costs to be stripped. Increased sustaining engineering, warranty work, underutilized repair labor and supplier delays could reduce realized margins below the selected bands [G4][G5][G19][S26]. Revenue recognition or line classification may differ from our provisional purchase-fee presentation [D18][S28].

## 7. Forecast

### How the evidence becomes the numbers

Consensus remains the required base because quantitative annual management guidance is absent. Equibles was reopened November 7; provider capture is October 30,2026 at 12:17EDT (America/Toronto), not a known analyst estimate publication date; coverage is one analyst and no product-level model is published [D13][E1][E2]. We do not add a full robotics build on top. Instead, allocate central Monogram and Helios contributions inside consensus, preserve acquired APM unscaled, and reconcile only residual core lines to the anchor [S28].

The own build is $82.617M/$89.279M [C9][C10]. Monogram engineering was already within NRE and Helios was already within CMF [S26][S27]. The FY28 own build is above the consensus anchor, and residual core is scaled down so the base total stays at consensus [S28].

Figure 4 maps primary facts to the actual revisions; dollars are recomputed from stream-specific costs rather than a uniform robotics royalty.

<div class="fig" markdown="1">

**Figure 4 – Evidence → assumption → forecast impact**

| Evidence | Forecast choice | Impact |
|---|---|---|
| Contract: hardware plus purchase-based fees, redacted economics [G15][G16] | Cost-estimated kits, explicit eligible basket/rate; no full disposable sales [S24][S25] | Central Monogram total 0.307/6.212M; high 1.054/9.979M |
| Validation H2FY27; conditional Zimmer H12027 launch [G10][G18] | FY27 stays the validation year; FY28 system count meets the rank band [S23] | Central 4/244 expected new robots vs high 25/279 |
| No published annual guide; one-analyst consensus [E1][E2] | Allocate central pipeline within total; scale residual core only [S28] | Base revenue unchanged 82.7/86.8; own build 82.617/89.279M |
| New APM space rent from November 2026 [G21] | Manufacturing occupancy cash-rent proxy, not integration [G21] | EBITDA deduction 0.0928/0.141056M in every case |
| More sustaining engineering and launch work [D2] | Explicit extra support, fee admin and distinct stream margins [S26] | Base EBITDA 15.493/16.514M |
| CEO rank: customer number two within a couple of years [G17] | FY28 base and bull meet the second-customer band; gsnext continues that cohort one year [S23][S14][S18] | Base Monogram 6.21M; bull 9.98M; gsnext 0.9% / 3.1% |

*Source: forecast.json and robotics_model.csv; estimates are analyst judgments, not new company guidance. May not sum due to rounding.*
</div>
**Historical normalization is unchanged and not double-counted.** Annual FY26 acquisition costs of$0.434M and$0.5Mformer-owner consulting are one-time; approximately$0.2Mof Q3 legal/consulting is likely within that annual$0.434M, not another add-back. Historical tables retain reported EBITDA. The forecast's Q1 run rate identifies no remaining separately quantified acquisition charge; permanent finance/M&A/HR/IT hires and ongoing APM overhead remain, while only demonstrated temporary integration spend ends when integration finishes [A40][A35][G14][G4][P1].

**Case reconciliation.** Delete the old bull combined$0.5M/$1.0MMonogram/Helios NRE allowance. Bull replaces central Monogram with high and central Helios with high, alongside the unchanged core medical/repair volume levers; bear replaces central with low/zero, alongside existing core declines [S15][S16][S28]. Each case applies its core margin only to non-Monogram sales, then adds explicit Monogram gross profit, deducts new APM rent, existing opex plus program support/fee administration, and adds existing D&A plus SBC. EBITDA here retains the inherited operating-income-plus-D&A-plus-SBC definition, not a new company adjusted EBITDA metric [C23][C24][C53][C54][C72][C73].

Figure 4a separates our unscaled line economics from the consensus-anchored base.

<div class="fig" markdown="1">

**Figure 4a – Estimate comparison**

| View | FY27 revenue | FY28 revenue | FY27 EBITDA | FY28 EBITDA |
|---|---|---|---|---|
| Own line/cost build | 82.6 [C9] | 89.3 [C10] | 15.5 [C25] | 17.3 [C26] |
| Top-down guidance / calibrated | n/a | n/a | n/a | n/a |
| Consensus | 82.7 [E1] | 86.8 [E2] | n/a | n/a |
| Base | 82.7 [E1] | 86.8 [E2] | 15.5 [C23] | 16.5 [C24] |

*Source: forecast.json views; no numerical annual guidance or published EBITDA consensus. May not sum due to rounding.*
</div>
### Base case

Figure 5 preserves the company's reported revenue lines: manufactured robotics hardware is medical devices, engineering is NRE and the small purchase fee is provisionally in discounts/other [S28].

<div class="fig" markdown="1">

**Figure 5 – Base case by line**

| US$M | FY25A | FY26A | Q1FY27A | FY27E | FY28E |
|---|---|---|---|---|---|
| Medical devices | 47.7 [A1] | 62.1 [A6] | 17.4 [A11] | 69.8 [C12] | 75.0 [C18] |
| Industrial and scientific | 0.9 [A2] | 1.5 [A7] | 0.7 [A12] | 3.0 [C13] | 3.1 [C19] |
| NRE and prototype services | 0.7 [A3] | 1.6 [A8] | 0.2 [A13] | 1.2 [C14] | 1.2 [C20] |
| Repairs | 18.6 [A4] | 12.5 [A9] | 2.1 [A14] | 8.5 [C15] | 7.1 [C21] |
| Discounts and other | -1.3 [A5] | -0.3 [A10] | 0.1 [A15] | 0.2 [C16] | 0.3 [C22] |
| Revenue | 66.6 [A16] | 77.5 [A17] | 20.6 [A18] | 82.7 [E1] | 86.8 [E2] |
| EBITDA | 12.5 [C1] | 15.1 [C2] | 4.1 [C3] | 15.5 [C23] | 16.5 [C24] |
| Revenue growth | 23.7% (derived) [D12] | 16.5% [C34] | 11.0% (derived) [A18] | 6.6% [C38] | 5.0% [C38] |
| EBITDA margin | 18.7% (derived) [C1] | 19.4% (derived) [C2] | 19.7% (derived) [C3] | 18.7% [C36] | 18.9% [C37] |

*Source: forecast.json; D1 p 19, D2 p 21. May not sum due to rounding.*
</div>
Figure 5b shows the nine-quarter history window used for one-time items and the inputs past FY28.

<div class="fig" markdown="1">

**Figure 5b – Quarterly history (derived) [C89]**

| | Q1 FY25 | Q2 | Q3 | Q4 | Q1 FY26 | Q2 | Q3 | Q4 | Q1 FY27 |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | 14.9 | 16.8 | 17.4 | 17.5 | 18.5 | 18.7 | 19.9 | 20.4 | 20.6 |
| EBITDA | 3.4 | 3.1 | 4.1 | 1.8 | 3.6 | 3.7 | 3.6 | 4.1 | 4.1 |

*Source: D3–D12; Q4 = fiscal year less nine months; EBITDA = operating income + D&A + stock comp.*
</div>

**Beyond FY28.** Base and bull gsnext are one more year of the FY28 system cohort with the FY28 core held, about 0.9% and 3.1% [S14][S18]. Bear gsnext stays −10% for the customer renewal and does not set the base [S20]. Incremental margin stays 25% because the added dollars are mostly hardware [S13]. The explicit window stays at FY28. Finagle v02 fades those rates toward its own terminal growth.

## Appendix A – Bull and Bear Cases

Figure 6 shows integrated scenarios, not full robotics contributions added to consensus. The high model assumes timely validation/clearance and 200 new commercial systems in FY28, an aggressive rollout rather than a company commitment. Low assumes no commercial sales within the window; total decline also includes the inherited core-customer and repair stress [S15][S16][S23].

<div class="fig" markdown="1">

**Figure 6 – Scenario financials**

| Case | Year | Revenue | EBITDA | Gross margin | EBITDA margin |
|---|---|---|---|---|---|
| Bear | FY27E | 78.3 [C70] | 12.9 [C72] | 30.9% [C274] | 16.5% [C74] |
| Bear | FY28E | 70.7 [C71] | 10.2 [C73] | 30.8% [C277] | 14.4% [C75] |
| Base | FY27E | 82.7 [E1] | 15.5 [C23] | 32.3% [C272] | 18.7% [C36] |
| Base | FY28E | 86.8 [E2] | 16.5 [C24] | 32.5% [C275] | 19.0% [C37] |
| Bull | FY27E | 85.0 [C51] | 17.1 [C53] | 33.4% [C273] | 20.1% [C55] |
| Bull | FY28E | 92.1 [C52] | 19.8 [C54] | 34.4% [C276] | 21.5% [C56] |

*Source: forecast.json; explicit stream economics plus case core margins. May not sum due to rounding.*
</div>

**SBC convention.** Headline EBITDA adds back stock compensation. Keeping SBC as an expense would instead give base FY27/FY28 EBITDA of 15.0 [C280] / 15.9 [C281]; the addback is 0.5 [C278] / 0.6 [C279] US$M. This changes presentation, not the operating forecast.

## Appendix C – Method

We refreshed origin/main and used forecaster method be46f4a in an isolated clone; no repository method/code was changed. Base annual revenue follows published consensus, with residual-core line reconciliation and acquired industrial revenue unscaled. EBITDA uses a cost build; robotics receives separate hardware, engineering and fee economics, support and administration, plus the newly disclosed manufacturing rent. Public facts, management aspirations and analyst judgments remain separately tagged; the supporting CSV is an audit trail, not a claim of disclosed robot prices. No customer identity is inferred from supplier status. All historical/year-zero inputs remain unchanged; all impacted scenario leaves and comparison views are recomputed. The explicit forecast ends at FY28. Finagle v02 values the leaves and fades next-year growth toward its own terminal growth [S28][S29].

## Four views and ratios [C]

Revenue base = consensus; EBITDA base = cost build on base revenue. Annual guide is absent; calibrated view is absent; EBITDA consensus is absent. One-analyst revenue consensus was reopened November7,2026, provider capture October30; analyst publication date unknown.

|Metric/year|Bottom-up/base|Bottom-up/consensus|Consensus/base|
|---|---|---|---|
|revenue FY27E|99.9% [C79]|99.9% [C81]|100.0% [C80]|
|ebitda FY27E|100.0% [C82]|n/a — no EBITDA Consensus|n/a — no EBITDA Consensus|
|revenue FY28E|98.3% [C83]|98.3% [C85]|100.0% [C84]|
|ebitda FY28E|100.0% [C86]|n/a — no EBITDA Consensus|n/a — no EBITDA Consensus|

## Assumptions to revise when evidence changes

The consequential moves are launch timing/systems, kits/price, eligible purchases/rate, underlying core mix/volume and launch cost. The complete ledger follows; every assumption remains judgment, not a quotation.

- [S1] Opex inflation into FY28: personnel build (accounting, M&A, HR, IT) named in Q1 FY27 release and Irvine lease step-ups of 3.5% from Oct 2027 (8-K 2026-09-18). Judgment. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S2] Medical devices FY27: Q1 FY27 x4. 10-Q: 'We expect to see similar sales volumes of our largest customer's next generation and legacy handpiece for the remainder of this fiscal year.' Backlog $42.4M due in rest of FY27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S3] Medical devices FY28: FY27 +3%. 10-K: 'we expect to see similar levels of revenue reported in orthopedic sales through 2028'; growth from CMF distributors (+39% in Q1 FY27) only. Clarification: 3% applies to total medical-device revenue; the dollar increase is attributed to CMF, not a claim that CMF itself grows only3%. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S4] Industrial and scientific FY27: Q1 FY27 x4 (APM third-party sales; acquired Feb 2026). Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S5] Industrial and scientific FY28: +5%, APM defence/aerospace machining; no company guide. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S6] Original unscaled NRE1.2 retained; contains central Monogram engineering0.15 FY27 and0.10 FY28 as an allocation. Validation hardware is in medical devices. See S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S7] NRE FY28 held at FY27; no stated program amounts. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S8] Repairs FY27: Q1 FY27 x4; legacy repair decline ('we may continue to see declines') offset by start of billable next-gen repairs (10-K: 'we do not know yet at what volumes'). Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S9] Repairs FY28: legacy repairs keep falling as customer replaces legacy handpieces; next-gen repairs partly offset. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S10] Discounts and other FY27: volume rebates removed by contract extension (10-Q: 'no longer includes volume rebates'); Q1 +0.059. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S11] Discounts and other FY28 held at FY27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S12] APM (acquired Feb 2026) is inside FY26A actuals and too small to split; path is total. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S13] mc stays 25% in every case. The rank path is mostly hardware at an ordinary gross margin, so the fee stream does not reprice the company-wide contribution margin. See S29.
- [S14] base gsnext = (FY28 revenue 86.8 − FY28 Monogram 6.211606 + one more FY28 cohort 7.008178) / FY28 revenue − 1 = 0.9177%. The cohort is the same expected new systems again, with the FY28 core held.
- [S15] Bull: core medical devices +1/+1 and repairs +0.5/+0.5 US$M vs base; core GM33.5%; replace embedded central Monogram/Helios with explicit high path, not old combined NRE allowance. See S23-S28. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S16] Bear: core medical devices -3/-8 and repairs -1/-1.5 US$M vs base; core GM31%; replace embedded central Monogram/Helios with low/delayed path. See S23-S28. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S17] bull gross margin lever: see bull levers Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S18] bull gsnext = (FY28 revenue 92.117174 − FY28 Monogram 9.97878 + one more FY28 cohort 12.80784) / FY28 revenue − 1 = 3.0712%. The cohort is the same expected new systems again, with the FY28 core held.
- [S19] bear gross margin lever: see bear levers Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S20] Bear gsnext stays −10%. That is the customer-1 renewal after calendar 2028, and it does not set the base.
- [S21] No capex guidance; capex method 1 for all years (standing preference). Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S22] Validation units are not established commercial revenue. Operative contract verifies end-effectors, gearing and sourced-product fees; prices, percentage rates, annual volume and margins remain unquantified. Bull allocation is a scenario assumption, not a customer order. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S23] Monogram timing/volume. FY27 validation 0/10/10 and conditional commercial systems 0/10/25 stay the validation year. FY28 conditional systems are solved to the second-customer band: base 348 at 70% realization, bull 279 at 100%. The old 120/200 plans were not a company cap. FY27 active system-years = expected new systems / 8; FY28 = prior expected systems + half current additions. Central 120 cases per active system-year; high 180.
- [S24] Hardware cost/price judgments: low materials1600 +8h*60 +overhead545 =2625 cost, price3500, GM25%; central materials2500 +10h*70 +overhead850 ~4050, rounded price6000 and TTM32.4516% GM; high materials3000 +12h*75 +overhead975 =4875, price7500, GM35%. Each priced kit includes one end effector plus gearing; 4 per new robot (one in use, backup/sterilization rotation), not a disclosed specification. Spares 5% of beginning installed fleet kits, no replacements of current-year kits, no repair revenue inside window. All prices and staffing are analyst estimates, not recovered redactions. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S25] Fee judgments: central eligible burr/blade purchases300 dollars per case-equivalent, rate5%; high500 and8%; low no commercial launch. Purchases/use inventory factor1.30FY27,1.15FY28 central /1.20FY28 high. Exclude standard Persona implants (not patient-specific custom implants), robotic arms, navigation cameras, drapes, taxes, freight, packaging. Fee GP95%, incremental EBITDA85% before shared launch support: allow5% direct processing and10% admin expense. Rates and basket costs unobservable; range is scenario judgment, not a statistical interval. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S26] Engineering revenue included within original NRE budget, not added twice: low0.05/0.05, central0.15/0.10, high0.20/0.15 US$M FY27/FY28; central FY27 about1000billable hours at150 dollars/hour, FY28 roughlytwo-thirds that workload as setup ends. GM25%/35%/40% low/central/high. Incremental shared launch support beyond current run rate0.04/0.06 low,0.04/0.10 central,0.10/0.25 high US$M. Covers QA/customer support/engineering contingency; permanent existing staff retained. No additional D&A assumed within existing capacity; risk if tooling/capex expands. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S27] Helios separated: central0.15/0.45 US$M already allocated within CMF line run-rate/growth (illustratively50/150 drivers at3000 each); high0.25/0.50; low0/0. No author50–65% GM adopted; apply respective case core margins. Label/software engineering remains in existing NRE, no second setup-fee uplift. Product released, no disclosed orders: sizing is modest channel trial judgment. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S28] Retain consensus base82.7/86.8, unknown product coverage; Monogram/Helios are explicit allocations inside total. Replace old bull0.5/1.0 combined allowance, do not stack. Bull/bear differences = unchanged core volume/repair shocks plus pipeline HIGH/LOW minus CENTRAL already in base. Acquired industrial line unscaled. Scale residual non-APM core only to preserve modeled pipeline amounts. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S29] FY28 explicit stop retained. Base and bull FY28 Monogram are the second-customer band, not a cross-check. gsnext is one more year of the FY28 system cohort with the FY28 core held. Bear gsnext is the customer-1 renewal. mc stays 25% because the added dollars are mostly hardware at an ordinary margin.
- [S30] bear FY27E: conditional_new_systems = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S31] bear FY27E: shipment_realization = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S32] bear FY27E: validation_units = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S33] bear FY27E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S34] bear FY27E: kit_price_USD = 3500. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S35] bear FY27E: hardware_gross_margin = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S36] bear FY27E: procedures_per_system_year = 60. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S37] bear FY27E: purchase_inventory_factor = 1.3. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S38] bear FY27E: eligible_basket_USD = 150. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S39] bear FY27E: fee_rate = 0.02. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S40] bear FY27E: engineering_revenue_M = 0.05. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S41] bear FY27E: engineering_gross_margin = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S42] bear FY27E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S43] bear FY27E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S44] bear FY27E: shared_launch_support_M = 0.04. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S45] bear FY27E: helios_revenue_M = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S46] bear FY28E: conditional_new_systems = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S47] bear FY28E: shipment_realization = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S48] bear FY28E: validation_units = 10. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S49] bear FY28E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S50] bear FY28E: kit_price_USD = 3500. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S51] bear FY28E: hardware_gross_margin = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S52] bear FY28E: procedures_per_system_year = 60. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S53] bear FY28E: purchase_inventory_factor = 1.3. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S54] bear FY28E: eligible_basket_USD = 150. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S55] bear FY28E: fee_rate = 0.02. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S56] bear FY28E: engineering_revenue_M = 0.05. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S57] bear FY28E: engineering_gross_margin = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S58] bear FY28E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S59] bear FY28E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S60] bear FY28E: shared_launch_support_M = 0.06. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S61] bear FY28E: helios_revenue_M = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S62] base FY27E: conditional_new_systems = 10. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S63] base FY27E: shipment_realization = 0.4. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S64] base FY27E: validation_units = 10. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S65] base FY27E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S66] base FY27E: kit_price_USD = 6000. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S67] base FY27E: hardware_gross_margin = 0.324516. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S68] base FY27E: procedures_per_system_year = 120. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S69] base FY27E: purchase_inventory_factor = 1.3. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S70] base FY27E: eligible_basket_USD = 300. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S71] base FY27E: fee_rate = 0.05. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S72] base FY27E: engineering_revenue_M = 0.15. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S73] base FY27E: engineering_gross_margin = 0.35. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S74] base FY27E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S75] base FY27E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S76] base FY27E: shared_launch_support_M = 0.04. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S77] base FY27E: helios_revenue_M = 0.15. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S78] base FY28E: conditional_new_systems = 120. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S79] base FY28E: shipment_realization = 0.7. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S80] base FY28E: validation_units = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S81] base FY28E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S82] base FY28E: kit_price_USD = 6000. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S83] base FY28E: hardware_gross_margin = 0.324516. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S84] base FY28E: procedures_per_system_year = 120. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S85] base FY28E: purchase_inventory_factor = 1.15. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S86] base FY28E: eligible_basket_USD = 300. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S87] base FY28E: fee_rate = 0.05. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S88] base FY28E: engineering_revenue_M = 0.1. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S89] base FY28E: engineering_gross_margin = 0.35. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S90] base FY28E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S91] base FY28E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S92] base FY28E: shared_launch_support_M = 0.1. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S93] base FY28E: helios_revenue_M = 0.45. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S94] bull FY27E: conditional_new_systems = 25. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S95] bull FY27E: shipment_realization = 1. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S96] bull FY27E: validation_units = 10. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S97] bull FY27E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S98] bull FY27E: kit_price_USD = 7500. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S99] bull FY27E: hardware_gross_margin = 0.35. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S100] bull FY27E: procedures_per_system_year = 180. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S101] bull FY27E: purchase_inventory_factor = 1.3. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S102] bull FY27E: eligible_basket_USD = 500. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S103] bull FY27E: fee_rate = 0.08. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S104] bull FY27E: engineering_revenue_M = 0.2. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S105] bull FY27E: engineering_gross_margin = 0.4. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S106] bull FY27E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S107] bull FY27E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S108] bull FY27E: shared_launch_support_M = 0.1. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S109] bull FY27E: helios_revenue_M = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S110] bull FY28E: conditional_new_systems = 200. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S111] bull FY28E: shipment_realization = 1. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S112] bull FY28E: validation_units = 0. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S113] bull FY28E: units_per_new_system = 4. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S114] bull FY28E: kit_price_USD = 7500. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S115] bull FY28E: hardware_gross_margin = 0.35. Analyst judgment, not disclosed contract terms; rationale and bounds in S24. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S116] bull FY28E: procedures_per_system_year = 180. Analyst judgment, not disclosed contract terms; rationale and bounds in S23. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S117] bull FY28E: purchase_inventory_factor = 1.2. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S118] bull FY28E: eligible_basket_USD = 500. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S119] bull FY28E: fee_rate = 0.08. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S120] bull FY28E: engineering_revenue_M = 0.15. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S121] bull FY28E: engineering_gross_margin = 0.4. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S122] bull FY28E: fee_gross_margin = 0.95. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S123] bull FY28E: fee_ebitda_margin = 0.85. Analyst judgment, not disclosed contract terms; rationale and bounds in S25. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S124] bull FY28E: shared_launch_support_M = 0.25. Analyst judgment, not disclosed contract terms; rationale and bounds in S26. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
- [S125] bull FY28E: helios_revenue_M = 0.5. Analyst judgment, not disclosed contract terms; rationale and bounds in S27. Revise against disclosed orders, pricing, utilization, audited costs or guidance; keep pipeline allocated inside consensus unless exclusions are verified.
