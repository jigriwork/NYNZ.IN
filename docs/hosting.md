# Hosting, DNS, rollback, analytics, uptime (plans)
Prices checked 2026-10-15 from official pages. Re-check before paying. Financial figures below are quotes from those pages, not NYNZ forecasts.

## Host decision (revised 2026-10-15: NO paid plans)
- Chosen: **Cloudflare Pages, Free plan** (static site + Pages Functions for the form). Details, sources and click-by-click steps: `tech/readiness/free-hosting-steps.md`.
- Commercial use: Cloudflare's Self-Serve Subscription Agreement has no restriction on commercial use of the Free plan (community-confirmed, last on 2026-05-20, https://community.cloudflare.com/t/use-free-plan-for-commercial-project-follow-up/732438; the old Section 2.8 was removed, https://blog.cloudflare.com/updated-tos/). The CDN terms restrict serving video or disproportionate large files; this site has none. https://www.cloudflare.com/service-specific-terms-application-services/
- Limits (https://developers.cloudflare.com/pages/platform/limits/, 2026-10-15): 500 builds/month, 20,000 files, 25 MiB per file, 100 custom domains, `_headers` 100 rules, `_redirects` 2,100. Functions count as Workers: 100,000 requests/day on Free (https://developers.cloudflare.com/workers/platform/pricing/).
- Trade-off: an apex domain (nynz.in) on Pages needs the zone on Cloudflare nameservers (https://developers.cloudflare.com/pages/configuration/custom-domains/). That moves DNS away from Hostinger and every mail record (MX, SPF, DKIM, DMARC) must be copied first. Alternative without the move: serve the site on `www.nynz.in` via a CNAME at Hostinger.
- Not chosen: Vercel Hobby (non-commercial, https://vercel.com/docs/limits/fair-use-guidelines), Vercel Pro and any paid plan (Adib: no paid plans). Netlify Free is allowed for commercial projects but has a hard 300-credit cap that pauses ALL sites when used (https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans). GitHub Pages: no custom headers, no redirects, no functions, and its terms bar sites "primarily directed at facilitating commercial transactions" (https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits); unsuitable.
- Analytics: Cloudflare Web Analytics (free). Plausible dropped (paid).

## Risks
- Python in the Vercel build image is unproven for this repo until the first preview build runs. Fallback: `build.py` output is committed, so set Build Command to empty and Output Directory `public`.
- `style-src 'unsafe-inline'` remains because pages use inline style attributes. Removing them is future work.
- The contact form backend is disabled (optional/form-backend/); the site uses a mailto link, so no Resend, Turnstile or Upstash is needed.

## www to apex
Cloudflare dashboard Redirect Rule (host equals www.nynz.in -> https://nynz.in, 301, keep path). Test: `curl -I https://www.nynz.in/pricing` returns 301 to `https://nynz.in/pricing`. `_redirects` cannot match on host.

## Rollback and deploy
- Deploy: merge PR to `main`. Preview first on every PR.
- Rollback: Vercel > Deployments > pick last good production deployment > Instant Rollback. Then open a revert PR so `main` matches production.
- Post-deploy check: open /, /pricing, /health-check; submit the form with a test message; confirm the mail; check sitemap.xml and robots.txt.

## Analytics (cookie-free)
Recommended: Cloudflare Web Analytics (free, no cookies, no fingerprinting per Cloudflare docs, https://developers.cloudflare.com/web-analytics/ ) or (Plausible dropped: paid). Not enabled in this repo: enabling needs a CSP change (`script-src`, `connect-src`) and a privacy page update, both prepared as notes in the privacy draft. Decision for Adib.

## Uptime
UptimeRobot Free: 50 monitors, 5-minute checks, commercial use allowed (https://uptimerobot.com/pricing/ , verified earlier; re-check). Monitor https://nynz.in/ and https://nynz.in/api/form-token (expects 200). Alert to sales@nynz.in. Created by Adib or with his consent, not by this repo.

## Access plan for Rohan (no passwords in chat)
Adib creates an EMPTY private repo. To let Rohan push, either (a) Adib adds a write deploy key whose public key Rohan supplies (private key stays on the box), or (b) Adib creates a fine-grained PAT limited to that one repo, Contents read/write, 30-day expiry, and delivers it only through the secure secret-request flow. Adib connects Vercel himself with the GitHub app set to "Only select repositories". Rohan gets no Vercel or DNS login.
