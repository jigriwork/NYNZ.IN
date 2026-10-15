// Site content, SEO and brand guards for the redesign.
const test = require('node:test'); const assert = require('node:assert'); const fs = require('fs'); const path = require('path'); const cp = require('child_process');
const root = path.join(__dirname, '..'), pub = path.join(root, 'public');
const pages = fs.readdirSync(pub).filter((f) => f.endsWith('.html')).map((f) => f.slice(0, -5));
const read = (p) => fs.readFileSync(path.join(pub, p), 'utf8'); const text = (h) => h.replace(/<[^>]+>/g, ' ');
const NOINDEX = ['privacy', 'terms'];
test('expected pages exist, brand page is gone', () => {
  for (const p of ['index', 'how-it-works', 'pricing', 'health-check', 'faq', 'about', 'contact', 'privacy', 'terms']) assert.ok(pages.includes(p), p);
  assert.ok(!pages.includes('brand'));
  for (const p of pages) assert.ok(!/brand\.html/.test(read(p + '.html')), p + ' links to brand');
});
test('canonical is the apex on every page and og:url matches', () => {
  for (const p of pages) { const h = read(p + '.html'); const want = 'https://nynz.in/' + (p === 'index' ? '' : p);
    assert.ok(h.includes(`<link rel="canonical" href="${want}">`), p + ' canonical'); assert.ok(h.includes(`<meta property="og:url" content="${want}">`), p + ' og:url');
    assert.ok(h.includes('og:image" content="https://nynz.in/og.png"'), p + ' og:image'); assert.ok(!/www\.nynz\.in/.test(h), p + ' mentions www'); }
});
test('sitemap lists every indexable page, no noindex page, apex only; robots points at it', () => {
  const sm = read('sitemap.xml'); const locs = [...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
  const want = pages.filter((p) => !NOINDEX.includes(p)).map((p) => 'https://nynz.in/' + (p === 'index' ? '' : p));
  assert.deepStrictEqual(locs.sort(), want.sort());
  for (const p of NOINDEX) assert.ok(read(p + '.html').includes('noindex'), p);
  assert.ok(read('robots.txt').includes('Sitemap: https://nynz.in/sitemap.xml'));
  const vj = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8')); assert.strictEqual(vj.redirects[0].destination, 'https://nynz.in/$1');
});
test('forbidden claims and content are absent', () => {
  for (const p of pages) { const t = text(read(p + '.html')).replace(/\s+/g, ' ');
    assert.ok(!/amazon\.in|flipkart/i.test(t), p + ' marketplace'); assert.ok(!/human review|reviewed by (a )?(human|person|expert)|manually reviewed|our (expert|team) (reviews|checks)/i.test(t), p + ' human-review claim');
    assert.ok(!/testimonial.*(said|"\w)|case study:|trusted by|as seen on/i.test(t), p + ' social proof'); assert.ok(!/adib@/i.test(read(p + '.html')), p + ' adib@'); }
  for (const p of pages) { const t = text(read(p + '.html')); for (const m of t.matchAll(/MITTY[^.]*\./g)) assert.ok(/affiliated internal testing example|brand affiliated with NYNZ/.test(t), p + ' MITTY wording'); }
});
test('contact is mailto sales@nynz.in only: no form, no postal address, no phone', () => {
  const c = read('contact.html'); assert.ok(!/<form|<input|<textarea/i.test(c)); assert.ok(/mailto:sales@nynz\.in/.test(c));
  for (const p of pages) { for (const m of read(p + '.html').matchAll(/mailto:([^"?]+)/g)) assert.strictEqual(m[1], 'sales@nynz.in', p); assert.ok(!/\btel:|\+\d{1,3}[ -]?\d{3}/.test(read(p + '.html')), p + ' phone'); }
});
test('pricing: only ₹1,999 (India detailed audit), no dollar amounts, no old plans', () => {
  for (const p of pages) { const t = text(read(p + '.html')).replace(/\s+/g, ' ');
    assert.ok(!/\$\s?\d|\bUSD\b|dollar/i.test(t), p + ' has a dollar amount');
    for (const bad of ['India Lite', 'Growth', 'India Pro', 'Starter', '399', '7,999', 'per SKU']) assert.ok(!t.includes(bad), p + ' mentions ' + bad);
    const rupees = t.match(/₹\s?[\d,]+/g) || []; for (const r of rupees) assert.strictEqual(r.replace(/\s/g, ''), '₹1,999', p + ' unexpected amount ' + r);
    for (const m of t.matchAll(/₹1,999/g)) { const ctx = t.slice(Math.max(0, m.index - 160), m.index + 160); assert.ok(/India|GST/.test(ctx), p + ' ₹1,999 outside an India context'); assert.ok(/GST/.test(t.slice(m.index, m.index + 40)), p + ' ₹1,999 without GST'); } }
  const t = text(read('pricing.html')); assert.ok(t.includes('₹1,999 + GST') && /Free health audit/.test(t) && /Detailed audit/.test(t) && /Monitoring/.test(t) && /Early access/.test(t) && /pricing confirmed after your free audit/i.test(t));
  const svc = text(read('pricing.html')); assert.ok(/International: early access, pricing confirmed after your free audit/.test(svc));
});
test('free audit CTA (mailto sales@nynz.in with prefilled subject and body) is the primary button on key pages', () => {
  for (const p of ['index', 'pricing', 'health-check', 'how-it-works', 'faq', 'about', 'contact']) { const h = read(p + '.html');
    const m = h.match(/<a class="btn " href="(mailto:sales@nynz\.in\?subject=Free%20catalogue%20health%20audit&amp;body=[^"]+)">Get your free health audit/); assert.ok(m, p + ' primary CTA');
    assert.ok(/store%20website%20or%20link/i.test(m[1]) && /Country/.test(m[1]) && /do%20not%20send%20passwords/.test(m[1]), p + ' prefilled body'); }
  const hero = read('index.html').split('<section class="section"')[0]; assert.ok(/class="btn " href="mailto:sales@nynz\.in/.test(hero));
});
test('audit is described honestly: read-only, no store access requested, no guarantees', () => {
  const t = text(read('health-check.html')).replace(/\s+/g, ' ');
  assert.ok(/read-only/i.test(t) && /Passwords are never needed/.test(t) && /No store access is requested/.test(t) && /cannot promise/.test(t));
  for (const p of pages) assert.ok(!/guarantee(d)? (results|sales|approval)|will increase|boost your sales/i.test(text(read(p + '.html'))), p);
  const f = text(read('faq.html')); for (const q of ['really free', 'What do I get', 'What do you need from me', 'change my store', 'Is GST added', 'What happens after', 'When is monitoring available']) assert.ok(f.includes(q), q);
});
test('mockups are labelled as example data', () => {
  for (const p of pages) { const h = read(p + '.html'); const n = (h.match(/<figure class="mock"/g) || []).length; if (!n) continue;
    assert.ok((h.match(/Example data/g) || []).length >= n, p + ' example labels'); assert.ok((h.match(/made-up example data/g) || []).length >= n, p + ' captions'); }
});
test('no third-party hosts, scripts only from self, logo header width >= 120', () => {
  for (const p of pages) { const h = read(p + '.html'); for (const m of h.matchAll(/\s(?:src|href)="(https?:)?\/\/([^"/]+)/g)) if (m[2] !== 'nynz.in') assert.fail(p + ' external ref ' + m[2]);
    for (const m of h.matchAll(/<script[^>]*src="([^"]+)"/g)) assert.ok(!/^(https?:)?\/\//.test(m[1]), p + ' script ' + m[1]);
    const w = h.match(/<a class="brand"[^>]*><img[^>]*width="(\d+)"/); assert.ok(w && +w[1] >= 120, p + ' logo width'); }
});
test('logo SVGs exist with brand colours; stale serif font and old logo files are gone', () => {
  const l = read('img/nynz-logo-dark.svg'); assert.ok(l.includes('#FF5A1F') && l.includes('#FFFFFF')); assert.ok(read('img/nynz-logo-light.svg').includes('#0A1A2F'));
  assert.ok(!fs.readdirSync(path.join(pub, 'fonts')).some((f) => /serif/i.test(f))); assert.ok(!/serif/i.test(read('styles.css').replace(/sans-serif/g, '')));
});
test('build is reproducible', () => {
  const before = fs.readdirSync(pub).filter((f) => /\.(html|xml|txt)$/.test(f)).map((f) => [f, read(f)]);
  cp.execSync('python3 build.py', { cwd: root }); for (const [f, c] of before) assert.strictEqual(read(f), c, f);
});
