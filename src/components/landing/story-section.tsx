import { brandStats } from "@/config/site";

export function StorySection() {
  return (
    <section id="story" className="border-b border-border py-20" aria-labelledby="story-title">
      <div className="container-nynz grid gap-10 lg:grid-cols-2 lg:items-start">
        <div className="space-y-4">
          <p className="text-xs uppercase tracking-[0.28em] text-muted-foreground">Brand Story</p>
          <h2 id="story-title" className="text-3xl font-semibold tracking-tight md:text-4xl">
            Structure ready for premium storytelling
          </h2>
          <p className="text-muted-foreground">
            This section is intentionally simple. It is prepared for long-form brand copy, campaign narrative, and editorial imagery.
          </p>
        </div>

        <ul className="space-y-4 rounded-2xl border border-border bg-muted p-6">
          {brandStats.map((stat) => (
            <li key={stat.label} className="grid gap-1 border-b border-border pb-4 last:border-none last:pb-0">
              <span className="text-xs uppercase tracking-[0.2em] text-muted-foreground">{stat.label}</span>
              <span className="text-base font-medium">{stat.value}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
