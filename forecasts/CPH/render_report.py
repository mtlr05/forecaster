"""Render forecasts/CPH/report.md to report.pdf. Tables stay on one page."""
import markdown
import weasyprint
from pathlib import Path

HERE = Path(__file__).parent
md = (HERE / "report.md").read_text()
body = markdown.markdown(md, extensions=["tables", "md_in_html"])
css = """
@page { size: A4; margin: 14mm 12mm;
  @bottom-center { content: counter(page); font-size: 8pt; } }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 9pt; line-height: 1.35; }
h1 { font-size: 16pt; margin: 0 0 2px; }
h2 { font-size: 12pt; color: #1a3d6d; margin-top: 14px; }
h3 { font-size: 10pt; }
table { border-collapse: collapse; width: 100%; font-size: 7.5pt; margin: 4px 0; }
th, td { border-bottom: 1px solid #ccc; padding: 2px 4px; text-align: right; vertical-align: top; }
th:first-child, td:first-child { text-align: left; }
th { background: #e8eef6; }
div.fig { break-inside: avoid; page-break-inside: avoid; margin: 8px 0 12px; }
div.fig.tight table { font-size: 6pt; }
div.fig p:first-child { break-after: avoid; page-break-after: avoid; }
thead { display: table-header-group; }
tr { break-inside: avoid; page-break-inside: avoid; }
li { margin-bottom: 2px; }
code { font-size: 8pt; }
"""
html = (
    "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>"
    % (css, body)
)
weasyprint.HTML(string=html, base_url=str(HERE)).write_pdf(HERE / "report.pdf")
print("wrote", HERE / "report.pdf")
