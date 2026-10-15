import { handleContact } from "../../../../lib/form-core.js";
export const onRequestPost = ({ request, env }) => handleContact(request, env);
export const onRequest = () => new Response(JSON.stringify({ ok: false, error: "method" }), { status: 405, headers: { allow: "POST", "content-type": "application/json" } });
