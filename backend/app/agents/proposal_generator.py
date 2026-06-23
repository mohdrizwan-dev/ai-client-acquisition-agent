from app.models import Lead, WebsiteAnalysis


class ProposalGeneratorAgent:
    def generate(self, lead: Lead, analysis: WebsiteAnalysis | None = None) -> str:
        contact = lead.contact_person or "there"
        company = lead.company_name
        industry = lead.industry or "your business"

        problems = analysis.problems if analysis else "- Website and lead capture audit needed"
        opportunities = analysis.opportunities if analysis else "- Improve conversion and follow-up systems"

        return (
            f"Hi {contact},\n\n"
            f"I took a quick look at {company} and noticed a few areas where a modern AI-assisted "
            f"client acquisition system could help your {industry} team convert more visitors into leads.\n\n"
            f"What stood out:\n{problems}\n\n"
            f"Potential improvements:\n{opportunities}\n\n"
            "I can help with a focused audit, website improvements, and simple CRM automation so every "
            "new inquiry is captured and followed up properly.\n\n"
            "Would it be useful if I sent over a short improvement plan?"
        )

