from uuid import UUID

from sqlalchemy import delete

from src.domain.spam_link_to_reason.interface.repo import ISpamLinkToReasonRepo
from src.domain.spam_link_to_reason.model.spam_link_to_reason import SpamLinkToReason
from src.infrastucture.database.repositories._repo import SQLAlchemyRepo


class SpamLinkToReasonRepo(SQLAlchemyRepo, ISpamLinkToReasonRepo):
    async def add(self, schema: SpamLinkToReason) -> SpamLinkToReason:
        self.session.add(schema)
        await self.session.flush()
        return schema

    async def delete(
            self,
            spam_link_to_reason_id: UUID | None,
            spam_link_id: UUID | None
    ) -> SpamLinkToReason:
        stmt = delete(SpamLinkToReason)
        if spam_link_id:
            stmt = stmt.where(SpamLinkToReason.spam_link_id == spam_link_id)
        elif spam_link_to_reason_id:
            stmt = stmt.where(SpamLinkToReason.id == spam_link_to_reason_id)
        else:
            raise Exception()
        stmt = stmt.returning(SpamLinkToReason)
        scalar = await self.session.scalar(stmt)
        if not scalar:
            pass
        return scalar