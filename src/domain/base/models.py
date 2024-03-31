from datetime import datetime
from uuid import UUID, uuid4

from attr import define, field

entity = define(slots=False, kw_only=True)


@entity
class IdentifiableModel:
    id: UUID = field(factory=uuid4)

@entity
class TimestampedModel:
    created_at: datetime | None = field(default=None)
