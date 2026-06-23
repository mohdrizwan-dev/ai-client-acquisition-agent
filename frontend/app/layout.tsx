import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Client Acquisition Agent",
  description: "Lead discovery, AI audits, proposals, outreach, and CRM tracking."
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

