"""Build the team genealogy SVG (_genealogy.qmd) for the Team page.

Layout coordinates come from the original genealogy sketch (1000 px wide).
Edit NODES / EDGES / MEMBERS and re-run:  python3 tools/make_genealogy.py
"""
from html import escape
from pathlib import Path

W, H = 1000, 1250

# (title, subtitle, x, y, w, kind)   kind: node | ext (external influence)
NODES = [
    ("BIG SCIENCE", "Price · 1963", 360, 121, 220, "node"),
    ("CITATION INDEXING", "Garfield · 1964", 705, 121, 170, "ext"),
    ("MATTHEW EFFECT", "Merton · 1968", 80, 173, 220, "node"),
    ("INVISIBLE COLLEGES", "Price & Beaver 1966 · Crane 1972", 350, 214, 240, "node"),
    ("LABORATORY LIFE", "Latour & Woolgar · 1979", 200, 300, 200, "node"),
    ("SEXENIOS", "Jiménez-Contreras et al. · 2003", 770, 365, 180, "node"),
    ("MATILDA EFFECT", "Rossiter · 1993", 30, 465, 160, "node"),
    ("MODE 2", "Gibbons et al. · 1994", 620, 470, 140, "node"),
    ("TRIPLE HELIX", "Etzkowitz & Leydesdorff · 1995", 785, 505, 180, "node"),
    ("CONTRIBUTORSHIP", "Rennie et al. · 1997", 270, 552, 180, "node"),
    ("WHAT IS|COLLABORATION?", "Katz & Martin · 1997", 455, 552, 210, "node"),
    ("CO-PRODUCTION", "Ostrom · 1996", 800, 575, 150, "node"),
    ("NETWORK SCIENCE", "Watts & Strogatz · Barabási", 615, 605, 170, "ext"),
    ("HYPERAUTHORSHIP", "Cronin · 2001", 195, 638, 190, "node"),
    ("CO-AUTHORSHIP|NETWORKS", "Newman · 2001", 450, 668, 220, "node"),
    ("GLOBAL NETWORK", "Wagner & Leydesdorff · 2005", 680, 725, 160, "node"),
    ("TEAM DOMINANCE", "Wuchty, Jones & Uzzi · 2007", 420, 768, 200, "node"),
    ("SCIENCE OF|TEAM SCIENCE", "Stokols et al. · 2008", 125, 790, 210, "node"),
    ("HELICOPTER|RESEARCH", "", 590, 896, 150, "ext"),
    ("GENDER GAPS", "Larivière et al. · 2013", 40, 898, 150, "node"),
    ("CRediT", "Allen et al. · 2014", 330, 920, 140, "node"),
    ("MOBILITY", "Sugimoto et al. · 2017", 670, 975, 140, "node"),
    ("SMALL vs LARGE TEAMS", "Wu, Wang & Evans · 2019", 495, 1028, 210, "node"),
    ("DIVISION OF LABOUR", "Larivière et al. 2016 · Robinson-Garcia et al. 2020", 240, 1050, 240, "node"),
    ("LOCAL RESEARCH", "Di Césare & Robinson-Garcia · 2026", 815, 1062, 180, "node"),
    ("REMOTE COLLABORATION", "Lin, Frey & Wu · 2023", 655, 1110, 210, "node"),
]

SOLID = ["M470 167 L470 210", "M500 158 C640 190 690 300 690 466", "M190 219 L112 461",
         "M490 260 L552 548", "M725 496 L783 520", "M875 552 L875 571", "M880 621 L903 1058",
         "M360 598 L398 916", "M560 616 L560 664", "M290 684 C360 720 385 820 392 916",
         "M550 734 L525 764", "M760 771 L742 971", "M440 792 L338 806", "M540 814 L592 1024",
         "M110 511 L110 894", "M125 944 L205 1188", "M95 944 L95 1236 L700 1236 L700 1216",
         "M230 856 L230 1188", "M398 966 L365 1046", "M340 1107 L260 1188", "M560 1074 L295 1188",
         "M640 1074 L735 1106", "M742 1021 L758 1106", "M765 1156 L770 1188", "M890 1126 L825 1188"]
DASHED = ["M305 346 L355 548", "M800 430 L708 466", "M430 1198 L348 1198", "M570 1198 L640 1198"]
EXT = ["M770 160 L578 548", "M815 160 L855 361", "M680 644 L600 664", "M720 644 L758 721",
       "M742 925 L893 1056"]

# Member chips: (id, label, x_left, y_center)
MEMBERS = [
    ("jimenez", "Jiménez-Contreras", 800, 428),
    ("ramos", "Ramos-Vielba", 818, 488),
    ("melkers", "Melkers", 656, 586),
    ("du", "Du", 730, 586),
    ("gonzalez", "González-Salmón", 128, 878),
    ("sugimoto", "Sugimoto", 708, 1030),
    ("miao", "Miao", 784, 1030),
    ("dicesare", "Di Césare", 905, 1121),
    ("robinson", "Robinson-García", 437, 1160),
]


def node(title, sub, x, y, w, kind):
    cx = x + w / 2
    lines = title.split("|")
    out = [f'<g class="g-{kind}">']
    ty = y + 16
    if kind == "ext":
        h = 22 + 18 * (len(lines) - 1) + (16 if sub else 4)
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="g-extbox"/>')
        ty = y + 17
    for i, ln in enumerate(lines):
        out.append(f'<text x="{cx}" y="{ty + i * 19}" class="g-title" text-anchor="middle">{escape(ln)}</text>')
    sy = ty + 19 * (len(lines) - 1) + 17
    if sub:
        out.append(f'<text x="{cx}" y="{sy}" class="g-sub" text-anchor="middle">{escape(sub)}</text>')
    if kind == "node":
        out.append(f'<line x1="{cx - 50}" x2="{cx + 50}" y1="{sy + 9}" y2="{sy + 9}" class="g-seam"/>')
    out.append("</g>")
    return "\n".join(out)


def chip(mid, label, x, yc):
    w = round(len(label) * 7.1 + 22)
    return (f'<a href="#m-{mid}" class="g-chip" data-member="{mid}" aria-label="Meet {escape(label)}">'
            f'<rect x="{x}" y="{yc - 11}" width="{w}" height="22" rx="11"/>'
            f'<text x="{x + w / 2}" y="{yc + 4}" text-anchor="middle">{escape(label)}</text></a>')


years = [(1960, 92), (1970, 195), (1980, 299), (1990, 402), (1995, 510), (2000, 619),
         (2005, 727), (2010, 835), (2015, 944), (2020, 1052), (2025, 1160)]

svg = [f'<svg class="genealogy" viewBox="0 30 {W} {H - 30}" role="img" '
       'aria-label="Genealogy of ideas behind STITCH, from Big Science (1963) to team organization and inequalities in science, with the starting point of each team member">',
       '<defs><marker id="gk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L10 5 L0 9 Z" class="g-head"/></marker>'
       '<marker id="gx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L10 5 L0 9 Z" class="g-headx"/></marker></defs>']
for yr, y in years:
    svg.append(f'<text x="18" y="{y + 4}" class="g-year">{yr}</text>')
    svg.append(f'<line x1="62" x2="{W - 20}" y1="{y}" y2="{y}" class="g-grid"/>')
svg.append('<g class="g-edges" marker-end="url(#gk)">' + "".join(f'<path d="{d}"/>' for d in SOLID) + "</g>")
svg.append('<g class="g-edges g-dash" marker-end="url(#gk)">' + "".join(f'<path d="{d}"/>' for d in DASHED) + "</g>")
svg.append('<g class="g-edges g-ext" marker-end="url(#gx)">' + "".join(f'<path d="{d}"/>' for d in EXT) + "</g>")
for n in NODES:
    svg.append(node(*n))
# convergence row
svg.append('<text x="230" y="1204" class="g-end" text-anchor="middle">TEAM ORGANIZATION</text>')
svg.append('<text x="770" y="1204" class="g-end" text-anchor="middle">INEQUALITIES IN SCIENCE</text>')
svg.append('<g class="g-stitch"><rect x="430" y="1176" width="140" height="49" rx="8"/>'
           '<text x="500" y="1197" text-anchor="middle" class="g-stitch-t">STITCH</text>'
           '<text x="500" y="1214" text-anchor="middle" class="g-stitch-s">University of Granada</text></g>')
for m in MEMBERS:
    svg.append(chip(*m))
svg.append("</svg>")

out = Path(__file__).resolve().parent.parent / "_genealogy.qmd"
out.write_text("```{=html}\n<div class=\"genealogy-wrap\">\n" + "\n".join(svg) + "\n</div>\n```\n", encoding="utf-8")
print("wrote", out)
