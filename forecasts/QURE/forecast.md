# QURE (uniQure) forecast, v14 (rev7) as of 2026-11-02

## Status and open items

- Version **v14 / rev7**, built on v13 / rev6 (kept intact in /workspace/out/QURE_run_v13/). Uncommitted. Rebuild: `python3 build_forecast.py`, `python3 build_request_v14.py`, `python3 run/run_finagle_v14.py`, `python3 run/write_v14.py`, `python3 run/replay_v14.py`, `python3 make_md_v14.py`, `python3 report_build_v14/make_report_v14.py`, then copy report_v14.md to report.md and `python3 report_build_v14/render_report.py`. Bands: same pipeline in /workspace/out/QURE_run_v14_band_lower and _band_upper with env CONF_BAND=lower/upper.
- Driver, David May 2026-11-02 (t124u): "Check the Aspen s-1 for more data. They will run a trial similar in size to AskBio and BlueRock. So this gives another data point. Bull, Base and Bear can use the same cost but include a detailed section in the report explaining analysis and upper and lower cost bands. Make it self contained and use prose to explain."
- Confirmatory-study cost: one separate opex line in bear, base and bull, US$M FY27E-FY31E 30/45/32/17/5 (total 129) [I1] = gross study cost 40/55/42/27/15 less ~$10M/yr already in the Q2 2026 run rate [S]. Bands: lower 15/25/16/7/0 (63), upper 50/75/55/30/12 (222). Analysis: /workspace/out/QURE_trial_cost/ (research.md, numbers.csv, report_section.md) and report Section 10. Was $70M/yr flat ($350M, unsourced) in all cases.
- Year-0 (David t129u, 2026-11-02: "Year-0 should be 2025 cash+short term. And then adjust for any equity raises during the 2026 year. Then increase sharecount from 2025 to account for the equity raises."): cash = 80.240 + 542.301 (10-K 12/31/2025) + 242.681 (June 2026 offering net) = 865.222; shares = 62.529408 + 5.686813 = 68.216221. Employee option/ESPP cash ($6.985M) and ~1.15M plan shares excluded [S]. Hercules debt 49.699; HemB royalty liability not debt.
- Extra year-0 raises (only to keep cash >= 0, $50M steps at $25.30): base $0M, bull $0M, bear $4,250M; band runs bear lower $4,150M, upper $4,300M.
- Value per share central / lower / upper: base 335.65 / 336.18 / 334.90; bull 560.67 / 561.20 / 559.93; bear -0.78 / -1.02 / -0.84.
- Valuation request /workspace/out/QURE_run_v14/valuation_request_v14.json (whole_request sha256 5089ab652064b48acd22b85fcb046ca429b91daecaf29fc11c59dd8ee96f8299). Market data pinned to the 2026-10-30 fetch (price $25.30, rf 4.989%, re 10.489%).
- Open: Q3 2026 results 2026-11-04 may narrow the cost range; AdCom date; FY27E not scaled to consensus.

## base

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| US centers implied by capacity at 2/week (count) | – | – | 0 [C44] | 6 [C45] | 24 [C46] | 29 [C47] | 29 [C48] | 29 [C49] | 29 [C50] | 29 [C51] |
| US treatment capacity (patients/yr) | – | – | 0 [C52] | 330 [C53] | 2,500 [C54] | 3,000 [C55] | 3,000 [C56] | 3,000 [C57] | 3,000 [C58] | 3,000 [C59] |
| US entrants to eligible pool (patients/yr) | – | – | 0 [C60] | 1,884 [C61] | 3,788 [C62] | 3,806 [C63] | 3,826 [C64] | 3,845 [C65] | 3,864 [C66] | 3,883 [C67] |
| US pool demand (patients/yr) | – | – | 0 [C68] | 4,980 [C69] | 8,332 [C70] | 5,686 [C71] | 3,982 [C72] | 3,138 [C73] | 2,840 [C74] | 2,832 [C75] |
| US untreated pool leavers (patients/yr) | – | – | 0 [C76] | 1,836 [C77] | 3,072 [C78] | 2,097 [C79] | 1,468 [C80] | 1,157 [C81] | 1,047 [C82] | 1,044 [C83] |
| US eligible pool at year end (patients) | – | – | 6,000 [C84] | 5,718 [C85] | 3,933 [C86] | 2,643 [C87] | 2,000 [C88] | 1,703 [C89] | 1,680 [C90] | 1,687 [C91] |
| **US patients treated (patients/yr)** | – | – | 0 [C92] | 330 [C93] | 2,500 [C94] | 3,000 [C95] | 3,000 [C96] | 2,984 [C97] | 2,840 [C98] | 2,832 [C99] |
| US cumulative treated (patients) | – | – | 0 [C100] | 330 [C101] | 2,830 [C102] | 5,830 [C103] | 8,830 [C104] | 11,814 [C105] | 14,654 [C106] | 17,486 [C107] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S13] | 35.0 [S14] | 40.0 [S15] | 44.0 [S16] | 47.5 [S17] | 50.0 [S18] | 52.2 [S19] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S21] | 660 [C11] | 5,000 [C12] | 6,000 [C13] | 6,000 [C13] | 5,372 [C14] | 5,112 [C15] | 5,097 [C16] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] | 0.0 [S22] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 690 [C20] | 5,035 [C21] | 6,040 [C22] | 6,044 [C23] | 5,419 [C24] | 5,162 [C25] | 5,149 [C26] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C33] | 85.4% [C34] | 86.1% [C35] | 87.0% [C36] | 88.0% [C37] | 87.8% [C38] | 88.9% [C39] | 88.9% [C40] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | 280 [S23] | 3,719 [S24] | 4,594 [S25] | 4,666 [S26] | 4,142 [S27] | 3,984 [S28] | 3,967 [S29] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | 40.6% | 73.9% | 76.1% | 77.2% | 76.4% | 77.2% | 77.0% |

me 77.0% [C43], mc 83.0% [S30], gsnext 0.03% [S31].

## bull

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| US centers implied by capacity at 2/week (count) | – | – | 0 [C135] | 17 [C136] | 43 [C137] | 34 [C138] | 34 [C139] | 34 [C140] | 34 [C141] | 34 [C142] |
| US treatment capacity (patients/yr) | – | – | 0 [C143] | 880 [C144] | 4,500 [C145] | 3,500 [C146] | 3,500 [C147] | 3,500 [C148] | 3,500 [C149] | 3,500 [C150] |
| US entrants to eligible pool (patients/yr) | – | – | 0 [C151] | 2,581 [C152] | 5,187 [C153] | 5,213 [C154] | 5,239 [C155] | 5,265 [C156] | 5,292 [C157] | 5,318 [C158] |
| US pool demand (patients/yr) | – | – | 0 [C159] | 11,196 [C160] | 18,258 [C161] | 12,651 [C162] | 11,572 [C163] | 11,099 [C164] | 10,936 [C165] | 10,931 [C166] |
| US untreated pool leavers (patients/yr) | – | – | 0 [C167] | 1,848 [C168] | 3,013 [C169] | 2,088 [C170] | 1,910 [C171] | 1,832 [C172] | 1,805 [C173] | 1,804 [C174] |
| US eligible pool at year end (patients) | – | – | 6,000 [C175] | 5,853 [C176] | 3,527 [C177] | 3,153 [C178] | 2,982 [C179] | 2,916 [C180] | 2,903 [C181] | 2,918 [C182] |
| **US patients treated (patients/yr)** | – | – | 0 [C183] | 880 [C184] | 4,500 [C185] | 3,500 [C186] | 3,500 [C187] | 3,500 [C188] | 3,500 [C189] | 3,500 [C190] |
| US cumulative treated (patients) | – | – | 0 [C191] | 880 [C192] | 5,380 [C193] | 8,880 [C194] | 12,380 [C195] | 15,880 [C196] | 19,380 [C197] | 22,880 [C198] |
| UK capacity (patients/yr) | – | – | 0 [C199] | 0 [C200] | 117 [C201] | 663 [C202] | 780 [C203] | 780 [C204] | 524 [C205] | 269 [C206] |
| **UK patients treated (patients/yr)** | – | – | 0 [C207] | 0 [C208] | 117 [C209] | 663 [C210] | 780 [C211] | 780 [C212] | 524 [C213] | 269 [C214] |
| UK eligible backlog at year end (patients) | – | – | 0 [C215] | 0 [C216] | 2,155 [C217] | 1,574 [C218] | 943 [C219] | 372 [C220] | 0 [C221] | 0 [C222] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S13] | 35.0 [S14] | 40.0 [S15] | 44.0 [S16] | 47.5 [S17] | 50.0 [S18] | 52.2 [S19] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S21] | 2,112 [C108] | 9,720 [C109] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S34] | 0.0 [S34] | 176 [C111] | 994 [C112] | 1,170 [C113] | 1,170 [C113] | 787 [C114] | 404 [C115] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 2,142 [C117] | 9,930 [C118] | 8,594 [C119] | 8,774 [C120] | 8,778 [C121] | 8,397 [C122] | 8,016 [C123] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C124] | 87.6% [C125] | 87.2% [C126] | 87.9% [C127] | 89.0% [C128] | 90.2% [C129] | 91.3% [C130] | 91.5% [C131] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | 1,473 [S35] | 7,746 [S36] | 6,727 [S37] | 6,984 [S38] | 7,100 [S39] | 6,868 [S40] | 6,546 [S41] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | 68.8% | 78.0% | 78.3% | 79.6% | 80.9% | 81.8% | 81.7% |

me 81.7% [C134], mc 86.6% [S42], gsnext 0.02% [S43].

## bear

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S13] | 35.0 [S14] | 40.0 [S15] | 44.0 [S16] | 47.5 [S17] | 50.0 [S18] | 52.2 [S19] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] | 0.0 [S20] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] | 0.0 [S44] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 30.0 [C223] | 35.0 [C224] | 40.0 [C225] | 44.0 [C226] | 47.5 [C227] | 50.0 [C228] | 52.2 [C229] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | -172 [S47] | -162 [S48] | -134 [S49] | -116 [S50] | -100 [S51] | -93.0 [S52] | -90.9 [S53] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | -572.7% | -463.2% | -336.1% | -262.9% | -211.3% | -186.1% | -174.0% |

me -174.0% [C233], mc 93.9% [S54], gsnext 3.00% [S55].

| Bear cash opex (US$M) | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|
| Restructured opex [S] | 170 | 150 | 140 | 140 | 140 | 140 | 140 |
| Confirmatory study [I1] | 30 | 45 | 32 | 17 | 5 | 0 | 0 |
| Total | 200 | 195 | 172 | 157 | 145 | 140 | 140 |

## Sensitivities

| Case (units) | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|
| base filed: US treated (patients/yr) | 330 | 2,500 | 3,000 | 3,000 | 2,984 | 2,840 | 2,832 |
| base filed: revenue (US$M) | 690 | 5,035 | 6,040 | 6,044 | 5,419 | 5,162 | 5,149 |
| base filed: EBITDA (US$M) | 280 | 3,719 | 4,594 | 4,666 | 4,142 | 3,984 | 3,967 |
| base approval Q4 2027 (2027-10-01): US treated (patients/yr) | 165 | 2,040 | 2,875 | 3,000 | 3,000 | 2,875 | 2,833 |
| base approval Q4 2027 (2027-10-01): revenue (US$M) | 360 | 4,115 | 5,790 | 6,044 | 5,448 | 5,226 | 5,151 |
| base approval Q4 2027 (2027-10-01): EBITDA (US$M) | 15.8 | 2,974 | 4,389 | 4,666 | 4,165 | 4,037 | 3,968 |
| base entrants = 30% of incidence: US treated (patients/yr) | 330 | 2,500 | 1,466 | 927 | 910 | 909 | 909 |
| base entrants = 30% of incidence: revenue (US$M) | 690 | 5,035 | 2,973 | 1,899 | 1,685 | 1,686 | 1,689 |
| base entrants = 30% of incidence: EBITDA (US$M) | 280 | 3,719 | 2,078 | 1,225 | 1,050 | 1,068 | 1,064 |
| bull filed: US treated (patients/yr) | 880 | 4,500 | 3,500 | 3,500 | 3,500 | 3,500 | 3,500 |
| bull filed: revenue (US$M) | 2,142 | 9,930 | 8,594 | 8,774 | 8,778 | 8,397 | 8,016 |
| bull filed: EBITDA (US$M) | 1,473 | 7,746 | 6,727 | 6,984 | 7,100 | 6,868 | 6,546 |
| bull approval Q4 2027 (2027-10-01): US treated (patients/yr) | 440 | 3,815 | 3,750 | 3,500 | 3,500 | 3,500 | 3,500 |
| bull approval Q4 2027 (2027-10-01): revenue (US$M) | 1,086 | 9,366 | 9,134 | 8,774 | 8,778 | 8,397 | 8,016 |
| bull approval Q4 2027 (2027-10-01): EBITDA (US$M) | 602 | 7,399 | 7,178 | 6,984 | 7,100 | 6,868 | 6,546 |
| bull entrants = 30% of incidence: US treated (patients/yr) | 880 | 4,037 | 1,365 | 1,392 | 1,392 | 1,392 | 1,392 |
| bull entrants = 30% of incidence: revenue (US$M) | 2,142 | 8,931 | 3,983 | 4,221 | 4,224 | 3,844 | 3,463 |
| bull entrants = 30% of incidence: EBITDA (US$M) | 1,473 | 6,924 | 2,880 | 3,133 | 3,196 | 2,922 | 2,599 |
