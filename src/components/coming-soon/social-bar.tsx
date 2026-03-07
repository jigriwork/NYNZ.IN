import { siteConfig } from "@/config/site";

function IconInstagram(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" strokeWidth="1.2" {...props}>
      <rect x="3" y="3" width="18" height="18" rx="5"/>
      <circle cx="12" cy="12" r="3.5"/>
      <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>
    </svg>
  );
}

export function SocialBar({ className = "" }: { className?: string }) {
  return (
    <div className={`flex items-center gap-4 text-white/70 ${className}`} aria-label="Social links">
      {siteConfig.social?.instagram && (
        <a
          href={siteConfig.social.instagram}
          target="_blank"
          rel="noopener noreferrer"
          className="group grid h-10 w-10 place-items-center rounded-full border border-white/10 bg-white/5 backdrop-blur-sm transition-all hover:scale-[1.03] hover:text-white/90 hover:shadow-[0_0_0_1px_rgba(255,255,255,0.06),0_0_30px_rgba(255,255,255,0.06)]"
          aria-label="Instagram"
        >
          <IconInstagram className="h-4 w-4 transition-transform group-hover:scale-105" />
        </a>
      )}
    </div>
  );
}
