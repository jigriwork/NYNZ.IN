import { handleToken } from "../../../lib/form-core.js";
export default { fetch: (request) => handleToken(request, process.env) };
