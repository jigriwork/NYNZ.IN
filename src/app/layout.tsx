import type { Metadata, Viewport } from "next";
import { Geist, Geist_Mono, Cormorant_Garamond } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// High-contrast editorial serif for premium fashion feel
const displaySerif = Cormorant_Garamond({
  variable: "--font-display",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title: "NYNZ | Luxury Clothing",
  description: "Dark Luxury Streetwear",
  metadataBase: new URL("https://nynz.in"),

  icons: {
    icon: "/favicon.png",
    shortcut: "/favicon.png",
    apple: "/app-icon.png"
  },

  openGraph: {
    title: "NYNZ | Luxury Clothing",
    description: "Dark Luxury Streetwear",
    images: [
      {
        url: "/app-icon.png",
        width: 1200,
        height: 630,
        alt: "NYNZ Luxury Clothing"
      }
    ]
  },

  twitter: {
    card: "summary_large_image",
    title: "NYNZ | Luxury Clothing",
    description: "Dark Luxury Streetwear",
    images: ["/app-icon.png"]
  }
};

export const viewport: Viewport = {
  themeColor: "#0b0b0c",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="bg-background">
      <body className={`${geistSans.variable} ${geistMono.variable} ${displaySerif.variable} antialiased`}> 
        {children}
      </body>
    </html>
  );
}
