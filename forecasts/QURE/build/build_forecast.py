"""v11 (rev4, 2026-10-30): build forecast.json (USD millions) under /workspace/out/QURE_run_v12/ from model.py (m = 0.62 pool model, CLPT ramp). Copy of the repo rev3 build_forecast.py; v10/rev3 files untouched."""
import json, pathlib
OUT = pathlib.Path("/workspace/out/QURE_run_v12/forecast.json")
H = "HTML; no page numbers"
DOCS = {
 "D1": ("uniQure Form 10-K FY2025 (filed 2026-03-02)", "https://www.sec.gov/Archives/edgar/data/1590560/000110465926021898/qure-20251231x10k.htm"),
 "D2": ("uniQure Form 10-Q Q2 2026 (filed 2026-07-29)", "https://www.sec.gov/Archives/edgar/data/1590560/000110465926087815/qure-20260630x10q.htm"),
 "D3": ("uniQure Q2 2026 results press release, 8-K Ex.99.1 (2026-07-29)", "https://www.sec.gov/Archives/edgar/data/1590560/000110465926087808/qure-20260729xex99d1.htm"),
 "D4": ("uniQure BLA submission press release, 8-K Ex.99.1 (2026-09-02)", "https://www.sec.gov/Archives/edgar/data/1590560/000110465926104463/qure-20260902xex99d1.htm"),
 "D5": ("uniQure four-year AMT-130 data press release, 8-K Ex.99.2 (2026-09-29)", "https://www.sec.gov/Archives/edgar/data/1590560/000110465926111654/tm2626514d1_ex99-2.htm"),
 "D6": ("Yahoo Finance / yfinance analyst revenue estimates for QURE, pulled 2026-10-29 (shown in EUR)", "https://finance.yahoo.com/quote/QURE/analysis/"),
 "D7": ("GEN StockWatch, Leerink net-price estimates and O'Keefe pricing/TAM comments (2025)", "https://www.genengnews.com/topics/translational-medicine/stockwatch-uniqure-shares-reach-five-year-high-on-game-changing-huntingtons-data/"),
 "D8": ("Clinaptis research, AMT-130 capacity ramp and net-price model", "https://www.clinaptisresearch.com/research/amt-130-huntingtons-uniqure-bla"),
 "D9": ("BioSpace, uniQure files for FDA, UK approval (2026-09)", "https://www.biospace.com/fda/uniqure-files-for-fda-uk-approval-of-first-gene-therapy-for-huntingtons-disease"),
 "D10": ("uniQure, Pivotal Phase I/II AMT-130 Huntington's Disease Update, investor presentation, slides 25-26 (2025-09-24)", "https://cdn.craft.cloud/fe68e1a2-b284-4f69-ba29-921f065edf17/assets/uploads/AMT-130-Pivotal-Sept-2025_final_09.24.25.pdf"),
 "D11": ("Medina et al., Prevalence and Incidence of Huntington's Disease: An Updated Systematic Review and Meta-Analysis, Movement Disorders 2022", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10086981/"),
 "D12": ("uniQure Q2 2026 earnings call transcript (Motley Fool, 2026-08-07)", "https://www.fool.com/earnings/call-transcripts/2026/08/07/uniqure-qure-q2-2026-earnings-call-transcript/"),
 "D13": ("uniQure Q1 2026 earnings call transcript (StockAnalysis)", "https://stockanalysis.com/stocks/qure/transcripts/578165-q1-2026/"),
 "D14": ("uniQure press release, sale of Lexington commercial manufacturing facility to Genezen (2024-07-01)", "https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-sale-commercial-manufacturing-facility-genezen"),
 "D15": ("US Census Bureau population clock (US resident population ~340 million)", "https://www.census.gov/popclock/"),
 "D16": ("Prompt: David May, direct message 2026-10-30", "n/a: user prompt (David May, direct message, 2026-10-30)"),
 "D17": ("Prompt: David May, direct messages 2026-10-30 (capacity-dependent short term; refill = incidence less a few)", "n/a: user prompt (David May, direct messages, 2026-10-30)"),
 "D18": ("EHDN Platform Meeting report, uniQure AMT-130 topline results (2025-12-04)", "https://ehdn.org/wp-content/uploads/2025/12/EHDN-Platform-Meeting-uniQure-Topline-Results-Report_Final_2-04-Dec-2025.pdf"),
 "D19": ("Sarepta ELEVIDYS label update call transcript, 2024-06-21 (StockAnalysis/Quartr)", "https://stockanalysis.com/stocks/srpt/transcripts/205218-status-update/"),
 "D20": ("Sarepta Q4 and FY2024 results, 8-K Ex.99.1 (2025-02-26) and preliminary release (2025-01-13)", "https://www.sec.gov/Archives/edgar/data/873303/000095017025027717/srpt-ex99_1.htm"),
 "D21": ("Sarepta 8-K 2023-06-22: ELEVIDYS US wholesale acquisition cost", "https://www.sec.gov/Archives/edgar/data/873303/000095017023029438/srpt-20230622.htm"),
 "D22": ("Investing.com, Goldman Sachs note summary on uniQure (2025-09)", "https://ph.investing.com/news/analyst-ratings/uniqure-stock-rises-after-positive-huntingtons-disease-gene-therapy-data-93CH-2010942"),
 "D23": ("Reuters, FDA approves Sarepta gene therapy (2023-06-22): Hemgenix list price", "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-sareptas-gene-therapy-rare-muscular-dystrophy-some-kids-2023-06-22/"),
 "D24": ("ClearPoint Neuro Q2 2026 earnings call transcript (2026-08-10, Motley Fool): CLEAR site-readiness program", "https://www.fool.com/earnings/call-transcripts/2026/08/10/clearpoint-neuro-clpt-q2-2026-earnings-call-transcript/"),
 "D25": ("ClearPoint Neuro Q3 2025 results press release, 8-K Ex.99.1 (2025-11-06)", "https://www.sec.gov/Archives/edgar/data/1285550/000119312525270019/clpt-ex99_1.htm"),
 "D26": ("ClearPoint Neuro Q3 2026 earnings call transcript (2026-10-28, StockAnalysis)", "https://stockanalysis.com/stocks/clpt/transcripts/722761-q3-2026/"),
 "D27": ("HDSA press release 2025-04-02: Centers of Excellence network expands to 69 sites", "https://hdsa.org/news/huntingtons-disease-society-of-america-awards-more-than-1-8-million-to-expand-hdsa-centers-of-excellence-network-to-sixty-nine-sites/"),
 "D28": ("IntuitionLabs, Most Expensive Drugs in the US: 2025 price list (secondary source for gene-therapy list prices)", "https://intuitionlabs.ai/articles/most-expensive-drugs-usa-2025"),
 "D30": ("David May direct message 2026-10-30 (t62u: centers do not limit capacity in year one; use the Kapusta bot's ~190 year-1 path)", "n/a: user prompt in chat"),
 "D31": ("David May direct messages 2026-10-30 (t92u-t97u: pool model; 'Write is up with m=0.62 its the most internally consistent'; t98u 'Redo the finagle too')", "n/a: user prompt in chat"),
 "D32": ("Forecaster CLPT case, forecasts/CLPT/forecast.md (AMT-130 capacity ramp 330 / 2,500 / 3,000 base, 880 / 4,500 / 3,500 bull) [S], uncommitted local case", "n/a: local forecaster case file /workspace/forecaster-work/forecaster-main/forecasts/CLPT/forecast.md"),
 "D33": ("uniQure, update on Phase I/II AMT-130 trials: 4 of 6 high-dose controls crossed over, 2 failed inclusion criteria (link unverified, search result)", "https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-update-phase-iii-clinical-trials-amt-130-gene"),
 "D29": ("David May direct messages 2026-10-30 (rev2b: t57u ClearPoint centers; 'Adjust as necessary and then send for finagle valuation')", "n/a: user prompt in chat"),
}
sources = [{"id": k, "text": "%s. %s. %s" % (v[0], v[1], H)} for k, v in DOCS.items()]
cnt = {}; seen = {}
def F(value, tag, text, doc, inputs=None, quote=None):
    key = (tag, repr(value), text)
    if key in seen:
        sid = seen[key]
    else:
        cnt[tag] = cnt.get(tag, 0) + 1; sid = "%s%d" % (tag, cnt[tag]); seen[key] = sid
        e = {"id": sid, "document": doc, "page_status": "unverified", "text": quote or text}
        if tag == "C": e["inputs"] = inputs or []
        sources.append(e)
    return {"value": value, "tag": tag, "citation": {"id": sid, "text": text, "url": DOCS[doc][1], "page_status": "unverified"}}
r = lambda x: round(x, 6)

# ---------- actuals [A] ----------
A = dict(lic24=10.133, lic25=15.934, col24=10.872, col25=0.164, cm24=6.114, cm25=0.0,
         rev24=27.119, rev25=16.098, h1=9.403, cogs_h1=0.569, cogs25=1.686,
         op24=-184.294, da24=12.641, sbc24=22.258, op25=-185.349, da25=14.759, sbc25=17.679,
         oph1=-97.923, dah1=7.863, sbch1=10.106, opq2=-52.203, daq2=4.907, sbcq2=5.016, revq2=5.841, cogsq2=0.350)
fA = lambda k, t, d: F(A[k], "A", t, d, quote=t)
ebitda24 = A["op24"] + A["da24"] + A["sbc24"]; ebitda25 = A["op25"] + A["da25"] + A["sbc25"]
ebitdah1 = A["oph1"] + A["dah1"] + A["sbch1"]
ebitdaq2 = A["opq2"] + A["daq2"] + A["sbcq2"]
gpq2 = A["revq2"] - A["cogsq2"]
opexq2 = gpq2 - ebitdaq2            # cash opex net of other income/expense
gm_lic = (A["h1"] - A["cogs_h1"]) / A["h1"]


# ---------- pre-register core facts so C entries can cite real IDs ----------
def sid(f): return f["citation"]["id"]
ID = {}
ID["lic24"] = sid(F(A["lic24"], "A", "License revenues 2024 $10,133k", "D1", quote="License revenues $ 15,934 $ 10,133 $ 2,758"))
ID["lic25"] = sid(F(A["lic25"], "A", "License revenues 2025 $15,934k", "D1", quote="License revenues $ 15,934 $ 10,133 $ 2,758"))
ID["col24"] = sid(F(A["col24"], "A", "Collaboration revenues 2024 $10,872k", "D1", quote="Collaboration revenues 164 10,872 2,250"))
ID["col25"] = sid(F(A["col25"], "A", "Collaboration revenues 2025 $164k", "D1", quote="Collaboration revenues 164 10,872 2,250"))
ID["cm24"] = sid(F(A["cm24"], "A", "Contract manufacturing revenues 2024 $6,114k", "D1", quote="Contract manufacturing revenues — 6,114 10,835"))
ID["rev24"] = sid(F(A["rev24"], "A", "Total revenues 2024 $27,119k", "D1", quote="Total revenues $ 16,098 $ 27,119 $ 15,843"))
ID["rev25"] = sid(F(A["rev25"], "A", "Total revenues 2025 $16,098k", "D1", quote="Total revenues $ 16,098 $ 27,119 $ 15,843"))
ID["h1"] = sid(F(A["h1"], "A", "License revenues six months ended June 30, 2026 $9,403k", "D2", quote="License revenues $ 5,841 $ 5,262 $ 9,403 $ 6,829"))
ID["ops25"] = sid(F([A["op24"], A["da24"], A["sbc24"], A["op25"], A["da25"], A["sbc25"]], "A", "Loss from operations, D&A, SBC for 2024 and 2025 (op loss -184,294/-185,349; D&A 12,641/14,759; SBC 22,258/17,679)", "D1", quote="Depreciation and amortization 14,759 12,641 ... Share-based compensation expense 17,679 22,258"))
ID["opsh1"] = sid(F([A["oph1"], A["dah1"], A["sbch1"], A["cogs_h1"]], "A", "H1 2026 loss from operations -97,923; D&A 7,863; SBC 10,106; cost of license revenues 569", "D2", quote="Loss from operations ( 52,203 ) ( 43,865 ) ( 97,923 ) ... Depreciation and amortization 7,863 ... Share-based compensation expense 10,106"))
ID["opsq2"] = sid(F([A["revq2"], A["cogsq2"], A["opq2"], A["daq2"], A["sbcq2"]], "A", "Q2 2026 revenue 5,841; cost of license revenues 350; loss from operations -52,203; D&A 4,907; SBC 5,016", "D2", quote="Segment reconciliation Q2 2026: Depreciation and amortization expense ( 4,907 ) Share-based compensation expense ( 5,016 )"))
ID["yago"] = sid(F(13.62374, "E", "Yahoo FY25 'year ago revenue' EUR 13.624M", "D6", quote="0y yearAgoRevenue 13623740 EUR"))
ID["c26eur"] = sid(F(21.08642, "E", "FY26 mean revenue consensus EUR 21.086M, 12 analysts, pulled 2026-10-29", "D6", quote="0y avg 21086420 EUR, 12 analysts"))
ID["c27eur"] = sid(F(96.184, "E", "FY27 mean revenue consensus EUR 96.184M, 11 analysts (range 12.653-299.146), pulled 2026-10-29", "D6", quote="+1y avg 96184000 EUR, low 12653000, high 299146000, 11 analysts"))

# ---------- consensus [E] ----------
fx = 16.098 / 13.62374  # C   # USD per EUR implied by Yahoo FY25 'year ago revenue' vs reported
cons26 = 21.08642 * fx; cons27 = 96.184 * fx


# ======================= rev2b =======================
import importlib.util, sys
_spec = importlib.util.spec_from_file_location("qmodel", str(pathlib.Path(__file__).with_name("model.py")))
M = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(M)
fx = 16.098 / 13.62374
cons26 = 21.08642 * fx; cons27 = 96.184 * fx
YEARS = ["FY%02dE" % y for y in range(26, 34)]          # FY26E-FY33E: every scenario at steady state by FY33E (bull UK last)
YN = {y: 2000 + int(y[2:4]) for y in YEARS}
# Hemgenix royalty [S]: rev1 path to FY31 (47.5), then +2.5/yr fading as Hemgenix matures
roy = {"FY27E": 30.0, "FY28E": 35.0, "FY29E": 40.0, "FY30E": 44.0, "FY31E": 47.5}
for k in range(32, 34): roy["FY%02dE" % k] = 47.5 + 2.5 * (k - 31) * (1 - 0.05 * (k - 32))
roy_next = roy["FY33E"] * 1.03

ANN = {n: M.annual(n, years=range(2026, 2035)) for n in ("base", "bull")}
QTR = {n: M.run(n) for n in ("base", "bull")}

P1 = sid(F("6,000 patients over two years; capacity used thereafter; think harder about the HD pool", "P", "David May direct message 2026-10-30 (rev1 instruction)", "D16",
           quote="The company has said that they plan to treat 6000 patients upon approval. This will take more than one year, so let's assume two. Also, if they are planning on treating this many patients, they wouldn't have built this capacity if it wasn't intented to be used thereafter. Please think harder about the patient pool for HD."))
P2 = sid(F("capacity-dependent short term; capacity scales to demand medium term", "P", "David May direct message 2026-10-30 (rev2 instruction; takes precedence over the two-year simplification)", "D17",
           quote="Ask the Matt Kapusta bot for more details and build a model. But bear in mind in the short term they are capacity dependent. In the medium term they scale to meet demand. That's just economics."))
P3 = sid(F("refill = incidence less a few for eligibility, willingness, coverage", "P", "David May direct message 2026-10-30 (t55u, refill logic)", "D17",
           quote="Yearly refill is the incidence rate and exclude a few due to eligibility, willingness and coverage."))
P4 = sid(F("patients rows next to $M revenue, units on every row", "P", "David May question 2026-10-30 ('why do you have 6000 patients in 2028?'), relayed: show patients treated as their own rows with units", "D17",
           quote="why do you have 6000 patients in 2028?"))
P5 = sid(F("~30 centers at launch, 1-2 procedures/week each", "P", "David May direct message 2026-10-30 (t57u, rev2b instruction on centers)", "D29",
           quote="Your centers count at the end of 27 is wrong. There are currently around 30 centers that can do 1-2 procedures a week. This is available info from ClearPoint"))
P6 = sid(F("adjust, then send for Finagle valuation", "P", "David May 2026-10-30, relayed by the parent agent with the Kapusta CEO-bot review of rev2", "D29",
           quote="Adjust as necessary and then send for finagle valuation."))
CLP1 = sid(F([15, 1, 2], "G", "ClearPoint (AMT-130 delivery device partner): 15 hospitals qualified via the CLEAR site-readiness program within a couple of months, each ready for 1, if not 2, procedures a week; 20-30 such centers = 50-100 cases a week", "D24",
           quote="I think we already have 15 centers just in the first couple months that have filled out and sort of qualified by saying, yes, not only do we have the materials, the patient recruitment, the cooperation with pharmacy to thaw out the drugs, all those types of things, but they've also pretty much raised their hand and say, yes, we could be ready to do 1, if not 2 of these procedures a week. So, if we can get to 20 or 30 of these centers that are each willing to commit 1 to 2 cases a week, which is 50 to 100 cases a week, you can imagine getting to a ramped-up procedure type pretty quickly here."))
CLP2 = sid(F([35, 40, 5000], "G", "ClearPoint: identify the first 35-40 specialized treatment centers which can add 5,000 patients a year in capacity (all partners)", "D25",
           quote="Our highest priority with the neurosurgical community is to work hand-in-hand with our biopharma partners and to identify the first 35-40 specialized treatment centers which can add 5,000 patients a year in capacity."))
CLP3 = sid(F("mid to 2H 2027", "G", "ClearPoint CEO: if accepted, FDA decision 6-8 months after acceptance, i.e. AMT-130 approval middle to second half of 2027 if everything goes to plan", "D26",
           quote="the expectation would be a final formal decision sometime six to eight months after the acceptance of that BLA. Again, if everything went perfectly. That would put a potential approval for the very first neuro gene therapy to treat Huntington's disease sometime middle to second half of next year."))
HDSA = sid(F(69, "A", "HDSA Centers of Excellence network: 69 sites (60 Centers of Excellence + 9 Partner Sites), 37 states + DC, April 2025", "D27",
           quote="HDSA recognized 60 HDSA Centers of Excellence and nine Partner Sites, ensuring expert HD in 37 states across the nation and Washington, DC."))
PRAN = sid(F([4.25, 3.95, 3.2, 3.5], "A", "US list prices: Lenmeldy $4.25M, Kebilidi (brain-delivered AADC gene therapy) $3.95M, Elevidys $3.2M, Hemgenix ~$3.5M (secondary compilation)", "D28",
           quote="Lenmeldy holds the highest list price of any U.S. drug at $4.25 million per dose, followed by Kebilidi at $3.95 million."))
CONF = sid(F("confirmatory study", "G", "FDA alignment: randomized standard-of-care-controlled confirmatory study, TFC at 36 months primary endpoint; should be well underway, potentially fully enrolled at accelerated approval", "D12",
           quote="Management and the FDA reached alignment on a randomized standard-of-care controlled design, substituting the previous sham procedure, with total functional capacity at 36 months as the primary endpoint ... the confirmatory study should be well underway and potentially fully enrolled at the time of accelerated approval."))
RFIN = sid(F(473.199, "A", "Hemgenix royalties sold to HemB SPV, L.P. (May 2023) under the Royalty Financing Agreement, accounted for as debt: liability $473.2M at 2025-12-31; Purchaser receives royalties up to 1.85x the upfront ($693.8M) by 2032-06-30, else up to 2.25x through 2038-12-31", "D1",
           quote="The Purchaser will receive 1.85 times the upfront payment (or $ 693.8 million) until June 30, 2032 (\u201cFirst Hard Cap Date\u201d) if such thresholds are met or, if such cap is not met by June 30, 2032, up to 2.25 times of the upfront payment through December 31, 2038 ... Liability from royalty financing agreement 473,199"))
REGX = sid(F("Regenxbio AAV9 licence = AMT-260", "A", "10-K: the royalty-bearing Regenxbio AAV9 licence covers AMT-260 (epilepsy), not AMT-130; no AMT-130 licensor royalty is disclosed, so none is modelled", "D1",
           quote="Temporal Lobe Epilepsy (AMT-260) Regenxbio In June 2020, uniQure France entered into an agreement ... with Regenxbio for an exclusive (in the field of using AAV9 to expression of the GRIK2 gene in humans"))
CONFR = sid(F(70.0, "S", "Confirmatory-study R&D $70M/yr FY27E-FY31E on top of the Q2 2026 R&D run rate (midpoint of $60-80M; cost undisclosed) [S]", "D12"))
G6K = sid(F(6000, "G", "uniQure: ~6,000 initial treatable US patients at launch (management estimate)", "D10",
            quote="~6,000 patients* Initial Treatable Patients at Launch ... ~20,000 patients Diagnosed HD ~40,000 patients Symptomatic HD ~100,000 patients Genetically Identifiable HD ... *Management Estimate. (slide 25)"))
G6Kb = sid(F(6000, "G", "O'Keefe: about 6,000 patients, the initially treatable ~30% of ~20,000 diagnosed symptomatic US patients", "D7",
            quote="About 6,000 patients, representing the initially treatable ~30% of the total ~20,000 total diagnosed and symptomatic HD patients in the United States today. Approximately 40,000 U.S. patients are symptomatic for HD."))
G75K = sid(F(75000, "G", "10-K: ~75,000 HD in US/EU/UK; ~40,000 symptomatic in the US", "D1",
            quote="Approximately 75,000 people have Huntington's disease in the U.S., European Union (\"EU\"), and United Kingdom (\"UK\"), with approximately 40,000 symptomatic Huntington's disease patients in the U.S."))
GNAB = sid(F("antibody exclusion", "G", "10-K: patients with pre-existing capsid antibodies might not be eligible", "D1",
            quote="Patients that have pre-existing antibodies to a particular capsid might not be eligible for administration of a gene therapy that includes this particular capsid."))
INC = sid(F([0.48, 1.04], "A", "HD incidence 0.48 per 100,000 person-years pooled; 1.04 in North America (meta-analysis)", "D11",
            quote="The pooled incidence calculated from these studies was 0.48 cases per 100,000 person-years ... North America (1.04 per 100,000 person-years; 95% CI, 0.28-1.80)"))
POPID = sid(F(340.0, "S", "US population ~340 million (Census pop clock, rounded) [S]", "D15"))
CAPG = sid(F("no number", "G", "Management: right number of centers at start, then build; no single capacity number (neurosurgeons, intraoperative OR suites)", "D12",
             quote="There are a number of centers that are available to do this, and we are working with what we think is the right number in the initial term, and then we will continue to build from there. From a capacity point of view, it's very challenging to give you one number, and we're still working through that because it depends on the number of neurosurgeons at a particular hospital. It depends on the number of intraoperative OR suites and other competing priorities."))
ANLG = sid(F("ZOLGENSMA / ELEVIDYS analogs", "G", "Management: ZOLGENSMA a reasonable analog for a hospital procedure; ELEVIDYS for capacity; no analog perfect", "D12",
             quote="I think ZOLGENSMA is a reasonable analog. Also, if you look at ELEVIDYS from a general understanding of capacity point of view, I think they're reasonable analogs, but I will caution that no analog is perfect."))
CAPE = sid(F([120, 250, 300, 500, 500, 800, 700, 1000], "E", "Clinaptis US capacity ramp: yr1 10-15 centers ~120-250, yr2 20-25 ~300-500, yr3 30-40 ~500-800, peak 50-60 ~700-1,000 procedures/yr", "D8",
             quote="Year 1 10-15 ~120-250; Year 2 20-25 ~300-500; Year 3 30-40 ~500-800; Peak 50-60 ~700-1,000"))
DUR = sid(F([14, 18], "A", "AMT-130 surgery takes around 14 to 18 hours (MRI-guided stereotactic delivery)", "D18",
            quote="This is pioneering neurosurgery, and given the relatively early stage of clinical development, the operations take considerable time - around 14 to 18 hours."))
ELS = sid(F(70, "A", "ELEVIDYS: >70 trained infusion sites within a year of June 2023 launch (goal was 50); 75% of sites had dosed", "D19",
            quote="We have, as we stand here right now, well over 70 ... Actually, I was wrong; it's 75% of sites that have been dosing."))
ELR = sid(F([200.4, 820.8, 384.2], "A", "ELEVIDYS net product revenue FY2023 $200.4M, FY2024 $820.8M, Q4 2024 $384.2M", "D20",
            quote="Fourth quarter and full-year 2024 net product revenue for ELEVIDYS totaled $384.2 million and $820.8 million"))
ELP = sid(F(3.2, "A", "ELEVIDYS US wholesale acquisition cost $3.2M", "D21", quote="The Company disclosed in the webcast the United States wholesale acquisition cost (gross price) of ELEVIDYS at $3.2 million."))
HGP = sid(F(3.5, "A", "Hemgenix US list price $3.5M", "D23", quote="a gene therapy for bleeding disorder hemophilia from Australian drugmaker CSL Ltd ... carries a list price of $3.5 million."))
ELIMP = sid(F(round(820.8 / 3.2), "C", "ELEVIDYS implied FY2024 infusions ~ $820.8M / $3.2M WAC = ~256 (upper bound on net: ~3.5 per site per year at ~73 sites, ~0.3/site/month)", "D20", [ELR, ELP, ELS]))
PRICE_E = sid(F([1.7, 2.6], "E", "Net price per patient: Leerink $1.7M US net (GEN); Clinaptis $2.6M average net", "D8", quote="We assume $2.6M average net price per patient."))
GS = sid(F(2500, "E", "Goldman Sachs: peak global AMT-130 sales $2.5B, 90% PoS, ~25% cumulative penetration of ~20,000 diagnosed symptomatic US patients", "D22",
           quote="Goldman Sachs modeling potential peak global sales of $2.5 billion with a 90% probability of success, assuming approximately 25% cumulative penetration into the estimated 20,000 diagnosed, symptomatic patients in the US."))
UKG = sid(F([7000, 8000], "G", "UK: 7,000-8,000 patients living with HD", "D13", quote="There are between 7,000-8,000 patients living with HD in the U.K., with approximately 30,000 at risk."))
MHRA = sid(F("MAA filed", "G", "MAA submitted to UK MHRA with the BLA; priority review requested (6 months after 60-day filing period)", "D4",
             quote="its Marketing Authorisation Application (MAA) for ifezuntirgene inilparvovec has been submitted to the United Kingdom's (U.K.) Medicines and Healthcare products Regulatory Agency (MHRA) ... The Company has requested priority review for the BLA. If granted, priority review would shorten the FDA review cycle to six months following the FDA's 60-day BLA filing review period."))
GENZ = sid(F("Genezen", "G", "Genezen (bought Lexington 2024) provides development and manufacturing services for uniQure's investigational gene therapies; uniQure has preferred access for AMT-130", "D1",
             quote="we rely on Genezen for the production of HEMGENIX and will have preferential access to the Lexington Facility for the production of materials related to AMT-130 and AMT-191 programs under separately negotiated development and supply arrangements."))
OPX = sid(F([140.673, 65.456, 6.5, 34.0, 17.4, 66.8, 810.3], "A", "R&D FY2025 $140.7M, SG&A FY2025 $65.5M incl. $6.5M US launch preparation; Q2 2026 R&D $34.0M, SG&A $17.4M; H1 2026 operating cash outflow $66.8M; cash and investments $810.3M at 2026-06-30, runway into 2030", "D2",
            quote="R&D expenses for the three months ended June 30, 2026 were $34.0 million ... Selling, general and administrative expenses for the three months ended June 30, 2026 were $17.4 million ... Net cash used in operating activities was $66.8 million for the six months ended June 30, 2026 ... cash and cash equivalents and investment securities of $810.3 million ... sufficient to fund our projected operating expenses into 2030"))

# ---- patient pool and refill [P]/[S]/[C] ----
P8 = sid(F("pool model m = 0.62", "P", "David May direct message 2026-10-30 (t97u): write up the pool model with m = 0.62 (progression 0.60 + death 0.02 per year)", "D31",
           quote="Write is up with m=0.62 its the most internally consistent"))
P9 = sid(F("redo Finagle", "P", "David May direct message 2026-10-30 (t98u)", "D31", quote="Redo the finagle too"))
H = M.HAIR
HAIRID = {n: sid(F([H[n]["ref"], H[n]["will"], H[n]["cov"]], "S", "%s treated share of the eligible pool P = referral %.0f%% x willing %.0f%% x covered %.0f%% = %.3f [S under P3]" % (n, H[n]["ref"] * 100, H[n]["will"] * 100, H[n]["cov"] * 100, M.P(n)), "D17")) for n in ("base", "bull")}
INC2 = sid(F([1.22, 1.59], "S", "US HD incidence per 100k/yr used in the pool model: base 1.22, bull 1.59 (AMT130 pool model inputs; North America 1.04, 95% CI 0.28-1.80, in Medina 2022) [S]", "D11"))
REFID = {n: sid(F(round(M.entrants(n, 2027), 3), "C", "%s US entrants to the early-manifest pool 2027 = %.2f/100k x 340M x share %.2f x filter %.4f x 1.005 = %.0f/yr (+0.5%%/yr)%s" % (n, M.INC[n], M.SHARE[n], M.FILT[n], M.entrants(n, 2027), "; filter holds the steady pool at the 6,000 start pool (reference run case A)" if n == "base" else "; unfiltered"), "D11", [INC2, POPID, P3, G6K])) for n in ("base", "bull")}
ATTRID = sid(F(M.M_LEAVE, "P", "Pool leave rate m = 0.62/yr (progression past eligibility 0.60 + death 0.02), average stay ~1.6 years [P8]; demand rate u = P(m+g)/(1-P) so steady-state treated = P x entrants", "D31", quote="Write is up with m=0.62 its the most internally consistent"))
CAPID = {n: sid(F({"FY27_half_year": M.CLPT[n][0], "FY28": M.CLPT[n][1], "cap_per_year_from_FY29": M.CLPT[n][2], "centers_shown_at_procedures_per_week": M.CPW}, "S",
                  "%s US capacity = CLPT AMT-130 ramp %d (FY27, from 2027-07-01) / %d (FY28) / %d per year cap from FY29, spread evenly by quarter; treated = min(capacity, demand). Centers shown = capacity / (2 procedures/week x 52), used only for the $1.5M/center opex item [S]" % ((n,) + M.CLPT[n]), "D32", )) for n in ("base", "bull")}
Y1ID = {n: sid(F(M.POOL0, "C", "%s US pool model (quarterly): start pool 6,000 at 2027-07-01 [G]; pool end = start + entrants - m/4 x pool - treated; demand = u/4 x pool, u = %.4f" % (n, M.P(n) * (M.M_LEAVE + M.G) / (1 - M.P(n))), "D10", [G6K, ATTRID, HAIRID[n], REFID[n], P8])) for n in ("base", "bull")}
BRID = CAPID
XOVER = sid(F([4, 2], "A", "Duration cross-check: 4 of 6 high-dose sham controls crossed over after 12 months; 2 no longer met inclusion criteria (link unverified)", "D33",
              quote="Four of the six control patients in the high-dose cohort were crossed over to treatment and the remaining two patients failed to meet the study's inclusion criteria."))
P7 = sid(F("centers do not limit capacity in year one; year-1 treated = Kapusta bot's ~190 path", "P", "David May direct message 2026-10-30 (t62u, rev3 instruction)", "D30",
           quote="We can say that centers don’t limits capacity in year one and use your 190"))
ALTREF = None
APPR = sid(F("2027-07-01", "S", "US approval/launch 2027-07-01: priority review gives an action date late Apr/early May 2027; ClearPoint expects mid to 2H 2027 [S]", "D4"))
ALTREF = {"base": 0.30 * M.refill("base")[0], "bull": 0.30 * M.refill("bull")[0]}   # sensitivity: entrants = 30% of incidence
UKID = sid(F({"launch": "Q3 2028", "backlog": M.UK["backlog"], "centers": M.UK["centers"], "per_center_month": M.UK["thr"], "price": M.UK["price"]}, "S",
             "Bull UK (unchanged from v10): MHRA approval and NHS access from Q3 2028; initial backlog 30%% x 7,500 = %.0f; refill 0.48/100k x 69M x bull haircut, 10%%/yr attrition; centers %s; 1 procedure/center/week (%.2f/month); net price $1.5M [S]" % (M.UK["backlog"], M.UK["centers"], M.UK["thr"]), "D13"))
PRICE = {"base": 2.0, "bull": 2.4, "bear": 0.0}
STEP = 0.90; STEP_TRIG = 2000.0; STEP_FLOOR = {"base": 2031, "bull": 2027}   # -10% from the year after US sales first pass $2B (base not before FY31E)
PRID = {"base": sid(F([2.0, 1.8], "S", "Base US net price $2.0M FY27E-FY30E, then -10%% to $1.8M from the year after annual US sales first pass $2B (payer budget pressure); Kebilidi $3.95M, Elevidys $3.2M, Hemgenix $3.5M list are gross [S]", "D7")),
        "bull": sid(F([2.4, 2.16], "S", "Bull US net price $2.4M, then -10%% to $2.16M from the year after annual US sales first pass $2B [S]", "D8"))}
COGS = {"base": (0.30, 0.02, 0.20), "bull": (0.30, 0.025, 0.18)}   # $M/patient at launch, fall per year, floor [S]
COGSID = {n: sid(F(list(COGS[n]), "S", "%s AMT-130 COGS (Genezen manufacturing, release, cold-chain; no licensor royalty, none disclosed for AMT-130): $%.2fM/patient in FY27, falling $%.3fM/yr to $%.2fM; UNVERIFIED, no uniQure disclosure [S]" % ((n,) + COGS[n]), "D1", )) for n in ("base", "bull")}
OPEX = {"base": dict(core=1.03, com_fixed=80.0, per_center=1.5, var=0.05, uk=0.0, conf=70.0), "bull": dict(core=1.03, com_fixed=90.0, per_center=1.5, var=0.05, uk=15.0, conf=70.0)}
BEAR_OPEX = [None, 170, 150, 140] + [140] * (len(YEARS) - 4)   # restructured opex excluding the confirmatory study
BEAR_CONF = 70.0   # v12 (David t120u 2026-11-02): same confirmatory-study cost as base/bull, FY27E-FY31E [S] CONFR

def build(name, **kw):
    h2rev = cons26 - A["h1"]
    lic = {y: (cons26 if y == "FY26E" else roy[y]) for y in YEARS}
    us = {y: 0.0 for y in YEARS}; uk = {y: 0.0 for y in YEARS}; cogs = {y: 0.0 for y in YEARS}; opex = {}
    pt = {k: {y: 0.0 for y in YEARS} for k in ("centers", "cap", "refill", "demand", "leave", "backlog", "treated", "cum", "uk_cap", "uk_treated", "uk_back")}
    if name != "bear":
        an = M.annual(name, years=range(2026, 2035), **kw) if kw else ANN[name]
        price = {}; passed = None
        for y in YEARS:
            d = an[YN[y]]
            pt["centers"][y] = d["centers_end"]; pt["cap"][y] = d["cap"]; pt["refill"][y] = d["refill"]; pt["backlog"][y] = d["backlog_end"]
            pt["treated"][y] = d["treated"]; pt["demand"][y] = d["demand"]; pt["leave"][y] = d["leave"]; pt["cum"][y] = d["cum"]; pt["uk_cap"][y] = d["uk_cap"]; pt["uk_treated"][y] = d["uk_treated"]; pt["uk_back"][y] = d["uk_back"]
            p = PRICE[name] * (STEP if (passed is not None and YN[y] > passed and YN[y] >= STEP_FLOOR[name]) else 1.0)
            price[y] = p; us[y] = d["treated"] * p; uk[y] = d["uk_treated"] * M.UK["price"]
            if passed is None and us[y] > STEP_TRIG: passed = YN[y]
            c0, dc, fl = COGS[name]; cpp = max(fl, c0 - dc * max(0, YN[y] - 2027))
            cogs[y] = (d["treated"] + d["uk_treated"]) * cpp
    rev0 = {y: lic[y] + us[y] + uk[y] for y in YEARS}
    scale27 = cons27 / rev0["FY27E"]   # reported only: P5 capacity model overrides consensus (not scaled)
    amt = {y: us[y] + uk[y] for y in YEARS}
    rev = {y: lic[y] + amt[y] for y in YEARS}
    core0 = 4 * opexq2
    e = {"FY26E": ebitdah1 + h2rev * gm_lic - 2 * opexq2}
    for i, y in enumerate(YEARS[1:], 1):
        if name == "bear":
            opex[y] = BEAR_OPEX[i] + (BEAR_CONF if 2027 <= YN[y] <= 2031 else 0.0)
        else:
            o = OPEX[name]; half = 0.5 if y == "FY27E" else 1.0
            avg_c = pt["centers"][y]
            opex[y] = core0 * o["core"] ** i + o["com_fixed"] * half + o["per_center"] * avg_c + o["var"] * amt[y] + (o["uk"] if YN[y] >= 2028 else 0.0) + (o["conf"] if 2027 <= YN[y] <= 2031 else 0.0)
        e[y] = lic[y] * gm_lic + amt[y] - cogs[y] - opex[y]
    gm_tot = {y: (lic[y] * gm_lic + amt[y] - cogs[y]) / rev[y] for y in YEARS}
    gm_tot["FY26E"] = (A["h1"] - A["cogs_h1"] + h2rev * gm_lic) / rev["FY26E"]
    return dict(lic=lic, us=us, uk=uk, amt=amt, rev=rev, cogs=cogs, opex=opex, e=e, gm=gm_tot, pt=pt, scale27=scale27, h2rev=h2rev, price=(price if name != "bear" else {}))

def facts(name, b):
    lic, us, uk, amt, rev, e, pt = b["lic"], b["us"], b["uk"], b["amt"], b["rev"], b["e"], b["pt"]
    yrs = YEARS
    def lic_f(y):
        if y == "FY26E": return F(r(lic[y]), "C", "FY26 consensus EUR x fx; all royalty/license, no AMT-130 sales before approval", "D6", [ID["c26eur"], ID["yago"], ID["rev25"]])
        return F(r(lic[y]), "S", "Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]", "D2", [RFIN])
    def us_f(y):
        if us[y] == 0:
            return F(0.0, "S", "No AMT-130 US revenue: %s." % ("bear case, AMT-130 not approved" if name == "bear" else "no approval before 2027"), "D5" if name == "bear" else "D9")
        t = "%s AMT-130 US (US$M) = %.0f patients treated (min of CLPT capacity %.0f/yr and pool demand, m = 0.62) x $%.2fM net, recognised at treatment" % (name, pt["treated"][y], pt["cap"][y], b["price"][y])
        return F(r(us[y]), "C", t, "D8", [P8, P2, Y1ID[name], CAPID[name], REFID[name], ATTRID, G6K, PRID[name]])
    def uk_f(y):
        if uk[y] == 0: return F(0.0, "S", "No AMT-130 UK revenue in %s%s" % (name, " (UK launch from Q3 2028 in bull only)" if name == "bull" else ""), "D4")
        return F(r(uk[y]), "C", "bull AMT-130 UK (US$M) = %.0f UK patients treated x $1.5M net" % pt["uk_treated"][y], "D13", [UKID, UKG, MHRA, ATTRID])
    lic_p = {"FY24A": fA("lic24", "License revenues 2024 $10,133k", "D1"), "FY25A": fA("lic25", "License revenues 2025 $15,934k", "D1"),
             "YoY": F(r(A["lic25"] / A["lic24"] - 1), "C", "FY25/FY24 - 1 license revenues", "D1", [ID["lic24"], ID["lic25"]]),
             "H1A": fA("h1", "License revenues six months ended June 30, 2026 $9,403k", "D2"),
             "H2E": F(r(b["h2rev"]), "C", "FY26E consensus - H1A", "D6", [ID["c26eur"], ID["yago"], ID["h1"]])}
    lic_p.update({y: lic_f(y) for y in yrs})
    col_p = {"FY24A": fA("col24", "Collaboration revenues 2024 $10,872k", "D1"), "FY25A": fA("col25", "Collaboration revenues 2025 $164k", "D1"),
             "YoY": F(r(A["col25"] / A["col24"] - 1), "C", "FY25/FY24 - 1 collaboration revenues", "D1", [ID["col24"], ID["col25"]]),
             "H1A": F(0.0, "A", "Q2 2026 10-Q shows only License revenues in H1 2026", "D2", quote="License revenues $ 5,841 $ 5,262 $ 9,403 $ 6,829 Total revenues 5,841 5,262 9,403 6,829"),
             "H2E": F(0.0, "S", "Collaboration services to CSL wound down after the 2024 Lexington Transaction; none in H1 2026 [S]", "D1")}
    col_p.update({y: col_p["H2E"] for y in yrs})
    cm_p = {"FY24A": fA("cm24", "Contract manufacturing revenues 2024 $6,114k", "D1"), "FY25A": F(0.0, "A", "Contract manufacturing revenues 2025: nil", "D1", quote="Contract manufacturing revenues — 6,114"),
            "YoY": F(-1.0, "C", "FY25/FY24 - 1 contract manufacturing", "D1", [ID["cm24"]]),
            "H1A": col_p["H1A"], "H2E": F(0.0, "G", "Manufacturing divested July 2024 (Lexington Transaction)", "D1", quote="divestment of our commercial manufacturing activities in July 2024")}
    cm_p.update({y: cm_p["H2E"] for y in yrs})
    z = F(0.0, "A", "AMT-130 not approved; no product revenue", "D1", quote="investigational gene therapy")
    h2z = F(0.0, "G", "BLA submitted 2026-09-02; no approval in 2026", "D4", quote="today announced the submission of a Biologics License Application")
    us_p = {"FY24A": z, "FY25A": z, "H1A": col_p["H1A"], "H2E": h2z}; us_p.update({y: us_f(y) for y in yrs})
    uk_p = {"FY24A": z, "FY25A": z, "H1A": col_p["H1A"], "H2E": h2z}; uk_p.update({y: uk_f(y) for y in yrs})
    gm_us = {y: (1 - b["cogs"][y] / amt[y]) for y in yrs if amt[y] > 0}
    lines = [
     {"name": "License revenue (Hemgenix royalties from CSL Behring)", "pattern": "ramping (royalty on Hemgenix sales)", "periods": lic_p,
      "gross_margin": F(r(gm_lic), "C", "1 - cost of license revenues 569 / license revenues 9,403, H1 2026", "D2", [ID["opsh1"], ID["h1"]])},
     {"name": "Collaboration revenue (CSL services)", "pattern": "mature or declining", "periods": col_p},
     {"name": "Contract manufacturing revenue", "pattern": "mature or declining", "periods": cm_p},
     {"name": "AMT-130 product revenue, US", "pattern": "new or acquired (capacity-limited, then pool demand, m = 0.62)" if name != "bear" else "milestone-dependent (approval event; probability 0 in bear)", "periods": us_p,
      "gross_margin": (F(r(gm_us.get("FY31E", 0.85)), "C", "AMT-130 gross margin FY31E = 1 - COGS/patient / net price (falls from COGS $0.30M/patient in FY27)", "D1", [COGSID[name], PRID[name]]) if name != "bear" else F(0.85, "S", "n/a in bear (not approved); placeholder product margin [S]", "D8"))},
     {"name": "AMT-130 product revenue, UK", "pattern": "new or acquired (bull only, MHRA filing 2026-09-02)" if name == "bull" else "milestone-dependent (no UK sales in this scenario)", "periods": uk_p},
    ]
    revt = {"FY24A": fA("rev24", "Total revenues 2024 $27,119k", "D1"), "FY25A": fA("rev25", "Total revenues 2025 $16,098k", "D1"),
            "YoY": F(r(A["rev25"] / A["rev24"] - 1), "C", "FY25/FY24 - 1 total revenue", "D1", [ID["rev24"], ID["rev25"]]),
            "H1A": lic_p["H1A"], "H2E": lic_p["H2E"]}
    for y in yrs:
        if y == "FY26E": revt[y] = lic_p[y]
        else: revt[y] = F(r(rev[y]), "C", "Sum of %s lines (US$M)" % name, "D8", [lic_p[y]["citation"]["id"], us_p[y]["citation"]["id"], uk_p[y]["citation"]["id"]])
    ebt = {"FY24A": F(r(ebitda24), "C", "EBITDA = loss from operations -184,294 + D&A 12,641 + SBC 22,258 (2024)", "D1", [ID["ops25"]]),
           "FY25A": F(r(ebitda25), "C", "EBITDA = loss from operations -185,349 + D&A 14,759 + SBC 17,679 (2025)", "D1", [ID["ops25"], ID["rev25"]]),
           "H1A": F(r(ebitdah1), "C", "EBITDA = loss from operations -97,923 + D&A 7,863 + SBC 10,106 (H1 2026)", "D2", [ID["opsh1"], ID["opsq2"]])}
    ebt["YoY"] = F(r(ebitda25 / ebitda24 - 1), "C", "FY25/FY24 - 1 EBITDA (both negative: a larger loss)", "D1", [ID["ops25"], ID["rev25"]])
    for y in yrs:
        if y == "FY26E":
            ebt[y] = F(r(e[y]), "C", "H1A EBITDA + H2 revenue x license GM - 2 x Q2 cash opex net of other items (%.3f) [S run rate]" % opexq2, "D3", [ID["opsh1"], ID["opsq2"]])
        elif name == "bear":
            ebt[y] = F(r(e[y]), "S", "bear: license gross profit - cash opex %.0f (restructured opex %d + confirmatory study %.0f) (US$M) [S]" % (b["opex"][y], BEAR_OPEX[YEARS.index(y)], b["opex"][y] - BEAR_OPEX[YEARS.index(y)]), "D3", [CONFR] if b["opex"][y] > BEAR_OPEX[YEARS.index(y)] else None)
        else:
            ebt[y] = F(r(e[y]), "S", "%s EBITDA (US$M) = license GP + AMT-130 revenue - COGS %.1f - cash opex %.1f (core Q2 2026 run rate x4 +3%%/yr, US commercial fixed $%.0fM, $1.5M per active center, 5%% variable%s) [S]" % (name, b["cogs"][y], b["opex"][y], OPEX[name]["com_fixed"], ", UK $15M from FY28" if name == "bull" else ""), "D2", )
    gmt = {"FY25A": F(r((A["rev25"] - A["cogs25"]) / A["rev25"]), "C", "(revenue - cost of license revenues 1,686)/revenue 2025", "D1", [ID["ops25"], ID["rev25"]])}
    for y in yrs: gmt[y] = F(r(b["gm"][y]), "C", "Revenue-weighted gross margin %s (license GM; AMT-130 1 - COGS/revenue)" % name, "D2", [ID["opsh1"]] + ([COGSID[name]] if name != "bear" else []))
    totals = {"revenue": revt, "ebitda": ebt, "gross_margin": gmt}
    org = {"revenue": {"FY25A": revt["FY25A"], **{y: revt[y] for y in yrs}}, "ebitda": {"FY25A": ebt["FY25A"], **{y: ebt[y] for y in yrs}}}
    rv = [A["rev25"]] + [rev[y] for y in yrs]; ev = [ebitda25] + [e[y] for y in yrs]
    sg = [r(rv[i + 1] / rv[i] - 1) for i in range(len(yrs))]; eg = [r(ev[i + 1] / ev[i] - 1) for i in range(len(yrs))]
    last = yrs[-1]; me = r(e[last] / rev[last])
    nxt = roy_next + (amt[last] if name != "bear" else 0.0)   # treated flow at steady state, same price
    gs = r(nxt / rev[last] - 1)
    if name == "bear":
        mc = r(gm_lic); mct = "Bear: opex fixed after restructuring; an incremental royalty dollar drops through at the license gross margin [S]"
    else:
        mc = r((me + b["gm"][last]) / 2); mct = "Average of me and FY33 gross margin (Finagle default rule); no positive-EBITDA history to set it against [S]"
    fin = {
     "note": "Operating path. Growth on a negative EBITDA base is an arithmetic ratio (E_t/E_t-1 - 1) and compounds exactly; not an economic growth rate.",
     "sales_growth": F(sg, "C", "Revenue growth FY26-FY38, %s" % name, "D6", [ID["rev25"], ID["c26eur"], ID["c27eur"]]),
     "ebitda_growth": F(eg, "C", "EBITDA ratio E_t/E_t-1 - 1 FY26-FY38, %s" % name, "D3", [ID["ops25"], ID["rev25"]]),
     "me": F(me, "C", "FY33E EBITDA / FY33E revenue (steady state: treated = pool demand, base; bull at capacity cap), %s" % name, "D3", [ID["ops25"], ID["rev25"]] + ([REFID[name]] if name != "bear" else [])),
     "mc": F(mc, "S", mct, "D2"),
     "gsnext": F(gs, "S", ("FY39 growth: royalty %.1f (+3%%) + AMT-130 at the FY33 steady-state flow and price, vs FY33 revenue [S]" % roy_next) if name != "bear" else "FY39 growth: Hemgenix royalty only, +3% [S]", "D8"),
     "ebitda_basis": F("organic", "S", "No acquisitions in the window; organic = total", "D2"),
     "acquisition_disclosure": {"status": F("none", "S", "No pending deals disclosed in the Q2 2026 10-Q or later 8-Ks", "D2")},
    }
    # patient rows (units: patients or count), their own block, every row a tagged fact
    pts = None
    if name != "bear":
        def row(k, label, src, inputs):
            return {y: F(round(pt[k][y], 1), "C", "%s, %s %s" % (label, name, y), src, inputs) for y in yrs}
        pts = {"units": "patients unless stated",
               "us_centers_active_year_end (count)": row("centers", "US centers implied at year end = capacity / (2/week x 52) (count)", "D32", [CAPID[name], CLP1]),
               "us_capacity (patients/yr)": row("cap", "US treatment capacity = CLPT AMT-130 ramp (patients/yr)", "D32", [CAPID[name]]),
               "us_refill_demand (patients/yr)": row("refill", "US entrants to the eligible pool (patients/yr)", "D11", [REFID[name], P3]),
               "us_pool_demand (patients/yr)": row("demand", "US pool demand = u x pool (patients/yr)", "D31", [Y1ID[name], ATTRID, HAIRID[name]]),
               "us_pool_leavers (patients/yr)": row("leave", "US untreated pool leavers = m x pool (patients/yr)", "D31", [ATTRID]),
               "us_backlog_year_end (patients)": row("backlog", "US eligible pool at year end = start 6,000 + entrants - leavers - treated (patients)", "D10", [G6K, REFID[name], ATTRID]),
               "us_treated (patients/yr)": row("treated", "US patients treated = min(CLPT capacity, pool demand) (patients/yr)", "D31", [P8, Y1ID[name], CAPID[name], REFID[name], G6K, P2]),
               "us_cumulative_treated (patients)": row("cum", "US cumulative patients treated (patients)", "D8", [CAPID[name], REFID[name], G6K])}
        if name == "bull":
            pts["uk_capacity (patients/yr)"] = row("uk_cap", "UK capacity (patients/yr)", "D13", [UKID])
            pts["uk_treated (patients/yr)"] = row("uk_treated", "UK patients treated (patients/yr)", "D13", [UKID, UKG])
            pts["uk_backlog_year_end (patients)"] = row("uk_back", "UK eligible backlog at year end (patients)", "D13", [UKID, UKG, ATTRID])
    blk = {"lines": lines, "totals": totals, "organic": org, "finagle": fin}
    if pts: blk["patients"] = pts
    return blk, dict(me=me, mc=mc, gs=gs, sg=sg, eg=eg)

blocks = {}; DIAG = {}
for n in ["base", "bull", "bear"]:
    b = build(n); blocks[n], extra = facts(n, b)
    DIAG[n] = {**{k: v for k, v in b.items() if k != "pt"}, **extra, "pt": b["pt"]}
SENS = {}
for n in ("base", "bull"):
    for lab, kw in (("q4_2027_approval", dict(delay=1)), ("kapusta_refill_30pct", dict(refill_override=ALTREF[n]))):
        bb = build(n, **kw); SENS[n + "_" + lab] = dict(rev=bb["rev"], e=bb["e"], treated=bb["pt"]["treated"], price=bb["price"])
DIAG["sens"] = SENS
fxf = F(r(fx), "C", "USD per EUR implied: reported FY25 revenue 16.098 / Yahoo FY25 year-ago revenue EUR 13.624", "D6", [ID["rev25"], ID["yago"]])
for k in (P8, P9, XOVER, INC2, P7, P6, CLP2, CLP3, HDSA, PRAN, CONF, CONFR, REGX, P1, P4, G6Kb, G75K, GNAB, ANLG, ELIMP, PRICE_E, GS, GENZ, OPX, APPR, HGP): pass   # cited in report / sources
payload = {"ticker": "QURE", "company": "uniQure N.V. (NASDAQ: QURE)", "units": "USD millions (patient rows in patients, as labelled)", "currency_note": "Reports in USD; Yahoo consensus is in EUR and converted at the implied rate (bridge.fx).",
  "baseline_period": "FY25A", "explicit_periods": YEARS, "as_of": "2026-11-02", "revision": "rev5 / v12 (David May t120u, 2026-11-02: bear opex carries the same $70M/yr confirmatory-study cost FY27E-FY31E as base/bull; BLA accepted 2026-11-02, PDUFA 2027-05-01). Built on rev4 / v11 (David May t97u-t98u, 2026-10-30: AMT-130 US treated from the pool model at m = 0.62, start pool 6,000, CLPT capacity ramp; supersedes rev3 year-1 ~190 path and center engine)",
  **blocks["base"], "bridge": {"fx_usd_per_eur": fxf,
     "q2_cash_opex": F(r(opexq2), "C", "Q2 2026 gross profit (5.841-0.350) - Q2 EBITDA (-52.203+4.907+5.016)", "D3", [ID["opsh1"], ID["opsq2"]]),
     "base_fy27_consensus_vs_build": F(r(DIAG["base"]["scale27"]), "C", "FY27 consensus / base line build: NOT applied (P5 capacity instruction overrides consensus); far from 1, flagged", "D6", [ID["c27eur"], ID["yago"], P5])},
  "scenarios": {"bull": blocks["bull"], "bear": blocks["bear"]}, "sources": sources}
OUT.write_text(json.dumps(payload, indent=1))
json.dump(DIAG, open(OUT.with_name("diag.json"), "w"), indent=1, default=float)
for n in ("base", "bull", "bear"):
    d = DIAG[n]; print(n, "scale27 %.3f me %.4f mc %.4f gs %.4f" % (d["scale27"], d["me"], d["mc"], d["gs"]))
    for y in YEARS: print(" ", y, "rev %8.1f us %8.1f uk %6.1f e %8.1f gm %.3f opex %s tr %6.0f" % (d["rev"][y], d["us"][y], d["uk"][y], d["e"][y], d["gm"][y], round(d["opex"].get(y, 0), 1), d["pt"]["treated"][y]))
NAMED = dict(P8=P8, P9=P9, XOVER=XOVER, INC2=INC2, P1=P1, P2=P2, P3=P3, P4=P4, G6K=G6K, G6Kb=G6Kb, G75K=G75K, GNAB=GNAB, INC=INC, POP=POPID, CAPG=CAPG, ANLG=ANLG, CAPE=CAPE, DUR=DUR, ELS=ELS, ELR=ELR, ELP=ELP, HGP=HGP, ELIMP=ELIMP,
             PRICE_E=PRICE_E, GS=GS, UKG=UKG, MHRA=MHRA, GENZ=GENZ, OPX=OPX, ATTR=ATTRID, APPR=APPR, UKID=UKID, HAIR_base=HAIRID["base"], HAIR_bull=HAIRID["bull"], REF_base=REFID["base"], REF_bull=REFID["bull"],
             CAP_base=CAPID["base"], CAP_bull=CAPID["bull"], PR_base=PRID["base"], PR_bull=PRID["bull"], COGS_base=COGSID["base"], COGS_bull=COGSID["bull"], c27=ID["c27eur"], c26=ID["c26eur"], fx=fxf["citation"]["id"], P5=P5, P6=P6, P7=P7, Y1_base=Y1ID["base"], Y1_bull=Y1ID["bull"], BR_base=BRID["base"], BR_bull=BRID["bull"], CLP1=CLP1, CLP2=CLP2, CLP3=CLP3, HDSA=HDSA, PRAN=PRAN, CONF=CONF, CONFR=CONFR, RFIN=RFIN, REGX=REGX)
json.dump(NAMED, open(OUT.with_name("ids.json"), "w"), indent=1)
