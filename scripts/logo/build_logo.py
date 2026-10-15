"""Builds the logo SVG set in public/ from trace.json (see trace.py). Run: python3 scripts/logo/build_logo.py"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, "../../public")
T = json.load(open(os.path.join(HERE, "trace.json")))
NAVY, ORANGE, WHITE = "#0A1A2F", "#FF5A1F", "#FFFFFF"
VB = "104 185 588 192"
def svg(vb, body, label="NYNZ"): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>'
def horizontal(letter): return svg(VB, f'<path fill="{letter}" d="{T["white"]}"/><path fill="{ORANGE}" d="{T["orange"]}"/>')
def first_letter():  # the left-most subpath is the N
    subs = ["M" + s for s in T["white"].split("M")[1:]]
    def minx(s): return min(float(x) for x in re.findall(r"(-?\d+\.\d+) -?\d+\.\d+", s))
    return min(subs, key=minx)
def icon(tile):
    N = first_letter(); bg = f'<rect width="100" height="100" rx="22" fill="{NAVY}"/>' if tile else ""
    # N spans x 107..~215, y 260..373 in source px; place it at the lower left of a 100 box, orbit arc scaled over the top right
    n = f'<g transform="translate(15 26) scale(0.6) translate(-107 -260)"><path fill="{WHITE if tile else NAVY}" d="{N}"/></g>'
    o = f'<g transform="translate(11 9) scale(0.36) translate(-459 -187)"><path fill="{ORANGE}" d="{T["orange"]}"/></g>'
    return svg("0 0 100 100", bg + n + o).replace("<svg ", "<svg width=\"100\" height=\"100\" ", 1)
if __name__ == "__main__":
    d = os.path.join(PUB, "img"); os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.startswith("nynz-"): os.remove(os.path.join(d, f))
    open(f"{d}/nynz-logo-light.svg", "w").write(horizontal(NAVY))
    open(f"{d}/nynz-logo-dark.svg", "w").write(horizontal(WHITE))
    open(f"{PUB}/favicon.svg", "w").write(icon(True))
    # faint orbit arc used as a hero background (decorative)
    open(f"{d}/orbit-bg.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="440 175 270 175" aria-hidden="true"><path fill="#FFFFFF" fill-opacity="0.06" d="{T["orange"]}"/></svg>')
