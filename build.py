"""Builds the static NYNZ site into public/. Run: python3 build.py"""
import os, html
SITE = "https://nynz.in"
NAV = [("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("faq.html", "FAQ")]
NOINDEX = {"privacy", "terms", "brand"}  # drafts and an internal brand page: keep out of search and the sitemap until approved
ORG_LD = '{"@context":"https://schema.org","@type":"Organization","name":"NYNZ","url":"https://nynz.in/","logo":"https://nynz.in/img/nynz-logo-horizontal-light.svg","email":"sales@nynz.in"}'
def page(slug, title, desc, body, current=None):
    nav = "".join(f'<li><a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}/{'' if slug == 'index' else slug}">
<meta property="og:type" content="website"><meta property="og:site_name" content="NYNZ">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="32x32"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#0A1A2F">
{'<meta name="robots" content="noindex,follow">' if slug in NOINDEX else '<meta name="robots" content="index,follow">'}
{('<script type="application/ld+json">' + ORG_LD + '</script>') if slug == "index" else ""}
<link rel="preload" href="fonts/source-serif-4-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><img src="img/nynz-logo-horizontal-dark.svg" alt="NYNZ home" width="76" height="28"></a>
<nav class="nav" aria-label="Main"><ul>{nav}<li><a class="btn" href="health-check.html"{" aria-current=page" if current == "health-check.html" else ""}>Free health check</a></li></ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><img src="img/nynz-logo-horizontal-dark.svg" alt="NYNZ" width="65" height="24"><p>Catalogue and feed care for Shopify stores.</p><p><a href="mailto:sales@nynz.in">sales@nynz.in</a></p></div>
<nav aria-label="Footer"><ul><li><a href="how-it-works.html">How it works</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="faq.html">FAQ</a></li><li><a href="health-check.html">Free health check</a></li></ul></nav>
<nav aria-label="Legal"><ul><li><a href="privacy.html">Privacy (draft)</a></li><li><a href="terms.html">Website terms (draft)</a></li><li><a href="brand.html">Brand</a></li></ul></nav>
</div>
<p class="small">&copy; 2026 NYNZ. Shopify, Google Merchant Center and eBay are trademarks of their owners. NYNZ is not affiliated with them.</p>
</div></footer>

</body>
</html>
"""
P = {}
P["index"] = ("NYNZ | Catalogue and feed care for Shopify stores",
 "NYNZ keeps Shopify product data and shopping feeds clean every month. Fixed price. Nothing goes live without your approval.",
f"""<section class="hero"><div class="wrap">
<p class="eyebrow">Catalogue &amp; Feed Care &middot; Early access</p>
<h1>Your product data and shopping feeds, kept clean every month.</h1>
<p class="lead">NYNZ fixes the catalogue problems that cost Shopify stores sales: missing barcodes, broken variants, wrong prices, stale stock and rejected feed items. One fixed monthly price. Software and AI do the work, a separate automated checker verifies every proposed change, and nothing goes live on your store until you approve it.</p>
<div class="actions"><a class="btn" href="health-check.html">Get a free catalogue health check</a><a class="btn secondary" href="pricing.html">See pricing</a></div>
</div></section>
<section><div class="wrap split">
<div><p class="eyebrow">What we look after</p><h2>The unglamorous data work, done properly.</h2><p>Most stores know their catalogue has problems. Few have someone whose job is to fix them every week.</p></div>
<ul class="list">
<li><strong>Product data</strong>Titles, attributes, variants, barcodes (GTINs) and duplicate listings.</li>
<li><strong>Stock and price checks</strong>Supplier stock files matched to your SKUs, with mismatches and out-of-stock items still on sale flagged.</li>
<li><strong>Shopping feeds</strong>Google Merchant Center and one marketplace feed checked weekly, with rejected items fixed.</li>
<li><strong>New listings</strong>Drafted from your supplier sheets, checked automatically and sent to you for approval before they are published.</li>
<li><strong>A monthly health report</strong>What we found, what we changed and what still needs your input.</li>
</ul></div></section>
<section><div class="wrap">
<p class="eyebrow">How it works</p><h2>Proposed, checked, approved, then published.</h2>
<div class="grid g3">
<div class="card"><h3>1. Detect and propose</h3><p>Software and AI read your catalogue export and feed error reports, sort every problem by type and draft a fix for each, with the old value, the new value and the evidence.</p></div>
<div class="card"><h3>2. Independent check</h3><p>A separate checker, never the one that drafted the fix, tests each proposal. Anything it cannot confirm is flagged for you rather than proposed as fixed.</p></div>
<div class="card"><h3>3. You approve, we publish</h3><p>You see each change as a before and after. Only changes you approve go live, with a saved copy of the previous state, so any batch can be undone.</p></div>
</div>
<p style="margin-top:1.5rem"><a href="how-it-works.html">Read the full process</a></p>
</div></section>
<section><div class="wrap split">
<div><p class="eyebrow">Early access</p><h2>New service, honest status.</h2></div>
<div><p>Catalogue &amp; Feed Care is in early access. We have tested our process only on example data in a local test, not on a live store, and we publish no results or client names. We also use MITTY, a brand affiliated with NYNZ, as an affiliated internal testing example. It is not a client case study, and we claim no results from it.</p></div>
</div></section>
<section><div class="wrap split">
<div><p class="eyebrow">Pricing</p><h2>One fixed monthly price.</h2></div>
<div><p class="lead">From <strong>$399 a month</strong> for stores in the US and UK, plus a one-time setup based on catalogue size. For Indian stores, <strong>India Pro is ₹7,999 a month + GST</strong>, with a one-time setup of ₹1,999 plus ₹2 per SKU above 600.</p><p><a href="pricing.html">Compare plans</a></p></div>
</div></section>
<section><div class="wrap split">
<div><p class="eyebrow">Out of scope</p><h2>What we do not do.</h2></div>
<ul class="list">
<li><strong>Theme and code work</strong>We do not build or change Shopify themes or apps.</li>
<li><strong>Advertising</strong>We keep feeds accurate. We do not run or manage ad campaigns.</li>
<li><strong>Approval promises</strong>Marketplaces and Google make their own decisions. We fix the data; we cannot promise a listing will be approved.</li>
</ul></div></section>
<section><div class="wrap"><h2>Find out what is wrong with your catalogue.</h2><p class="lead">Send us a product export. We will reply with a short report of the problems we find, grouped by type. Free, and no store access needed.</p><div class="actions"><a class="btn" href="health-check.html">Request a health check</a></div></div></section>
""")
P["how-it-works"] = ("How it works | NYNZ", "How NYNZ finds, checks, publishes and reports catalogue and feed fixes for Shopify stores, and where your approval comes in.",
"""<section class="hero"><div class="wrap"><p class="eyebrow">How it works</p><h1>A clear process, with your approval before anything goes live.</h1>
<p class="lead">Software and AI do the finding, drafting and checking. A separate automated checker verifies every proposal. You approve every change before it goes live on your store.</p></div></section>
<section><div class="wrap">
<ol class="steps">
<li><div><h2 class="step-title">Set up</h2><p>You share a product export or limited staff access, your supplier stock files and the feeds you sell through. We propose a one-time cleanup for your approval, then agree who on your side approves changes.</p></div></li>
<li><div><h2 class="step-title">Detect</h2><p>Each week we read the catalogue and feed error reports and sort every problem by type: missing barcodes, broken variants, price mismatches, policy words, stock that is out but still on sale.</p></div></li>
<li><div><h2 class="step-title">Propose</h2><p>Software and AI draft each fix as a single change with the old value, the new value, the evidence used and how confident the match is. Nothing is applied automatically.</p></div></li>
<li><div><h2 class="step-title">Independent check</h2><p>A separate checking agent tests every proposal. The agent that drafts a fix never approves it. Fixed rules check that each change is well formed. For prices, stock, SKUs, barcodes and product identity, a change needs authoritative evidence, such as your supplier file or your own records. Without it, the item is flagged for you and no fix is proposed.</p></div></li>
<li><div><h2 class="step-title">Your approval</h2><p>We send you the change set through the approval method in your agreement: the review queue, a shared sheet or email. You approve or reject each change, or approve a whole change set you have seen. Silence is not approval, and without your approval nothing is published.</p></div></li>
<li><div><h2 class="step-title">Publish and check</h2><p>Only the changes you approved are published, with a saved copy of the previous state. We then re-run the checks to see whether the error count went down, and flag anything that did not improve.</p></div></li>
<li><div><h2 class="step-title">Monthly report</h2><p>You get a one-page summary: problems found, changes made, items waiting on you, and anything we could not fix. Any batch can be rolled back.</p></div></li>
</ol></div></section>
<section><div class="wrap split">
<div><p class="eyebrow">Example</p><h2>What a change looks like.</h2><p>An illustration using made-up products. Every change is shown to you this way, and nothing is published until you approve it.</p></div>
<div class="table-scroll" tabindex="0" role="region" aria-label="Example review queue"><table>
<caption class="eyebrow" style="text-align:left;caption-side:top;padding-bottom:.5rem">Example review queue (illustrative data)</caption>
<thead><tr><th scope="col">Product</th><th scope="col">Field</th><th scope="col">Before</th><th scope="col">After</th><th scope="col">Route</th></tr></thead>
<tbody>
<tr><td>Canvas Tote, Navy</td><td>Title</td><td class="diff-old">CANVAS TOTE!!</td><td class="diff-new">Canvas Tote</td><td>Low risk, you can approve in bulk</td></tr>
<tr><td>Steel Bottle, L</td><td>Stock</td><td class="diff-old">14</td><td class="diff-new">0</td><td>Match confirmed by barcode, needs your approval</td></tr>
<tr><td>Linen Shirt, M</td><td>Price</td><td class="diff-old">$4,250.00</td><td class="diff-new">$42.50</td><td>Needs your approval</td></tr>
<tr><td>Herbal Tea</td><td>Description</td><td class="diff-old">"cures anxiety"</td><td class="diff-new">(removed)</td><td>Flagged, needs your approval</td></tr>
</tbody></table></div>
</div></section>
<section><div class="wrap split"><div><p class="eyebrow">Safeguards</p><h2>Built to be undone.</h2></div>
<ul class="list">
<li><strong>Nothing auto-applied</strong>Every change waits for your approval, given in the review queue, a shared sheet or by email. Low-confidence matches and destructive changes are flagged for extra care.</li>
<li><strong>Two keys for stock</strong>A supplier stock update is only proposed when the SKU match is confirmed by barcode or product title. Uncertain matches are flagged, and you still approve every update.</li>
<li><strong>Rollback</strong>Every published batch keeps the previous state so it can be restored.</li>
<li><strong>Honest limits</strong>Automated checks can be wrong. That is why you approve every change, why uncertain items are flagged instead of fixed, and why every batch can be rolled back.</li>
<li><strong>Limited access</strong>We work from exports or restricted staff accounts, never full owner access.</li>
</ul></div></section>
<section><div class="wrap"><h2>See it on your own data.</h2><div class="actions"><a class="btn" href="health-check.html">Request a free health check</a></div></div></section>
""")
P["pricing"] = ("Pricing | NYNZ", "Catalogue & Feed Care (early access): Starter from $399 a month for US and UK Shopify stores, and India Pro at ₹7,999 a month plus GST for Indian stores. Launch prices, subject to change.",
"""<section class="hero"><div class="wrap"><p class="eyebrow">Pricing</p><h1>Fixed monthly prices. No hourly billing.</h1>
<p class="lead">Catalogue &amp; Feed Care is in early access, so these are launch prices. Each plan includes a set number of changes a month. If you need more, extra changes are billed per change at the rate shown.</p></div></section>
<section><div class="wrap"><h2>US and UK</h2><div class="grid g2" style="margin-top:1rem">
<div class="card plan primary"><span class="tag">US and UK</span><h2 style="margin-top:1rem">Starter</h2>
<p class="price">$399 <small>per month</small></p>
<p>Setup: <strong>$0.35 per SKU, minimum $199</strong>, one time. For example, $350 for 1,000 SKUs.</p>
<ul>
<li>Up to 1,000 live SKUs</li><li>1 Shopify store and 2 feeds from Google Merchant Center and an eBay file</li>
<li>150 changes a month, including up to 40 new listings</li><li>Weekly feed error sweep</li><li>Monthly catalogue health report</li>
<li>Target turnaround: 1 business day for rejected feed items, 2 for routine changes</li>
<li>Every change approved by you before we publish</li>
</ul>
<p class="hint">Billed in US dollars. Monthly, with a 2-month minimum. Extra changes $1 each, only if you approved them.</p>
<a class="btn" href="health-check.html">Start with a free health check</a></div>
</div>
<h2 style="margin-top:3rem">India</h2><div class="grid g2" style="margin-top:1rem">
<div class="card plan primary"><span class="tag">India</span><h2 style="margin-top:1rem">India Pro</h2>
<p class="price">₹7,999 <small>per month + GST</small></p>
<p>Setup: <strong>₹1,999 plus ₹2 per SKU above 600</strong>, one time. For example, ₹2,799 for 1,000 SKUs.</p>
<ul>
<li>251 to 1,000 live SKUs</li><li>1 Shopify store, with Google Merchant Center and eBay file feeds (the tested types)</li>
<li>60 client-approved changes a month</li><li>Monthly health report</li>
<li>Every change approved by you before we publish</li>
</ul>
<p class="hint">Monthly, no lock-in. Extra changes are quoted before we do them, and only done if you approve them.</p>
<a class="btn secondary" href="health-check.html">Start with a free health check</a></div>
</div>
<p class="hint" style="margin-top:2rem">Launch prices and plan allowances are our current assumptions, not yet tested with paying customers, and may change before we sign a client. For businesses only. Prices exclude taxes. Paid services are provided only under a signed client agreement. We cannot guarantee that Google or any marketplace will approve a listing.</p>
<p>Larger catalogue or more channels? <a href="mailto:sales@nynz.in?subject=Larger%20catalogue">Email us</a> and we will quote a fixed price.</p>
</div></section>
<section><div class="wrap split"><div><h2>What counts as a change</h2></div>
<div><p>One edit to one product or variant: a price, a stock level, an attribute, a variant fix, or one new listing. A bulk fix that corrects the same field on 30 products counts as 30 changes.</p>
<p>Theme or code work, advertising management and photography are not included in any plan.</p></div></div></section>
""")
P["health-check"] = ("Free catalogue health check | NYNZ", "Send a Shopify product export and get a free report of the catalogue problems we find, grouped by type.",
f"""<section class="hero"><div class="wrap split">
<div><p class="eyebrow">Free health check</p><h1>Find out what is wrong with your catalogue.</h1>
<p class="lead">Tell us about your store. We will reply by email and ask for a product export. You get back a short report of the problems we find, grouped by type, with no obligation.</p>
<ul class="list"><li><strong>No store access</strong>A CSV export from Shopify admin is enough.</li><li><strong>What you receive</strong>Counts by problem type and examples from your own data.</li><li><strong>What it is not</strong>An audit of your theme, ads or marketplace account health.</li></ul></div>
<div class="card">
<h2 style="font-size:var(--t-lg)">Request a health check</h2>
<p>Email us and we will reply and ask for a product export.</p>
<a class="btn" href="mailto:sales@nynz.in?subject=Free%20catalogue%20health%20check&amp;body=Name%3A%0AStore%20website%3A%0AApproximate%20number%20of%20products%20and%20variants%3A%0AWhere%20you%20sell%20(Google%20Merchant%20Center%2C%20eBay%2C%20other)%3A%0AAnything%20we%20should%20know%3A%0A">Email sales@nynz.in</a>
<p>Please include your name, store website, roughly how many products and variants you have, and where you sell.</p>
<p class="hint">We use these details only to reply and prepare your health check. When we ask for an export, send product data only, never customer or order data. See our <a href="privacy.html">privacy policy (draft)</a>. Or write to <a href="mailto:sales@nynz.in">sales@nynz.in</a>.</p>
</div></div></section>
""", )
FAQ = [
("Do you need access to my Shopify store?", "Not to start. The health check and setup can work from a product export. For ongoing work we ask for a staff account limited to products and inventory, never owner access."),
("Will you change anything without asking?", "No. Nothing goes live on your store without your approval, given in the review queue, a shared sheet or by email as agreed, and nothing is applied automatically. Silence is not approval."),
("Can you guarantee my products will be approved by Google or a marketplace?", "No. Google and marketplaces make their own decisions and change their rules. We fix the data they report problems with and tell you what remains."),
("What if a change is wrong?", "Every published batch keeps the previous state, so it can be restored. Tell us and we will roll it back and look at why it happened."),
("How do you use AI?", "AI and software find problems, draft fixes and check them. A separate checking agent verifies every proposal, and the agent that drafts a fix never approves it. Where a change depends on facts such as price, stock, SKU, barcode or product identity, it needs authoritative evidence, such as your supplier file. Otherwise it is flagged for you. Nothing is published without your approval."),
("Does a person at NYNZ check every change?", "No. The checking is automated, and we do not claim otherwise. Your approval is the human decision in the process. That is why nothing is applied without it, why uncertain items are flagged, and why every published batch can be rolled back. Automated checks can be wrong, so look at each before and after."),
("Which platforms do you support?", "Shopify stores, with Google Merchant Center and eBay file feeds. These are the only integrations we have tested so far, and only on example data in a local test, not on a live store. Other marketplaces are not supported yet. Ask if you need something else and we will tell you honestly whether we can do it."),
("Is there a contract?", "Yes, a signed client agreement. Starter is monthly with a 2-month minimum. India Pro is monthly with no lock-in. All plans have a one-time setup fee."),
]
P["faq"] = ("FAQ | NYNZ", "Answers to common questions about NYNZ Catalogue & Feed Care: access, approvals, rollback, AI and contracts.",
"""<section class="hero"><div class="wrap"><p class="eyebrow">FAQ</p><h1>Questions we are asked.</h1></div></section>
<section><div class="wrap" style="max-width:820px">""" + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ) +
"""<p style="margin-top:2rem">Something else? <a href="mailto:sales@nynz.in">sales@nynz.in</a></p></div></section>""")
DRAFT = '<p class="draft"><strong>DRAFT FOR PROFESSIONAL REVIEW.</strong> Prepared for review by NYNZ\'s lawyer. It is not in force and should not be relied on. Items in [square brackets] are still to be decided.</p>'
P["privacy"] = ("Privacy policy (draft) | NYNZ", "Draft privacy policy for the NYNZ website, enquiries and the free health check.", f"""<section><div class="wrap prose" style="max-width:780px"><h1>Privacy policy</h1>{DRAFT}
<h2>Who we are</h2><p>This website is run by NYNZ, [legal entity name and type], based in Berhampur, Odisha, India. [Postal address: to be provided]. For any privacy question or complaint, email <a href="mailto:sales@nynz.in">sales@nynz.in</a>. Grievance contact: [name to be confirmed].</p>
<h2>What this website collects</h2>
<p><strong>Hosting logs.</strong> The site is hosted by [website host: Cloudflare, Inc. is the recommended host; confirm before launch]. Like any web host, it records technical request data when you visit, including your IP address, the pages and files requested, the date and time, your browser's user agent and the referring page. We use this only to run and secure the site. [Retention period of host logs: to be confirmed.]</p>
<p><strong>No cookies.</strong> The site sets no cookies and uses no advertising or cross-site tracking tools. It does not use analytics today. [Planned: Cloudflare Web Analytics, which Cloudflare says uses no cookies or localStorage and does not fingerprint visitors. This policy will be updated before it is switched on.] The site loads no third-party scripts.</p>
<p><strong>Fonts.</strong> The fonts (Source Serif 4, IBM Plex Sans and IBM Plex Mono, all under the SIL Open Font License) are served from this website itself. No font service such as Google Fonts receives your data.</p>
<h2>Health check requests</h2><p>The site has no form. To ask for a health check you email us at sales@nynz.in, so the details you send reach our business mailbox directly. We use them to reply and prepare your health check. If we then ask for a product export, please send product data only, never customer or order data.</p>
<h2>Data you send us by email</h2><p>We keep enquiry emails for 12 months after our last contact, and health-check exports for 30 days after we send your report, then delete them. If you ask us not to contact you again, we keep your email address on a do-not-contact list only. Records about paying clients are kept for as long as tax law requires [period to be confirmed].</p>
<h2>Business contacts we find ourselves</h2><p>We may contact people at businesses we think could use our service, by email or LinkedIn message, using work details they or their business have made public. Our sources are company websites, Companies House (the UK register of companies), Shopify App Store reviews that name a store, and LinkedIn profiles we view by hand. We do this on the basis of our legitimate interest in offering a business service. Every such message tells you where we found your details and how to opt out, and you can object at any time. We keep prospect records for at most 6 months after our last message if you do not reply, then delete them. If you opt out, we keep a minimal record (email or company domain, reason and date) so we do not contact you again. [Lawful basis under India's DPDP Act, and for US contacts, to be confirmed.]</p>
<h2>Why we use your data</h2><p>To answer enquiries and provide the health check (steps you asked for, or our legitimate interests), to perform client agreements (contract), and to meet tax and legal duties (legal obligation).</p>
<h2>Who we share it with</h2><ul><li>[Website host: Vercel Inc. or Cloudflare, Inc., to be confirmed] (visitor request logs).</li><li>Hostinger, our domain, DNS and business email provider.</li><li>[File storage and AI tools used to process client catalogue data: to be confirmed. Our service uses AI to read and draft changes to catalogue data, so these providers will process client data under the client agreement.]</li><li>Our professional advisers, and authorities when the law requires it.</li></ul><p>We do not sell personal data or share it for advertising. Some of these providers may process data outside India; see the UK and EU section below.</p>
<h2>If you are in the UK or EU</h2><p>NYNZ is based in India. If you are in the UK or the EU, the personal data you give us, or that we collect about you, is transferred to and processed in India, and some of our providers (for example our website host) may process it in other countries, including the US. We protect these transfers with [transfer safeguard: e.g. UK IDTA / EU SCCs, to be confirmed], and limit the data to what we need. You can ask us for a copy of the safeguard at sales@nynz.in. [Whether NYNZ needs a UK or EU representative: to be confirmed.]</p>
<h2>Client catalogue data</h2><p>Product data and store access for paying clients are handled under our signed client agreement and data processing addendum, not this policy.</p>
<h2>Your rights</h2><p><strong>UK:</strong> access, correction, erasure, restriction, objection (including an absolute right to object to direct marketing) and portability. You can complain to the Information Commissioner's Office. <strong>India:</strong> access to information, correction and erasure, grievance redressal and nomination; after using our grievance process you can approach the Data Protection Board of India. <strong>US:</strong> where a state privacy law applies, the rights to know, delete and correct. Email sales@nynz.in to use any right; we aim to reply within [30] days.</p>
<h2>Security</h2><p>We limit access to the people who need it, use accounts with two-step sign-in where offered, and delete data on the schedule above.</p>
<h2>Children</h2><p>Our service is for businesses and is not aimed at children.</p>
<h2>Changes</h2><p>We will post any change here with a new date.</p>
<p>Last updated: [DRAFT, date to be set on approval]</p></div></section>""")
P["terms"] = ("Website terms (draft) | NYNZ", "Draft terms of use for the NYNZ website and free health check.", f"""<section><div class="wrap prose" style="max-width:780px"><h1>Website terms</h1>{DRAFT}
<h2>Who we are</h2><p>NYNZ, [legal entity name and type], Berhampur, Odisha, India. [Postal address: to be provided]. Contact: <a href="mailto:sales@nynz.in">sales@nynz.in</a>.</p>
<h2>What these terms cover</h2><p>These terms cover your use of this website and the free health check. Paid services are provided only under a signed Client Service Agreement, which takes priority over anything on this website.</p>
<h2>Business users only</h2><p>This website and our services are for businesses, not consumers.</p>
<h2>Information only</h2><p>The website is for information. Prices shown are list prices, exclude taxes and may change. The free health check is offered at our discretion. It is not an audit and gives no guarantee.</p>
<h2>How changes are approved</h2><p>Under a client agreement, nothing goes live on a client's store or feeds unless the client has approved that change through the approval method in its agreement: by marking it approved in the review queue, by a reply in a shared sheet, or by email from a named address. The client may approve changes one by one or approve a whole change set it has seen. Approval covers only the changes shown; it never covers future changes. Nothing is applied automatically, and silence is not approval.</p>
<h2>No guarantee of platform outcomes</h2><p>Shopify, Google, eBay and other platforms make their own decisions. We do not guarantee that any listing, feed or account will be approved, ranked or kept active, or that any sales will result. Nothing on this site is legal advice or a promise of legal compliance.</p>
<h2>Intellectual property</h2><p>The site content and the NYNZ name and logo belong to NYNZ. Shopify, Google Merchant Center and eBay are trademarks of their owners, and NYNZ is not affiliated with them.</p>
<h2>Acceptable use</h2><p>Do not misuse the site, try to break its security, or send us data you have no right to share.</p>
<h2>Liability</h2><p>[FOR LAWYER REVIEW: cap amount and period.] To the extent the law allows, our total liability arising out of or in connection with this website or the free health check, whether in contract, tort (including negligence) or otherwise, is limited to the total fees you have paid to NYNZ in the 12 months before the event giving rise to the claim. We are not liable for loss of profit, revenue, sales, business or goodwill, or for indirect or consequential loss. Nothing limits liability for fraud, wilful misconduct, or any liability that cannot be limited by law. For paid services, the liability terms of the signed client agreement apply instead.</p>
<h2>Links</h2><p>We are not responsible for other websites we link to.</p>
<h2>Governing law and disputes</h2><p>These terms are governed by the laws of India. Subject to any arbitration option below, the courts at [Berhampur, Odisha] [or: the courts having jurisdiction in Odisha, India] have exclusive jurisdiction. [Arbitration option: to be decided by the lawyer, as in the client agreement.] Either party may seek urgent interim relief from a competent court.</p>
<h2>Changes</h2><p>We may update these terms and will post the new date here.</p>
<p>Last updated: [DRAFT, date to be set on approval]</p></div></section>""")
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+0.05)/(lb+0.05)
PAL=[("Midnight navy","#0A1A2F","Text on light, header, hero, footer"),("Navy 2","#13263F","Raised surfaces on navy"),("Slate","#4A5668","Secondary text on light"),("Mist","#C4CAD3","Secondary text on navy"),
("Signal orange","#FF5A1F","Orbit, buttons (navy text), accents on navy. Not for small text on light"),("Ember","#B8400F","Orange text and links on light"),("Orange tint","#FFEDE5","Note backgrounds"),
("Paper","#F7F6F3","Page background"),("White","#FFFFFF","Cards, logo on navy"),("Line","#DDE1E6","Rules, borders")]
sw="".join(f'<tr><td><span style="display:inline-block;width:2.5rem;height:2.5rem;border:1px solid var(--line);border-radius:4px;background:{h}" aria-hidden="true"></span></td><td>{n}</td><td class="mono">{h}</td><td>{u}</td><td>{cr(h,"#F7F6F3"):.1f}:1</td><td>{cr(h,"#0A1A2F"):.1f}:1</td></tr>' for n,h,u in PAL)
SCALE=[("3XL / H1","3.25rem","52px","var(--serif)",600),("2XL / H2","2.5625rem","41px","var(--serif)",600),("XL","2.0625rem","33px","var(--serif)",600),("LG","1.625rem","26px","var(--serif)",600),("MD / H3, lead","1.3125rem","21px","var(--sans)",600),("Base / body","1.0625rem","17px","var(--sans)",400),("SM","0.9375rem","15px","var(--sans)",400),("XS / labels","0.8125rem","13px","var(--sans)",500)]
ts="".join(f'<tr><td>{n}</td><td class="mono">{r} ({p})</td><td><span style="font-family:{f};font-weight:{w};font-size:{r};line-height:1.2">Catalogue care</span></td></tr>' for n,r,p,f,w in SCALE)
P["brand"]=("Brand sheet | NYNZ","NYNZ logo, colours and typography.",f"""<section class="hero"><div class="wrap"><p class="eyebrow">Brand sheet</p><h1>NYNZ brand basics.</h1><p class="lead">One page for anyone making something with the NYNZ name on it.</p></div></section>
<section><div class="wrap"><h2>Logo</h2><p>A bold NYNZ wordmark with one orange orbit rising around the top right of the Z. It should always read as moving up and forward. Letters and orbit are hand-drawn SVG paths, so the logo has no font dependency. Use light versions on Paper or white and dark versions on Navy.</p>
<div class="grid g2">
<div class="card"><img src="img/nynz-logo-horizontal-light.svg" alt="NYNZ logo, horizontal, light version" width="300" height="111"><p class="hint" style="margin-top:1rem">Horizontal, light. Primary logo.</p></div>
<div class="card" style="background:var(--navy)"><img src="img/nynz-logo-horizontal-dark.svg" alt="NYNZ logo, horizontal, dark version" width="300" height="111"><p class="hint" style="margin-top:1rem;color:var(--mist)">Horizontal, dark. Used in the site header and footer.</p></div>
<div class="card"><img src="img/nynz-logo-stacked-light.svg" alt="NYNZ logo, stacked, light version" width="140" height="149"><p class="hint" style="margin-top:1rem">Stacked, light. For square spaces.</p></div>
<div class="card" style="background:var(--navy)"><img src="img/nynz-logo-stacked-dark.svg" alt="NYNZ logo, stacked, dark version" width="140" height="149"><p class="hint" style="margin-top:1rem;color:var(--mist)">Stacked, dark.</p></div>
<div class="card"><img src="img/nynz-icon-light.svg" alt="NYNZ icon, light version" width="96" height="96"><p class="hint" style="margin-top:1rem">Icon, light: the N with the orbit.</p></div>
<div class="card" style="background:var(--navy)"><img src="img/nynz-app-tile.svg" alt="NYNZ app icon" width="96" height="96"><p class="hint" style="margin-top:1rem;color:var(--mist)">App icon and favicon: white N and orbit on a navy tile.</p></div>
</div><p style="margin-top:1rem">The name is NYNZ, always in capitals, never extended or combined with another word. Keep clear space equal to the height of the N's top half on every side. Do not flip or rotate the orbit so that it points down, recolour it, add effects or outlines, or stretch the logo. Files: <a href="img/nynz-logo-horizontal-light.svg">horizontal</a>, <a href="img/nynz-logo-stacked-light.svg">stacked</a>, <a href="img/nynz-icon-light.svg">icon</a>, <a href="og.png">social image</a>.</p></div></section>
<section><div class="wrap"><h2>Colour</h2><p>Navy, signal orange and white. Orange on navy measures 5.6:1, which passes AA, but keep it to accents, buttons and large text. on light backgrounds use Ember for any orange text, because Signal orange on white is 3.1:1 (large text only). Buttons are orange with navy text (5.6:1). Ratios are WCAG 2 values.</p>
<div class="table-scroll" tabindex="0" role="region" aria-label="Colour palette"><table><thead><tr><th scope="col">Swatch</th><th scope="col">Name</th><th scope="col">Hex</th><th scope="col">Use</th><th scope="col">On Paper</th><th scope="col">On Navy</th></tr></thead><tbody>{sw}</tbody></table></div></div></section>
<section><div class="wrap"><h2>Type</h2><p><strong>Source Serif 4</strong> (600) for headings. <strong>IBM Plex Sans</strong> (400, 500, 600) for text and interface. <strong>IBM Plex Mono</strong> for figures in tables and code. All are SIL Open Font License fonts, self-hosted. Scale ratio 1.25 from a 17px base.</p>
<div class="table-scroll" tabindex="0" role="region" aria-label="Type scale"><table><thead><tr><th scope="col">Step</th><th scope="col">Size</th><th scope="col">Sample</th></tr></thead><tbody>{ts}</tbody></table></div></div></section>
<section><div class="wrap"><h2>Voice</h2><ul class="list"><li><strong>Plain and specific</strong>Say what we do, in the customer's words. Short sentences.</li><li><strong>No promises we cannot keep</strong>No guaranteed results, no compliance claims, no invented figures. Internal test numbers are always labelled as such.</li><li><strong>No filler</strong>No em dashes, no hype words, no emoji.</li></ul></div></section>
""")
def run():
    for slug, (t, d, b) in P.items():
        cur = f"{slug}.html" if slug != "index" else None
        open(f"public/{slug}.html", "w").write(page(slug, t, d, b, cur))
    urls = [slug for slug in P if slug not in NOINDEX]
    loc = lambda slug: SITE + "/" + ("" if slug == "index" else slug)
    open("public/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{loc(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
    open("public/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(P), "pages;", len(urls), "in sitemap")
if __name__ == "__main__": run()
