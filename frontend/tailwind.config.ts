import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {
      colors: {
        ink: "#111827",
        mist: "#eef2f7",
        signal: "#0f766e",
        flame: "#dc2626"
      }
    }
  },
  plugins: []
};

export default config;

