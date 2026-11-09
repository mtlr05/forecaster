import finagle as cmp

# Scenario copy. Edit this cell; leave the cell above as the base case.
# First variant: uncomment the margin-path forecast_ebitda and comment the growth-only call.

ticker = 'PDEX'
rd = 0.04286770140428677
re = 0.10336999999999999
t = 0.21
te = None
shares = 3.200001
price = 61.2
gt = 0.048369999999999996
roict = 0.15
year = 10
dividend = 0

co = cmp.company(
    ticker=ticker, rd=rd, re=re, t=t, te=te,
    shares=shares, price=price, gt=gt, roict=roict,
    year=year, dividend=dividend,
)

n = year + 1
financials = {
    'date': '2026-06-30',
    'revenue': [77.548, 78.29283000099998, 74.71897999999999],  # leave [0] if forecast_ebitda is commented; that call overwrites it
    'ebitda': [15.073],  # TTM only, or a full list of year + 1 values
    'capex': [0.483],
    'dwc': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sbc': [0.688],
    'tax': [4.353],
    'da': [1.394],
    'debt': [18.942, 18.942, 18.942, 18.942, 18.942, 18.942, 18.942, 18.942, 18.942, 18.942, 18.942],
    'interest': [0.812],
    'cash': 9.342,
    'nol': 0,
    'noa': 0,
}

# gf: explicit EBITDA growth. Interpolated toward gt. Non-NaN prefix = explicit years.
# Growth-only: ebitda[i+1] = ebitda[i] * (1 + g[i]); revenue is 0.
# Margin path (me, mc, and gsnext all set), after the explicit gf years:
#   me = EBITDA/sales at the handoff; revenue = ebitda/me * (1+gs)
#   mc = incremental EBITDA / incremental sales
#   gsnext = sales growth in the first year after explicit EBITDA growth, then faded to gt
#   ebitda[i+1] = ebitda[i] * (1 + (mc/me) * gs[i]); me is updated to the new margin
ebitda_ttm = 15.073
gf = [-0.142906037285212, -0.11724840634250511]

# Comment this out when ebitda is already a full list. Keep revenue at [0] in that case.
# co.forecast_ebitda(ebitda_ttm, gf, financials)

me = 0.1526285262459418
mc = 0.25
gsnext = -0.1
co.forecast_ebitda(ebitda_ttm, gf, financials, me=me, mc=mc, gsnext=gsnext)

co.forecast_sbc(sbc_f=[0.688], financials=financials)
# method omitted: 1 when revenue was forecast, 2 when revenue stays 0.
co.forecast_capex(capex_f=[0.483], method=1, financials=financials)

co.load_financials(financials=financials.copy())
co.fcf_from_ebitda()
# co.fcf_from_earnings(payout=1, gf=0, ROE=1)  # alternate path; do not combine with EBITDA

# co.fcf_to_acquire(adjust_cash=False, year_a=1, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.fcf_to_acquire(adjust_cash=False, year_a=2, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.noa_to_dispose(dnoa=0, tax=0, year_dis=1)
co.fcf_to_debt(leverage=1.256684137198965, year_d=1)

# Exactly one distribution method:
# co.fcf_to_allocate(price=price, dp='proportional', buybacks=None)
# co.fcf_to_buyback(price=price, dp='proportional')
# co.fcf_to_bs()

co.value()
co.display_fin()
