from app.models import Lead, Priority


COUNTRY_SCORE = {
    "united states": 20,
    "usa": 20,
    "canada": 18,
    "united kingdom": 18,
    "australia": 18,
    "india": 12,
}

HIGH_VALUE_INDUSTRIES = {
    "real estate",
    "healthcare",
    "finance",
    "legal",
    "saas",
    "ecommerce",
    "education",
}


class ClientScoringAgent:
    def score(self, lead: Lead) -> tuple[int, Priority]:
        business_size = 10
        website_quality = 15 if lead.website else 3
        country = COUNTRY_SCORE.get((lead.country or "").lower(), 10)
        industry = 15 if (lead.industry or "").lower() in HIGH_VALUE_INDUSTRIES else 8
        revenue_potential = 25 if lead.email or lead.website else 12

        total = min(100, business_size + website_quality + country + industry + revenue_potential)

        if total >= 75:
            return total, Priority.high
        if total >= 50:
            return total, Priority.medium
        return total, Priority.low

