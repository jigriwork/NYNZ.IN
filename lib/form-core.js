// Contact / health-check form handler. Runs unchanged in Cloudflare Pages Functions (Workers runtime)
// and in Node 20 (local mock server and tests). No cookies, no storage of submissions.
// Layers: origin check, honeypot, signed time token (minimum fill time), Turnstile, per-IP rate limit, validation.
export const LIMITS = { minFillMs: 4000, maxAgeMs: 2 * 3600 * 1000, perIpPerHour: 5, globalPerDay: 100,
  name: 120, email: 254, store: 200, message: 2000, channels: 8 };
const enc = new TextEncoder();
const b64u = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
async function hmac(secret, data) {
  const key = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64u(await crypto.subtle.sign("HMAC", key, enc.encode(data)));
}
async function sha(data) { return b64u(await crypto.subtle.digest("SHA-256", enc.encode(data))).slice(0, 22); }
function eq(a, b) { if (a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }
export async function issueToken(secret, now) { const t = String(now); return `${t}.${await hmac(secret, "ft1:" + t)}`; }
export async function checkToken(secret, token, now) {
  if (typeof token !== "string" || !/^\d{10,15}\.[\w-]{20,}$/.test(token)) return "bad_token";
  const [t, sig] = token.split("."); if (!eq(sig, await hmac(secret, "ft1:" + t))) return "bad_token";
  const age = now - Number(t); if (age < LIMITS.minFillMs) return "too_fast"; if (age > LIMITS.maxAgeMs) return "expired"; return null;
}
const clean = (s, n) => String(s ?? "").replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, "").trim().slice(0, n);
const oneLine = (s, n) => clean(s, n).replace(/[\r\n]+/g, " ");
export function validate(p) {
  const v = { name: oneLine(p.name, LIMITS.name), email: oneLine(p.email, LIMITS.email).toLowerCase(), store: oneLine(p.store, LIMITS.store),
    skus: oneLine(p.skus, 40), message: clean(p.message, LIMITS.message),
    channels: (Array.isArray(p.channels) ? p.channels : p.channels ? [p.channels] : []).slice(0, LIMITS.channels).map((c) => oneLine(c, 40)) };
  const errors = {};
  if (v.name.length < 2) errors.name = "Enter your name.";
  if (!/^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[a-z]{2,}$/i.test(v.email)) errors.email = "Enter a valid email address.";
  if (!/^(https?:\/\/)?[a-z0-9-]+(\.[a-z0-9-]+)+(\/\S*)?$/i.test(v.store)) errors.store = "Enter your store website, for example yourstore.com.";
  if ((v.message.match(/https?:\/\//gi) || []).length > 2) errors.message = "Please remove extra links from the message.";
  return { v, errors };
}
async function rateLimit(kv, ip, now, salt) {
  if (!kv) return { ok: false, reason: "no_rate_limit_store" };
  const hour = Math.floor(now / 3600000), day = Math.floor(now / 86400000);
  const kIp = `rl:ip:${await sha(salt + ip)}:${hour}`, kDay = `rl:day:${day}`;
  const nIp = Number((await kv.get(kIp)) || 0), nDay = Number((await kv.get(kDay)) || 0);
  if (nIp >= LIMITS.perIpPerHour) return { ok: false, reason: "rate_ip" };
  if (nDay >= LIMITS.globalPerDay) return { ok: false, reason: "rate_global" };
  await kv.put(kIp, String(nIp + 1), { expirationTtl: 3700 }); await kv.put(kDay, String(nDay + 1), { expirationTtl: 90000 });
  return { ok: true };
}
async function turnstile(env, token, ip, fetchFn) {
  if (!token) return false;
  const body = new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: token, remoteip: ip });
  const r = await fetchFn("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body });
  const j = await r.json().catch(() => ({})); return j.success === true;
}
// ALLOWED_ORIGINS: comma list. "https://nynz.in" is exact. An entry starting with "." (for example ".vercel.app") matches any https host with that suffix, for preview deployments.
export function originAllowed(origin, list = "https://nynz.in") {
  if (!origin) return false;
  return list.split(",").map((x) => x.trim()).filter(Boolean).some((a) => a.startsWith(".") ? (() => { try { const u = new URL(origin); return u.protocol === "https:" && u.hostname.endsWith(a); } catch { return false; } })() : a === origin);
}
export function renderMail(v) {
  const lines = [`Name: ${v.name}`, `Email: ${v.email}`, `Store: ${v.store}`, `Products and variants: ${v.skus || "not given"}`,
    `Sells on: ${v.channels.join(", ") || "not given"}`, "", v.message || "(no message)"];
  return { subject: `Health check request: ${v.store}`.slice(0, 120), text: lines.join("\n") };
}
const json = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json", "cache-control": "no-store" } });
// deps: { now(): ms, fetch, sendMail(env, {to, replyTo, subject, text}) }
export async function handleToken(request, env, deps = {}) {
  if (!env.FORM_SECRET) return json({ ok: false, error: "not_configured" }, 503);
  return json({ ok: true, token: await issueToken(env.FORM_SECRET, (deps.now || Date.now)()) });
}
export async function handleContact(request, env, deps = {}) {
  const now = (deps.now || Date.now)(), fetchFn = deps.fetch || fetch;
  if (!env.FORM_SECRET || !env.TURNSTILE_SECRET || !env.RL || !(deps.sendMail || env.RESEND_API_KEY)) return json({ ok: false, error: "not_configured" }, 503);
  const origin = request.headers.get("origin"); if (!originAllowed(origin, env.ALLOWED_ORIGINS)) return json({ ok: false, error: "origin" }, 403);
  const len = Number(request.headers.get("content-length") || 0); if (len > 20000) return json({ ok: false, error: "too_large" }, 413);
  let p; try { p = await request.json(); } catch { return json({ ok: false, error: "bad_request" }, 400); }
  const ip = request.headers.get("cf-connecting-ip") || "unknown";
  // 1. honeypot: pretend success so bots learn nothing
  if (clean(p.website_url, 200) !== "") return json({ ok: true });
  // 2. signed time token
  const tk = await checkToken(env.FORM_SECRET, p.form_token, now); if (tk) return json({ ok: false, error: tk }, tk === "too_fast" ? 429 : 400);
  // 3. Turnstile
  if (!(await turnstile(env, p["cf-turnstile-response"], ip, fetchFn))) return json({ ok: false, error: "challenge_failed" }, 400);
  // 4. rate limit (after cheap checks so abuse cannot burn quota)
  const rl = await rateLimit(env.RL, ip, now, env.FORM_SECRET); if (!rl.ok) return json({ ok: false, error: rl.reason }, 429);
  // 5. validation
  const { v, errors } = validate(p); if (Object.keys(errors).length) return json({ ok: false, error: "invalid", fields: errors }, 422);
  const mail = renderMail(v), send = deps.sendMail || sendViaResend;
  try { await send(env, { to: env.MAIL_TO || "sales@nynz.in", replyTo: v.email, ...mail }, fetchFn); } catch { return json({ ok: false, error: "delivery_failed" }, 502); }
  return json({ ok: true });
}
export async function sendViaResend(env, m, fetchFn = fetch) {
  const r = await fetchFn("https://api.resend.com/emails", { method: "POST",
    headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, "content-type": "application/json" },
    body: JSON.stringify({ from: env.MAIL_FROM || "NYNZ website <forms@nynz.in>", to: [m.to], reply_to: m.replyTo, subject: m.subject, text: m.text }) });
  if (!r.ok) throw new Error("resend " + r.status);
}
