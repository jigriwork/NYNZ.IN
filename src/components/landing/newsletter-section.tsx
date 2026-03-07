export function NewsletterSection() {
  return (
    <section id="contact" className="border-b border-border py-20" aria-labelledby="newsletter-title">
      <div className="container-nynz grid gap-6 rounded-2xl border border-border bg-muted p-8 md:grid-cols-[1.2fr_1fr] md:items-center">
        <div>
          <h2 id="newsletter-title" className="text-2xl font-semibold tracking-tight md:text-3xl">
            Newsletter Placeholder
          </h2>
          <p className="mt-3 text-sm text-muted-foreground">
            Email capture structure is ready. Connect this to your preferred marketing platform later.
          </p>
        </div>

        <form className="grid gap-3" aria-label="Newsletter signup">
          <input
            type="email"
            placeholder="you@example.com"
            className="h-11 rounded-xl border border-border bg-background px-4 text-sm outline-none"
          />
          <button
            type="button"
            className="h-11 rounded-xl border border-border bg-foreground px-4 text-sm font-medium text-background"
          >
            Join Waitlist
          </button>
        </form>
      </div>
    </section>
  );
}
