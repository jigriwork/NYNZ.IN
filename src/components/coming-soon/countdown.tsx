"use client";

import { useEffect, useMemo, useState } from "react";

function pad(n: number) { return n.toString().padStart(2, "0"); }

export function Countdown({ targetDate, className = "" }: { targetDate?: string; className?: string }) {
  const target = useMemo(() => (targetDate ? new Date(targetDate).getTime() : undefined), [targetDate]);
  const [now, setNow] = useState<number>(() => Date.now());

  useEffect(() => {
    if (!target) return;
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, [target]);

  if (!target) return null;

  const diff = Math.max(0, target - now);
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const mins = Math.floor((diff / (1000 * 60)) % 60);
  const secs = Math.floor((diff / 1000) % 60);

  return (
    <div className={`grid grid-cols-4 gap-2 text-center text-white/80 ${className}`} aria-label="Countdown to launch">
      {[{label:"Days", value: pad(days)}, {label:"Hrs", value: pad(hours)}, {label:"Min", value: pad(mins)}, {label:"Sec", value: pad(secs)}].map(({label, value}) => (
        <div key={label} className="rounded-2xl border border-white/10 bg-white/5 px-3 py-3 backdrop-blur-md">
          <div className="font-display text-2xl md:text-3xl leading-none tracking-tight">{value}</div>
          <div className="mt-1 text-[10px] uppercase tracking-[0.24em] text-white/60">{label}</div>
        </div>
      ))}
    </div>
  );
}
