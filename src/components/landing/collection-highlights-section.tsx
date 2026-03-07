import { collectionHighlights } from "@/config/site";

export function CollectionHighlightsSection() {
  return (
    <section id="collections" className="border-b border-border py-20" aria-labelledby="collections-title">
      <div className="container-nynz space-y-8">
        <h2 id="collections-title" className="text-3xl font-semibold tracking-tight md:text-4xl">
          Collection Highlights
        </h2>

        <div className="grid gap-4 md:grid-cols-3">
          {collectionHighlights.map((item) => (
            <article key={item.title} className="rounded-2xl border border-border bg-muted p-6">
              <h3 className="text-lg font-medium">{item.title}</h3>
              <p className="mt-3 text-sm text-muted-foreground">{item.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
