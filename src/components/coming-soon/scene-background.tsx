export function SceneBackground() {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 -z-10 overflow-hidden">
      {/* Base atmospheric field on pure black */}
      <div
        className="absolute -inset-1 animate-drift opacity-95"
        style={{
          animationDuration: "36s",
          animationTimingFunction: "ease-in-out",
          animationIterationCount: "infinite",
          background:
            "radial-gradient(1080px 640px at 50% 16%, rgba(238,241,255,0.26), transparent 63%)," +
            "radial-gradient(780px 420px at 22% 72%, rgba(150,158,220,0.14), transparent 72%)," +
            "radial-gradient(820px 460px at 78% 74%, rgba(150,158,220,0.12), transparent 72%)," +
            "linear-gradient(180deg, rgba(0,0,0,0.04) 0%, rgba(0,0,0,0.80) 56%, rgba(0,0,0,1) 100%)",
        }}
      />

      {/* Premium top halo */}
      <div
        className="absolute left-1/2 top-[-14%] h-[52rem] w-[52rem] -translate-x-1/2 rounded-full opacity-85 blur-3xl"
        style={{
          animation: "pulseGlow 12s ease-in-out infinite",
          background:
            "radial-gradient(circle, rgba(255,255,255,0.28) 0%, rgba(204,209,255,0.14) 34%, rgba(255,255,255,0) 74%)",
        }}
      />

      {/* Slow cinematic light sweep (still subtle) */}
      <div
        className="absolute left-1/2 top-[-10%] h-[120vh] w-[58vw] -translate-x-1/2 opacity-30 blur-2xl"
        style={{
          animation: "drift 28s ease-in-out infinite",
          background:
            "linear-gradient(120deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.10) 45%, rgba(255,255,255,0.02) 65%, rgba(255,255,255,0) 100%)",
        }}
      />

      {/* Bottom focus glow */}
      <div
        className="absolute bottom-[-22%] left-1/2 h-[38rem] w-[38rem] -translate-x-1/2 rounded-full opacity-55 blur-3xl"
        style={{
          animation: "floaty 16s ease-in-out infinite",
          background:
            "radial-gradient(circle, rgba(140,148,230,0.22) 0%, rgba(140,148,230,0.10) 36%, rgba(255,255,255,0) 76%)",
        }}
      />

      {/* Visible but refined micro-particles */}
      <div
        className="absolute inset-0 opacity-[0.42]"
        style={{
          animation: "drift 48s ease-in-out infinite",
          backgroundImage:
            "radial-gradient(circle at 12% 24%, rgba(255,255,255,0.46) 0 1.6px, transparent 2.2px)," +
            "radial-gradient(circle at 68% 18%, rgba(189,194,220,0.36) 0 1.6px, transparent 2.2px)," +
            "radial-gradient(circle at 84% 42%, rgba(255,255,255,0.38) 0 1.6px, transparent 2.2px)," +
            "radial-gradient(circle at 26% 66%, rgba(184,188,214,0.34) 0 1.6px, transparent 2.2px)," +
            "radial-gradient(circle at 56% 78%, rgba(255,255,255,0.32) 0 1.6px, transparent 2.2px)",
          backgroundRepeat: "no-repeat",
        }}
      />

      {/* Subtle vignette */}
      <div className="vignette absolute inset-0" />

      {/* Film grain */}
      <div className="noise-overlay absolute inset-0" />
    </div>
  );
}
