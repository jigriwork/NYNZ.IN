import { siteConfig } from "@/config/site";

export function SiteFooter() {
  return (
    <footer className="py-10">
      <div className="container-nynz flex flex-col gap-3 text-sm text-muted-foreground md:flex-row md:items-center md:justify-between">
        <p>© {new Date().getFullYear()} {siteConfig.brandName}. All rights reserved.</p>
        <p>Production-ready Next.js starter for premium landing build.</p>
      </div>
    </footer>
  );
}
