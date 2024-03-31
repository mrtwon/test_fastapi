from abc import ABC
from uuid import UUID

from src.domain.reason.schema.reason import CreateReasonSchema, ReasonSchema
from src.domain.reason.service.reason import ReasonServiceABC


class ReasonUseCaseABC(ABC):
    def __init__(self, reason_service: ReasonServiceABC):
        self.reason_service = reason_service

    async def add(self, schema: CreateReasonSchema) -> ReasonSchema:
        raise NotImplementedError

    async def delete(self, reason_id: UUID) -> ReasonSchema:
        raise NotImplementedError

    async def list_reasons(self) -> list[ReasonSchema]:
        raise NotImplementedError
