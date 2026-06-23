from datetime import datetime, timedelta, timezone


class FollowUpAgent:
    def next_follow_up_at(self, last_contact_at: datetime | None = None) -> datetime:
        base = last_contact_at or datetime.now(timezone.utc)
        return base + timedelta(days=3)

    def draft_follow_up(self, company_name: str) -> str:
        return (
            "Hi, just following up on my previous note about improving "
            f"{company_name}'s lead capture and follow-up process. "
            "Happy to send a quick audit if this is relevant."
        )

