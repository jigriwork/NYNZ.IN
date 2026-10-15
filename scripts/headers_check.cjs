// Loads every page with the exact headers from vercel.json applied and fails on any CSP violation, console error or failed asset request.
// Also checks the header set is present and the redirect rule targets the apex.
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path'); const { start } = require('./mock_server.cjs');
const pages = ['index', 'how-it-works', 'pricing', 'health-check', 'faq', 'about', 'contact', 'privacy', 'terms'];
(async () => {
  const m = await start(0, { vercelHeaders: true }); const b = await chromium.launch(); let bad = 0;
  const vj = JSON.parse(fs.readFileSync(path.join(__dirname, '../vercel.json'), 'utf8'));
  const must = ['Strict-Transport-Security', 'X-Content-Type-Options', 'Referrer-Policy', 'Permissions-Policy', 'Content-Security-Policy'];
  const have = vj.headers[0].headers.map((h) => h.key); for (const k of must) if (!have.includes(k)) { console.log('missing header', k); bad++; }
  const red = vj.redirects[0]; if (!(red.permanent && red.destination === 'https://nynz.in/$1' && red.has[0].value === 'www.nynz.in')) { console.log('www redirect rule wrong'); bad++; }
  for (const w of [{ w: 1440, h: 900 }, { w: 390, h: 844 }]) {
    const ctx = await b.newContext({ viewport: { width: w.w, height: w.h } }); const p = await ctx.newPage(); const issues = [];
    await p.addInitScript(() => document.addEventListener('securitypolicyviolation', (e) => (window.__csp = (window.__csp || []).concat(e.violatedDirective + ' ' + e.blockedURI))));
    p.on('console', (x) => x.type() === 'error' && issues.push('console: ' + x.text())); p.on('requestfailed', (r) => issues.push('failed: ' + r.url()));
    p.on('response', (r) => r.status() >= 400 && !r.url().includes('/api/') && issues.push(r.status() + ' ' + r.url()));
    for (const pg of pages) { await p.goto(`http://127.0.0.1:${m.port}/${pg}.html`, { waitUntil: 'networkidle' }); const v = await p.evaluate(() => window.__csp || []); v.forEach((x) => issues.push(pg + ' CSP: ' + x)); }
    const r = await p.request.get(`http://127.0.0.1:${m.port}/index.html`); const h = r.headers();
    for (const k of must) if (!h[k.toLowerCase()]) { issues.push('response lacks ' + k); }
    if (issues.length) { bad += issues.length; console.log(w.w, issues.join('\n')); } await ctx.close();
  }
  console.log(bad ? 'headers check: FAIL' : 'headers check: PASS (9 pages x 2 viewports, no CSP violations, all headers present)'); await b.close(); m.srv.close(); process.exit(bad ? 1 : 0);
})();
