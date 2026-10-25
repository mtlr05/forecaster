"""Render report.md -> report.pdf with tables never split across pages.
Each table is wrapped with its caption/label paragraph(s) before and its Source line after in <div class="fig">."""
import re, sys, os, markdown, weasyprint
HERE=os.path.dirname(os.path.abspath(__file__))
CSS = """@page{size:A4 landscape;margin:1.2cm}
body{font-family:sans-serif;font-size:9pt}
table{border-collapse:collapse;font-size:7pt}
td,th{border:1px solid #ccc;padding:2px 4px}
.fig, table, figure{page-break-inside:avoid;break-inside:avoid}
.fig > p:first-child{break-after:avoid;page-break-after:avoid}
thead{display:table-header-group}
tr{break-inside:avoid}
.fig.long table{font-size:6pt}
.cap,h1,h2,h3,h4{break-after:avoid;page-break-after:avoid}
img{max-width:100%;max-height:11cm;display:block;margin:auto;page-break-inside:avoid}"""
def wrap(h):
    n=[0]
    cap=r'(?:<p><strong>(?:Figure|Bull|Bear)[^<]*</strong>[^\n]*</p>\s*)?(?:<p><em>FY[^<]*</em></p>\s*)?'
    def f(m):
        n[0]+=1; long=' long' if m.group(0).count('<tr>')>24 else ''
        return f'<div class="fig{long}">'+m.group(0).replace('<table>',f'<table id="t{n[0]}">',1)+'</div>'
    h=re.sub(r'<p><strong>(Figure|Bull|Bear)',r'<p class="cap"><strong>\1',h)
    cap=cap.replace('<p><strong>','<p(?: class="cap")?><strong>')
    return re.sub(r'('+cap+r'<table>.*?</table>(?:\s*<p><em>Source[^\n]*</p>)?)', f, h, flags=re.S), n[0]
def render(md='report.md', pdf='report.pdf'):
    h,k=wrap(markdown.markdown(open(md).read(), extensions=['tables']))
    doc=weasyprint.HTML(string=f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{h}</body></html>', base_url=HERE).render()
    doc.write_pdf(pdf)
    # verify: every table appears on exactly one page
    pages={}
    def walk(b,i):
        el=getattr(b,'element',None)
        if el is not None and el.tag=='table' and type(b).__name__=='TableBox':
            pid=el.get('id'); pages.setdefault(pid,set()).add(i)
        for c in getattr(b,'children',[]) or []: walk(c,i)
    for i,p in enumerate(doc.pages,1): walk(p._page_box,i)
    split={t:sorted(v) for t,v in pages.items() if len(v)>1}
    print(f'pages {len(doc.pages)}; tables {len(pages)}/{k}; split {split}')
    return not split and len(pages)==k
if __name__=='__main__': sys.exit(0 if render() else 1)
