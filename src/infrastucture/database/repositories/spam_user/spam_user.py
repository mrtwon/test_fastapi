from uuid import UUID

from sqlalchemy import delete, Integer, select

from src.domain.spam_user.exception.spam_user import IdSpamUserNotFound, UserIdNotFoundOnSpamUser
from src.domain.spam_user.interface.repo import ISpamUserRepo
from src.domain.spam_user.model.spam_user import SpamUser
from src.infrastucture.database.repositories._repo import SQLAlchemyRepo


class SpamUserRepo(SQLAlchemyRepo, ISpamUserRepo):
    async def add(self, spam_user: SpamUser) -> SpamUser:
        self.session.add(spam_user)
        await self.session.flush()
        return spam_user

    async def delete(self, spam_user_id: UUID) -> None:
        stmt = delete(SpamUser).where(SpamUser.user_id == spam_user_id).returning(SpamUser)
        r = await self.session.scalar(stmt)
        if not r:
            raise IdSpamUserNotFound()
        return r

    async def get_by_id(self, user_id: int) -> SpamUser:
        stmt = select(SpamUser).where(SpamUser.user_id == user_id)
        scalar = await self.session.scalar(stmt)
        if not scalar:
            raise UserIdNotFoundOnSpamUser()
        return scalar
