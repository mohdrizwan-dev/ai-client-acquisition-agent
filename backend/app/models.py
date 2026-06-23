from datetime import datetime, timezone
from enum import Enum

from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class LeadStatus(str, Enum):
    new = "new"
    analyzed = "analyzed"
    approved = "approved"
    contacted = "contacted"
    replied = "replied"
    meeting_booked = "meeting_booked"
    closed = "closed"
    rejected = "rejected"


class Priority(str, Enum):
    low = "LOW"
    medium = "MEDIUM"
    high = "HIGH"


class Channel(str, Enum):
    email = "email"
    linkedin = "linkedin"
    whatsapp = "whatsapp"
    contact_form = "contact_form"
    note = "note"


class LeadBase(SQLModel):
    company_name: str
    website: str | None = None
    email: str | None = None
    industry: str | None = None
    country: str | None = None
    contact_person: str | None = None


class Lead(LeadBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tech_stack: str | None = None
    website_speed: str | None = None
    mobile_friendly: bool | None = None
    seo_score: int | None = Field(default=None, ge=0, le=100)
    score: int | None = Field(default=None, ge=0, le=100)
    priority: Priority = Priority.low
    status: LeadStatus = LeadStatus.new
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


class LeadCreate(LeadBase):
    pass


class LeadRead(LeadBase):
    id: int
    tech_stack: str | None
    website_speed: str | None
    mobile_friendly: bool | None
    seo_score: int | None
    score: int | None
    priority: Priority
    status: LeadStatus
    created_at: datetime
    updated_at: datetime


class LeadUpdate(SQLModel):
    company_name: str | None = None
    website: str | None = None
    email: str | None = None
    industry: str | None = None
    country: str | None = None
    contact_person: str | None = None
    status: LeadStatus | None = None


class WebsiteAnalysis(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lead_id: int = Field(index=True)
    summary: str
    problems: str
    opportunities: str
    created_at: datetime = Field(default_factory=utc_now)


class Proposal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lead_id: int = Field(index=True)
    proposal_text: str
    sent_status: str = "draft"
    response_status: str = "none"
    created_at: datetime = Field(default_factory=utc_now)


class Interaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lead_id: int = Field(index=True)
    message: str
    channel: Channel
    timestamp: datetime = Field(default_factory=utc_now)


class InteractionCreate(SQLModel):
    message: str
    channel: Channel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    subscription_plan: str = "starter"
