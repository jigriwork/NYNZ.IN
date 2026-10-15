// Renders favicon PNGs, favicon.ico and the 1200x630 OG image with Playwright (local files only).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  const svg = fs.readFileSync(path.join(root, 'public/favicon.svg'), 'utf8');
  const out = {};
  for (const s of [16, 32, 48, 180, 192, 512]) {
    await p.setViewportSize({ width: s, height: s });
    await p.setContent(`<html><body style="margin:0">${svg.replace(/width="\d+" height="\d+"/, `width="${s}" height="${s}"`)}</body></html>`);
    out[s] = await p.screenshot({ omitBackground: true });
  }
  fs.writeFileSync(path.join(root, 'public/apple-touch-icon.png'), out[180]);
  fs.writeFileSync(path.join(root, 'public/icon-192.png'), out[192]);
  fs.writeFileSync(path.join(root, 'public/icon-512.png'), out[512]);
  // ICO with embedded PNGs (16, 32, 48)
  const imgs = [16, 32, 48].map(s => [s, out[s]]);
  const head = Buffer.alloc(6); head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(imgs.length, 4);
  let off = 6 + 16 * imgs.length; const dirs = [];
  for (const [s, buf] of imgs) { const d = Buffer.alloc(16); d.writeUInt8(s, 0); d.writeUInt8(s, 1); d.writeUInt16LE(1, 4); d.writeUInt16LE(32, 6); d.writeUInt32LE(buf.length, 8); d.writeUInt32LE(off, 12); off += buf.length; dirs.push(d); }
  fs.writeFileSync(path.join(root, 'public/favicon.ico'), Buffer.concat([head, ...dirs, ...imgs.map(i => i[1])]));
  await p.setViewportSize({ width: 1200, height: 630 });
  await p.goto('file://' + path.join(root, 'scripts/og.html')); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(root, 'public/og.png') });
  await b.close(); console.log('assets ok');
})();
