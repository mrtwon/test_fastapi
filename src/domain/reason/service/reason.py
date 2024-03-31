from abc import ABC
from uuid import UUID

from src.domain.reason.schema.reason import CreateReasonSchema, ReasonSchema


class ReasonServiceABC(ABC):
    async def add(self, schema: CreateReasonSchema) -> ReasonSchema:
        raise NotImplementedError

    async def delete(self, reason_id: UUID) -> ReasonSchema:
        raise NotImplementedError

    async def list_reasons(self) -> list[ReasonSchema]:
        raise NotImplementedError
