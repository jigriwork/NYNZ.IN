"""NYNZ logo set: ORBIT concept. Original hand-built SVG paths (no font dependency).
Bold NYNZ with one orange arc rising around the top right of the Z. Navy #0A1A2F, orange #FF5A1F, white."""
import os
NAVY="#0A1A2F"; ORANGE="#FF5A1F"; WHITE="#FFFFFF"
N="M0 100V0H25L59 58V0H84V100H59L25 42V100Z"
Y="M0 0H28L46 35L64 0H92L58 58V100H34V58Z"
Z="M3 0H79V19L30 80H80V100H0V81L49 20H3Z"
GLYPHS=[(N,0),(Y,92),(N,194),(Z,288)]
def word(fill): return "".join(f'<path transform="translate({x} 0)" d="{d}" fill="{fill}"/>' for d,x in GLYPHS)
# Orbit: thin at the left, rising to the upper right, wrapping down past the Z. Crescent = outer curve out, inner curve back.
ORBIT="M214 2C262 -34 352 -50 386 -26C410 -9 398 34 352 74C384 36 392 4 376 -12C352 -34 278 -24 214 2Z"
ICON_ORBIT="M28 22C44 8 70 0 84 8C96 15 92 38 74 58C84 40 86 22 78 16C68 9 48 12 28 22Z"
def svg(vb,body,label="NYNZ"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}"><title>{label}</title>{body}</svg>'
def horizontal(letter): return svg("-4 -48 412 152", word(letter)+f'<path d="{ORBIT}" fill="{ORANGE}"/>')
def mark(letter, tile=None, r=22):
    bg=f'<rect width="100" height="100" rx="{r}" fill="{tile}"/>' if tile else ""
    return bg+f'<path transform="translate(23 30) scale(0.52)" d="{N}" fill="{letter}"/><path d="{ICON_ORBIT}" fill="{ORANGE}"/>'
def icon(letter, tile=None): return svg("0 0 100 100", mark(letter, tile))
def stacked(letter):  # two-line lockup: NY over NZ, orbit around the Z
    rows=f'<path d="{N}" fill="{letter}"/><path transform="translate(92 0)" d="{Y}" fill="{letter}"/>'
    rows+=f'<path transform="translate(0 138)" d="{N}" fill="{letter}"/><path transform="translate(94 138)" d="{Z}" fill="{letter}"/>'
    return svg("-4 -4 232 246", rows+f'<path transform="translate(-194 138)" d="{ORBIT}" fill="{ORANGE}"/>')
if __name__=="__main__":
    d="public/img"; os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.startswith("nynz-"): os.remove(os.path.join(d,f))
    files={"nynz-logo-horizontal-light.svg":horizontal(NAVY),"nynz-logo-horizontal-dark.svg":horizontal(WHITE),
           "nynz-logo-stacked-light.svg":stacked(NAVY),"nynz-logo-stacked-dark.svg":stacked(WHITE),
           "nynz-icon-light.svg":icon(NAVY),"nynz-icon-dark.svg":icon(WHITE,NAVY),"nynz-app-tile.svg":icon(WHITE,NAVY)}
    for k,v in files.items(): open(f"{d}/{k}","w").write(v)
    open("public/favicon.svg","w").write(icon(WHITE,NAVY).replace('viewBox="0 0 100 100"','viewBox="0 0 100 100" width="64" height="64"'))
    print("logo set:", ", ".join(files))
