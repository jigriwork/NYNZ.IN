export function HeroAtmosphere() {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 -z-10">
      {/* Stronger central glow behind headline */}
      <div className="absolute left-1/2 top-[42%] h-[46vw] w-[46vw] -translate-x-1/2 -translate-y-1/2 rounded-full bg-white/[0.06] blur-[120px] md:h-[520px] md:w-[520px]" />

      {/* Soft vertical spotlight falloff */}
      <div
        className="absolute left-1/2 top-[38%] h-[80vh] w-[90vw] -translate-x-1/2 -translate-y-1/2 rounded-[999px] opacity-70 blur-[80px]"
        style={{
          background:
            "radial-gradient(60% 60% at 50% 40%, rgba(255,255,255,0.11) 0%, rgba(255,255,255,0.05) 40%, rgba(255,255,255,0.0) 70%)",
        }}
      />
    </div>
  );
}
