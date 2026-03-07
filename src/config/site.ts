import type { BrandStat, CollectionItem, NavItem } from "@/types/landing";

export const siteConfig = {
  brandName: "NYNZ",
  tagline: "Dark Luxury",
  description:
    "NYNZ is a high-end luxury streetwear label. A study in dark luxury, editorial edge, and refined power.",
  // Social + contact
  social: {
    instagram: "https://instagram.com/nynz.in",
  },
  instagramHandle: "@nynz.in",
  contactEmail: "hello@nynz.in",
};

// The following exports remain for potential future sections but are unused in the Coming Soon composition.
export const navigationItems: NavItem[] = [
  { label: "Collections", href: "#collections" },
  { label: "Story", href: "#story" },
  { label: "Craftsmanship", href: "#craftsmanship" },
  { label: "Contact", href: "#contact" },
];

export const collectionHighlights: CollectionItem[] = [
  {
    title: "Signature Tailoring",
    description: "Structured silhouettes designed for timeless elegance.",
  },
  {
    title: "Evening Essentials",
    description: "Refined statement pieces for curated occasions.",
  },
  {
    title: "Modern Heritage",
    description: "Classic influences interpreted through contemporary luxury.",
  },
];

export const brandStats: BrandStat[] = [
  { label: "Design Direction", value: "Editorial Minimalism" },
  { label: "Material Focus", value: "Premium Textiles" },
  { label: "Brand Position", value: "High Luxury" },
];


