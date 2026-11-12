import finagle as cmp

# Scenario copy. Edit this cell; leave the cell above as the base case.
# First variant: uncomment the margin-path forecast_ebitda and comment the growth-only call.

ticker = 'HROW'
rd = 0.09672
re = 0.10498
t = 0.21
te = None
shares = 40.63399386550903
price = 29.37
gt = 0.049980000000000004
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
    'date': '2025-12-31',
    'revenue': [272.303, 358.458999879226, 645.9589996668138, 866.3529995128174, 1127.46599939712, 1382.4419988314369, 1627.7989992139273, 1845.3669997350828],  # leave [0] if forecast_ebitda is commented; that call overwrites it
    'ebitda': [61.923],  # TTM only, or a full list of year + 1 values
    'capex': [0.887],
    'dwc': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sbc': [12.502],
    'tax': [3.771],
    'da': [18.906],
    'debt': [250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0],
    'interest': [24.18],
    'cash': 44.19632247836452,
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
ebitda_ttm = 61.923
gf = [-0.175007671, 3.002603453, 0.694968138, 0.550317097, 0.335471756, 0.241272916, 0.17122491]

# Comment this out when ebitda is already a full list. Keep revenue at [0] in that case.
# co.forecast_ebitda(ebitda_ttm, gf, financials)

me = 0.5653092312703962
mc = 0.664961
gsnext = 0.118788
co.forecast_ebitda(ebitda_ttm, gf, financials, me=me, mc=mc, gsnext=gsnext)

co.forecast_sbc(sbc_f=[12.502], financials=financials)
# method omitted: 1 when revenue was forecast, 2 when revenue stays 0.
co.forecast_capex(capex_f=[0.887], method=1, financials=financials)

co.load_financials(financials=financials.copy())
co.fcf_from_ebitda()
# co.fcf_from_earnings(payout=1, gf=0, ROE=1)  # alternate path; do not combine with EBITDA

# co.fcf_to_acquire(adjust_cash=False, year_a=1, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.fcf_to_acquire(adjust_cash=False, year_a=2, ebitda_frac=0.10, multiple=10, leverage=3, gnext=0.10, cap_frac=0.20)
# co.noa_to_dispose(dnoa=0, tax=0, year_dis=1)
co.fcf_to_debt(leverage=4.037272095990181, year_d=1)

# Exactly one distribution method:
# co.fcf_to_allocate(price=price, dp='proportional', buybacks=None)
# co.fcf_to_buyback(price=price, dp='proportional')
# co.fcf_to_bs()

co.value()
co.display_fin()
