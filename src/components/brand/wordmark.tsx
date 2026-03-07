"use client";

import { useState } from "react";

export function Wordmark({ className = "", height = 24 }: { className?: string; height?: number | string }) {
  const sources = ["/nynz-logo.png?v=3", "/nynz-logo.svg?v=3"];
  const [sourceIndex, setSourceIndex] = useState(0);
  const [failed, setFailed] = useState(false);

  const handleError = () => {
    if (sourceIndex < sources.length - 1) {
      setSourceIndex((prev) => prev + 1);
      return;
    }

    setFailed(true);
  };


  return (
    <div className={className}>
      {!failed ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={sources[sourceIndex]}
          alt="NYNZ"
          style={{ height: typeof height === 'number' ? `${height}px` : height, width: "auto" }}
          className="block h-auto w-auto max-w-full select-none object-contain"
          onError={handleError}
        />
      ) : (
        <div className="select-none text-sm font-semibold tracking-[0.35em] text-white/90">NYNZ</div>
      )}
    </div>
  );
}
