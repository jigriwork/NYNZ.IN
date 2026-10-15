"""Builds the static NYNZ site into public/. Run: python3 build.py
Logo files and favicon come from scripts/logo/build_logo.py (traced from the approved ORBIT artwork)."""
import os, html
SITE = "https://nynz.in"
EMAIL = "sales@nynz.in"
AUDIT_MAIL = "mailto:sales@nynz.in?subject=Free%20catalogue%20health%20audit&amp;body=Hello%2C%0A%0AI%20would%20like%20the%20free%20health%20audit.%0A%0AName%3A%0AStore%20website%20or%20link%3A%0APlatform%20(for%20example%20Shopify)%3A%0ACountry%3A%0AWhere%20you%20sell%20(for%20example%20Google%20Merchant%20Center%2C%20eBay%2C%20other)%3A%0A%0AI%20can%20share%3A%20a%20product%20export%20%2F%20a%20feed%20file%20%2F%20just%20my%20store%20link%0A%0APlease%20do%20not%20send%20passwords%20or%20store%20access.%20We%20do%20not%20need%20them%20at%20this%20stage.%0A"
NAV = [("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("about.html", "About"), ("faq.html", "FAQ"), ("contact.html", "Contact")]
NOINDEX = {"privacy", "terms"}  # drafts, not in force: keep out of search and the sitemap until approved
ORG_LD = '{"@context":"https://schema.org","@type":"Organization","name":"NYNZ","description":"Free read-only catalogue health audits for Shopify stores, and catalogue and feed care in early access.","url":"https://nynz.in/","logo":"https://nynz.in/icon-512.png","email":"sales@nynz.in"}'
ICONS = {
 "barcode": '<path d="M4 6v12M8 6v12M12 6v12M16 6v12M20 6v12"/><path d="M6 6v12" opacity="0"/>',
 "title": '<path d="M5 7V5h14v2M12 5v14M9 19h6"/>',
 "variants": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
 "stock": '<path d="M4 8l8-4 8 4v8l-8 4-8-4V8z"/><path d="M4 8l8 4 8-4M12 12v8"/>',
 "feed": '<path d="M5 12h11M12 7l5 5-5 5"/><path d="M5 5v14" opacity=".5"/>',
 "listing": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5L15.5 10"/>',
 "undo": '<path d="M9 7L4 12l5 5"/><path d="M4 12h10a6 6 0 010 12" transform="translate(0 -6)"/>',
 "doc": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h5"/>',
 "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
 "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
}
def icon(n): return f'<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONS[n]}</svg></span>'
ARROW = '<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M2 7h9M7.5 3.5L11 7l-3.5 3.5"/></svg>'
def page(slug, title, desc, body, current=None):
    nav = "".join(f'<li><a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    robots = "noindex,follow" if slug in NOINDEX else "index,follow"
    url = f"{SITE}/{'' if slug == 'index' else slug}"
    ld = f'<script type="application/ld+json">{ORG_LD}</script>' if slug == "index" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="NYNZ"><meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="32x32"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#0A1A2F">
<meta name="robots" content="{robots}">
{ld}
<link rel="preload" href="fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/ibm-plex-sans-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
<script src="nav.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><img src="img/nynz-logo-dark.svg" alt="NYNZ home" width="136" height="44"></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main"><ul>{nav}<li><a class="btn" href="{AUDIT_MAIL}">Free health audit</a></li></ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="top">
<div class="about"><img src="img/nynz-logo-dark.svg" alt="NYNZ" width="136" height="44"><p>Catalogue and feed care for Shopify stores. Early access.</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<nav aria-label="Product"><h2>Product</h2><ul><li><a href="how-it-works.html">How it works</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="health-check.html">Free health audit</a></li><li><a href="faq.html">FAQ</a></li></ul></nav>
<nav aria-label="Company"><h2>Company</h2><ul><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li></ul></nav>
<nav aria-label="Legal"><h2>Legal</h2><ul><li><a href="privacy.html">Privacy (draft)</a></li><li><a href="terms.html">Website terms (draft)</a></li></ul></nav>
</div>
<div class="legal"><p>&copy; 2026 NYNZ. Shopify, Google Merchant Center and eBay are trademarks of their owners. NYNZ is not affiliated with them.</p><p>Screens shown on this site are illustrations with made-up example data.</p></div>
</div></footer>
</body>
</html>
"""
# ---------- mockups (every one is labelled as example data) ----------
def mock(bar, body, foot="", cap="Illustration with made-up example data. Not a real store."):
    f = f'<div class="mock-foot">{foot}</div>' if foot else ""
    return f'<figure class="mock"><div class="mock-bar" aria-hidden="true"><i></i><i></i><i></i><b>{bar}</b></div><div class="mock-body">{body}</div>{f}<figcaption class="mock-cap" style="padding:0 20px 14px;margin:0">{cap}</figcaption></figure>'
EX = '<span class="badge early">Example data</span>'
def approval():
    rows = [("Example Canvas Tote", "EX-1001", "Title", "CANVAS TOTE!!", "Canvas Tote", '<span class="badge ok">Check passed</span>', True),
            ("Example Steel Bottle, L", "EX-1042", "Stock", "14", "0", '<span class="badge ok">Barcode match</span>', True),
            ("Example Linen Shirt, M", "EX-1077", "Price", "4,250.00", "42.50", '<span class="badge ok">Supplier file</span>', True),
            ("Example Herbal Tea", "EX-1103", "Description", "cures anxiety", "(removed)", '<span class="badge warn">Flagged</span>', False)]
    r = "".join(f'<div class="row approve"><span class="tick{" on" if on else ""}" aria-hidden="true"></span><span><span class="pname">{n}</span><span class="sku">{s}</span></span><span class="chg"><span class="fld">{f}</span><span class="old">{o}</span>{ARROW}<span class="new">{w}</span></span>{b}</div>' for n, s, f, o, w, b, on in rows)
    head = f'<div class="mock-title"><div><p class="mh">Change set 14</p><p>Waiting for your approval</p></div>{EX}</div>'
    foot = '<p>3 of 4 selected. Nothing is published until you approve. The previous state is saved.</p><span><span class="mbtn">Reject</span> <span class="mbtn p">Approve 3 changes</span></span>'
    return mock("NYNZ review screen", head + r, foot)
def issue_report():
    data = [("Missing barcodes (GTIN)", 31, True), ("Titles with stray capitals or symbols", 22, False), ("Price differs from supplier file", 14, False), ("Out of stock but still on sale", 9, False), ("Feed items rejected", 7, False), ("Duplicate listings", 4, False)]
    bars = "".join(f'<div class="bar-row"><span>{n}</span><span class="n">{v}</span><div class="bar{" hi" if hi else ""}"><span style="width:{round(v/31*100)}%"></span></div></div>' for n, v, hi in data)
    head = f'<div class="mock-title"><div><p class="mh">Free health audit: summary of findings</p><p>Read-only. Issues grouped by type.</p></div>{EX}</div>'
    kp = '<div class="kpis"><div class="kpi"><b>412</b><span>Products read</span></div><div class="kpi"><b>87</b><span>Issues found</span></div><div class="kpi"><b>6</b><span>Issue types</span></div></div>'
    return mock("NYNZ free health audit", head + kp + f'<div class="bars">{bars}</div>')
def diff_table():
    rows = [("Example Canvas Tote", "Title", "CANVAS TOTE!!", "Canvas Tote", "Style rule"),
            ("Example Steel Bottle, L", "Stock", "14", "0", "Barcode match to supplier file"),
            ("Example Linen Shirt, M", "Price", "4,250.00", "42.50", "Supplier file"),
            ("Example Herbal Tea", "Description", "cures anxiety", "(remove)", "Flagged: no evidence, needs your decision")]
    t = "".join(f'<tr><td><span class="pname">{a}</span></td><td class="hide-s">{b}</td><td><span class="old">{c}</span></td><td><span class="new">{d}</span></td><td class="hide-s">{e}</td></tr>' for a, b, c, d, e in rows)
    head = f'<div class="mock-title"><div><p class="mh">Detailed audit: proposed fixes</p><p>Proposed only. Nothing is applied to your store.</p></div>{EX}</div>'
    return mock("NYNZ detailed audit", head + f'<table class="dtable"><thead><tr><th scope="col">Product</th><th scope="col" class="hide-s">Field</th><th scope="col">Found</th><th scope="col">Proposed</th><th scope="col" class="hide-s">Evidence</th></tr></thead><tbody>{t}</tbody></table>')
def monthly():
    head = f'<div class="mock-title"><div><p class="mh">Monitoring: monthly report</p><p>Early access service</p></div>{EX}</div>'
    kp = '<div class="kpis"><div class="kpi"><b>61</b><span>Changes published</span></div><div class="kpi"><b>19</b><span>Waiting on you</span></div><div class="kpi"><b>7</b><span>Could not fix</span></div></div>'
    spark = '<svg class="spark" viewBox="0 0 300 96" role="img" aria-label="Open issues by week, example: 87, 52, 31, 26"><line class="ax" x1="10" y1="80" x2="290" y2="80"/><polyline class="ln" points="30,12 110,40 190,60 270,66"/><circle class="dot" cx="270" cy="66" r="5"/><circle cx="30" cy="12" r="3.5" fill="#0A1A2F"/><circle cx="110" cy="40" r="3.5" fill="#0A1A2F"/><circle cx="190" cy="60" r="3.5" fill="#0A1A2F"/><text x="30" y="94" text-anchor="middle">W1</text><text x="110" y="94" text-anchor="middle">W2</text><text x="190" y="94" text-anchor="middle">W3</text><text x="270" y="94" text-anchor="middle">W4</text></svg>'
    lst = '<ul class="rlist"><li><span>Open issues, week 1 to week 4</span><span class="mono">87 to 26</span></li><li><span>Batches published</span><span class="mono">3</span></li><li><span>Batches rolled back</span><span class="mono">0</span></li></ul>'
    return mock("NYNZ monthly report", head + kp + spark + lst)
def pipeline(cls="", s=None):
    s = s or [("Detect", "Read the catalogue and feed errors and sort problems by type.", ""), ("Propose", "Draft one fix per problem, with old value, new value and evidence.", ""),
         ("Independent check", "A separate checker tests every proposal. It never checks its own work.", ""), ("Your approval", "You approve or reject. Nothing goes live without it.", "gate"),
         ("Publish and verify", "Publish approved changes, save the previous state, re-check.", "")]
    return f'<ol class="pipeline {cls}">' + "".join(f'<li class="{c}"><h3>{t}</h3><p>{d}</p></li>' for t, d, c in s) + "</ol>"
def cta(h, p, label="Get your free health audit", href=AUDIT_MAIL):
    return f'<section class="cta on-navy"><div class="wrap"><div class="t"><h2>{h}</h2><p>{p}</p></div><div class="a"><a class="btn" href="{href}">{label}</a></div></div></section>'
P = {}
def btn(label="Get your free health audit", cls=""): return f'<a class="btn {cls}" href="{AUDIT_MAIL}">{label}</a>'
AUDIT_STEPS = [("Share", "Email us your store link and country, and a product export or feed file if you have one.", ""), ("We read it", "Software and AI read the data. Read-only: nothing in your store is touched.", ""), ("You get a summary", "Counts by problem type, with examples from your own data. Free.", "gate")]
P["index"] = ("Free catalogue health audit for Shopify stores | NYNZ",
 "Get a free, read-only health audit of your product catalogue: a summary of what is wrong, with examples from your data. NYNZ changes nothing in your store.",
f"""<section class="hero on-navy"><div class="wrap grid center gutter-m">
<div class="c-6"><p class="eyebrow">Free health audit &middot; India and international</p>
<h1>See what is wrong with your product catalogue. Free.</h1>
<p class="lead">Share a product export or your store link. We look for the problems that cost stores sales, such as missing barcodes, wrong prices and rejected feed items, and send you a summary of what we found. The audit is read-only: it changes nothing in your store.</p>
<div class="actions">{btn()}<a class="btn secondary" href="how-it-works.html">See how it works</a></div>
<div class="meta"><span class="badge early">Free</span><span class="small">No passwords. No store access needed at this stage.</span></div></div>
<div class="c-6 mock-wrap">{issue_report()}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><p class="eyebrow">How the audit works</p><h2>Three steps, and nothing changes in your store.</h2><p>We work from the export, feed file or store link you share. You decide what happens next.</p></div>
{pipeline("three", AUDIT_STEPS)}
</div></section>
<section class="section paper"><div class="wrap">
<div class="section-head"><p class="eyebrow">What the audit looks at</p><h2>The data problems that stores keep putting off.</h2></div>
<div class="cards">
<div class="card">{icon("barcode")}<h3>Barcodes and identifiers</h3><p>Missing or malformed GTINs, which feeds reject first.</p></div>
<div class="card">{icon("title")}<h3>Titles and attributes</h3><p>Stray capitals, symbols and missing fields that feeds flag.</p></div>
<div class="card">{icon("variants")}<h3>Variants and duplicates</h3><p>Broken option sets and listings that appear twice.</p></div>
<div class="card">{icon("stock")}<h3>Stock and price</h3><p>Where you share a supplier file, mismatches are flagged, never guessed.</p></div>
<div class="card">{icon("feed")}<h3>Shopping feeds</h3><p>Items that Google Merchant Center or an eBay file would reject, where you share the feed or its errors.</p></div>
<div class="card">{icon("doc")}<h3>What we could not check</h3><p>The summary says what the data you shared did not let us confirm.</p></div>
</div></div></section>
<section class="section"><div class="wrap">
<div class="showcase"><div class="txt"><p class="eyebrow">Detailed audit</p><h2>Want every fix listed? Take the detailed audit.</h2><p>The detailed audit lists each problem with a proposed fix and the evidence behind it. It is still read-only: proposals only, nothing applied.</p>
<ul class="checks"><li>India: ₹1,999 + GST</li><li>International: early access, pricing confirmed after your free audit</li></ul></div>
<div class="vis">{diff_table()}</div></div>
<div class="showcase flip"><div class="txt"><p class="eyebrow">Monitoring &middot; early access</p><h2>Ongoing care, only with your approval.</h2><p>After an audit you can ask about monitoring: regular checks, with fixes published only when you approve them and every batch reversible. Pricing is confirmed after your free audit.</p>
<ul class="checks"><li>Nothing goes live without your approval</li><li>Previous state saved for rollback</li><li>Early access: tested on example data only</li></ul></div>
<div class="vis">{monthly()}</div></div>
</div></section>
<section class="section paper"><div class="wrap">
<div class="section-head"><p class="eyebrow">Pricing</p><h2>Start free. Decide later.</h2></div>
<div class="cards">
<div class="card"><span class="badge ok">Free</span><h3 style="margin-top:16px">Health audit</h3><p>A read-only summary of findings. India and international.</p></div>
<div class="card"><span class="badge">India</span><h3 style="margin-top:16px">Detailed audit</h3><p class="price" style="font-size:var(--t-3xl)">₹1,999 <small>+ GST</small></p><p>International: early access, pricing confirmed after your free audit.</p></div>
<div class="card"><span class="badge early">Early access</span><h3 style="margin-top:16px">Monitoring</h3><p>Pricing is confirmed after your free audit.</p></div>
</div><p style="margin-top:24px"><a class="link-arrow" href="pricing.html">Compare in detail</a></p>
</div></section>
<section class="section navy on-navy"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">Status</p><h2>A new service, with a plain status.</h2></div>
<div class="c-7"><p class="lead">Our process has been tested only on example data in a local test, not on a live store. We publish no results or client names, and we cannot promise any outcome from an audit.</p>
<p>We also use MITTY, a brand affiliated with NYNZ, as an affiliated internal testing example. It is not a client case study, and we claim no results from it.</p>
<p><a class="link-arrow" style="color:#fff;border-color:var(--orange)" href="about.html">About NYNZ</a></p></div>
</div></section>
{cta("Find out what is wrong with your catalogue.", "Email us your store link and country. The audit is free and read-only.")}
""")
P["how-it-works"] = ("How it works | NYNZ", "How the free read-only health audit works, what the detailed audit adds, and how monitoring (early access) keeps every change behind your approval.",
f"""<section class="hero page on-navy"><div class="wrap"><p class="eyebrow">How it works</p><h1>Audit first. Changes only if you ask, and only with your approval.</h1>
<p class="lead">The free health audit is read-only. Software and AI read the data you share and report what they find. Nothing is changed or published in your store.</p><div class="actions">{btn()}</div></div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">The audit</p><h2>From your export to a summary of findings.</h2><p class="lead" style="margin-top:16px">Free, read-only and the same for India and international stores.</p></div>
<div class="c-7"><ol class="vsteps">
<li><h3>Share</h3><p>Email us your store link, platform and country. Add a product export or a feed file if you have one (for Shopify, a CSV from admin). Please do not send passwords. We do not ask for store access at this stage.</p></li>
<li><h3>We read</h3><p>Software and AI read what you shared, and your public store pages where that helps, and sort every problem by type: missing barcodes, broken variants, titles feeds would flag, price or stock mismatches against a supplier file you share.</p></li>
<li class="gate"><h3>Summary of findings</h3><p>You get a short report: counts by problem type, examples from your own data, and what the data you shared did not let us check. It is free, and nothing is changed or published.</p></li>
<li><h3>Detailed audit (optional)</h3><p>The detailed audit lists each problem with a proposed fix and the evidence for it. It is still read-only. In India it costs ₹1,999 + GST. For international stores it is early access, with pricing confirmed after your free audit.</p></li>
</ol></div></div></section>
<section class="section paper"><div class="wrap">
<div class="showcase"><div class="txt"><p class="eyebrow">Detailed audit</p><h2>Every problem, with a proposed fix and its evidence.</h2><p>Each row says what field is affected, what it is now, what it would become and the evidence behind it. Where there is no evidence, the item is flagged rather than guessed.</p></div>
<div class="vis">{diff_table()}</div></div>
</div></section>
<section class="section"><div class="wrap">
<div class="section-head"><p class="eyebrow">Monitoring &middot; early access</p><h2>If you want ongoing care, every change still waits for you.</h2><p>Monitoring is an early access service, and our process has been tested only on example data in a local test, not on a live store. Pricing is confirmed after your free audit.</p></div>
{pipeline()}
<div class="showcase flip" style="margin-top:96px"><div class="txt"><p class="eyebrow">Your decision</p><h2>You choose what goes live.</h2><p>Select the changes you accept. Flagged items stay out until you decide. Publishing saves the previous state first, so a batch can be restored. Silence is never approval.</p></div>
<div class="vis">{approval()}</div></div>
</div></section>
<section class="section paper"><div class="wrap">
<div class="section-head"><p class="eyebrow">Safeguards</p><h2>Built to change nothing without you.</h2></div>
<div class="cards five">
<div class="card">{icon("lock")}<h3>The audit is read-only</h3><p>It reads what you share. It does not edit, publish or delete anything in your store.</p></div>
<div class="card">{icon("search")}<h3>Evidence or a flag</h3><p>A fix for price, stock, SKU or barcode needs evidence such as your supplier file. Without it, the item is flagged.</p></div>
<div class="card">{icon("shield")}<h3>A separate checker</h3><p>In monitoring, a separate automated checker tests each proposal. It never checks its own work.</p></div>
<div class="card">{icon("undo")}<h3>Rollback</h3><p>In monitoring, every published batch keeps the previous state so it can be restored.</p></div>
<div class="card">{icon("doc")}<h3>Honest limits</h3><p>Automated findings can be wrong. Look at each example, and tell us if something is off.</p></div>
</div></div></section>
{cta("See it on your own data.", "The free audit needs a store link and, ideally, a product export.")}
""")
P["pricing"] = ("Pricing | NYNZ", "The NYNZ health audit is free and read-only. The detailed audit is ₹1,999 + GST in India. International detailed audit and monitoring are early access, with pricing confirmed after your free audit.",
f"""<section class="hero page on-navy"><div class="wrap"><p class="eyebrow">Pricing</p><h1>Start with the free audit.</h1>
<p class="lead">The health audit is free and read-only, for India and international stores. Everything after it is optional.</p><div class="actions">{btn()}</div></div></section>
<section class="section"><div class="wrap"><div class="cards">
<div class="card plan feature"><header><h2>Free health audit</h2><span class="badge ok">Free</span></header>
<p class="price">Free</p>
<p class="setup">India and international. No obligation.</p>
<ul class="checks"><li>Read-only: nothing is changed or published</li><li>Summary of findings, grouped by problem type</li><li>Examples from your own data</li><li>Works from a product export or feed file you share, or your store link</li><li>No passwords and no store access needed</li></ul>
{btn("Get your free health audit")}</div>
<div class="card plan"><header><h2>Detailed audit</h2><span class="badge">Read-only</span></header>
<p class="price">₹1,999 <small>+ GST, India</small></p>
<p class="setup">International: early access, pricing confirmed after your free audit.</p>
<ul class="checks"><li>Every problem listed, with a proposed fix and its evidence</li><li>Proposals only: nothing is applied to your store</li><li>Flags items where evidence is missing</li><li>Available after your free audit</li></ul>
<a class="btn secondary" href="mailto:sales@nynz.in?subject=Detailed%20audit%20enquiry">Ask about the detailed audit</a></div>
<div class="card plan"><header><h2>Monitoring</h2><span class="badge early">Early access</span></header>
<p class="price" style="font-size:var(--t-2xl)">Pricing confirmed after your free audit</p>
<p class="setup">India and international.</p>
<ul class="checks"><li>Regular catalogue and feed checks</li><li>Every change approved by you before it is published</li><li>Previous state saved, so a batch can be rolled back</li><li>Tested on example data only, not yet on a live store</li></ul>
<a class="btn secondary" href="mailto:sales@nynz.in?subject=Monitoring%20early%20access%20enquiry">Ask about early access</a></div>
</div></div></section>
<section class="section paper"><div class="wrap">
<div class="section-head"><p class="eyebrow">Compare</p><h2>Free audit, detailed audit and monitoring.</h2></div>
<table class="cmp"><thead><tr><th scope="col"><span class="sr">Feature</span></th><th scope="col">Free audit</th><th scope="col">Detailed audit</th><th scope="col">Monitoring (early access)</th></tr></thead><tbody>
<tr><th scope="row">Price</th><td>Free</td><td>India: ₹1,999 + GST. International: early access, pricing confirmed after your free audit</td><td>Early access. Pricing confirmed after your free audit</td></tr>
<tr><th scope="row">What you get</th><td>Summary of findings by problem type, with examples</td><td>Every problem with a proposed fix and its evidence</td><td>Regular checks, proposed fixes and a monthly report</td></tr>
<tr><th scope="row">Changes your store</th><td>No</td><td>No</td><td>Only changes you approve</td></tr>
<tr><th scope="row">Your approval</th><td>Not needed, nothing changes</td><td>Not needed, nothing changes</td><td>Required for every change</td></tr>
<tr><th scope="row">What we need from you</th><td>Store link, country, and a product export or feed file if you have one</td><td>The same, after your free audit</td><td>Agreed after your free audit</td></tr>
<tr><th scope="row">Available to</th><td>India and international</td><td>India now. International in early access</td><td>Early access</td></tr>
</tbody></table>
</div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-5"><h2>Good to know</h2></div>
<div class="c-7"><p>India prices are shown before GST, which is added where it applies. We do not ask for payment details for the free audit.</p>
<p>Theme or code work, advertising management and photography are not part of any of these.</p>
<p>Questions? <a href="mailto:{EMAIL}?subject=Question">Email us</a>.</p>
<p class="hint">Prices and plan details may change before we sign a client. For businesses only. Paid services are provided only under a signed client agreement. An audit finds problems, and automated findings can be wrong. We cannot guarantee that Google or any marketplace will approve a listing, or any other result.</p></div>
</div></section>
""")
def _label_cmp(body):
    import re
    cols = ["Free audit", "Detailed audit", "Monitoring (early access)"]
    def row(m):
        i = iter(cols)
        return re.sub(r"<td", lambda _: f'<td data-label="{next(i)}"', m.group(0))
    return re.sub(r"<tr><th scope=\"row\">.*?</tr>", row, body, flags=re.S)
_t, _d, _b = P["pricing"]; P["pricing"] = (_t, _d, _label_cmp(_b))
P["health-check"] = ("Free catalogue health audit | NYNZ", "A free, read-only audit of your product catalogue: a summary of findings with examples from your data. India and international. We change nothing in your store.",
f"""<section class="hero page on-navy"><div class="wrap grid center gutter-m">
<div class="c-6"><p class="eyebrow">Free health audit</p><h1>Find out what is wrong with your catalogue.</h1>
<p class="lead">Email us your store link and country, and share a product export if you have one. We reply with a summary of what we found. It is free, read-only, and for India and international stores.</p>
<div class="actions">{btn()}</div><div class="meta"><span class="badge early">Example report shown</span></div></div>
<div class="c-6 mock-wrap">{issue_report()}</div></div></section>
<section class="section"><div class="wrap">
<div class="section-head"><p class="eyebrow">What to expect</p><h2>Simple, free, and nothing changes in your store.</h2></div>
<div class="cards">
<div class="card">{icon("doc")}<h3>What you get</h3><p>A summary of findings: counts by problem type, examples from your own data, and what the data you shared did not let us check.</p></div>
<div class="card">{icon("mail")}<h3>What we need</h3><p>Your store link or platform, your country, and ideally a product export or feed file. Passwords are never needed.</p></div>
<div class="card">{icon("lock")}<h3>What we do not do</h3><p>We do not log in to your store, change anything or publish anything. No store access is requested at this stage.</p></div>
</div></div></section>
<section class="section paper"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">What happens next</p><h2>You stay in control.</h2></div>
<div class="c-7"><ol class="vsteps">
<li><h3>You email us</h3><p>Use the button above. It opens an email with the details we need filled in as a template.</p></li>
<li><h3>We reply</h3><p>We confirm what we need. For Shopify, a product CSV exported from admin is enough.</p></li>
<li><h3>You get the summary</h3><p>We send the summary of findings. We cannot promise what an audit will find, and automated findings can be wrong.</p></li>
<li><h3>You decide</h3><p>Nothing continues unless you ask. The detailed audit costs ₹1,999 + GST in India, and is early access with pricing confirmed after your free audit for international stores. Monitoring is early access, with pricing confirmed after your free audit.</p></li>
</ol></div></div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">Not included</p><h2>What the audit is not.</h2></div>
<div class="c-7"><ul class="checks no"><li>An audit of your theme, ads or marketplace account health</li><li>A promise that Google or a marketplace will approve a listing</li><li>Any change to your store</li></ul>
<p class="hint" style="margin-top:24px">We use the details you send only to reply and prepare your audit. If we ask for an export, send product data only, never customer or order data. See our <a href="privacy.html">privacy policy (draft)</a>.</p></div>
</div></section>
{cta("Ready for your free audit?", "One email is enough to start.")}
""")
FAQ = [
("Is the free audit really free?", "Yes. There is no charge and no obligation, and we do not ask for payment details. It is available for India and international stores."),
("What do I get?", "A summary of findings: counts by problem type, examples from your own data, and a note of what the data you shared did not let us check. It is a report only."),
("What do you need from me?", "Your store link or platform, your country, and ideally a product export (for Shopify, a CSV from admin) or a feed file you already have. We do not need passwords and we do not ask for store access at this stage."),
("Do you change my store?", "No. The audit is read-only. It changes nothing and publishes nothing."),
("What does the detailed audit cost?", "In India it is ₹1,999 + GST. For international stores it is early access, with pricing confirmed after your free audit."),
("Is GST added?", "India prices are shown before GST, which is added where it applies."),
("What happens after the free audit?", "You decide. Nothing continues unless you ask. If you want every problem listed with a proposed fix, ask about the detailed audit. If you want ongoing care, ask about monitoring."),
("When is monitoring available?", "Monitoring is early access. We have tested our process only on example data in a local test, not on a live store. Pricing is confirmed after your free audit, and we will tell you honestly whether we can take you on."),
("Will monitoring change my store without asking?", "No. Nothing goes live without your approval, given in the review queue, a shared sheet or by email as agreed, and nothing is applied automatically. Silence is not approval. Every published batch keeps the previous state so it can be restored."),
("Can you guarantee my products will be approved by Google or a marketplace?", "No. Google and marketplaces make their own decisions and change their rules. We report what the data shows and what remains."),
("How do you use AI?", "AI and software read the data, find problems and draft fixes. In monitoring, a separate checking agent verifies every proposal, and the agent that drafts a fix never approves it. Where a finding depends on facts such as price, stock, SKU, barcode or product identity, it needs evidence such as your supplier file. Otherwise it is flagged."),
("Does a person at NYNZ check every finding?", "No. The analysis and checking are automated, and we do not claim otherwise. Automated findings can be wrong, so look at each example. For any change to your store, your approval is the human decision."),
("Which platforms do you support?", "Shopify stores, with Google Merchant Center and eBay file feeds. These are the only integrations we have tested so far, and only on example data in a local test. Tell us if you use something else and we will say honestly whether we can help."),
]
P["faq"] = ("FAQ | NYNZ", "Answers about the free NYNZ health audit: what it is, what we need from you, whether it changes your store, GST, the detailed audit and monitoring in early access.",
f"""<section class="hero page on-navy"><div class="wrap"><p class="eyebrow">FAQ</p><h1>Questions we are asked.</h1></div></section>
<section class="section"><div class="wrap grid gutter-m"><div class="c-4"><h2>Plain answers.</h2><p class="lead" style="margin-top:16px">Something missing? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p><div class="actions">{btn()}</div></div>
<div class="c-8 faq">""" + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ) + """</div></div></section>""")
P["about"] = ("About NYNZ", "NYNZ is a new company founded by Adib Sattar, based in Berhampur, Odisha, India. It offers a free read-only health audit of product catalogues for Shopify stores.",
f"""<section class="hero page on-navy"><div class="wrap"><p class="eyebrow">About</p><h1>One job, done carefully: clean catalogue data.</h1>
<p class="lead">NYNZ is a new company based in Berhampur, Odisha, India, founded by Adib Sattar. We start with a free, read-only health audit of your product catalogue.</p><div class="actions">{btn()}</div></div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">What NYNZ is</p><h2>Catalogue and feed care for Shopify stores.</h2></div>
<div class="c-7"><p class="lead">Product data goes wrong slowly: a missing barcode here, a stale price there, a feed item rejected and never looked at again. NYNZ finds those problems and reports them.</p>
<p>The audit comes first, and it is free. If you want more, there is a detailed audit and, in early access, ongoing monitoring. We do not build themes, run advertising or promise marketplace approvals.</p></div>
</div></section>
<section class="section paper"><div class="wrap">
<div class="section-head"><p class="eyebrow">How the work is done</p><h2>Software and AI do the work. You make the decisions.</h2></div>
<div class="cards">
<div class="card">{icon("search")}<h3>Software and AI read</h3><p>They read the export or feed you share and report what they find, with examples.</p></div>
<div class="card">{icon("shield")}<h3>Findings are automated</h3><p>We do not claim a person checks every finding, and automated findings can be wrong. We say so in every report.</p></div>
<div class="card">{icon("lock")}<h3>You approve any change</h3><p>The audit changes nothing. If you later choose monitoring, nothing goes live without your approval, and batches can be rolled back.</p></div>
</div></div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-5"><p class="eyebrow">Where we are</p><h2>An honest status.</h2></div>
<div class="c-7"><dl class="facts">
<div><dt>Stage</dt><dd>New. The free audit is the starting point. Monitoring is early access.</dd></div>
<div><dt>What we have tested</dt><dd>Our process, on example data in a local test. Not yet on a live store.</dd></div>
<div><dt>Results and clients</dt><dd>We publish no results, testimonials or client names.</dd></div>
<div><dt>MITTY</dt><dd>A brand affiliated with NYNZ. We use it as an affiliated internal testing example. It is not a client case study, and we claim no results from it.</dd></div>
<div><dt>Platforms</dt><dd>Shopify, with Google Merchant Center and eBay file feeds.</dd></div>
</dl></div></div></section>
{cta("Get your free health audit.", "Email us your store link and country. Read-only, and no passwords needed.")}
""")
P["contact"] = ("Contact NYNZ", "Email NYNZ at sales@nynz.in to ask for your free catalogue health audit, or with any question.",
f"""<section class="hero page on-navy"><div class="wrap"><p class="eyebrow">Contact</p><h1>Write to us. We reply by email.</h1>
<p class="lead">Email is the only way to reach NYNZ for now. One address handles audits and questions.</p></div></section>
<section class="section"><div class="wrap grid gutter-m">
<div class="c-6"><div class="mailbox">{icon("mail")}<div><p class="small" style="margin:0">Email</p><p class="mono" style="margin:0"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
<div class="actions">{btn()}<a class="btn secondary" href="mailto:{EMAIL}?subject=NYNZ%20question">Ask something else</a></div></div>
<div class="c-6"><h2 style="font-size:var(--t-xl)">For your free audit, include</h2><ul class="checks" style="margin-top:16px"><li>Your name and your store website or link</li><li>Your platform (for example Shopify) and your country</li><li>Where you sell: Google Merchant Center, eBay, other</li><li>A product export or feed file, if you have one</li></ul>
<p class="hint" style="margin-top:24px">Please do not send passwords or store access. If we ask for an export, send product data only, never customer or order data. See the <a href="privacy.html">privacy policy (draft)</a>.</p></div>
</div></section>
""")
DRAFT = '<p class="draft"><strong>DRAFT FOR PROFESSIONAL REVIEW.</strong> Prepared for review by NYNZ\'s lawyer. It is not in force and should not be relied on. Items in [square brackets] are still to be decided.</p>'
P["privacy"] = ("Privacy policy (draft) | NYNZ", "Draft privacy policy for the NYNZ website, enquiries and the free health audit.", f"""<section class="section"><div class="wrap prose"><h1>Privacy policy</h1>{DRAFT}
<h2>Who we are</h2><p>This website is run by NYNZ, [legal entity name and type], based in Berhampur, Odisha, India. [Postal address: to be provided]. For any privacy question or complaint, email <a href="mailto:sales@nynz.in">sales@nynz.in</a>. Grievance contact: [name to be confirmed].</p>
<h2>What this website collects</h2>
<p><strong>Hosting logs.</strong> The site is hosted by [website host: Cloudflare, Inc. is the recommended host; confirm before launch]. Like any web host, it records technical request data when you visit, including your IP address, the pages and files requested, the date and time, your browser's user agent and the referring page. We use this only to run and secure the site. [Retention period of host logs: to be confirmed.]</p>
<p><strong>No cookies.</strong> The site sets no cookies and uses no advertising or cross-site tracking tools. It does not use analytics today. [Planned: Cloudflare Web Analytics, which Cloudflare says uses no cookies or localStorage and does not fingerprint visitors. This policy will be updated before it is switched on.] The site loads no third-party scripts.</p>
<p><strong>Fonts.</strong> The fonts (IBM Plex Sans and IBM Plex Mono, both under the SIL Open Font License) are served from this website itself. No font service such as Google Fonts receives your data.</p>
<h2>Health audit requests</h2><p>The site has no form. To ask for a health audit you email us at sales@nynz.in, so the details you send reach our business mailbox directly. We use them to reply and prepare your health audit. If we then ask for a product export, please send product data only, never customer or order data.</p>
<h2>Data you send us by email</h2><p>We keep enquiry emails for 12 months after our last contact, and health-check exports for 30 days after we send your report, then delete them. If you ask us not to contact you again, we keep your email address on a do-not-contact list only. Records about paying clients are kept for as long as tax law requires [period to be confirmed].</p>
<h2>Business contacts we find ourselves</h2><p>We may contact people at businesses we think could use our service, by email or LinkedIn message, using work details they or their business have made public. Our sources are company websites, Companies House (the UK register of companies), Shopify App Store reviews that name a store, and LinkedIn profiles we view by hand. We do this on the basis of our legitimate interest in offering a business service. Every such message tells you where we found your details and how to opt out, and you can object at any time. We keep prospect records for at most 6 months after our last message if you do not reply, then delete them. If you opt out, we keep a minimal record (email or company domain, reason and date) so we do not contact you again. [Lawful basis under India's DPDP Act, and for US contacts, to be confirmed.]</p>
<h2>Why we use your data</h2><p>To answer enquiries and provide the health audit (steps you asked for, or our legitimate interests), to perform client agreements (contract), and to meet tax and legal duties (legal obligation).</p>
<h2>Who we share it with</h2><ul><li>[Website host: Vercel Inc. or Cloudflare, Inc., to be confirmed] (visitor request logs).</li><li>Hostinger, our domain, DNS and business email provider.</li><li>[File storage and AI tools used to process client catalogue data: to be confirmed. Our service uses AI to read and draft changes to catalogue data, so these providers will process client data under the client agreement.]</li><li>Our professional advisers, and authorities when the law requires it.</li></ul><p>We do not sell personal data or share it for advertising. Some of these providers may process data outside India; see the UK and EU section below.</p>
<h2>If you are in the UK or EU</h2><p>NYNZ is based in India. If you are in the UK or the EU, the personal data you give us, or that we collect about you, is transferred to and processed in India, and some of our providers (for example our website host) may process it in other countries, including the US. We protect these transfers with [transfer safeguard: e.g. UK IDTA / EU SCCs, to be confirmed], and limit the data to what we need. You can ask us for a copy of the safeguard at sales@nynz.in. [Whether NYNZ needs a UK or EU representative: to be confirmed.]</p>
<h2>Client catalogue data</h2><p>Product data and store access for paying clients are handled under our signed client agreement and data processing addendum, not this policy.</p>
<h2>Your rights</h2><p><strong>UK:</strong> access, correction, erasure, restriction, objection (including an absolute right to object to direct marketing) and portability. You can complain to the Information Commissioner's Office. <strong>India:</strong> access to information, correction and erasure, grievance redressal and nomination; after using our grievance process you can approach the Data Protection Board of India. <strong>US:</strong> where a state privacy law applies, the rights to know, delete and correct. Email sales@nynz.in to use any right; we aim to reply within [30] days.</p>
<h2>Security</h2><p>We limit access to the people who need it, use accounts with two-step sign-in where offered, and delete data on the schedule above.</p>
<h2>Children</h2><p>Our service is for businesses and is not aimed at children.</p>
<h2>Changes</h2><p>We will post any change here with a new date.</p>
<p>Last updated: [DRAFT, date to be set on approval]</p></div></section>""")
P["terms"] = ("Website terms (draft) | NYNZ", "Draft terms of use for the NYNZ website and free health audit.", f"""<section class="section"><div class="wrap prose"><h1>Website terms</h1>{DRAFT}
<h2>Who we are</h2><p>NYNZ, [legal entity name and type], Berhampur, Odisha, India. [Postal address: to be provided]. Contact: <a href="mailto:sales@nynz.in">sales@nynz.in</a>.</p>
<h2>What these terms cover</h2><p>These terms cover your use of this website and the free health audit. Paid services are provided only under a signed Client Service Agreement, which takes priority over anything on this website.</p>
<h2>Business users only</h2><p>This website and our services are for businesses, not consumers.</p>
<h2>Information only</h2><p>The website is for information. Prices shown are list prices, exclude taxes and may change. The free health audit is offered at our discretion. It is not an audit and gives no guarantee.</p>
<h2>How changes are approved</h2><p>Under a client agreement, nothing goes live on a client's store or feeds unless the client has approved that change through the approval method in its agreement: by marking it approved in the review queue, by a reply in a shared sheet, or by email from a named address. The client may approve changes one by one or approve a whole change set it has seen. Approval covers only the changes shown; it never covers future changes. Nothing is applied automatically, and silence is not approval.</p>
<h2>No guarantee of platform outcomes</h2><p>Shopify, Google, eBay and other platforms make their own decisions. We do not guarantee that any listing, feed or account will be approved, ranked or kept active, or that any sales will result. Nothing on this site is legal advice or a promise of legal compliance.</p>
<h2>Intellectual property</h2><p>The site content and the NYNZ name and logo belong to NYNZ. Shopify, Google Merchant Center and eBay are trademarks of their owners, and NYNZ is not affiliated with them.</p>
<h2>Acceptable use</h2><p>Do not misuse the site, try to break its security, or send us data you have no right to share.</p>
<h2>Liability</h2><p>[FOR LAWYER REVIEW: cap amount and period.] To the extent the law allows, our total liability arising out of or in connection with this website or the free health audit, whether in contract, tort (including negligence) or otherwise, is limited to the total fees you have paid to NYNZ in the 12 months before the event giving rise to the claim. We are not liable for loss of profit, revenue, sales, business or goodwill, or for indirect or consequential loss. Nothing limits liability for fraud, wilful misconduct, or any liability that cannot be limited by law. For paid services, the liability terms of the signed client agreement apply instead.</p>
<h2>Links</h2><p>We are not responsible for other websites we link to.</p>
<h2>Governing law and disputes</h2><p>These terms are governed by the laws of India. Subject to any arbitration option below, the courts at [Berhampur, Odisha] [or: the courts having jurisdiction in Odisha, India] have exclusive jurisdiction. [Arbitration option: to be decided by the lawyer, as in the client agreement.] Either party may seek urgent interim relief from a competent court.</p>
<h2>Changes</h2><p>We may update these terms and will post the new date here.</p>
<p>Last updated: [DRAFT, date to be set on approval]</p></div></section>""")
CURRENT = {"how-it-works": "how-it-works.html", "pricing": "pricing.html", "about": "about.html", "faq": "faq.html", "contact": "contact.html", "health-check": "health-check.html"}
def run():
    os.makedirs("public", exist_ok=True)
    for slug, (t, d, b) in P.items():
        open(f"public/{slug}.html", "w", encoding="utf-8").write(page(slug, t, d, b, CURRENT.get(slug)))
    urls = [slug for slug in P if slug not in NOINDEX]
    loc = lambda slug: SITE + "/" + ("" if slug == "index" else slug)
    open("public/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{loc(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
    open("public/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(P), "pages;", len(urls), "in sitemap")
if __name__ == "__main__": run()
