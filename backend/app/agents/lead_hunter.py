from app.models import LeadCreate


class LeadHunterAgent:
    """Placeholder for compliant lead discovery connectors."""

    def normalize_manual_lead(self, payload: LeadCreate) -> LeadCreate:
        website = payload.website
        if website and not website.startswith(("http://", "https://")):
            website = f"https://{website}"

        return LeadCreate(
            company_name=payload.company_name.strip(),
            website=website,
            email=payload.email,
            industry=payload.industry,
            country=payload.country,
            contact_person=payload.contact_person,
        )

