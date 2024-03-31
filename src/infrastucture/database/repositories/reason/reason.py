from uuid import UUID

from sqlalchemy import delete, select

from src.domain.reason.exception.reason import ReasonNotFound
from src.domain.reason.interface.repo import IReasonRepo
from src.domain.reason.model.reason import Reason
from src.infrastucture.database.repositories._repo import SQLAlchemyRepo


class ReasonRepo(SQLAlchemyRepo, IReasonRepo):
    async def add_reason(self, reason: Reason) -> Reason:
        self.session.add(reason)
        return reason

    async def delete_reason(self, reason_id: UUID) -> Reason:
        stmt = delete(Reason).where(Reason.id == reason_id).returning(Reason)
        r = await self.session.scalar(stmt)
        if not r:
            raise ReasonNotFound()
        return r

    async def list_reasons(self) -> list[Reason]:
        stmt = select(Reason)
        return await self.session.scalars(stmt)
