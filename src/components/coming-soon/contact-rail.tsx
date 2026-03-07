import { siteConfig } from "@/config/site";
import { SocialBar } from "./social-bar";

export function ContactRail({ className = "" }: { className?: string }) {
  return (
    <aside className={`hidden md:flex flex-col items-end gap-3 text-white/70 ${className}`}>
      <div className="group inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 backdrop-blur-md transition hover:bg-white/10">
        <SocialBar />
        <a
          href={siteConfig.social.instagram}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs tracking-[0.22em] uppercase text-white/70 group-hover:text-white/90"
        >
          {siteConfig.instagramHandle}
        </a>
      </div>

      <a
        href={`mailto:${siteConfig.contactEmail}`}
        className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-xs tracking-[0.18em] text-white/70 backdrop-blur-md transition hover:bg-white/10 hover:text-white/90"
      >
        {siteConfig.contactEmail}
      </a>
    </aside>
  );
}
