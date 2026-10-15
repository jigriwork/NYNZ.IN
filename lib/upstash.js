// Minimal KV adapter over the Upstash Redis REST API (works from Vercel functions, no SDK needed).
export function upstashKV(url, token, fetchFn = fetch) {
  const call = async (path) => { const r = await fetchFn(`${url}/${path}`, { headers: { authorization: `Bearer ${token}` } }); if (!r.ok) throw new Error("upstash " + r.status); return (await r.json()).result; };
  return { get: (k) => call(`get/${encodeURIComponent(k)}`), put: (k, v, o = {}) => call(`set/${encodeURIComponent(k)}/${encodeURIComponent(v)}` + (o.expirationTtl ? `/EX/${o.expirationTtl}` : "")) };
}
// Rate-limit store for the form. Production needs Upstash. RATE_LIMIT_STORE=memory is for local runs only (per-instance, resets on cold start).
const mem = new Map();
export function rateLimitStore(env) {
  if (env.UPSTASH_REDIS_REST_URL && env.UPSTASH_REDIS_REST_TOKEN) return upstashKV(env.UPSTASH_REDIS_REST_URL, env.UPSTASH_REDIS_REST_TOKEN);
  if (env.RATE_LIMIT_STORE === "memory") return { get: async (k) => mem.get(k) ?? null, put: async (k, v) => { mem.set(k, v); } };
  return null;
}
