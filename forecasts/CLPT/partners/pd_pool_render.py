import sys, os, functools, weasyprint
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+'/..')
import render_report as r
r.CSS += '\nimg{max-width:100%;max-height:16cm;display:block;margin:auto;break-inside:avoid}'
r.weasyprint.HTML = functools.partial(weasyprint.HTML, base_url=os.path.dirname(os.path.abspath(__file__))+'/')
sys.exit(0 if r.render('pd_pool_report.md','pd_pool_report.pdf') else 1)
