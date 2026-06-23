from app.models import Lead


class WebsiteAnalyzerAgent:
    """MVP analyzer with deterministic heuristics until external audit tools are wired in."""

    def analyze(self, lead: Lead) -> dict[str, str | int | bool]:
        website = lead.website or ""
        problems: list[str] = []
        opportunities: list[str] = []

        if not website:
            problems.append("No website captured")
            opportunities.append("Find verified website and contact information")
        if website and not website.startswith("https://"):
            problems.append("Website may not be using HTTPS")
            opportunities.append("Improve trust and technical SEO with secure configuration")
        if not lead.email:
            problems.append("No direct email found")
            opportunities.append("Add clear lead capture and contact flows")
        if not lead.industry:
            problems.append("Industry not classified")
            opportunities.append("Enrich lead profile before outreach")

        if not problems:
            problems.append("Needs deeper website audit")
            opportunities.append("Run Lighthouse and conversion audit")

        return {
            "summary": f"{lead.company_name} has {len(problems)} visible acquisition signals.",
            "problems": "\n".join(f"- {problem}" for problem in problems),
            "opportunities": "\n".join(f"- {opportunity}" for opportunity in opportunities),
            "seo_score": 55 if problems else 75,
            "mobile_friendly": True,
            "website_speed": "unknown",
        }

