"use client";

import { useState } from "react";

function validateEmail(email: string) {
  return /[^@\s]+@[^@\s]+\.[^@\s]+/.test(email);
}

export function EmailCapture({ className = "" }: { className?: string }) {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (!validateEmail(email)) {
      setError("Enter a valid email");
      return;
    }
    try {
      setLoading(true);
      const res = await fetch("/api/notify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      if (!res.ok) throw new Error("Failed");
      setSuccess(true);
      setEmail("");
    } catch {
      setError("Please try again later");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className={className}>
      <form onSubmit={onSubmit} className="relative isolate flex w-full max-w-xl items-center gap-2 rounded-2xl border border-white/10 bg-white/5 p-1 backdrop-blur-md shadow-[inset_0_0_60px_rgba(255,255,255,0.02)]">
        <div aria-hidden className="pointer-events-none absolute inset-0 rounded-2xl ring-1 ring-inset ring-white/5"></div>
        <input
          type="email"
          name="email"
          autoComplete="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full bg-transparent px-4 py-3 text-sm text-white/90 placeholder:text-white/40 outline-none"
          aria-label="Email address"
        />
        <button
          type="submit"
          disabled={loading}
          className="group relative inline-flex shrink-0 items-center justify-center overflow-hidden rounded-xl bg-white/10 px-4 py-2 text-sm font-medium text-white/90 shadow-[0_0_0_rgba(255,255,255,0)] transition-all duration-500 hover:scale-[1.02] hover:bg-white/15 hover:shadow-[0_0_22px_rgba(255,255,255,0.14)] active:scale-[0.99] disabled:opacity-50"
        >
          <span className="pointer-events-none absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/30 to-transparent opacity-0 transition group-hover:translate-x-0 group-hover:opacity-100" style={{transitionDuration:'800ms'}} />
          <span className="pointer-events-none absolute -inset-0.5 rounded-xl bg-white/10 opacity-0 blur-md transition-opacity group-hover:opacity-100" />
          Notify Me
        </button>
      </form>

      {/* Feedback */}
      <div className="mt-3 min-h-5 text-xs">
        {error && <p className="text-red-300/80">{error}</p>}
        {success && <p className="text-white/70">You’re on the list.</p>}
      </div>
    </div>
  );
}
