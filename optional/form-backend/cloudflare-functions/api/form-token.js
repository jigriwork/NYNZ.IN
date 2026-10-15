import { handleToken } from "../../../../lib/form-core.js";
export const onRequestGet = ({ request, env }) => handleToken(request, env);
