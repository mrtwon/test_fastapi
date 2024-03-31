from uuid import UUID

from src.domain.reason.interface.uow import IReasonUOW
from src.domain.reason.model.reason import Reason
from src.domain.reason.schema.reason import CreateReasonSchema, ReasonSchema
from src.domain.reason.service.reason import ReasonServiceABC
from src.implementation.reason.service.base import ReasonBaseCase


class AddReason(ReasonBaseCase):
    async def __call__(self, schema: CreateReasonSchema) -> ReasonSchema:
        reason_model = Reason.create(schema.text)
        result_add = await self.uow.reason.add_reason(reason_model)
        to_schema = ReasonSchema.model_validate(result_add)
        await self.uow.commit()
        return to_schema


class DeleteReason(ReasonBaseCase):
    async def __call__(self, reason_id: UUID):
        r = await self.uow.reason.delete_reason(reason_id)
        to_schema = ReasonSchema.model_validate(r)
        await self.uow.commit()
        return to_schema


class ListReason(ReasonBaseCase):
    async def __call__(self):
        r = await self.uow.reason.list_reasons()
        list_r = [ReasonSchema.model_validate(i) for i in r]
        return list_r


class ReasonService(ReasonServiceABC):
    def __init__(self, uow: IReasonUOW):
        self.uow = uow

    async def add(self, schema: CreateReasonSchema) -> ReasonSchema:
        return await AddReason(self.uow)(schema)

    async def delete(self, reason_id: UUID) -> ReasonSchema:
        return await DeleteReason(self.uow)(reason_id)

    async def list_reasons(self) -> list[ReasonSchema]:
        raise await ListReason(self.uow)()
