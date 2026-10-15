"""Fails if published copy contains em/en dashes, banned AI phrasing or emoji."""
import re, glob, sys
BANNED = ["unlock","seamless","elevate","fast-paced","in today's","empower","leverage","cutting-edge","game-chang","supercharg","revolutioni","effortless","delve","robust","harness","next-level","world-class","synerg","streamline","journey","tailored","best-in-class","guarantee results","100%"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\U0001F000-\U0001F2FF]")
bad = 0
for f in sorted(glob.glob("public/*.html")) + ["scripts/og.html"]:
    t = open(f, encoding="utf-8").read(); text = re.sub(r"<[^>]+>", " ", t).lower()
    for ch, name in (("\u2014", "em dash"), ("\u2013", "en dash")):
        if ch in t: print(f, name, t.count(ch)); bad += 1
    for w in BANNED:
        if w in text: print(f, "banned:", w); bad += 1
    if EMOJI.search(t): print(f, "emoji"); bad += 1
print("copy check:", "PASS" if not bad else f"FAIL ({bad})"); sys.exit(1 if bad else 0)
