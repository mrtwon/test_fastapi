from uuid import UUID

from sqlalchemy import Integer

from src.domain.base.schemas import BaseSchema, TimestampedSchema, IdentifiableSchema


class CreateSpamUserSchema(BaseSchema):
    user_id: Integer
    reasons_id: list[UUID]


class SpamUserSchema(IdentifiableSchema, TimestampedSchema):
    user_id: Integer
