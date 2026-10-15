// node --test tests/   Exercises the real form handler through the local mock server.
const test = require('node:test'), assert = require('node:assert/strict'), fs = require('fs');
const { start } = require('../scripts/mock_server.cjs');
let clock = Date.now(); const now = () => clock;
const good = (token) => ({ name: 'Test Person', email: 'test@example.com', store: 'example-store.com', skus: '250 to 1,000', channels: ['eBay'], message: 'hello', website_url: '', form_token: token, 'cf-turnstile-response': 'mock-ok' });
async function setup() { const s = await start(0, { now }); const base = `http://127.0.0.1:${s.port}`;
  const post = (b, ip = '203.0.113.9', origin = base) => fetch(base + '/api/contact', { method: 'POST', headers: { 'content-type': 'application/json', origin, 'x-test-ip': ip }, body: JSON.stringify(b) });
  const token = async () => (await (await fetch(base + '/api/form-token')).json()).token; return { s, base, post, token }; }
test('happy path sends one mail to the outbox', async () => {
  const { s, post, token } = await setup(); fs.rmSync(s.outbox, { recursive: true, force: true });
  const t = await token(); clock += 5000; const r = await post(good(t)); assert.equal(r.status, 200); assert.equal((await r.json()).ok, true);
  const files = fs.readdirSync(s.outbox); assert.equal(files.length, 1); const m = JSON.parse(fs.readFileSync(s.outbox + '/' + files[0])); assert.equal(m.to, 'sales@nynz.in'); assert.equal(m.replyTo, 'test@example.com'); s.srv.close(); });
test('honeypot filled: fake success, nothing sent', async () => {
  const { s, post, token } = await setup(); fs.rmSync(s.outbox, { recursive: true, force: true }); const t = await token(); clock += 5000;
  const r = await post({ ...good(t), website_url: 'http://spam.example' }); assert.equal((await r.json()).ok, true); assert.equal(fs.existsSync(s.outbox), false); s.srv.close(); });
test('too fast is rejected', async () => { const { s, post, token } = await setup(); const t = await token(); clock += 500; const r = await post(good(t)); assert.equal(r.status, 429); assert.equal((await r.json()).error, 'too_fast'); s.srv.close(); });
test('forged and expired tokens are rejected', async () => { const { s, post, token } = await setup();
  assert.equal((await (await post(good('1700000000000.AAAAAAAAAAAAAAAAAAAAAAAA'))).json()).error, 'bad_token');
  const t = await token(); clock += 3 * 3600 * 1000; assert.equal((await (await post(good(t))).json()).error, 'expired'); s.srv.close(); });
test('missing or bad Turnstile response is rejected', async () => { const { s, post, token } = await setup(); const t = await token(); clock += 5000;
  const r = await post({ ...good(t), 'cf-turnstile-response': 'nope' }); assert.equal((await r.json()).error, 'challenge_failed'); s.srv.close(); });
test('wrong origin is rejected', async () => { const { s, post, token } = await setup(); const t = await token(); clock += 5000;
  const r = await post(good(t), '203.0.113.9', 'https://evil.example'); assert.equal(r.status, 403); s.srv.close(); });
test('validation errors', async () => { const { s, post, token } = await setup(); const t = await token(); clock += 5000;
  const r = await post({ ...good(t), email: 'not-an-email', store: 'x' }); assert.equal(r.status, 422); const j = await r.json(); assert.ok(j.fields.email && j.fields.store); s.srv.close(); });
test('rate limit: 6th request from one IP in an hour is blocked, another IP is fine', async () => { const { s, post, token } = await setup(); clock += 7200000; const t = await token(); clock += 5000;
  const codes = []; for (let i = 0; i < 6; i++) codes.push((await post(good(t), '198.51.100.7')).status);
  assert.deepEqual(codes, [200, 200, 200, 200, 200, 429]); assert.equal((await post(good(t), '198.51.100.8')).status, 200); s.srv.close(); });
test('header injection in name is flattened to one line', async () => { const { s, post, token } = await setup(); fs.rmSync(s.outbox, { recursive: true, force: true }); clock += 7200000; const t = await token(); clock += 5000;
  await post({ ...good(t), name: 'A\r\nBcc: x@evil.example' }, '192.0.2.50'); const m = JSON.parse(fs.readFileSync(s.outbox + '/' + fs.readdirSync(s.outbox)[0])); assert.ok(!/\r|\n/.test(m.subject)); assert.ok(m.text.split('\n')[0].startsWith('Name: A Bcc')); s.srv.close(); });
test('fails closed when not configured', async () => { const core = await import('../lib/form-core.js'); const r = await core.handleContact(new Request('http://x', { method: 'POST', headers: { origin: 'https://nynz.in' }, body: '{}' }), {}); assert.equal(r.status, 503); });
