from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra="ignore", from_attributes=True
    )


class TimestampedSchema(BaseSchema):
    created_at: datetime


class IdentifiableSchema(BaseSchema):
    id: UUID
