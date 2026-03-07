import { siteConfig } from "@/config/site";

export function BrandSignals({ className = "" }: { className?: string }) {
  return (
    <div className={`flex flex-col gap-2 text-sm text-white/70 md:flex-row md:items-center md:gap-6 ${className}`}>
      <a
        href={siteConfig.social.instagram}
        target="_blank"
        rel="noopener noreferrer"
        className="underline-offset-4 hover:text-white/90 hover:underline"
      >
        Instagram: <span className="text-white/90">{siteConfig.instagramHandle}</span>
      </a>
      <span className="hidden text-white/30 md:block">•</span>
      <a href={`mailto:${siteConfig.contactEmail}`} className="underline-offset-4 hover:text-white/90 hover:underline">
        Contact: <span className="text-white/90">{siteConfig.contactEmail}</span>
      </a>
    </div>
  );
}
