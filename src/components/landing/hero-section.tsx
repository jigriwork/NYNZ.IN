import { siteConfig } from "@/config/site";

export function HeroSection() {
  return (
    <section className="border-b border-border py-24" aria-labelledby="hero-title">
      <div className="container-nynz space-y-6">
        <p className="text-xs uppercase tracking-[0.3em] text-muted-foreground">
          {siteConfig.tagline}
        </p>
        <h1 id="hero-title" className="max-w-3xl text-4xl font-semibold tracking-tight md:text-6xl">
          NYNZ Landing Page Starter
        </h1>
        <p className="max-w-2xl text-base text-muted-foreground md:text-lg">
          This is a clean production-ready foundation. Final visuals, imagery, and brand storytelling can now be added quickly by the frontend team.
        </p>
      </div>
    </section>
  );
}
