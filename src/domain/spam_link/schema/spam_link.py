from uuid import UUID

from src.domain.base.schemas import BaseSchema, TimestampedSchema, IdentifiableSchema


class CreateSpamLinkSchema(BaseSchema):
    link: str
    reasons_id: list[UUID]


class SpamLinkSchema(IdentifiableSchema, TimestampedSchema):
    link: str
