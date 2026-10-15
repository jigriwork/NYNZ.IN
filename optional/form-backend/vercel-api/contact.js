import { handleContact } from "../../../lib/form-core.js";
import { rateLimitStore } from "../../../lib/upstash.js";
export default {
  fetch(request) {
    if (request.method !== "POST") return new Response('{"ok":false,"error":"method"}', { status: 405, headers: { allow: "POST", "content-type": "application/json" } });
    const env = { ...process.env, RL: rateLimitStore(process.env) };
    // Vercel puts the client IP in x-real-ip / x-forwarded-for; core reads cf-connecting-ip, so map it.
    const h = new Headers(request.headers); h.set("cf-connecting-ip", h.get("x-real-ip") || (h.get("x-forwarded-for") || "unknown").split(",")[0].trim());
    return handleContact(new Request(request, { headers: h }), env);
  },
};
