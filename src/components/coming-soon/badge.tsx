export function Badge({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <div
      className={`rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[10px] uppercase tracking-[0.24em] text-white/80 backdrop-blur-md shadow-[0_0_0_1px_rgba(255,255,255,0.04)] ${className}`}
    >
      {children}
    </div>
  );
}
