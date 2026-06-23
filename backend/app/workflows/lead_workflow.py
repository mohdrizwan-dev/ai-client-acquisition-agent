from sqlmodel import Session, select

from app.agents.analyzer import WebsiteAnalyzerAgent
from app.agents.proposal_generator import ProposalGeneratorAgent
from app.agents.scoring import ClientScoringAgent
from app.models import Lead, LeadStatus, Proposal, WebsiteAnalysis, utc_now


class LeadWorkflow:
    def __init__(self) -> None:
        self.analyzer = WebsiteAnalyzerAgent()
        self.scorer = ClientScoringAgent()
        self.proposal_generator = ProposalGeneratorAgent()

    def analyze_score_and_generate(self, session: Session, lead: Lead) -> Proposal:
        analysis_payload = self.analyzer.analyze(lead)

        lead.seo_score = int(analysis_payload["seo_score"])
        lead.mobile_friendly = bool(analysis_payload["mobile_friendly"])
        lead.website_speed = str(analysis_payload["website_speed"])
        lead.score, lead.priority = self.scorer.score(lead)
        lead.status = LeadStatus.analyzed
        lead.updated_at = utc_now()

        analysis = WebsiteAnalysis(
            lead_id=lead.id or 0,
            summary=str(analysis_payload["summary"]),
            problems=str(analysis_payload["problems"]),
            opportunities=str(analysis_payload["opportunities"]),
        )
        session.add(analysis)
        session.add(lead)
        session.commit()
        session.refresh(analysis)
        session.refresh(lead)

        existing = session.exec(select(Proposal).where(Proposal.lead_id == lead.id)).first()
        if existing:
            existing.proposal_text = self.proposal_generator.generate(lead, analysis)
            session.add(existing)
            session.commit()
            session.refresh(existing)
            return existing

        proposal = Proposal(
            lead_id=lead.id or 0,
            proposal_text=self.proposal_generator.generate(lead, analysis),
        )
        session.add(proposal)
        session.commit()
        session.refresh(proposal)
        return proposal

