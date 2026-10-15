// Checks every internal href/src in public/*.html: file exists (clean URLs allowed) and #fragments exist. External links are not fetched.
const fs = require('fs'), path = require('path'); const pub = path.resolve(__dirname, '../public'); let bad = 0, n = 0;
const pages = fs.readdirSync(pub).filter((f) => f.endsWith('.html'));
const ids = {}; for (const p of pages) ids[p] = new Set([...fs.readFileSync(path.join(pub, p), 'utf8').matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]));
for (const p of pages) {
  const html = fs.readFileSync(path.join(pub, p), 'utf8');
  for (const m of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const u = m[1]; if (/^(https?:|mailto:|tel:|data:)/.test(u)) continue; n++;
    let [file, frag] = u.split('#'); file = file.split('?')[0];
    if (file.startsWith('/api/')) continue;
    const target = file === '' ? p : file.replace(/^\//, '');
    let t = path.join(pub, target); if (!fs.existsSync(t) && fs.existsSync(t + '.html')) t += '.html';
    if (!fs.existsSync(t)) { console.log(`${p}: missing ${u}`); bad++; continue; }
    if (frag && t.endsWith('.html') && !ids[path.basename(t)]?.has(frag)) { console.log(`${p}: no #${frag} in ${path.basename(t)}`); bad++; }
  }
  for (const m of html.matchAll(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/g)) if (!m[1].startsWith('https://nynz.in')) { console.log(p, 'canonical off-domain', m[1]); bad++; }
}
console.log(`link check: ${bad ? 'FAIL (' + bad + ')' : 'PASS'} (${n} internal references in ${pages.length} pages)`); process.exit(bad ? 1 : 0);
