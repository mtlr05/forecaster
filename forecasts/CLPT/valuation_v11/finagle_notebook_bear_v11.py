import finagle as cmp

# Scenario copy. Edit this cell; leave the cell above as the base case.
# First variant: uncomment the margin-path forecast_ebitda and comment the growth-only call.

ticker = 'CLPT'
rd = 0.092
re = 0.10453000000000001
t = 0.21
te = None
shares = 30.503132
price = 9.25
gt = 0.049530000000000005
roict = 0.25
year = 15
dividend = 0

co = cmp.company(
    ticker=ticker, rd=rd, re=re, t=t, te=te,
    shares=shares, price=price, gt=gt, roict=roict,
    year=year, dividend=dividend,
)

n = year + 1
financials = {
    'date': '2025-12-31',
    'revenue': [36.971, 48.000003865, 56.000020509167946, 67.88003286004437, 89.31844787816645, 119.14393194898743, 180.18744462698308],  # leave [0] if forecast_ebitda is commented; that call overwrites it
    'ebitda': [-15.17],  # TTM only, or a full list of year + 1 values
    'capex': [0.522],
    'dwc': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sbc': [8.18, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 7.9098971906569036, 7.819794381313807, 7.729691571970711, 7.639588762627614, 7.549485953284517, 7.45938314394142, 7.369280334598324, 7.2791775252552275, 7.189074715912131],
    'tax': [0.055],
    'da': [0.814],
    'debt': [49.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077, 99.077],
    'interest': [2.388],
    'cash': 45.923,
    'nol': 258.2,
    'noa': 0.0,
}

# gf: explicit EBITDA growth. Interpolated toward gt. Non-NaN prefix = explicit years.
# Growth-only: ebitda[i+1] = ebitda[i] * (1 + g[i]); revenue is 0.
# Margin path (me, mc, and gsnext all set), after the explicit gf years:
#   me = EBITDA/sales at the handoff; revenue = ebitda/me * (1+gs)
#   mc = incremental EBITDA / incremental sales
#   gsnext = sales growth in the first year after explicit EBITDA growth, then faded to gt
#   ebitda[i+1] = ebitda[i] * (1 + (mc/me) * gs[i]); me is updated to the new margin
ebitda_ttm = -15.17
gf = [0.630362, 0.018651, -0.027229, -0.331949, -0.663431, -5.673908]

# Comment this out when ebitda is already a full list. Keep revenue at [0] in that case.
# co.forecast_ebitda(ebitda_ttm, gf, financials)

me = 0.14293711764106784
mc = 0.45
gsnext = 0.15
co.forecast_ebitda(ebitda_ttm, gf, financials, me=me, mc=mc, gsnext=gsnext)

# co.forecast_sbc(sbc_f=financials['sbc'], sbc_rate_t=None, financials=financials)
# method omitted: 1 when revenue was forecast, 2 when revenue stays 0.
co.forecast_capex(capex_f=[0.522], method=1, financials=financials)

co.load_financials(financials=financials.copy())
co.fcf_from_ebitda()
# co.fcf_from_earnings(payout=1, gf=0, ROE=1)  # alternate path; do not combine with EBITDA

# co.fcf_to_acquire(adjust_cash=False, year_a=1, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.fcf_to_acquire(adjust_cash=False, year_a=2, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.noa_to_dispose(dnoa=0, tax=0, year_dis=1)
co.fcf_to_debt(leverage=2.0, year_d=6)

# Exactly one distribution method:
# co.fcf_to_allocate(price=price, dp='proportional', buybacks=None)
# co.fcf_to_buyback(price=price, dp='proportional')
# co.fcf_to_bs()

co.value()
co.display_fin()
