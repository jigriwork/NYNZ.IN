import { navigationItems, siteConfig } from "@/config/site";
import { Wordmark } from "@/components/brand/wordmark";

export function SiteHeader() {
  return (
    <header className="border-b border-border">
      <div className="container-nynz flex h-16 items-center justify-between">
        <div className="flex items-center py-2">
          <Wordmark className="pr-2" height={28} />
          <span className="sr-only">{siteConfig.brandName}</span>
        </div>

        <nav aria-label="Primary navigation">
          <ul className="hidden gap-6 text-sm text-muted-foreground md:flex">
            {navigationItems.map((item) => (
              <li key={item.href}>
                <a href={item.href} className="transition-colors hover:text-foreground">
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </header>
  );
}
