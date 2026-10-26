"""ClearPoint Neuro (Nasdaq: CLPT) forecast, FY26E-FY32E (v4: explicit to bemdaneprocel steady state; v3 capacity ramp to incidence-based steady state, $20k [P2]). USD millions.

Scenario per the prompt [P]: uniQure's AMT-130 (Huntington's) and BlueRock's bemdaneprocel
(Parkinson's) are approved and drive a new commercial drug delivery line. Timing and volume
of those approvals are judgments [S] and are listed in forecast.md.
Every fact carries a tag plus a source id (A1, G1, E1, P1, S1, C1...) resolved in forecast.md.
Run: python3 build_forecast.py
"""
import json
from pathlib import Path

OUT = Path(__file__).with_name("forecast.json")
K10 = "https://www.sec.gov/Archives/edgar/data/1285550/000119312526111231/clpt-20251231.htm"
Q10 = "https://www.sec.gov/Archives/edgar/data/1285550/000119312526330842/clpt-20260630.htm"
R26Q2 = "https://www.sec.gov/Archives/edgar/data/1285550/000119312526330541/clpt-ex99_1.htm"
R25Q4 = "https://www.sec.gov/Archives/edgar/data/1285550/000119312526110780/clpt-ex99_1.htm"
R24Q4 = "https://www.sec.gov/Archives/edgar/data/1285550/000095017025027716/clpt-ex99_1.htm"
TQ2 = "https://seekingalpha.com/article/4929731-clearpoint-neuro-inc-clpt-q2-2026-earnings-call-transcript"
EQ = "https://equibles.com/stocks/clpt/analyst-estimates"
QURE = "https://www.sec.gov/Archives/edgar/data/1590560/000110465926104463/qure-20260902x8k.htm"
QURE_PR = "https://www.biopharmadive.com/news/uniqure-submit-fda-approval-huntingtons-gene-therapy/829400/"
CTG = "https://clinicaltrials.gov/study/NCT06944522"
PROMPT = "prompt:t342u"

LINES = ["Biologics and drug delivery", "Neurosurgery navigation and therapy", "Capital equipment and software"]
CALN = "Preclinical services uplift, CAL GLP facility [scenario]"
NEW = "Commercial drug delivery (AMT-130, one-time Parkinson's cell/gene therapy class) [scenario]"
FY24 = dict(zip(LINES, (17.310, 10.285, 3.795)))
FY25 = dict(zip(LINES, (19.040, 14.831, 3.100)))
H1_25 = dict(zip(LINES, (9.430, 6.709, 1.561)))
H1 = dict(zip(LINES, (8.839, 11.439, 2.730)))
Q2 = dict(zip(LINES, (4.031, 5.552, 1.297)))
H2_25 = {n: FY25[n] - H1_25[n] for n in LINES}
REV24, REV25, H1_REV = 31.390, 36.971, 23.008
GP25, H1_GP = 22.692, 14.466
# Finagle basis EBITDA (before SBC): operating loss + D&A + SBC (+ intangible amortization in 2026)
EBITDA25 = -24.164 + 0.814 + 8.180
H1_EBITDA = -18.722 + 0.236 + 1.007 + 4.489
H1_OPEX = H1_GP - H1_EBITDA          # cash operating cost, H1 2026 [C]
GM = H1_GP / H1_REV                  # trailing gross margin [A]/[C]

# FY2025 original guidance position (2a)
LO25, HI25 = 36.0, 41.0
C25 = (REV25 - LO25) / (HI25 - LO25)

# unscaled line drivers [S]
H2_U = {LINES[0]: H2_25[LINES[0]] * 1.05,      # S1: CAL services return BDD to growth in Q3
        LINES[1]: 2 * Q2[LINES[1]] * 1.03,      # S2: Q2 run rate x2, slight growth (OR 3.0 software, IRRAflow)
        LINES[2]: H1[LINES[2]]}                 # S3: H1 run rate, lumpy capital
G27 = {LINES[0]: 0.12, LINES[1]: 0.12, LINES[2]: 0.05}   # S4-S6
CONS = {"base": (49.0, 56.55), "bear": (48.0, 56.0), "bull": (50.0, 57.1)}   # E1
G28_CORE = {"base": 0.12, "bear": 0.08, "bull": 0.15}                     # S7

# ---- approved-therapy line, v2 (2026-10-23, approved by David [P2]) ----
TQURE = "https://cdn.craft.cloud/fe68e1a2-b284-4f69-ba29-921f065edf17/assets/uploads/AMT-130-Pivotal-Sept-2025_final_09.24.25.pdf"
INC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC6579693/"
REUT = "https://www.reuters.com/business/healthcare-pharmaceuticals/parkinsons-disease-forefront-bayer-bet-cell-gene-therapies-2025-09-25/"
PRICE = 0.020                     # P2: $20k per procedure, both therapies, all cases
POOL = 6000                       # uniQure 'initial treatable patients at launch' (management estimate) [D17]
US_POP_M = 335.0                  # S28 judgment: approx. US population, millions
INCID = 1.22e-5                   # US age-adjusted HD incidence per person-year (Bruzelius 2019) [D18]
ELIG_SHARE = 6000 / 20000         # treatable / diagnosed in uniQure deck (C21)
NEW_ELIG = US_POP_M * 1e6 * INCID * ELIG_SHARE   # C22: newly eligible per year, ~1,226
PERIODS = ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"]   # v4: to bemdaneprocel steady state (David t350u)
LAST = PERIODS[-1]
CORE_G = {"base": 0.15, "bear": 0.08, "bull": 0.18}   # v6: base at low end of Burnett's 15-20% (G12), = FY27 consensus growth            # S7 FY28 and S26 FY29-30 core growth
PROC_GM = 0.70                    # S23 judgment: gross margin on procedure revenue
VAR_OPEX = 0.10                   # S24 judgment: clinical specialist cost, share of procedure revenue
FIX_OPEX = 2.0                    # S25 judgment: $M per therapy per year from launch year (field team)


# v3 (David t347u): AMT-130 steady state follows a share of HD incidence -> ~3,000/yr from FY30 [S30]
US_HD_INC = US_POP_M * 1e6 * INCID                 # C23: ~4,087 new US HD cases/yr
UK_POP_M = 68.0                                    # S28 judgment: approx. UK population, millions
UK_INC = 0.67e-5                                   # UK incidence 0.67/100k (Wexler 2016, in meta-analysis) [A8]
USUK_HD_INC = US_HD_INC + UK_POP_M * 1e6 * UK_INC  # C24: ~4,543 (US + UK, the two filed markets)
AMT_SS = {"base": 3000, "bull": 3500, "bear": 3000}              # S30
AMT_SS_PCT_US = {k: v / US_HD_INC for k, v in AMT_SS.items()}     # C25
AMT_SS_PCT_USUK = {k: v / USUK_HD_INC for k, v in AMT_SS.items()}
PD_INC = 90000                                     # US PD diagnoses/yr (Parkinson's Foundation / Willis 2022) [A9]
DBS_PD = 3990                                      # US inpatient DBS for PD, 2019 (NIS, Table 4) [A10]
# v7 (David t393-t396): PD class demand from the label-style eligible-pool model (partners/pd_simple2_model.py, report Appendix C)
_POOL = json.load(open(Path(__file__).with_name("partners") / "pd_simple4_model.json"))   # v10 (David t414u): 180k pool, DBS not exclusive
PD_CLASS = {"FY%02dE" % (r["t"] % 100): round(r["T"]) for r in _POOL["rows"]}   # C40: one-time treated = 6% of pool from FY29 (S45); DBS not deducted (S44)
PD_PREV_2026 = _POOL["inputs"]["P26"]             # C41: interpolated from A15/A16
POOL_2026 = _POOL["chain"]["U0"]                  # C42: medically eligible pool FY2026 (DBS patients included)
BULL_U = 0.08                                     # S59 v10: bull treated share 8%
PD_CLASS_BULL = {"FY%02dE" % (r["t"] % 100): round(r["T"]) for r in _POOL["bull_u08"]}   # C46
PD_CLASS_BEAR = {"FY%02dE" % (r["t"] % 100): round(r["T"]) for r in _POOL["bear_trial_excl"]}   # C50: prior-DBS excluded (pool 137,813)
PD_CLASS_CASE = {"base": PD_CLASS, "bull": PD_CLASS_BULL, "bear": PD_CLASS_BEAR}
BR_CAP = {"bear": 4500}      # S43: bear capacity 4,500; base/bull demand-driven (S61)
import os
LUMP = True   # S62: one-time PD class line
RAMP_SHARE = (0, 0, 1/3, 2/3, 1, 1)   # S64 (David t415u/t416u): 3-year ramp to class demand from FY29 launch
BEAR_RAMP = (0, 0, 0, 330, 2500, 4500)
def br_vol(key):
    if key == "bear": return {y: min(v, PD_CLASS_BEAR[y]) for y, v in zip(PERIODS, BEAR_RAMP)}
    return {y: round(f * PD_CLASS_CASE[key][y]) for y, f in zip(PERIODS, RAMP_SHARE)}
BR_SS = {"base": PD_CLASS["FY33E"], "bull": PD_CLASS_BULL["FY33E"], "bear": min(4500, PD_CLASS_BEAR["FY33E"])}   # FY33 = class demand (bear capacity)
BR_SS_PCT = {k: v / PD_INC for k, v in BR_SS.items()}
# v5 CAL (ClearPoint Advanced Laboratories, GLP preclinical CRO, Torrey Pines): incremental BDD revenue above core growth (S37)
CAL = {"base": (0.0, 7.0, 14.0, 22.0, 29.0, 36.0),    # v6: 60% of capacity by FY32    # FY27 inside consensus; large GLP studies from H2'27 (G10); ~50% of $60M capacity by FY32 (G9)
       "bull": (3.0, 10.0, 18.0, 27.0, 36.0, 45.0),   # Burnett: CAL could accelerate above high-teens 2027 growth (G9); 75% of capacity FY32
       "bear": (0.0, 2.0, 4.0, 6.0, 8.0, 10.0)}       # GLP slow to fill; ~1 mid-size study a year
CAL_OPEX = 0.20          # S38 judgment: incremental opex per CAL revenue dollar (lease/staff largely in core opex, G9 'built into that cost structure')


def amt_vol(key):
    if key == "base":   # S20 ramp; FY29 = rest of 6,000 pool; FY30 = steady state S30
        v27, v28 = 330, 2500
        v29 = min(4500, POOL - v27 - v28)
        v30 = AMT_SS["base"]
        v31 = v32 = AMT_SS["base"]
    elif key == "bull": # S21: faster ramp, cap FY28; FY29 = rest of pool + one year of steady-state flow (cap 4,500)
        v27 = 880
        v28 = min(4500, POOL - v27)
        v29 = min(4500, POOL - v27 - v28 + AMT_SS["bull"])
        v30 = AMT_SS["bull"]
        v31 = v32 = AMT_SS["bull"]
    else:               # S22 v3: slow, demand-limited launch (~270 in FY28, per the earlier top-down proposal)
        v27, v28, v29, v30, v31, v32 = 0, 270, 1000, 1800, 2300, 2700   # S22/S32 v5: slower ramp, steady 3,000 in FY33
    return dict(zip(PERIODS, (v27, v28, v29, v30, v31, v32)))


SC = {
    "base": dict(opex_h2=-0.02, opex27=0.06, opex_g=0.05, mc=0.50, gsnext=0.12),
    "bull": dict(opex_h2=-0.02, opex27=0.06, opex_g=0.05, mc=0.55, gsnext=0.15),
    "bear": dict(opex_h2=0.0, opex27=0.10, opex_g=0.07, mc=0.45, gsnext=0.08),
}


def fact(v, tag, sid, text, url, page=None):
    if isinstance(v, float):
        v = round(v, 6)
    if isinstance(v, list):
        v = [round(x, 6) for x in v]
    c = {"id": sid, "text": text, "url": url}
    if page is not None:
        c["page"] = page
    return {"value": v, "tag": tag, "citation": c}


def scenario(key):
    p = SC[key]
    r26, r27c = CONS[key]
    h2t = r26 - H1_REV
    k26 = h2t / sum(H2_U.values())
    h2 = {n: H2_U[n] * k26 for n in LINES}
    fy = {"FY26E": {n: H1[n] + h2[n] for n in LINES}}
    f27u = {n: fy["FY26E"][n] * (1 + G27[n]) for n in LINES}
    k27 = r27c / sum(f27u.values())
    fy["FY27E"] = {n: f27u[n] * k27 for n in LINES}
    for prev, cur in zip(PERIODS[:-1], PERIODS[1:]):
        fy[cur] = {n: fy[prev][n] * (1 + CORE_G[key]) for n in LINES}
    av, bv = amt_vol(key), br_vol(key)
    fy["FY26E"][NEW] = 0.0
    fy["FY26E"][CALN] = 0.0
    h2[NEW] = 0.0
    core_opex = {}
    opex_h2 = H1_OPEX * (1 + p["opex_h2"])
    core_opex["FY27E"] = 2 * opex_h2 * (1 + p["opex27"])
    for prev, cur in zip(PERIODS[:-1], PERIODS[1:]):
        core_opex[cur] = core_opex[prev] * (1 + p["opex_g"])
    rev, e, proc, popex = {"FY26E": r26}, {}, {}, {}
    e["FY26E"] = H1_EBITDA + h2t * GM - opex_h2
    for per in PERIODS:
        cal = CAL[key][PERIODS.index(per)]
        fy[per][CALN] = cal
        pr = (av[per] + bv[per]) * PRICE
        fy[per][NEW] = pr
        proc[per] = pr
        n_th = (av[per] > 0) + (bv[per] > 0)
        popex[per] = VAR_OPEX * pr + FIX_OPEX * n_th + CAL_OPEX * cal
        core = sum(fy[per][n] for n in LINES) + cal
        rev[per] = core + pr
        e[per] = core * GM + pr * PROC_GM - core_opex[per] - popex[per]
    seq = ["FY26E"] + PERIODS
    gf = [e["FY26E"] / EBITDA25 - 1] + [e[seq[i]] / e[seq[i - 1]] - 1 for i in range(1, len(seq))]
    sg = [r26 / REV25 - 1] + [rev[seq[i]] / rev[seq[i - 1]] - 1 for i in range(1, len(seq))]
    return dict(key=key, p=p, rev=rev, r26=r26, r27c=r27c, k26=k26, k27=k27, h2=h2, fy=fy, av=av, bv=bv, proc=proc,
                popex=popex, opex_h2=opex_h2, core_opex=core_opex, e=e, gf=gf, sg=sg)


def lines(s):
    out = []
    for i, n in enumerate(LINES):
        per = {
            "FY24A": fact(FY24[n], "A", "A2", "FY2024 column, disaggregated revenue, 2025 Form 10-K (Note 2 / MD&A).", K10),
            "FY25A": fact(FY25[n], "A", "A2", "FY2025 column, disaggregated revenue, 2025 Form 10-K.", K10),
            "YoY": fact(FY25[n] / FY24[n] - 1, "C", "C1", "FY25A / FY24A - 1 (A2).", K10),
            "H1A": fact(H1[n], "A", "A4", "Six months ended June 30, 2026, disaggregated revenue, Q2 2026 Form 10-Q.", Q10),
            "H2E": fact(s["h2"][n], "S", "S%d" % (i + 1), "Unscaled H2 driver x scale C4 (see forecast.md).", R26Q2),
            "FY26E": fact(s["fy"]["FY26E"][n], "C", "C5", "H1A (A4) + H2E.", Q10),
            "FY27E": fact(s["fy"]["FY27E"][n], "S", "S%d" % (i + 4), "FY26E x (1 + driver growth) x scale C6.", TQ2),
            "FY28E": fact(s["fy"]["FY28E"][n], "S", "S7", "FY27E x (1 + core growth S7). No consensus for FY28.", TQ2),
        }
        for y in PERIODS[2:]:
            per[y] = fact(s["fy"][y][n], "S", "S26" if y in ("FY29E", "FY30E") else "S32", "Prior year x (1 + core growth S26, judgment). No consensus.", TQ2)
        out.append({"name": n, "periods": per})
    per = {
        "FY24A": fact(0.0, "A", "A2", "No commercial (approved-product) drug delivery revenue reported.", K10),
        "FY25A": fact(0.0, "A", "G3", "Management: 2026 guidance 'does not include any meaningful expected revenue from commercial drug delivery'.", TQ2),
        "H1A": fact(0.0, "A", "A4", "None reported in H1 2026.", Q10),
        "H2E": fact(0.0, "S", "S8", "AMT-130 action date no earlier than late Apr/early May 2027 (uniQure).", QURE_PR),
        "FY26E": fact(0.0, "C", "C5", "H1A + H2E.", Q10),
    }
    for y in PERIODS:
        per[y] = fact(s["proc"][y], "P", "P2", "Prompt P1 (approved) + P2 ($20k, full ClearPoint capacity): AMT-130 %d + one-time PD class %d procedures x $20k (S20-S22, G7)." % (s["av"][y], s["bv"][y]), PROMPT)
    out.append({"name": NEW, "periods": per})
    per = {"FY24A": fact(0.0, "A", "A2", "No CAL facility before the June 2025 lease (inside BDD line).", K10),
           "FY25A": fact(0.0, "A", "A2", "Lease signed June 2025; first sponsor study 2025, in BDD line (D7).", K10),
           "H2E": fact(0.0, "G", "G10", "No large CAL study in H2 2026 guidance; first GLP SOW to complete H1 2027.", TQ2),
           "H1A": fact(0.0, "A", "A4", "CAL revenue so far reported inside BDD; Q2 miss 'attributed to a delayed ramp of these preclinical CAL services' (G9).", TQ2),
           "FY26E": fact(0.0, "G", "G10", "FY26 guidance 'does not include the execution of any of these large studies'.", TQ2)}
    for y in PERIODS:
        per[y] = fact(s["fy"][y][CALN], "S", "S37", "CAL GLP uplift above core BDD growth (judgment; capacity >$60M vs ~$8M before, G9; large studies from H2 2027, G10; single large GLP study $15-20M, G11).", TQ2)
    out.append({"name": CALN, "periods": per})
    return out


def totals(s):
    R = {
        "FY24A": fact(REV24, "A", "A1", "Total revenue 2024, 2025 Form 10-K.", K10),
        "FY25A": fact(REV25, "A", "A1", "Total revenue 2025, 2025 Form 10-K.", K10),
        "YoY": fact(REV25 / REV24 - 1, "C", "C1", "A1 FY25 / FY24 - 1.", K10),
        "H1A": fact(H1_REV, "A", "A4", "Total revenue six months ended June 30, 2026.", Q10),
        "H2E": fact(s["r26"] - H1_REV, "C", "C3", "E1 FY26 consensus - A4.", EQ),
        "FY26E": fact(s["r26"], "E", "E1", "%s FY26 revenue consensus, Equibles (2 analysts), captured 2026-09-30." % s["key"], EQ),
        "FY27E": fact(s["rev"]["FY27E"], "C", "C7", "E1 FY27 core consensus %.2f + procedure line P2." % s["r27c"], EQ),
    }
    for y in PERIODS[1:]:
        R[y] = fact(s["rev"][y], "C", "C7", "Sum of lines (core S7/S26 + CAL S37 + procedure line P2).", EQ)
    GMd = {"FY25A": fact(GP25 / REV25, "C", "C8", "Gross profit 22.692 / revenue 36.971, 2025 Form 10-K.", K10),
           "H1A": fact(GM, "C", "C8", "Gross profit 14.466 / revenue 23.008, H1 2026 (A5).", R26Q2),
           "FY26E": fact((H1_GP + (s["r26"] - H1_REV) * GM) / s["r26"], "S", "S13", "H2 at trailing H1 gross margin.", R26Q2)}
    for y in PERIODS:
        core = s["rev"][y] - s["proc"][y]
        GMd[y] = fact((core * GM + s["proc"][y] * PROC_GM) / s["rev"][y], "S", "S23", "Core at 62.9% (S13) + procedure revenue at 70% (S23, judgment; 10-K says disposables are 'high margin', no % disclosed).", K10)
    E = {"FY25A": fact(EBITDA25, "C", "A3", "Operating loss -24.164 + D&A 0.814 + SBC 8.180 (2025 10-K; Finagle build_baseline basis, before SBC).", K10),
         "H1A": fact(H1_EBITDA, "C", "C2", "H1 2026 operating loss -18.722 + D&A 0.236 + intangible amortization 1.007 + SBC 4.489 (A5).", R26Q2),
         "FY26E": fact(s["e"]["FY26E"], "C", "C9", "H1A + H2 revenue x gross margin - H2 cash opex (S14). No EBITDA guidance or consensus.", R26Q2)}
    for y in PERIODS:
        E[y] = fact(s["e"][y], "S", "S15", "Core GP + procedure GP - core opex (S15/S16) - procedure opex (S24/S25).", R26Q2)
    OP = {"H1A": fact(H1_OPEX, "C", "C2", "H1 gross profit 14.466 - H1 EBITDA (C2).", R26Q2),
          "H2E": fact(s["opex_h2"], "S", "S14", "H1 run rate x (1 %+.0f%%): 'operational cash burn to decrease in the second half'." % (s["p"]["opex_h2"] * 100), R26Q2)}
    for y in PERIODS:
        OP[y] = fact(s["core_opex"][y] + s["popex"][y], "S", "S16", "Core opex (FY27 2xH2 x (1+%.0f%%), then +%.0f%%/yr) + procedure opex %.3f (S24/S25)." % (s["p"]["opex27"] * 100, s["p"]["opex_g"] * 100, s["popex"][y]), R26Q2)
    seq = ["FY25A", "FY26E"] + PERIODS
    EM = {"FY25A": fact(EBITDA25 / REV25, "C", "C10", "EBITDA / revenue.", R26Q2), "H1A": fact(H1_EBITDA / H1_REV, "C", "C10", "EBITDA / revenue.", R26Q2)}
    for y in ["FY26E"] + PERIODS:
        EM[y] = fact(s["e"][y] / s["rev"][y], "C", "C10", "EBITDA / revenue.", R26Q2)
    return {"revenue": R, "gross_margin": GMd, "ebitda": E, "ebitda_margin": EM, "cash_opex": OP,
            "procedures": {y: fact(s["av"][y] + s["bv"][y], "S", "S20", "AMT-130 %d + one-time Parkinson's cell/gene therapy procedures (class) %d." % (s["av"][y], s["bv"][y]), TQ2) for y in PERIODS}}


def organic_and_leaves(s):
    p = s["p"]
    org = {"revenue": {"FY25A": fact(REV25, "A", "A1", "Organic = total; IRRAS closed Nov 2025 (inside year 0); no future deal.", K10),
                       "FY26E": fact(s["r26"], "E", "E1", "Organic = total.", EQ)},
           "ebitda": {"FY25A": fact(EBITDA25, "C", "A3", "Organic = total.", K10),
                      "FY26E": fact(s["e"]["FY26E"], "C", "C9", "Organic = total.", R26Q2)}}
    for y in PERIODS:
        org["revenue"][y] = fact(s["rev"][y], "C", "C7", "Organic = total.", EQ)
        org["ebitda"][y] = fact(s["e"][y], "S", "S15", "Organic = total.", R26Q2)
    fin = {"ebitda_growth": fact(s["gf"], "C", "C11", "EBITDA growth FY26-FY32: ratio of consecutive EBITDA levels - 1 (sign changes make some rates large).", R26Q2),
           "sales_growth": fact(s["sg"], "C", "C11", "Revenue growth FY26-FY32.", EQ),
           "me": fact(s["e"][LAST] / s["rev"][LAST], "C", "C12", "FY32E EBITDA / FY32E revenue.", R26Q2),
           "mc": fact(p["mc"], "S", "S17", "Incremental EBITDA per incremental revenue dollar after FY32: procedure GM 70% less 10% specialists, blended with core.", R26Q2),
           "gsnext": fact((sum(s["fy"][LAST][n] for n in LINES) * CORE_G[s["key"]] + min(CAL[s["key"]][-1] - CAL[s["key"]][-2], 60.0 - CAL[s["key"]][-1]) + (AMT_SS[s["key"]] - s["av"][LAST] + BR_SS[s["key"]] - s["bv"][LAST]) * PRICE) / s["rev"][LAST], "C", "C29", "v5: FY33 growth = (FY32 core x core growth S26 + one more year of the FY32 CAL increment, capped at $60M G9, + procedures stepping to steady state S30/S31 if not yet there, bear only) / FY32 revenue; Finagle then fades it linearly to its default gt over FY34-FY45 (year=20).", TQ2),
           "ebitda_basis": "total",
           "acquisition_disclosure": {"status": "none"}}
    return org, fin


def main():
    S = {k: scenario(k) for k in ("base", "bull", "bear")}

    def block(s):
        org, fin = organic_and_leaves(s)
        return {"lines": lines(s), "totals": totals(s), "organic": org, "finagle": fin}

    payload = {"ticker": "CLPT", "company": "ClearPoint Neuro, Inc. (Nasdaq: CLPT)", "units": "USD millions",
               "baseline_period": "FY25A", "explicit_periods": ["FY26E"] + PERIODS, "as_of": "2026-10-23",
               "explicit_window_note": "Window extended to FY32E (David t350u, 2026-10-23) so bemdaneprocel reaches steady state inside the explicit years in all cases (base FY31, bull FY30, bear FY32). FY28E-FY32E rest on judgments; forecastcheck checks growth compounding only to FY28E.",
               **block(S["base"]),
               "bridge": {
                   "c_fy25_revenue": fact(C25, "C", "C13", "(36.971 - 36.0) / (41.0 - 36.0): FY25 original range $36.0-41.0M (G1).", R24Q4),
                   "fy26_guidance_low": fact(48.0, "G", "G2", "'adjusting our 2026 revenue guidance to between $48.0 - $52.0 million' (Aug 3, 2026; original $52.0-56.0M).", R26Q2),
                   "fy26_guidance_high": fact(52.0, "G", "G2", "Revised range high.", R26Q2),
                   "scale_h2": fact(S["base"]["k26"], "C", "C4", "Consensus H2 / unscaled H2 line build.", EQ),
                   "scale_fy27": fact(S["base"]["k27"], "C", "C6", "FY27 core consensus / unscaled FY27 line build.", EQ),
                   "unscaled_h2": fact(sum(H2_U.values()), "S", "S1", "Sum of S1-S3 drivers (diagnostic).", R26Q2),
                   "amt130_rev_per_procedure_range_low": fact(0.015, "G", "G4", "'$15,000 to $25,000 per procedure' for a typical uniQure procedure (Q2 2026 call).", TQ2),
                   "amt130_rev_per_procedure_range_high": fact(0.025, "G", "G4", "Same quote.", TQ2),
                   "partner_rev_per_patient_low": fact(0.012, "G", "G5", "'$12,000 to $15,000 range per patient' across pharma partners (Q2 2026 call).", TQ2),
                   "partner_rev_per_patient_high": fact(0.015, "G", "G5", "Same quote.", TQ2),
                   "price_per_procedure": fact(PRICE, "P", "P2", "David: all procedures at $20k, both therapies, all cases.", PROMPT),
                   "amt130_treatable_pool": fact(POOL, "G", "G8", "uniQure: '~6,000 patients* Initial Treatable Patients at Launch' (*management estimate), Sept 2025 deck p.25.", TQURE),
                   "hd_incidence_per_person_year": fact(INCID, "A", "A7", "Age-adjusted cumulative incidence 1.22 per 100,000 person-years, US insured cohort 2003-2016 (Bruzelius et al. 2019).", INC),
                   "new_eligible_per_year": fact(NEW_ELIG, "C", "C22", "US population 335M (S28) x 1.22/100k (A7) x treatable/diagnosed 6,000/20,000 (C21).", INC),
                   "us_hd_incidence_cases": fact(US_HD_INC, "C", "C23", "335M (S28) x 1.22/100k (A7).", INC),
                   "usuk_hd_incidence_cases": fact(USUK_HD_INC, "C", "C24", "C23 + 68M (S28) x 0.67/100k UK (A8).", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10086981/"),
                   "amt130_steady_state": fact(AMT_SS["base"], "S", "S30", "David: treated ~3,000/yr from FY30 = %.0f%% of US / %.0f%% of US+UK incident HD (C25)." % (AMT_SS_PCT_US["base"] * 100, AMT_SS_PCT_USUK["base"] * 100), PROMPT),
                   "pd_incidence_us": fact(PD_INC, "A", "A9", "'nearly 90,000 people are diagnosed with Parkinson's disease every year in the U.S.'", "https://www.parkinson.org/understanding-parkinsons/statistics/prevalence-incidence"),
                   "dbs_pd_per_year": fact(DBS_PD, "A", "A10", "NIS 2019: 3,990 DBS for PD (1.10% of PD discharges; 3,615-4,025 a year 2016-19), Table 4.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10898494/"),
                   "pd_class_fy33_volume": fact(BR_SS["base"], "S", "S31", "FY33 one-time PD class procedures = class demand (C40 %d base, C46 %d bull); bear capped at 4,500 capacity (S43; bear class demand C50 %d) = %s." % (PD_CLASS["FY33E"], PD_CLASS_BULL["FY33E"], PD_CLASS_BEAR["FY33E"], BR_SS), "https://doi.org/10.1038/s41531-018-0058-0"),
                   "pd_class_demand": fact([PD_CLASS[y] for y in PERIODS], "C", "C40", "FY27-32: eligible-pool model one-time treated (6% of opening pool from FY29, S45); DBS not deducted (S44); Appendix C.", "https://doi.org/10.1038/s41531-018-0058-0"),
                   "pd_untreated_pool_2026": fact(POOL_2026, "C", "C42", "Appendix C funnel: 1.104M x (0.729-0.28) x 0.50 x 0.806 x 0.90 = 179,813 (DBS patients included, S44).", "https://doi.org/10.1038/s41531-018-0058-0"),
                   "cal_capacity_quote": fact(60.0, "G", "G9", "Burnett: prior preclinical capacity '$8 million a year'; new CAL facility 'could surpass $60 million or so' (Q2 2026 call).", TQ2),
                   "capacity_quote": fact(4500, "G", "G7", "Burnett: 15 centres 'ready to do 1, if not 2' a week; 20-30 centres '50 to 100 cases a week' (Q2 2026 call); 4,500/yr = 30 centres x 3/wk x 50 wks (S20).", TQ2),
               },
               "scenarios": {"bull": block(S["bull"]), "bear": block(S["bear"])}}
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    for k, s in S.items():
        print(k, "rev", {y: round(v, 2) for y, v in s["rev"].items()}, "ebitda", {y: round(v, 2) for y, v in s["e"].items()},
              "amt", s["av"], "br", s["bv"], "k", round(s["k26"], 4), round(s["k27"], 4), "gf", [round(x, 3) for x in s["gf"]], "me", round(s["e"][LAST] / s["rev"][LAST], 4))
    print("BR_SS", BR_SS, "PD_CLASS", PD_CLASS, "BULL", PD_CLASS_BULL)

if __name__ == "__main__":
    main()
