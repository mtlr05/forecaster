# QURE (uniQure) forecast, v11 (rev4) as of 2026-10-30

## Status and open items

- Version **v11 / rev4**, supersedes v10 (rev3, kept intact in /workspace/out/QURE_run/ and forecasts/QURE/). Uncommitted. Rebuild from `/workspace/out/QURE_run_v11/build/`: `python3 build_forecast.py` (needs `model.py`), then `cd .. && python3 build_request_v11.py` (scratch dry check via `dry11.py`), then `python3 build/make_md_v11.py`.
- Driver, David May 2026-10-30 [P7]: "Write is up with m=0.62 its the most internally consistent"; [P8] "Redo the finagle too".
- US AMT-130 treated = min(CLPT capacity, pool demand) [S6][C4]: start pool 6,000 at 2027-07-01 [G5]; leave rate m = 0.62/yr (progression 0.60 + death 0.02) [P9]; P = 0.9 x 0.9 x 0.9 = 0.729 [S3]; entrants 1.22/100k x 340M x 0.90 x 1.0045 (filter that holds the steady pool at 6,000), +0.5%/yr [C2]; quarterly. Capacity: CLPT ramp 330 (FY27, half year) / 2,500 (FY28) / 3,000 cap from FY29 (bull 880 / 4,500 / 3,500) [S7].
- Bull: incidence 1.59, share 0.95, P = 0.95^3 = 0.857, same 6,000 start pool, entrants unfiltered (steady pool ~8,200) [C3]; capacity binds every year. UK unchanged from v10. Bear: not approved (unchanged).
- Unchanged from v10: price ($2.0M base, -10% from FY31E; bull $2.4M, $2.16M from FY28E), COGS/patient, opex rules (incl. $1.5M per center, now centers = capacity / 104 procedures/yr), confirmatory R&D $70M/yr, Hemgenix royalty and HemB SPV treatment, FY26E = consensus, FY27E not scaled to consensus (ratio 0.165, flagged).
- Open: (1) m = 0.62 (stay ~1.6 yr) is shorter than the duration evidence; crossover data (2 of 6 high-dose controls failed inclusion after ~12 months [A23]) point to ~0.41/yr; (2) bull start pool and unfiltered entrants [S]; (3) center count used for opex [S]; (4) raise sizes and bear raise (see flags); (5) Q3 2026 results 2026-11-04.

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
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S14] | 35.0 [S15] | 40.0 [S16] | 44.0 [S17] | 47.5 [S18] | 50.0 [S19] | 52.2 [S20] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S22] | 660 [C11] | 5,000 [C12] | 6,000 [C13] | 6,000 [C13] | 5,372 [C14] | 5,112 [C15] | 5,097 [C16] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] | 0.0 [S23] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 690 [C20] | 5,035 [C21] | 6,040 [C22] | 6,044 [C23] | 5,419 [C24] | 5,162 [C25] | 5,149 [C26] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C33] | 85.4% [C34] | 86.1% [C35] | 87.0% [C36] | 88.0% [C37] | 87.8% [C38] | 88.9% [C39] | 88.9% [C40] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | 240 [S24] | 3,694 [S25] | 4,556 [S26] | 4,613 [S27] | 4,077 [S28] | 3,984 [S29] | 3,967 [S30] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | 34.8% | 73.4% | 75.4% | 76.3% | 75.2% | 77.2% | 77.0% |

me 77.0% [C43], mc 83.0% [S31], gsnext 0.03% [S32]. Rows may not sum due to rounding.

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
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S14] | 35.0 [S15] | 40.0 [S16] | 44.0 [S17] | 47.5 [S18] | 50.0 [S19] | 52.2 [S20] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S22] | 2,112 [C108] | 9,720 [C109] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] | 7,560 [C110] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S35] | 0.0 [S35] | 176 [C111] | 994 [C112] | 1,170 [C113] | 1,170 [C113] | 787 [C114] | 404 [C115] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 2,142 [C117] | 9,930 [C118] | 8,594 [C119] | 8,774 [C120] | 8,778 [C121] | 8,397 [C122] | 8,016 [C123] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C124] | 87.6% [C125] | 87.2% [C126] | 87.9% [C127] | 89.0% [C128] | 90.2% [C129] | 91.3% [C130] | 91.5% [C131] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | 1,433 [S36] | 7,721 [S37] | 6,689 [S38] | 6,931 [S39] | 7,035 [S40] | 6,868 [S41] | 6,546 [S42] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | 66.9% | 77.8% | 77.8% | 79.0% | 80.1% | 81.8% | 81.7% |

me 81.7% [C134], mc 86.6% [S43], gsnext 0.02% [S44].

## bear

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|---|---|
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C8] | 30.0 [S14] | 35.0 [S15] | 40.0 [S16] | 44.0 [S17] | 47.5 [S18] | 50.0 [S19] | 52.2 [S20] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] | 0.0 [S21] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A25] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] | 0.0 [S45] |
| AMT-130 revenue, UK (US$M) | 0.0 [A26] | 0.0 [A26] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] | 0.0 [S46] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C8] | 30.0 [C223] | 35.0 [C224] | 40.0 [C225] | 44.0 [C226] | 47.5 [C227] | 50.0 [C228] | 52.2 [C229] |
| Gross margin (%) | – | 89.5% [C32] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] | 93.9% [C230] |
| **EBITDA (US$M)** | -149 [C27] | -153 [C28] | -161 [C31] | -142 [S48] | -117 [S49] | -102 [S50] | -98.7 [S51] | -95.4 [S52] | -93.0 [S53] | -90.9 [S54] |
| EBITDA margin (%, derived from the two rows above) | -550.9% | -949.9% | -645.9% | -472.7% | -334.6% | -256.1% | -224.2% | -200.8% | -186.1% | -174.0% |

me -174.0% [C233], mc 93.9% [S55], gsnext 3.00% [S56]. Bear (not approved): unchanged from v10.

## Sensitivities

| Case (units) | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|
| base filed: US treated (patients/yr) | 330 | 2,500 | 3,000 | 3,000 | 2,984 | 2,840 | 2,832 |
| base filed: revenue (US$M) | 690 | 5,035 | 6,040 | 6,044 | 5,419 | 5,162 | 5,149 |
| base filed: EBITDA (US$M) | 240 | 3,694 | 4,556 | 4,613 | 4,077 | 3,984 | 3,967 |
| base approval Q4 2027 (2027-10-01): US treated (patients/yr) | 165 | 2,040 | 2,875 | 3,000 | 3,000 | 2,875 | 2,833 |
| base approval Q4 2027 (2027-10-01): revenue (US$M) | 360 | 4,115 | 5,790 | 6,044 | 5,448 | 5,226 | 5,151 |
| base approval Q4 2027 (2027-10-01): EBITDA (US$M) | -24.2 | 2,949 | 4,351 | 4,613 | 4,100 | 4,037 | 3,968 |
| base entrants = 30% of incidence: US treated (patients/yr) | 330 | 2,500 | 1,466 | 927 | 910 | 909 | 909 |
| base entrants = 30% of incidence: revenue (US$M) | 690 | 5,035 | 2,973 | 1,899 | 1,685 | 1,686 | 1,689 |
| base entrants = 30% of incidence: EBITDA (US$M) | 240 | 3,694 | 2,040 | 1,172 | 985 | 1,068 | 1,064 |
| bull filed: US treated (patients/yr) | 880 | 4,500 | 3,500 | 3,500 | 3,500 | 3,500 | 3,500 |
| bull filed: revenue (US$M) | 2,142 | 9,930 | 8,594 | 8,774 | 8,778 | 8,397 | 8,016 |
| bull filed: EBITDA (US$M) | 1,433 | 7,721 | 6,689 | 6,931 | 7,035 | 6,868 | 6,546 |
| bull approval Q4 2027 (2027-10-01): US treated (patients/yr) | 440 | 3,815 | 3,750 | 3,500 | 3,500 | 3,500 | 3,500 |
| bull approval Q4 2027 (2027-10-01): revenue (US$M) | 1,086 | 9,366 | 9,134 | 8,774 | 8,778 | 8,397 | 8,016 |
| bull approval Q4 2027 (2027-10-01): EBITDA (US$M) | 562 | 7,374 | 7,140 | 6,931 | 7,035 | 6,868 | 6,546 |
| bull entrants = 30% of incidence: US treated (patients/yr) | 880 | 4,037 | 1,365 | 1,392 | 1,392 | 1,392 | 1,392 |
| bull entrants = 30% of incidence: revenue (US$M) | 2,142 | 8,931 | 3,983 | 4,221 | 4,224 | 3,844 | 3,463 |
| bull entrants = 30% of incidence: EBITDA (US$M) | 1,433 | 6,899 | 2,842 | 3,080 | 3,131 | 2,922 | 2,599 |

## v10 -> v11

| base (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| US patients treated, v10 (patients/yr) | 0 | 40 | 665 | 2,365 | 4,329 | 1,957 | 1,124 | 1,124 |
| US patients treated, v11 (patients/yr) | 0 | 330 | 2,500 | 3,000 | 3,000 | 2,984 | 2,840 | 2,832 |
| Revenue, v10 (US$M) | 24.9 | 110 | 1,364 | 4,770 | 8,702 | 3,570 | 2,073 | 2,075 |
| Revenue, v11 (US$M) | 24.9 | 690 | 5,035 | 6,040 | 6,044 | 5,419 | 5,162 | 5,149 |
| EBITDA, v10 (US$M) | -161 | -237 | 723 | 3,503 | 6,790 | 2,544 | 1,390 | 1,386 |
| EBITDA, v11 (US$M) | -161 | 240 | 3,694 | 4,556 | 4,613 | 4,077 | 3,984 | 3,967 |

| bull (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| US patients treated, v10 (patients/yr) | 0 | 60 | 942 | 3,263 | 5,460 | 6,607 | 2,872 | 2,872 |
| US patients treated, v11 (patients/yr) | 0 | 880 | 4,500 | 3,500 | 3,500 | 3,500 | 3,500 | 3,500 |
| Revenue, v10 (US$M) | 24.9 | 174 | 2,472 | 8,084 | 13,008 | 15,489 | 7,041 | 6,660 |
| Revenue, v11 (US$M) | 24.9 | 2,142 | 9,930 | 8,594 | 8,774 | 8,778 | 8,397 | 8,016 |
| EBITDA, v10 (US$M) | -161 | -187 | 1,645 | 6,254 | 10,473 | 12,720 | 5,698 | 5,376 |
| EBITDA, v11 (US$M) | -161 | 1,433 | 7,721 | 6,689 | 6,931 | 7,035 | 6,868 | 6,546 |

| bear (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|---|
| Revenue, v10 (US$M) | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 50.0 | 52.2 |
| Revenue, v11 (US$M) | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 50.0 | 52.2 |
| EBITDA, v10 (US$M) | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -93.0 | -90.9 |
| EBITDA, v11 (US$M) | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -93.0 | -90.9 |

## Flags (volume-dependent v10 items)

Base/bull year-0 raises ($400M/$350M) were sized for the old path; with EBITDA positive from FY2027E minimum year-end cash is now base 293.2 / bull 243.2 (dry), so the raises are larger than needed but kept (David's v10 values). Bear raise $4900M (~3.1x market cap) driven by bear capex = base dollars (base capex now larger). Centers implied by CLPT capacity at 2/week: ~29 base, ~34-43 bull (opex $1.5M/center). Bull starts from the same 6,000 pool with unfiltered entrants (steady pool ~8,200), base entrants filtered x1.0045 to hold 6,000. m = 0.62 (stay ~1.6y) is shorter than the duration evidence (crossover 2 of 6 lost eligibility in ~1 year implies ~0.41/yr).

Scratch dry check (not a valuation):

```
v11 scratch dry check (read-only Finagle copy /workspace/out/finagle_scratch, dry11.py; NOT a valuation, Finagle bot not called)
base revenue [16.1, 24.92, 690.0, 5035.0, 6040.0, 6044.0, 5419.36, 5161.95, 5149.22, 5150.78, 5203.08]
base ebitda [-152.91, -160.92, 239.85, 3694.1, 4555.51, 4613.0, 4076.55, 3983.9, 3966.6, 3967.9, 4011.3]
base capex [0.44, 3.5, 3.5, 418.97, 515.07, 515.45, 455.72, 431.11, 429.89, 430.04, 435.04]
base da [0.22, 0.34, 9.41, 68.65, 82.36, 82.41, 73.89, 70.38, 70.21, 70.23, 70.95]
base cash [480.24, 293.17, 680.2, 6406.92, 9656.51, 12080.41, 13588.76, 15545.23, 17572.73, 19620.88, 21736.47]
base debt [49.7, 49.7, 239.85, 3694.1, 4555.51, 4613.0, 4076.55, 3983.9, 3966.6, 3967.9, 4011.3]
base min cash 293.17, min D&A 0.22
bull revenue [16.1, 24.92, 2142.0, 9930.5, 8594.5, 8774.0, 8777.5, 8396.76, 8015.78, 8017.35, 8098.31]
bull ebitda [-152.91, -160.92, 1433.38, 7721.31, 6689.32, 6931.29, 7035.13, 6868.34, 6545.53, 6546.89, 6616.98]
bull capex [0.44, 3.5, 3.5, 932.66, 773.27, 794.69, 795.1, 749.68, 704.23, 704.42, 714.08]
bull da [0.22, 0.34, 29.21, 135.4, 117.19, 119.64, 119.68, 114.49, 109.3, 109.32, 110.42]
bull cash [430.24, 243.17, 2797.87, 13442.5, 15739.18, 19538.48, 23258.21, 26634.07, 29684.98, 33084.79, 36592.86]
bull debt [49.7, 49.7, 1433.38, 7721.31, 6689.32, 6931.29, 7035.13, 6868.34, 6545.53, 6546.89, 6616.98]
bull min cash 243.17, min D&A 0.22
bear revenue [16.1, 24.92, 30.0, 35.0, 40.0, 44.0, 47.5, 50.0, 52.25, 53.82, 55.16]
bear ebitda [-152.91, -160.92, -141.82, -117.12, -102.42, -98.66, -95.37, -93.03, -90.91, -89.44, -88.18]
bear capex [0.44, 3.5, 3.5, 418.97, 515.07, 515.45, 455.72, 431.11, 429.89, 430.04, 435.04]
bear da [0.22, 111.78, 176.09, 239.35, 302.6, 353.21, 397.48, 429.11, 457.58, 477.41, 494.43]
bear cash [4980.24, 4793.17, 4625.21, 4066.47, 3426.34, 2789.58, 2215.83, 1669.05, 1125.6, 583.47, 37.61]
bear debt [49.7, 49.7, 49.7, 49.7, 49.7, 49.7, 49.7, 49.7, 49.7, 49.7, 49.7]
bear min cash 37.61, min D&A 0.22
bear raise $4900M (v10 $3250M)
```

## Assumptions to revise

1. m = 0.62 [P] [P9]: the main lever; at m = 0.40 base treated falls to ~1,850/yr long run if the 6,000 needs a filter on entrants.
2. CLPT capacity ramp [S] [S6]: binds through FY30E base, every year bull.
3. Price $2.0M and -10% step [S] [S10].
4. Bull start pool 6,000 with unfiltered entrants [S] [C3].
5. COGS [S12], commercial fixed and per-center opex [S].

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
- D31: David May direct messages 2026-10-30 (t92u-t97u: pool model; 'Write is up with m=0.62 its the most internally consistent'; t98u 'Redo the finagle too'). n/a: user prompt in chat. HTML; no page numbers
- D32: Forecaster CLPT case, forecasts/CLPT/forecast.md (AMT-130 capacity ramp 330 / 2,500 / 3,000 base, 880 / 4,500 / 3,500 bull) [S], uncommitted local case. n/a: local forecaster case file /workspace/forecaster-work/forecaster-main/forecasts/CLPT/forecast.md. HTML; no page numbers
- D33: uniQure, update on Phase I/II AMT-130 trials: 4 of 6 high-dose controls crossed over, 2 failed inclusion criteria (link unverified, search result). https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-update-phase-iii-clinical-trials-amt-130-gene. HTML; no page numbers
- D29: David May direct messages 2026-10-30 (rev2b: t57u ClearPoint centers; 'Adjust as necessary and then send for finagle valuation'). n/a: user prompt in chat. HTML; no page numbers
