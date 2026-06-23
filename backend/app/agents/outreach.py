from app.models import Lead, Proposal


class OutreachAgent:
    def prepare_email(self, lead: Lead, proposal: Proposal) -> dict[str, str]:
        return {
            "to": lead.email or "",
            "subject": f"Quick improvement idea for {lead.company_name}",
            "body": proposal.proposal_text,
            "status": "requires_human_approval",
        }

