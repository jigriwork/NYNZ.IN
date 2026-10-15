# nynz-site

Static marketing site for NYNZ (nynz.in). Pure static files: no server code, no form backend, no secrets, no environment variables. Contact is by email (sales@nynz.in); the health-check page is a mailto link.

## Layout
```
build.py            generates public/ (pages, sitemap.xml, robots.txt) from templates and copy
public/             build output, COMMITTED and deployed (CI fails if it is stale)
public/_headers     Cloudflare Pages headers (kept equal to vercel.json by tests/host_config.test.cjs)
vercel.json         Vercel: www -> apex redirect, security headers, cache rules
scripts/            copy check, link check, axe accessibility QA, header/CSP check, local mock server
tests/              host-config guards and tests of the (unused) form core
lib/                form core used only by optional/ (not deployed, not referenced by any page)
optional/form-backend/  DISABLED, unreferenced contact-form backend (Vercel api, Cloudflare functions, widget). Needs Resend/Turnstile/KV; not needed. Do not move back to the repo root without approval.
docs/               hosting, rollback, analytics, access plan, approved process wording
.github/            CI workflow, PR template
```

## Hosting (works on both; no environment variables needed)
- **Vercel** (current plan, auto-deploy from `main`): Framework Other, Build `python3 build.py` (falls back to the committed `public/` if Python is missing), Output `public`. NOTE: Vercel Hobby is for non-commercial use only; NYNZ advertises a paid service, so a commercial-OK plan is needed. See `tech/readiness/free-hosting-steps.md`.
- **Cloudflare Pages Free** (commercial use allowed): Framework None, Build command `python3 build.py` (or empty, `public/` is committed), Output `public`. `_headers` is applied; www -> apex is a dashboard Redirect Rule.

## Branch and deploy flow
1. Work on a branch, open a PR to `main`. CI (`.github/workflows/ci.yml`) must pass. Cloudflare Pages posts a Preview URL on the PR.
2. Fill the PR checklist. Merge only when green and the preview is checked.
3. Merge to `main` deploys to production. Nothing unfinished goes on `main`.
4. Bad release: Cloudflare dashboard > Workers & Pages > project > Deployments > previous good deployment > Rollback to this deployment (verify the button name on first use), then fix forward with a revert PR. See docs/hosting.md.

GitHub settings Adib must apply: protect `main` (require PR, require the `check` status, no force push, block direct pushes), and in Cloudflare Pages set `main` as the only Production branch.

## Local
```
npm install
npx playwright install chromium
npm run dev        # http://127.0.0.1:PORT with mock form backend (Turnstile token "mock-ok", mail goes to an in-memory outbox)
npm run check      # build:check, copy check, link check, tests, axe, headers/CSP, form e2e
```
Requires Node 20+ (22 recommended) and Python 3.12.

## Editing content
Copy and page templates live in `build.py`. Edit, run `npm run build`, commit `public/` with it. Rules: no em dashes, no banned phrases, no claim that a person at NYNZ reviews changes, only tested integrations named, every figure labelled as a test result or assumption. See docs/process-wording.md.

## Design system and logo (redesign branch)
- One sans (IBM Plex Sans) plus mono, type scale 1.25 from 16px, 4px spacing scale, 12-column grid, 1200px max. Tokens are at the top of `public/styles.css`.
- Navy #0A1A2F, orange #FF5A1F (primary action and accents), link and eyebrow text on light uses Ember #B8400F for AA contrast.
- Product screens on the site are HTML/CSS/SVG illustrations, each labelled "Example data".
- Logo: `public/img/nynz-logo-*.svg` and `public/favicon.svg` are retraced from `brand/logo-concept-orbit-FINAL.jpg` (the only copy of the approved ORBIT artwork). Regenerate with `scripts/logo/trace.py` (needs a venv with potracer, opencv-python-headless, numpy, pillow) then `python3 scripts/logo/build_logo.py` and `node scripts/assets.cjs`. If a vector master exists, replace the traced paths with it.
- Mobile menu is progressive enhancement (`public/nav.js`, same-origin). FAQ uses `<details>` and needs no JavaScript.
