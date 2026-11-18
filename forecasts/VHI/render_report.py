"""Render report.md to report.pdf beside this file.

The markdown is the source of the figures. This script does not read
forecast.json and does not change a forecast number. It also writes
report.html and layout_checks.json for the page-break check.
"""
from pathlib import Path
import re
import json
from lxml import html, etree
import markdown
from weasyprint import HTML

H = Path(__file__).parent
md = (H / "report.md").read_text(encoding="utf-8")
root = html.fromstring(
    "<html><body>" + markdown.markdown(md, extensions=["tables", "md_in_html"]) + "</body></html>"
)
pat = re.compile(r"\[[ACDEGPS]\d+(?:_\d+)?\](?:[ \t]*\[[ACDEGPS]\d+(?:_\d+)?\])*")
converted = 0
for element in list(root.xpath("//p[not(ancestor::table)] | //li[not(ancestor::table)]")):
    if "".join(element.itertext()).lstrip().startswith("Source:"):
        continue
    text = etree.tostring(element, encoding="unicode", method="html", with_tail=False)
    def convert(m):
        global converted
        converted += 1
        return "<sup>" + ", ".join(re.findall(r"[ACDEGPS]\d+(?:_\d+)?", m.group())) + "</sup>"
    new = pat.sub(convert, text)
    if new != text:
        element.getparent().replace(element, html.fromstring(new))
figs = root.xpath('//div[contains(@class,"fig")]')
for i, e in enumerate(figs):
    e.set("id", f"figure-check-{i}")
css = """@page{size:letter;margin:16mm 14mm;@bottom-right{content:counter(page);font-size:7pt;color:#667}}
body{font-family:'DejaVu Sans',sans-serif;font-size:9pt;line-height:1.37;color:#17222d}
h1{font-size:16pt;margin:0}h2{font-size:11.5pt;border-bottom:1px solid #456;margin-top:13px}
h3{font-size:10pt;margin-top:11px}
table{border-collapse:collapse;width:100%;font-size:7.2pt}
th,td{border:1px solid #bec6cd;padding:3px 4px}th{background:#e7eef4}
thead{display:table-header-group}tr{break-inside:avoid}
.fig{break-inside:avoid;page-break-inside:avoid;margin:6px 0}
.fig>p:first-child{break-after:avoid}
p,li{orphans:2;widows:2}code{font-size:7.8pt}
sup{font-size:0.75em;line-height:0;vertical-align:super}"""
htmltext = (
    '<html><head><meta charset="utf-8"><title>Vitalhub VHI — Company Update, 17 November 2026</title><style>'
    + css
    + "</style></head>"
    + etree.tostring(root.find("body"), encoding="unicode", method="html")
    + "</html>"
)
(H / "report.html").write_text(htmltext, encoding="utf-8")
doc = HTML(string=htmltext).render()
doc.write_pdf(H / "report.pdf")
mapping = {f"figure-check-{i}": set() for i in range(len(figs))}
for n, page in enumerate(doc.pages, 1):
    for box in page._page_box.descendants():
        e = getattr(box, "element", None)
        if e is not None and e.get("id") in mapping:
            mapping[e.get("id")].add(n)
broken = {k: sorted(v) for k, v in mapping.items() if len(v) != 1}
assert not broken, broken
assert len(root.xpath("//table")) == len(figs)
checks = {
    "pages": len(doc.pages),
    "figures": len(figs),
    "tables_single_page": True,
    "superscript_clusters": converted,
}
(H / "layout_checks.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
print(json.dumps(checks))
