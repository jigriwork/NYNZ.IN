// Local mock of the production form backend. Serves public/ and /api/* using the SAME code as functions/api/*.
// Turnstile is faked (token "mock-ok" passes) and mail goes to mock-outbox/ instead of the internet. Nothing leaves this machine.
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..'), pub = path.join(root, 'public'), outbox = path.join(root, 'mock-outbox');
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.ico': 'image/x-icon', '.webmanifest': 'application/manifest+json', '.xml': 'application/xml', '.txt': 'text/plain' };
const vj = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
// Same matching idea as Vercel's header rules (path-to-regexp subset used in vercel.json): later rules add to earlier ones.
const vercelRules = (vj.headers || []).map((x) => ({ re: new RegExp('^' + x.source.replace('(.*)', '.*').replace(/\/$/, '') + '$'), headers: x.headers }));
async function start(port = 0, opts = {}) {
  const core = await import(path.join(root, 'lib/form-core.js'));
  const mem = new Map(), kv = { get: async (k) => mem.get(k) ?? null, put: async (k, v) => { mem.set(k, v); } };
  const env = { FORM_SECRET: 'mock-secret-' + Math.random(), TURNSTILE_SECRET: 'mock', RL: kv, ALLOWED_ORIGINS: opts.origin || '', MAIL_TO: 'sales@nynz.in' };
  const deps = { now: opts.now || Date.now,
    fetch: async (url, init) => ({ ok: true, json: async () => ({ success: new URLSearchParams(init.body).get('response') === 'mock-ok' }) }),
    sendMail: async (_e, m) => { fs.mkdirSync(outbox, { recursive: true }); fs.writeFileSync(path.join(outbox, Date.now() + '-' + Math.random().toString(36).slice(2, 6) + '.json'), JSON.stringify(m, null, 1)); } };
  const srv = http.createServer(async (q, r) => {
    const url = new URL(q.url, 'http://x');
    if (url.pathname.startsWith('/api/')) {
      const chunks = []; for await (const c of q) chunks.push(c); const body = Buffer.concat(chunks);
      const origin = q.headers.origin || (opts.noOrigin ? undefined : undefined); env.ALLOWED_ORIGINS = opts.origin || `http://127.0.0.1:${srv.address().port}`;
      const req = new Request('http://x' + q.url, { method: q.method, headers: { ...q.headers, 'cf-connecting-ip': q.headers['x-test-ip'] || '203.0.113.9' }, body: ['GET', 'HEAD'].includes(q.method) ? undefined : body });
      let res; if (url.pathname === '/api/form-token' && q.method === 'GET') res = await core.handleToken(req, env, deps);
      else if (url.pathname === '/api/contact' && q.method === 'POST') res = await core.handleContact(req, env, deps);
      else res = new Response('{"ok":false}', { status: 404 });
      r.writeHead(res.status, Object.fromEntries(res.headers)); return r.end(Buffer.from(await res.arrayBuffer()));
    }
    let f = path.join(pub, decodeURIComponent(url.pathname)); if (f.endsWith('/')) f += 'index.html';
    if (!path.extname(f) && fs.existsSync(f + '.html')) f += '.html';
    fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end('not found'); }
      const h = { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' };
      if (opts.vercelHeaders) for (const rule of vercelRules) if (rule.re.test(url.pathname)) for (const x of rule.headers) h[x.key] = x.value;
      r.writeHead(200, h); r.end(d); });
  });
  await new Promise((ok) => srv.listen(port, '127.0.0.1', ok)); return { srv, port: srv.address().port, env, outbox };
}
module.exports = { start };
if (require.main === module) start(Number(process.env.PORT || 8788)).then((s) => console.log(`mock site + form backend: http://127.0.0.1:${s.port}/  (mail goes to ${s.outbox})`));
