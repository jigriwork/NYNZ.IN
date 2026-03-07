import { siteConfig } from "@/config/site";
import { SceneBackground } from "@/components/coming-soon/scene-background";
import { EmailCapture } from "@/components/coming-soon/email-capture";
import { BrandSignals } from "@/components/coming-soon/brand-signals";
import { Wordmark } from "@/components/brand/wordmark";

export default function Home() {
  return (
    <div className="relative min-h-dvh overflow-hidden bg-background text-foreground">
      <SceneBackground />

      {/* Refined luxury atmosphere */}
      <div aria-hidden className="pointer-events-none absolute inset-0">
        <div className="absolute inset-0 bg-black" />

        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_42%,rgba(54,64,120,0.08),transparent_24%),radial-gradient(circle_at_50%_48%,rgba(255,255,255,0.025),transparent_18%),radial-gradient(circle_at_50%_50%,rgba(0,0,0,0),rgba(0,0,0,0.72)_72%)]" />

        <div className="absolute left-1/2 top-[44%] h-[24rem] w-[24rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-white/[0.025] blur-[140px] animate-[pulse_12s_ease-in-out_infinite] md:h-[32rem] md:w-[32rem]" />

        <div className="absolute left-1/2 top-[46%] h-[36rem] w-[36rem] -translate-x-1/2 -translate-y-1/2 rounded-full bg-indigo-300/[0.03] blur-[220px] animate-[pulse_16s_ease-in-out_infinite] md:h-[48rem] md:w-[48rem]" />

        <div className="absolute inset-0 opacity-[0.035] [background-image:radial-gradient(rgba(255,255,255,0.7)_0.7px,transparent_0.9px)] [background-size:28px_28px]" />

        <div className="absolute inset-0 bg-[linear-gradient(180deg,rgba(255,255,255,0.01),transparent_22%,transparent_78%,rgba(255,255,255,0.01))]" />
      </div>

      {/* Top logo */}
      <header className="container-nynz relative z-10 pt-10 md:pt-14 lg:pt-16">
        <div className="flex justify-center">
          <Wordmark className="opacity-100" height={112} />
        </div>
      </header>

      {/* Hero */}
      <main className="relative z-10 flex-1">
        <section className="container-nynz flex min-h-[calc(100dvh-14rem)] items-center py-8 md:min-h-[calc(100dvh-15rem)] md:py-10 lg:py-12">
          <div className="mx-auto w-full max-w-5xl">
            <div className="mx-auto max-w-[52rem]">
              <p className="text-center text-[12px] uppercase tracking-[0.30em] text-white/58 md:text-[13px]">
                DARK LUXURY — DROPPING SOON
              </p>

              <div className="relative mt-7 md:mt-8">
                {/* Softer glow behind H1 */}
                <div
                  aria-hidden
                  className="pointer-events-none absolute left-1/2 top-1/2 h-[22rem] w-[34rem] -translate-x-1/2 -translate-y-1/2 rounded-full opacity-70 blur-[130px] md:h-[28rem] md:w-[46rem]"
                  style={{
                    background:
                      "radial-gradient(circle, rgba(255,255,255,0.12) 0%, rgba(190,200,255,0.06) 34%, rgba(255,255,255,0) 74%)",
                  }}
                />
                <div
                  aria-hidden
                  className="pointer-events-none absolute left-1/2 top-1/2 hidden md:block h-[42rem] w-[62rem] -translate-x-1/2 -translate-y-1/2 rounded-full opacity-35 blur-[200px]"
                  style={{
                    background:
                      "radial-gradient(circle, rgba(255,255,255,0.05) 0%, rgba(150,160,240,0.04) 28%, rgba(255,255,255,0) 72%)",
                  }}
                />

                <h1 className="font-display relative text-center text-[clamp(2.4rem,8vw,6.7rem)] leading-[0.88] tracking-[-0.02em] text-white">
                  <span className="block whitespace-nowrap">AFTER DARK</span>

                  <span className="mt-2 block whitespace-nowrap text-white/84">
                    <span className="inline-flex items-end justify-center gap-2 md:gap-3">
                      <span className="relative inline-block h-[0.92em] w-[1.7em] overflow-hidden">
                        <span className="absolute left-1/2 top-1/2 flex -translate-x-1/2 -translate-y-1/2 scale-[2.2]">
                          <Wordmark className="opacity-100" height="0.92em" />
                        </span>
                      </span>

                      <span>ARRIVES</span>
                    </span>
                  </span>
                </h1>
              </div>

              <p className="mx-auto mt-7 max-w-xl text-center text-sm leading-relaxed text-white/72 md:mt-8 md:text-base">
                Tailored street codes. Cut with precision.
              </p>

              <EmailCapture className="mx-auto mt-9 max-w-xl md:mt-10" />

              <BrandSignals className="mt-6 justify-center md:mt-7" />
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="container-nynz relative z-10 pb-8 pt-8 md:pb-10">
        <p className="text-center text-xs tracking-[0.16em] text-white/45">
          © 2026 {siteConfig.brandName}
        </p>
      </footer>
    </div>
  );
}