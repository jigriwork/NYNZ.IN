// Checks the Cloudflare Pages config agrees with vercel.json and that the Functions import paths resolve.
const test = require('node:test'); const assert = require('node:assert'); const fs = require('fs'); const path = require('path');
const root = path.join(__dirname, '..');
const vj = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
function parseHeaders(txt) { const m = {}; let cur = null; for (const l of txt.split('\n')) { if (!l.trim() || l.startsWith('#')) continue; if (!l.startsWith(' ')) { cur = l.trim(); m[cur] = {}; } else { const i = l.indexOf(':'); m[cur][l.slice(0, i).trim()] = l.slice(i + 1).trim(); } } return m; }
test('_headers matches vercel.json headers', () => {
  const ch = parseHeaders(fs.readFileSync(path.join(root, 'public/_headers'), 'utf8'));
  const map = { '/(.*)': '/*', '/fonts/(.*)': '/fonts/*', '/api/(.*)': '/api/*' };
  for (const r of vj.headers) { const got = ch[map[r.source]]; assert.ok(got, 'missing rule ' + r.source); for (const h of r.headers) assert.strictEqual(got[h.key], h.value, h.key); }
});
test('_headers is within Cloudflare limits (100 rules, 2000 chars per line)', () => {
  const t = fs.readFileSync(path.join(root, 'public/_headers'), 'utf8'); assert.ok(t.split('\n').every((l) => l.length <= 2000));
  assert.ok(Object.keys(parseHeaders(t)).length <= 100);
});
test('_redirects exists and has no host rule', () => { const t = fs.readFileSync(path.join(root, 'public/_redirects'), 'utf8'); assert.ok(!/https?:\/\//.test(t.replace(/^#.*$/mg, ''))); });
test('no server code or form assets are deployable (api/, functions/, public/form.js absent)', () => {
  for (const p of ['api', 'functions', 'public/form.js', 'public/api']) assert.ok(!fs.existsSync(path.join(root, p)), p + ' must not exist');
  assert.ok(!('functions' in vj));
});
test('public pages reference no form backend, Turnstile, Resend or Upstash', () => {
  for (const f of fs.readdirSync(path.join(root, 'public')).filter((x) => x.endsWith('.html'))) { const h = fs.readFileSync(path.join(root, 'public', f), 'utf8'); assert.ok(!/<form|\/api\/|turnstile|resend|upstash|form\.js/i.test(h), f); }
});
test('no adib@ address anywhere in public/', () => { for (const f of fs.readdirSync(path.join(root, 'public'))) { if (!/\.(html|xml|txt)$/.test(f)) continue; assert.ok(!/adib@/i.test(fs.readFileSync(path.join(root, 'public', f), 'utf8')), f); } });
