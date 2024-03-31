from uuid import UUID

from src.domain.reason.schema.reason import CreateReasonSchema, ReasonSchema
from src.domain.reason.usecase.reason import ReasonUseCaseABC


class ReasonUseCase(ReasonUseCaseABC):
    async def add(self, schema: CreateReasonSchema) -> ReasonSchema:
        return await self.reason_service.add(schema)

    async def delete(self, reason_id: UUID) -> ReasonSchema:
        return await self.reason_service.delete(reason_id)

    async def list_reasons(self) -> list[ReasonSchema]:
        return await self.reason_service.list_reasons()
