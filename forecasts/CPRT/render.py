import markdown, weasyprint
md=open('report.md').read()
body=markdown.markdown(md, extensions=['tables','md_in_html'])
css="""@page{size:A4;margin:16mm 15mm;@bottom-center{content:counter(page);font-size:8pt}}
body{font-family:'DejaVu Sans',sans-serif;font-size:9pt;line-height:1.35}
h1{font-size:17pt;margin:0}h2{font-size:12pt;color:#1a3d6d;margin-top:14px}h3{font-size:10pt}
table{border-collapse:collapse;width:100%;font-size:7.6pt;margin:4px 0}th,td{border-bottom:1px solid #ccc;padding:2px 4px;text-align:right}
th:first-child,td:first-child{text-align:left}th{background:#e8eef6}
div.fig{break-inside:avoid;page-break-inside:avoid;margin:8px 0}div.fig p:first-child{break-after:avoid}
thead{display:table-header-group}tr{break-inside:avoid}li{margin-bottom:2px}code{font-size:8pt}"""
weasyprint.HTML(string=f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>").write_pdf('report.pdf')
