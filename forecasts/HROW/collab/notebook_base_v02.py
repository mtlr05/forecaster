import finagle as cmp

# Scenario copy. Edit this cell; leave the cell above as the base case.
# First variant: uncomment the margin-path forecast_ebitda and comment the growth-only call.

ticker = 'HROW'
rd = 0.09672
re = 0.10603
t = 0.21
te = None
shares = 37.229159
price = 28.3
gt = 0.05103
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
    'revenue': [272.303, 344.7459999746, 633.5009998693833, 852.3999996832733, 1076.5459997419873, 1309.8609999523574, 1549.0489996103927, 1738.981999334374],  # leave [0] if forecast_ebitda is commented; that call overwrites it
    'ebitda': [61.923],  # TTM only, or a full list of year + 1 values
    'capex': [0.887],
    'dwc': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sbc': [12.502],
    'tax': [3.771],
    'da': [18.906],
    'debt': [250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0],
    'interest': [24.18],
    'cash': -41.483990601455986,
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
gf = [-0.344669993, 3.755988172, 0.736131981, 0.484979258, 0.324765059, 0.251347915, 0.157804002]

# Comment this out when ebitda is already a full list. Keep revenue at [0] in that case.
# co.forecast_ebitda(ebitda_ttm, gf, financials)

me = 0.5491776226607604
mc = 0.654348
gsnext = 0.114885
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
