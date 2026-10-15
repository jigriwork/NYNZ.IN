// Serves public/ locally, runs axe-core (WCAG 2.2 A/AA + best practice) and takes full-page screenshots.
const { chromium } = require('playwright');
const axeSrc = require('fs').readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..'), pub = path.join(root, 'public');
const types = { '.html': 'text/html', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.ico': 'image/x-icon', '.webmanifest': 'application/manifest+json' };
const pages = ['index', 'how-it-works', 'pricing', 'health-check', 'faq', 'about', 'contact', 'privacy', 'terms'];
const { start } = require('./mock_server.cjs');
(async () => {
  const m = await start(0); const srv = m.srv;
  {

  const port = m.port, b = await chromium.launch(); const report = []; let total = 0;
  fs.mkdirSync(path.join(root, '.qa'), { recursive: true });
  for (const [vw, vh, label] of [[1440, 900, 'desktop'], [390, 844, 'mobile']]) {
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: 1 }); const p = await ctx.newPage();
    const errs = []; p.on('console', m => m.type() === 'error' && errs.push(m.text())); p.on('response', r => r.status() >= 400 && errs.push(r.status() + ' ' + r.url()));
    for (const pg of pages) {
      await p.goto(`http://127.0.0.1:${port}/${pg}.html`, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
      if (pg === 'faq') await p.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
      await p.addScriptTag({ content: axeSrc });
      const res = await p.evaluate(() => axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] } }));
      const overflow = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
      total += res.violations.length;
      report.push({ page: pg, viewport: label, violations: res.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, target: v.nodes[0]?.target })), passes: res.passes.length, horizontalOverflow: overflow });
      await p.screenshot({ path: path.join(root, `.qa/${pg}-${label}.png`), fullPage: true });
    }
    if (errs.length) report.push({ viewport: label, consoleOrNetworkErrors: errs });
    await ctx.close();
  }
  fs.writeFileSync(path.join(root, '.qa/axe-report.json'), JSON.stringify(report, null, 1));
  console.log(report.map(r => r.page ? `${r.page}/${r.viewport}: ${r.violations.length} violations${r.violations.length ? ' ' + JSON.stringify(r.violations) : ''}${r.horizontalOverflow ? ' OVERFLOW' : ''}` : JSON.stringify(r)).join('\n'));
  console.log('TOTAL violations:', total); await b.close(); srv.close(); if (total || report.some(r => r.consoleOrNetworkErrors || r.horizontalOverflow)) process.exit(1);
  }
})();
