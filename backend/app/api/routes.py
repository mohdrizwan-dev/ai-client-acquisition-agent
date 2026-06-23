from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.agents.lead_hunter import LeadHunterAgent
from app.database import get_session
from app.models import Interaction, InteractionCreate, Lead, LeadCreate, LeadRead, LeadUpdate, Proposal, utc_now
from app.workflows.lead_workflow import LeadWorkflow

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/leads", response_model=list[LeadRead])
def list_leads(session: Session = Depends(get_session)) -> list[Lead]:
    return list(session.exec(select(Lead).order_by(Lead.created_at.desc())).all())


@router.post("/leads", response_model=LeadRead)
def create_lead(payload: LeadCreate, session: Session = Depends(get_session)) -> Lead:
    normalized = LeadHunterAgent().normalize_manual_lead(payload)
    lead = Lead.model_validate(normalized)
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead


@router.patch("/leads/{lead_id}", response_model=LeadRead)
def update_lead(lead_id: int, payload: LeadUpdate, session: Session = Depends(get_session)) -> Lead:
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(lead, key, value)
    lead.updated_at = utc_now()

    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead


@router.post("/leads/{lead_id}/run")
def run_lead_workflow(lead_id: int, session: Session = Depends(get_session)) -> dict[str, object]:
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    proposal = LeadWorkflow().analyze_score_and_generate(session, lead)
    session.refresh(lead)
    return {"lead": lead, "proposal": proposal}


@router.get("/leads/{lead_id}/proposals", response_model=list[Proposal])
def list_proposals(lead_id: int, session: Session = Depends(get_session)) -> list[Proposal]:
    return list(session.exec(select(Proposal).where(Proposal.lead_id == lead_id)).all())


@router.post("/leads/{lead_id}/interactions", response_model=Interaction)
def create_interaction(
    lead_id: int,
    payload: InteractionCreate,
    session: Session = Depends(get_session),
) -> Interaction:
    if not session.get(Lead, lead_id):
        raise HTTPException(status_code=404, detail="Lead not found")

    interaction = Interaction(
        lead_id=lead_id,
        message=payload.message,
        channel=payload.channel,
    )
    session.add(interaction)
    session.commit()
    session.refresh(interaction)
    return interaction

@router.get("/analytics")
def analytics(session: Session = Depends(get_session)) -> dict[str, int]:
    leads = list(session.exec(select(Lead)).all())
    return {
        "total_leads": len(leads),
        "high_priority": sum(1 for lead in leads if lead.priority == "HIGH"),
        "contacted": sum(1 for lead in leads if lead.status == "contacted"),
        "closed": sum(1 for lead in leads if lead.status == "closed"),
    }
