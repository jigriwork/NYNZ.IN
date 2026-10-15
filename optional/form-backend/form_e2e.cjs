// Browser test of the real form page against the local mock backend. Run: node scripts/form_e2e.js
const { chromium } = require('playwright'); const fs = require('fs');
const { start } = require('./mock_server.cjs');
(async () => {
  const m = await start(0); fs.rmSync(m.outbox, { recursive: true, force: true });
  const b = await chromium.launch(); const ctx = await b.newContext(); const p = await ctx.newPage();
  await p.goto(`http://127.0.0.1:${m.port}/health-check.html`); await p.waitForFunction(() => document.querySelector('[name=form_token]').value);
  await p.fill('#name', 'E2E Tester'); await p.fill('#email', 'e2e@example.com'); await p.fill('#store', 'example-store.com'); await p.check('input[value=eBay]');
  await p.evaluate(() => { const i = document.createElement('input'); i.type = 'hidden'; i.name = 'cf-turnstile-response'; i.value = 'mock-ok'; document.getElementById('hc-form').appendChild(i); });
  await p.click('button[type=submit]'); await p.waitForSelector('#hc-status.bad'); const early = await p.textContent('#hc-status');
  await p.waitForTimeout(4500); await p.click('button[type=submit]'); await p.waitForSelector('#hc-status.ok'); const ok = await p.textContent('#hc-status');
  const cookies = await ctx.cookies(); const sent = fs.readdirSync(m.outbox).length;
  console.log(JSON.stringify({ early_submit_message: early, final_message: ok, mails_in_outbox: sent, cookies_set: cookies.length }));
  await b.close(); m.srv.close(); if (sent !== 1 || cookies.length) process.exit(1);
})();
