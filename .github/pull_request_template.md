## What changed and why


## Checklist (all must be ticked before merge to `main`)
- [ ] `npm run check` passes locally (build, copy check, link check, tests, axe, form test)
- [ ] `public/` is regenerated and committed (CI fails on any diff after `npm run build`)
- [ ] No em dashes, banned phrases, emoji or hype wording (copy check covers this)
- [ ] No claim that a person at NYNZ reviews changes. Process wording matches `docs/process-wording.md`
- [ ] Only tested integrations are named (Shopify CSV, Google Merchant Center, eBay file). No Amazon, Flipkart or others
- [ ] Any figure on the site is labelled as a test result or an assumption
- [ ] No secrets, tokens or personal data in the diff (`.env` is not committed)
- [ ] Vercel preview URL opened and checked on desktop and a phone
- [ ] Nothing unfinished: no TODO text, placeholder copy marked DRAFT is only on privacy and terms
