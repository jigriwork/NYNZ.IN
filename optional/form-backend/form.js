(function () {
  var f = document.getElementById("hc-form"); if (!f) return;
  var status = document.getElementById("hc-status"), btn = f.querySelector("button[type=submit]"), tokenField = f.querySelector("[name=form_token]");
  function say(msg, bad) { status.textContent = msg; status.className = "form-status" + (bad ? " bad" : " ok"); }
  var fallback = "Please email sales@nynz.in instead.";
  fetch("/api/form-token", { cache: "no-store" }).then(function (r) { return r.json(); }).then(function (j) {
    if (j && j.token) { tokenField.value = j.token; } else { say("The form is not available right now. " + fallback, true); btn.disabled = true; }
  }).catch(function () { say("The form is not available right now. " + fallback, true); btn.disabled = true; });
  f.addEventListener("submit", function (e) {
    e.preventDefault(); if (!f.reportValidity()) return;
    var fd = new FormData(f), body = {}; fd.forEach(function (v, k) { if (k === "channel") { (body.channels = body.channels || []).push(v); } else { body[k] = v; } });
    btn.disabled = true; say("Sending...", false);
    fetch("/api/contact", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) })
      .then(function (r) { return r.json().then(function (j) { return { r: r, j: j }; }); })
      .then(function (x) {
        if (x.j.ok) { f.reset(); say("Thank you. We have your request and will reply by email.", false); return; }
        var m = { too_fast: "That was very quick. Please wait a few seconds and try again.", expired: "This page has been open a while. Please reload it and try again.",
          challenge_failed: "The spam check did not pass. Please try again.", invalid: "Please check your name, email and store website.", rate_ip: "Too many requests from your network. Please try again later.",
          rate_global: "We are receiving too many requests. " + fallback };
        say((m[x.j.error] || "Something went wrong. " + fallback), true); btn.disabled = false;
        if (window.turnstile) try { window.turnstile.reset(); } catch (e2) {}
      }).catch(function () { say("Could not reach the form service. " + fallback, true); btn.disabled = false; });
  });
})();
