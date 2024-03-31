from uuid import UUID

from sqlalchemy import delete

from src.domain.spam_user_to_reason.interface.repo import ISpamUserToReasonRepo
from src.domain.spam_user_to_reason.model.spam_user_to_reason import SpamUserToReason
from src.infrastucture.database.repositories._repo import SQLAlchemyRepo


class SpamUserToReasonRepo(SQLAlchemyRepo, ISpamUserToReasonRepo):
    async def add(self, schema: SpamUserToReason) -> SpamUserToReason:
        self.session.add(schema)
        await self.session.flush()
        return schema

    async def delete(
            self,
            spam_user_to_reason_id: UUID | None,
            spam_user_id: UUID | None
    ) -> SpamUserToReason:
        stmt = delete(SpamUserToReason)
        if spam_user_to_reason_id:
            stmt = stmt.where(SpamUserToReason.id == spam_user_to_reason_id)
        elif spam_user_id:
            stmt = stmt.where(SpamUserToReason.spam_user_id == spam_user_id)
        else:
            raise Exception()
        stmt.returning(SpamUserToReason)
        scalar = await self.session.scalar(stmt)
        if not scalar:
            pass
        return scalar
