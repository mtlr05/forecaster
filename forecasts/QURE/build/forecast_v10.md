# QURE (uniQure) forecast, rev3 as of 2026-10-30

## Status and open items

- Version **rev3** (supersedes rev2b of 2026-10-30; rev2b kept intact in /workspace/out/QURE_forecast_rev2b/), uncommitted. Rebuild: `python3 build_forecast.py` (needs `model.py`), `python3 make_md.py`.
- Driver of this revision, David May 2026-10-30 [P7]: "We can say that centers don’t limits capacity in year one and use your 190". "Your 190" is the Matt Kapusta CEO-simulation bot's year-1 path of about 10 / 30 / 60 / 90 patients per quarter (a pointer, not a document).
- Year one (Q3 2027-Q2 2028): US treated = base 10/30/60/90 = 190 [S8]; bull 15/45/90/135 = 285 (1.5x base [S]) [S9]. Centers do not bind.
- Year two (Q3 2028-Q2 2029) bridge [S] [S10][S11]: capacity rises linearly from the year-1 exit run-rate (90/qtr base, 135 bull) to 30 centers x throughput at Q2 2029 (base 536/qtr, bull 731); centers 15 -> 30. Which 30: ClearPoint said on its Q2 2026 call that 15 centers had qualified and the goal is 20-30 [G1]; the Kapusta bot put ~30 by the end of year 2. David's earlier "around 30 centers that can do 1-2 procedures a week" [P5] is therefore used as the end-of-year-2 network, not the launch network: that is the more defensible reading once year one is decoupled from centers (it matches the documented 15 today and the 20-30 goal).
- From Q3 2029: rev2b logic unchanged (centers +3/qtr base, +5 bull while a backlog exists, to 70/100; throughput rising to 2.0/week; then demand = backlog + refill per David's refill rule [P3]).
- All other rev2b inputs kept: price, COGS, opex incl. confirmatory R&D $70M/yr, Hemgenix royalty treatment, bear.
- Open: (1) refill: David's incidence-less-a-few (base 1,124/yr) vs Kapusta's 30% of incidence (490/yr base, 1,061 bull); (2) year-2 bridge shape [S]; (3) bull year-1 multiple [S]; (4) price step-down; (5) confirmatory-study cost; (6) royalty cash to HemB SPV; (7) Q3 2026 results 2026-11-04.

## Background: rev2b (kept unless changed above)

1. *(rev2b; superseded by rev3 for year one and year two, see above)* **Capacity at launch [P5] (assumption [S] [S6][S7]).** 30 centers ready at approval (2027-07-01; ClearPoint expects a decision mid to 2H 2027 [G3]). Throughput: base 1.0 procedure/center/week at launch rising 0.125/qtr to 2.0; bull 1.5 rising to 2.0. Capacity = centers x procedures/week x 13 weeks x utilisation.
2. *(rev2b; replaced in rev3 by the fixed year-1 path)* **Short-term limit (undisclosed, assumed [S]).** Utilisation of the ready capacity in the first quarters: base 50% / 67% / 83% / 100%, bull 67% / 83% / 100%. This stands for site activation, surgeon proctoring, the referral and prior-authorisation pipeline. Genezen vector supply is assumed not binding through FY29E (no disclosed dose capacity). ClearPoint says its own technology and support would not be the bottleneck; hospital scaling is [G1].
3. **Growth beyond 30 [S].** While a backlog exists, +3 centers/qtr (bull +5), capped at 70 (bull 100). Cross-checks: HDSA has 69 Centers of Excellence and partner sites [A12]; ClearPoint targets "the first 35-40 specialized treatment centers which can add 5,000 patients a year in capacity" across all its partners [G2] (about 2.4-2.75 procedures/center/week). The cap never binds before the backlog clears (peak: base 51, bull 80 centers). After clearing, the network falls back to the 30 launch centers with spare capacity (demand-limited).
4. **Demand unchanged from rev2.** Backlog ~6,000 [G5]; refill (David's rule [P3]) base 1,632 x 85% x 90% x 90% = **1,124/yr**, bull 3,536 x 90% x 95% x 95% = **2,872/yr**; untreated backlog attrition 10%/yr.
5. **Price [S].** Base $2.0M net FY27E-FY30E, then -10% to $1.8M from FY31E (US sales pass $2B in FY28E; step applied not before FY31E). Bull $2.4M, $2.16M from FY28E (passes $2B in FY27E) [S14][S15]. Gross list analogues: Lenmeldy $4.25M, Kebilidi $3.95M, Elevidys $3.2M, Hemgenix ~$3.5M [A13] (secondary compilation). Zolgensma ~$2.1M not opened (unverified).
6. **Costs [S].** COGS $0.30M/patient falling to $0.20M (bull $0.18M), **unverified**; no AMT-130 licensor royalty is disclosed (the royalty-bearing Regenxbio AAV9 licence is for AMT-260 [A15]), so none is modelled. Opex: Q2 2026 cash run rate x4 +3%/yr, US commercial fixed **$80M** (bull $90M), $1.5M/active center, 5% of AMT-130 revenue, UK $15M (bull), plus **confirmatory-study R&D $70M/yr FY27E-FY31E** [S1] (FDA-aligned randomized standard-of-care-controlled study, TFC at 36 months [G4]).
7. **Hemgenix royalty (financing).** uniQure sold Hemgenix royalties to HemB SPV (May 2023), booked as debt: liability $473.2M at 2025-12-31, cap 1.85x upfront ($693.8M) by 2032-06-30, else up to 2.25x through 2038 [A14]. License revenue stays in GAAP revenue and EBITDA, but the **cash goes to the SPV** until the cap is met; for valuation, treat the $473.2M as debt (or remove royalty cash). 
8. **FY27E not scaled to consensus.** David's capacity instruction overrides consensus: base FY27E revenue $110M vs consensus $114M (ratio 1.033) [C205]: flagged.
9. **Window FY26E-FY33E.** rev3: base backlog clears in 2031 and reaches steady state in FY32E, bull UK in FY33E; me is a steady-state margin.

**Time to work down the backlog (quarter when cumulative US treated passes 6,000 / quarter when the eligible US backlog is cleared):**

| Scenario | Case | Cumulative 6,000 treated | Backlog cleared |
|---|---|---|---|
| base | filed (approval 2027-07-01) | Q3 2030 | Q1 2031 |
| base | approval Q4 2027 | Q4 2030 | Q2 2031 |
| base | Kapusta refill 30% of incidence | Q3 2030 | Q4 2030 |
| bull | filed (approval 2027-07-01) | Q2 2030 | Q4 2031 |
| bull | approval Q4 2027 | Q3 2030 | Q1 2032 |
| bull | Kapusta refill 30% of incidence | Q2 2030 | Q3 2030 |

Bull UK backlog (~2,250) is cleared in FY32E. Bear: not approved.

## Kapusta review: applied / not applied and why

| Item | Status | Why |
|---|---|---|
| (a) Confirmatory-study R&D ~$60-80M/yr FY27-31 | Applied, $70M/yr [S] [S1] | Design confirmed in the Q2 2026 call [G4]; cost undisclosed |
| (b) US commercial fixed ~$80M | Applied, base $80M, bull $90M [S] | judgment, no disclosure |
| (c) Price $2.0M base, -10% past $2B/yr; bull $2.4M | Applied [S] [S14][S15] | analogue list prices cited [A13] |
| (d) Vector not binding through FY29E; COGS unverified | Applied | Genezen preferential access [G13]; no dose capacity disclosed |
| (e) Hemgenix royalties sold to HemB SPV; drop AMT-130 licensor royalty | Applied [A14][A15] | liability $473.2M confirmed in the 10-K |
| (f) Q4 2027 approval sensitivity | Applied as sensitivity; base stays 2027-07-01 | ClearPoint: mid to 2H 2027 [G3] |
| (g) UK in bull from Q3 2028 | Kept | unchanged |
| (1) Refill 30% of incidence (~490 base / ~1,000 bull) | **Not applied to the filed case**; shown as a sensitivity | David's refill rule [P3] takes precedence; key open question |
| (2) Center ceiling 70 base / 100 bull | Applied as cap [S] (non-binding) | HDSA 69 sites [A12], ClearPoint 35-40 initial centers [G2]; launch count is David's 30 [P5], not Kapusta's |

## base

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| US treatment centers at year end (count) | – | – | 0 [C42] | 15 [C43] | 22 [C44] | 36 [C45] | 48 [C46] | 30 [C47] | 30 [C48] | 30 [C49] |
| US treatment capacity (patients/yr) | – | – | 0 [C50] | 40 [C51] | 665 [C52] | 2,365 [C53] | 4,329 [C54] | 3,666 [C55] | 3,120 [C56] | 3,120 [C57] |
| US refill demand (patients/yr) | – | – | 0 [C58] | 562 [C59] | 1,124 [C60] | 1,124 [C61] | 1,124 [C62] | 1,124 [C63] | 1,124 [C64] | 1,124 [C65] |
| US eligible backlog at year end (patients) | – | – | 6,000 [C66] | 6,206 [C67] | 6,029 [C68] | 4,269 [C69] | 834 [C70] | 0 [C71] | 0 [C72] | 0 [C73] |
| **US patients treated (patients/yr)** | – | – | 0 [C74] | 40 [C75] | 665 [C76] | 2,365 [C77] | 4,329 [C78] | 1,957 [C79] | 1,124 [C80] | 1,124 [C81] |
| US cumulative treated (patients) | – | – | 0 [C82] | 40 [C83] | 705 [C84] | 3,070 [C85] | 7,399 [C86] | 9,356 [C87] | 10,479 [C88] | 11,603 [C89] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S26] | 80.0 [C9] | 1,329 [C10] | 4,730 [C11] | 8,658 [C12] | 3,523 [C13] | 2,023 [C14] | 2,023 [C14] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 110 [C18] | 1,364 [C19] | 4,770 [C20] | 8,702 [C21] | 3,570 [C22] | 2,073 [C23] | 2,075 [C24] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C31] | 87.4% [C32] | 86.2% [C33] | 87.1% [C34] | 88.0% [C35] | 87.9% [C36] | 89.0% [C37] | 89.0% [C38] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -237 [S28] | 723 [S29] | 3,503 [S30] | 6,790 [S31] | 2,544 [S32] | 1,390 [S33] | 1,386 [S34] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -215.6% | 53.0% | 73.4% | 78.0% | 71.3% | 67.1% | 66.8% |

me 66.8% [C41], mc 77.9% [S35], gsnext 0.08% [S36]. May not sum due to rounding.

Base capacity ramp [S8], first 12 quarters after approval (rev3: Q3 2027-Q2 2028 fixed year-1 path, centers shown are the 15 qualified and do not bind; Q3 2028-Q2 2029 bridge) [S6]:

| Quarter | Centers active (count) | Procedures per center per week | Utilisation (%) | Capacity (patients/qtr) | Treated (patients/qtr) | Backlog at quarter end (patients) |
|---|---|---|---|---|---|---|
| Q3 2027 | 15 | 0.000 | n/a | 10 | 10 | 6,114 |
| Q4 2027 | 15 | 0.000 | n/a | 30 | 30 | 6,206 |
| Q1 2028 | 15 | 0.000 | n/a | 60 | 60 | 6,266 |
| Q2 2028 | 15 | 0.000 | n/a | 90 | 90 | 6,296 |
| Q3 2028 | 19 | 1.000 | 83% | 202 | 202 | 6,216 |
| Q4 2028 | 22 | 1.125 | 95% | 313 | 313 | 6,029 |
| Q1 2029 | 26 | 1.250 | 100% | 425 | 425 | 5,738 |
| Q2 2029 | 30 | 1.375 | 100% | 536 | 536 | 5,345 |
| Q3 2029 | 33 | 1.500 | 100% | 644 | 644 | 4,858 |
| Q4 2029 | 36 | 1.625 | 100% | 760 | 760 | 4,269 |
| Q1 2030 | 39 | 1.750 | 100% | 887 | 887 | 3,571 |
| Q2 2030 | 42 | 1.875 | 100% | 1024 | 1024 | 2,758 |

## bull

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| US treatment centers at year end (count) | – | – | 0 [C120] | 15 [C121] | 22 [C122] | 40 [C123] | 60 [C124] | 80 [C125] | 30 [C126] | 30 [C127] |
| US treatment capacity (patients/yr) | – | – | 0 [C128] | 60 [C129] | 942 [C130] | 3,263 [C131] | 5,460 [C132] | 7,540 [C133] | 3,120 [C134] | 3,120 [C135] |
| US refill demand (patients/yr) | – | – | 0 [C136] | 1,436 [C137] | 2,872 [C138] | 2,872 [C139] | 2,872 [C140] | 2,872 [C141] | 2,872 [C142] | 2,872 [C143] |
| US eligible backlog at year end (patients) | – | – | 6,000 [C144] | 7,028 [C145] | 8,150 [C146] | 6,979 [C147] | 3,861 [C148] | 0 [C149] | 0 [C150] | 0 [C151] |
| **US patients treated (patients/yr)** | – | – | 0 [C152] | 60 [C153] | 942 [C154] | 3,263 [C155] | 5,460 [C156] | 6,607 [C157] | 2,872 [C158] | 2,872 [C159] |
| US cumulative treated (patients) | – | – | 0 [C160] | 60 [C161] | 1,002 [C162] | 4,266 [C163] | 9,726 [C164] | 16,333 [C165] | 19,205 [C166] | 22,077 [C167] |
| UK capacity (patients/yr) | – | – | 0 [C168] | 0 [C169] | 117 [C170] | 663 [C171] | 780 [C172] | 780 [C173] | 524 [C174] | 269 [C175] |
| **UK patients treated (patients/yr)** | – | – | 0 [C176] | 0 [C177] | 117 [C178] | 663 [C179] | 780 [C180] | 780 [C181] | 524 [C182] | 269 [C183] |
| UK eligible backlog at year end (patients) | – | – | 0 [C184] | 0 [C185] | 2,155 [C186] | 1,574 [C187] | 943 [C188] | 372 [C189] | 0 [C190] | 0 [C191] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S26] | 144 [C90] | 2,261 [C91] | 7,049 [C92] | 11,794 [C93] | 14,271 [C94] | 6,204 [C95] | 6,204 [C95] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S39] | 0.0 [S39] | 176 [C96] | 994 [C97] | 1,170 [C98] | 1,170 [C98] | 787 [C99] | 404 [C100] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 174 [C102] | 2,472 [C103] | 8,084 [C104] | 13,008 [C105] | 15,489 [C106] | 7,041 [C107] | 6,660 [C108] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C109] | 88.6% [C110] | 88.1% [C111] | 87.8% [C112] | 89.2% [C113] | 90.4% [C114] | 91.3% [C115] | 91.5% [C116] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -187 [S40] | 1,645 [S41] | 6,254 [S42] | 10,473 [S43] | 12,720 [S44] | 5,698 [S45] | 5,376 [S46] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -107.7% | 66.6% | 77.4% | 80.5% | 82.1% | 80.9% | 80.7% |

me 80.7% [C119], mc 86.1% [S47], gsnext 0.02% [S48].

Bull capacity ramp [S7][S9]:

| Quarter | Centers active (count) | Procedures per center per week | Utilisation (%) | Capacity (patients/qtr) | Treated (patients/qtr) | Backlog at quarter end (patients) |
|---|---|---|---|---|---|---|
| Q3 2027 | 15 | 0.000 | n/a | 15 | 15 | 6,535 |
| Q4 2027 | 15 | 0.000 | n/a | 45 | 45 | 7,028 |
| Q1 2028 | 15 | 0.000 | n/a | 90 | 90 | 7,465 |
| Q2 2028 | 15 | 0.000 | n/a | 135 | 135 | 7,847 |
| Q3 2028 | 19 | 1.500 | 78% | 284 | 284 | 8,074 |
| Q4 2028 | 22 | 1.625 | 91% | 433 | 433 | 8,150 |
| Q1 2029 | 26 | 1.750 | 97% | 582 | 582 | 8,078 |
| Q2 2029 | 30 | 1.875 | 100% | 731 | 731 | 7,863 |
| Q3 2029 | 35 | 2.000 | 100% | 910 | 910 | 7,480 |
| Q4 2029 | 40 | 2.000 | 100% | 1040 | 1040 | 6,979 |
| Q1 2030 | 45 | 2.000 | 100% | 1170 | 1170 | 6,364 |
| Q2 2030 | 50 | 2.000 | 100% | 1300 | 1300 | 5,637 |

## bear

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 30.0 [C192] | 35.0 [C193] | 40.0 [C194] | 44.0 [C195] | 47.5 [C196] | 50.0 [C197] | 52.2 [C198] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -142 [S52] | -117 [S53] | -102 [S54] | -98.7 [S55] | -95.4 [S56] | -93.0 [S57] | -90.9 [S58] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -472.7% | -334.6% | -256.1% | -224.2% | -200.8% | -186.1% | -174.0% |

me -174.0% [C202], mc 93.9% [S59], gsnext 3.00% [S60]. Bear (not approved): no confirmatory study or launch costs; lines unchanged from rev2b.

## Sensitivities

| Case (units) | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|
| base filed: US treated (patients/yr) | 40 | 665 | 2,365 | 4,329 | 1,957 | 1,124 | 1,124 |
| base filed: revenue (US$M) | 110 | 1,364 | 4,770 | 8,702 | 3,570 | 2,073 | 2,075 |
| base filed: EBITDA (US$M) | -237 | 723 | 3,503 | 6,790 | 2,544 | 1,390 | 1,386 |
| base approval Q4 2027 (2027-10-01): US treated (patients/yr) | 10 | 382 | 1,918 | 3,842 | 3,011 | 1,124 | 1,124 |
| base approval Q4 2027 (2027-10-01): revenue (US$M) | 50.0 | 798 | 3,875 | 7,727 | 5,468 | 2,073 | 2,075 |
| base approval Q4 2027 (2027-10-01): EBITDA (US$M) | -285 | 270 | 2,774 | 5,986 | 4,115 | 1,390 | 1,386 |
| base Kapusta refill 30% of incidence: US treated (patients/yr) | 40 | 665 | 2,365 | 3,292 | 490 | 490 | 490 |
| base Kapusta refill 30% of incidence: revenue (US$M) | 110 | 1,364 | 4,770 | 6,627 | 929 | 931 | 934 |
| base Kapusta refill 30% of incidence: EBITDA (US$M) | -237 | 723 | 3,503 | 5,068 | 358 | 433 | 428 |
| bull filed: US treated (patients/yr) | 60 | 942 | 3,263 | 5,460 | 6,607 | 2,872 | 2,872 |
| bull filed: revenue (US$M) | 174 | 2,472 | 8,084 | 13,008 | 15,489 | 7,041 | 6,660 |
| bull filed: EBITDA (US$M) | -187 | 1,645 | 6,254 | 10,473 | 12,720 | 5,698 | 5,376 |
| bull approval Q4 2027 (2027-10-01): US treated (patients/yr) | 15 | 554 | 2,657 | 4,940 | 7,020 | 3,659 | 2,872 |
| bull approval Q4 2027 (2027-10-01): revenue (US$M) | 66.0 | 1,540 | 7,410 | 11,884 | 16,381 | 8,740 | 6,660 |
| bull approval Q4 2027 (2027-10-01): EBITDA (US$M) | -276 | 872 | 5,773 | 9,530 | 13,492 | 7,171 | 5,376 |
| bull Kapusta refill 30% of incidence: US treated (patients/yr) | 60 | 942 | 3,263 | 4,011 | 1,061 | 1,061 | 1,061 |
| bull Kapusta refill 30% of incidence: revenue (US$M) | 174 | 2,472 | 8,084 | 9,877 | 3,509 | 3,128 | 2,747 |
| bull Kapusta refill 30% of incidence: EBITDA (US$M) | -187 | 1,645 | 6,254 | 7,869 | 2,523 | 2,308 | 1,985 |

## rev2b -> rev3

| base (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| US patients treated, rev2b (patients/yr) | 0 | 518 | 2,952 | 4,461 | 1,124 | 1,124 | 1,124 | 1,124 |
| US patients treated, rev3 (patients/yr) | 0 | 40 | 665 | 2,365 | 4,329 | 1,957 | 1,124 | 1,124 |
| Revenue, rev2b (US$M) | 24.9 | 1,067 | 5,940 | 8,963 | 2,291 | 2,070 | 2,073 | 2,075 |
| Revenue, rev3 (US$M) | 24.9 | 110 | 1,364 | 4,770 | 8,702 | 3,570 | 2,073 | 2,075 |
| EBITDA, rev2b (US$M) | -161 | 501 | 4,395 | 6,910 | 1,496 | 1,302 | 1,390 | 1,386 |
| EBITDA, rev3 (US$M) | -161 | -237 | 723 | 3,503 | 6,790 | 2,544 | 1,390 | 1,386 |

| bull (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| US patients treated, rev2b (patients/yr) | 0 | 1,006 | 4,737 | 6,489 | 2,872 | 2,872 | 2,872 | 2,872 |
| US patients treated, rev3 (patients/yr) | 0 | 60 | 942 | 3,263 | 5,460 | 6,607 | 2,872 | 2,872 |
| Revenue, rev2b (US$M) | 24.9 | 2,444 | 10,442 | 15,051 | 7,418 | 7,421 | 7,041 | 6,660 |
| Revenue, rev3 (US$M) | 24.9 | 174 | 2,472 | 8,084 | 13,008 | 15,489 | 7,041 | 6,660 |
| EBITDA, rev2b (US$M) | -161 | 1,655 | 8,125 | 12,014 | 5,790 | 5,878 | 5,698 | 5,376 |
| EBITDA, rev3 (US$M) | -161 | -187 | 1,645 | 6,254 | 10,473 | 12,720 | 5,698 | 5,376 |

| bear (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| Revenue, rev2b (US$M) | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 50.0 | 52.2 |
| Revenue, rev3 (US$M) | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 50.0 | 52.2 |
| EBITDA, rev2b (US$M) | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -93.0 | -90.9 |
| EBITDA, rev3 (US$M) | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -93.0 | -90.9 |

## Verified vs assumed

Verified this revision (opened): ClearPoint Q2 2026 call (15 qualified centers, 1-2/week, 20-30 goal, hospital scaling is the constraint); ClearPoint Q3 2025 press release (35-40 centers, 5,000/yr); ClearPoint Q3 2026 call (approval mid to 2H 2027); ClearPoint 8-K 2026-10-28 (>175 active global centers, all indications); HDSA (69 sites); uniQure 10-K (HemB SPV royalty financing, $473.2M liability, caps; Regenxbio licence is AMT-260); uniQure Q2 2026 call (confirmatory study design); IntuitionLabs list prices (secondary).
Assumed [S]: launch utilisation, throughput path, center additions and cap, price and step-down, COGS, commercial fixed cost, confirmatory cost, approval date, refill haircuts, attrition, UK.

## Sources

See `sources` in forecast.json. Documents:
- D1: uniQure Form 10-K FY2025 (filed 2026-03-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926021898/qure-20251231x10k.htm. HTML; no page numbers
- D2: uniQure Form 10-Q Q2 2026 (filed 2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087815/qure-20260630x10q.htm. HTML; no page numbers
- D3: uniQure Q2 2026 results press release, 8-K Ex.99.1 (2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087808/qure-20260729xex99d1.htm. HTML; no page numbers
- D4: uniQure BLA submission press release, 8-K Ex.99.1 (2026-09-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926104463/qure-20260902xex99d1.htm. HTML; no page numbers
- D5: uniQure four-year AMT-130 data press release, 8-K Ex.99.2 (2026-09-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926111654/tm2626514d1_ex99-2.htm. HTML; no page numbers
- D6: Yahoo Finance / yfinance analyst revenue estimates for QURE, pulled 2026-10-29 (shown in EUR). https://finance.yahoo.com/quote/QURE/analysis/. HTML; no page numbers
- D7: GEN StockWatch, Leerink net-price estimates and O'Keefe pricing/TAM comments (2025). https://www.genengnews.com/topics/translational-medicine/stockwatch-uniqure-shares-reach-five-year-high-on-game-changing-huntingtons-data/. HTML; no page numbers
- D8: Clinaptis research, AMT-130 capacity ramp and net-price model. https://www.clinaptisresearch.com/research/amt-130-huntingtons-uniqure-bla. HTML; no page numbers
- D9: BioSpace, uniQure files for FDA, UK approval (2026-09). https://www.biospace.com/fda/uniqure-files-for-fda-uk-approval-of-first-gene-therapy-for-huntingtons-disease. HTML; no page numbers
- D10: uniQure, Pivotal Phase I/II AMT-130 Huntington's Disease Update, investor presentation, slides 25-26 (2025-09-24). https://cdn.craft.cloud/fe68e1a2-b284-4f69-ba29-921f065edf17/assets/uploads/AMT-130-Pivotal-Sept-2025_final_09.24.25.pdf. HTML; no page numbers
- D11: Medina et al., Prevalence and Incidence of Huntington's Disease: An Updated Systematic Review and Meta-Analysis, Movement Disorders 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC10086981/. HTML; no page numbers
- D12: uniQure Q2 2026 earnings call transcript (Motley Fool, 2026-08-07). https://www.fool.com/earnings/call-transcripts/2026/08/07/uniqure-qure-q2-2026-earnings-call-transcript/. HTML; no page numbers
- D13: uniQure Q1 2026 earnings call transcript (StockAnalysis). https://stockanalysis.com/stocks/qure/transcripts/578165-q1-2026/. HTML; no page numbers
- D14: uniQure press release, sale of Lexington commercial manufacturing facility to Genezen (2024-07-01). https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-sale-commercial-manufacturing-facility-genezen. HTML; no page numbers
- D15: US Census Bureau population clock (US resident population ~340 million). https://www.census.gov/popclock/. HTML; no page numbers
- D16: Prompt: David May, direct message 2026-10-30. n/a: user prompt (David May, direct message, 2026-10-30). HTML; no page numbers
- D17: Prompt: David May, direct messages 2026-10-30 (capacity-dependent short term; refill = incidence less a few). n/a: user prompt (David May, direct messages, 2026-10-30). HTML; no page numbers
- D18: EHDN Platform Meeting report, uniQure AMT-130 topline results (2025-12-04). https://ehdn.org/wp-content/uploads/2025/12/EHDN-Platform-Meeting-uniQure-Topline-Results-Report_Final_2-04-Dec-2025.pdf. HTML; no page numbers
- D19: Sarepta ELEVIDYS label update call transcript, 2024-06-21 (StockAnalysis/Quartr). https://stockanalysis.com/stocks/srpt/transcripts/205218-status-update/. HTML; no page numbers
- D20: Sarepta Q4 and FY2024 results, 8-K Ex.99.1 (2025-02-26) and preliminary release (2025-01-13). https://www.sec.gov/Archives/edgar/data/873303/000095017025027717/srpt-ex99_1.htm. HTML; no page numbers
- D21: Sarepta 8-K 2023-06-22: ELEVIDYS US wholesale acquisition cost. https://www.sec.gov/Archives/edgar/data/873303/000095017023029438/srpt-20230622.htm. HTML; no page numbers
- D22: Investing.com, Goldman Sachs note summary on uniQure (2025-09). https://ph.investing.com/news/analyst-ratings/uniqure-stock-rises-after-positive-huntingtons-disease-gene-therapy-data-93CH-2010942. HTML; no page numbers
- D23: Reuters, FDA approves Sarepta gene therapy (2023-06-22): Hemgenix list price. https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-sareptas-gene-therapy-rare-muscular-dystrophy-some-kids-2023-06-22/. HTML; no page numbers
- D24: ClearPoint Neuro Q2 2026 earnings call transcript (2026-08-10, Motley Fool): CLEAR site-readiness program. https://www.fool.com/earnings/call-transcripts/2026/08/10/clearpoint-neuro-clpt-q2-2026-earnings-call-transcript/. HTML; no page numbers
- D25: ClearPoint Neuro Q3 2025 results press release, 8-K Ex.99.1 (2025-11-06). https://www.sec.gov/Archives/edgar/data/1285550/000119312525270019/clpt-ex99_1.htm. HTML; no page numbers
- D26: ClearPoint Neuro Q3 2026 earnings call transcript (2026-10-28, StockAnalysis). https://stockanalysis.com/stocks/clpt/transcripts/722761-q3-2026/. HTML; no page numbers
- D27: HDSA press release 2025-04-02: Centers of Excellence network expands to 69 sites. https://hdsa.org/news/huntingtons-disease-society-of-america-awards-more-than-1-8-million-to-expand-hdsa-centers-of-excellence-network-to-sixty-nine-sites/. HTML; no page numbers
- D28: IntuitionLabs, Most Expensive Drugs in the US: 2025 price list (secondary source for gene-therapy list prices). https://intuitionlabs.ai/articles/most-expensive-drugs-usa-2025. HTML; no page numbers
- D30: David May direct message 2026-10-30 (t62u: centers do not limit capacity in year one; use the Kapusta bot's ~190 year-1 path). n/a: user prompt in chat. HTML; no page numbers
- D29: David May direct messages 2026-10-30 (rev2b: t57u ClearPoint centers; 'Adjust as necessary and then send for finagle valuation'). n/a: user prompt in chat. HTML; no page numbers
