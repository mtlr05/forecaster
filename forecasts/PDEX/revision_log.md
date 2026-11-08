# PDEX v3 → v4 revisions

7 November 2026, America/Toronto. All amounts US$M; full precision in JSON.

|Case|Year|Revenue before|After|EBITDA before|After|
|---|---|---|---|---|---|
|base|FY27E|82.700000|82.700000|15.621463|15.493111|
|base|FY28E|86.800000|86.800000|16.615498|16.427038|
|bull|FY27E|84.700000|85.047080|17.158500|17.122411|
|bull|FY28E|89.300000|93.401480|18.363020|20.002472|
|bear|FY27E|78.700000|78.292830|13.181000|12.918977|
|bear|FY28E|77.300000|74.718980|12.410520|11.404248|

Base revenue remains consensus; Monogram now explicitly0.307170/2.216020M inside it. Own build82.617170/85.283180M (old82.460000/83.167160). Replace old bull combined0.5/1.0M allowance; high Monogram1.054250/7.267500M, low0.050000/0.085000M; Helios separate. Base EBITDA is lower because high-margin purchase fees are small early, with explicit launch support and new APM rent0.092800/0.141056M. No whole-robot or sourced-disposable gross bill counted as PDEX sales; no CVR operating revenue.

History/year-zero, capex method1, horizon and next-year growth/margin leaves retained. No Finagle/terminal growth, valuation, repository method changes or commits. See report for evidence and judgment bands, robotics_model.csv for arithmetic, revision_log.csv for line-by-line amounts and growth revisions.

## Detailed line changes

|Case|Year|Line|Old|New|Delta|Old growth|New growth|Why|
|---|---|---|---|---|---|---|---|---|
|base|FY27E|Medical devices|69.782028|69.800604|0.018576|0.123740|0.124039|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|base|FY27E|Industrial and scientific|2.960000|2.960000|0.000000|0.956378|0.956378|APM acquired-line run rate remains unscaled.|
|base|FY27E|NRE and prototype services|1.203623|1.201098|-0.002525|-0.270532|-0.272062|Reconcile core while retaining explicit robotics allocations.|
|base|FY27E|Repairs|8.553745|8.536919|-0.016826|-0.317883|-0.319225|Residual-core reconciliation plus retained case repair stress.|
|base|FY27E|Discounts and other|0.200604|0.201379|0.000775|-1.792901|-1.795965|Eligible sourced-product fee only, not gross disposable purchase bill.|
|base|FY27E|revenue|82.700000|82.700000|0.000000|0.066436|0.066436|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|base|FY27E|ebitda|15.621463|15.493111|-0.128352|0.036387|0.027872|Stream margins, fee admin, launch support and newly disclosed APM rent.|
|base|FY28E|Medical devices|74.910834|75.038438|0.127604|0.073498|0.075040|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|base|FY28E|Industrial and scientific|3.108000|3.108000|0.000000|0.050000|0.050000|APM acquired-line run rate remains unscaled.|
|base|FY28E|NRE and prototype services|1.254452|1.220985|-0.033467|0.042230|0.016557|Reconcile core while retaining explicit robotics allocations.|
|base|FY28E|Repairs|7.317639|7.133541|-0.184098|-0.144511|-0.164389|Residual-core reconciliation plus retained case repair stress.|
|base|FY28E|Discounts and other|0.209075|0.299035|0.089960|0.042227|0.484937|Eligible sourced-product fee only, not gross disposable purchase bill.|
|base|FY28E|revenue|86.800000|86.800000|0.000000|0.049577|0.049577|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|base|FY28E|ebitda|16.615498|16.427038|-0.188460|0.063633|0.060280|Stream margins, fee admin, launch support and newly disclosed APM rent.|
|bull|FY27E|Medical devices|70.782028|71.569604|0.787576|0.139844|0.152527|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|bull|FY27E|Industrial and scientific|2.960000|2.960000|0.000000|0.956378|0.956378|APM acquired-line run rate remains unscaled.|
|bull|FY27E|NRE and prototype services|1.703623|1.251098|-0.452525|0.032499|-0.241759|Reconcile core while retaining explicit robotics allocations.|
|bull|FY27E|Repairs|9.053745|9.036919|-0.016826|-0.278011|-0.279353|Residual-core reconciliation plus retained case repair stress.|
|bull|FY27E|Discounts and other|0.200604|0.229459|0.028855|-1.792901|-1.906953|Eligible sourced-product fee only, not gross disposable purchase bill.|
|bull|FY27E|revenue|84.700000|85.047080|0.347080|0.092227|0.096702|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|bull|FY27E|ebitda|17.158500|17.122411|-0.036089|0.138360|0.135966|Stream margins, fee admin, launch support and newly disclosed APM rent.|
|bull|FY28E|Medical devices|75.910834|80.105138|4.194304|0.072459|0.119262|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|bull|FY28E|Industrial and scientific|3.108000|3.108000|0.000000|0.050000|0.050000|APM acquired-line run rate remains unscaled.|
|bull|FY28E|NRE and prototype services|2.254452|1.270985|-0.983467|0.323328|0.015896|Reconcile core while retaining explicit robotics allocations.|
|bull|FY28E|Repairs|7.817639|7.633541|-0.184098|-0.136530|-0.155294|Residual-core reconciliation plus retained case repair stress.|
|bull|FY28E|Discounts and other|0.209075|1.283815|1.074740|0.042227|4.594963|Eligible sourced-product fee only, not gross disposable purchase bill.|
|bull|FY28E|revenue|89.300000|93.401480|4.101480|0.054309|0.098233|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|bull|FY28E|ebitda|18.363020|20.002472|1.639452|0.070200|0.168204|Stream margins, fee admin, launch support and newly disclosed APM rent.|
|bear|FY27E|Medical devices|66.782028|66.494604|-0.287424|0.075430|0.070801|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|bear|FY27E|Industrial and scientific|2.960000|2.960000|0.000000|0.956378|0.956378|APM acquired-line run rate remains unscaled.|
|bear|FY27E|NRE and prototype services|1.203623|1.101098|-0.102525|-0.270532|-0.332668|Reconcile core while retaining explicit robotics allocations.|
|bear|FY27E|Repairs|7.553745|7.536919|-0.016826|-0.397628|-0.398970|Residual-core reconciliation plus retained case repair stress.|
|bear|FY27E|Discounts and other|0.200604|0.200209|-0.000395|-1.792901|-1.791341|Eligible sourced-product fee only, not gross disposable purchase bill.|
|bear|FY27E|revenue|78.700000|78.292830|-0.407170|0.014855|0.009605|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|bear|FY27E|ebitda|13.181000|12.918977|-0.262023|-0.125522|-0.142906|Stream margins, fee admin, launch support and newly disclosed APM rent.|
|bear|FY28E|Medical devices|66.910834|64.602638|-2.308196|0.001929|-0.028453|Core consensus reconciliation; manufactured Monogram and Helios high/central/low allocations.|
|bear|FY28E|Industrial and scientific|3.108000|3.108000|0.000000|0.050000|0.050000|APM acquired-line run rate remains unscaled.|
|bear|FY28E|NRE and prototype services|1.254452|1.170985|-0.083467|0.042230|0.063470|Reconcile core while retaining explicit robotics allocations.|
|bear|FY28E|Repairs|5.817639|5.633541|-0.184098|-0.229834|-0.252541|Residual-core reconciliation plus retained case repair stress.|
|bear|FY28E|Discounts and other|0.209075|0.203815|-0.005260|0.042227|0.018013|Eligible sourced-product fee only, not gross disposable purchase bill.|
|bear|FY28E|revenue|77.300000|74.718980|-2.581020|-0.017789|-0.045647|Sum reported lines; base consensus retained; explicit pipeline differences in scenarios.|
|bear|FY28E|ebitda|12.410520|11.404248|-1.006272|-0.058454|-0.117248|Stream margins, fee admin, launch support and newly disclosed APM rent.|
