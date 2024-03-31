from uuid import UUID

from sqlalchemy import delete, select

from src.domain.spam_link.exception.spam_link import IdSpamLinkNotFound, SpamLinkNotFound
from src.domain.spam_link.interface.repo import ISpamLinkRepo
from src.domain.spam_link.model.spam_link import SpamLink
from src.infrastucture.database.repositories._repo import SQLAlchemyRepo


class SpamLinkRepo(SQLAlchemyRepo, ISpamLinkRepo):
    async def add(self, spam_link: SpamLink) -> SpamLink:
        self.session.add(spam_link)
        return spam_link

    async def delete(self, spam_link_id: UUID) -> None:
        stmt = delete(SpamLink).where(SpamLink.id == spam_link_id).returning(SpamLink)
        r = await self.session.scalar(stmt)
        if not r:
            raise IdSpamLinkNotFound()
        return r

    async def get_by_id(self, spam_link: str) -> SpamLink:
        stmt = select(SpamLink).where(SpamLink.link == spam_link)
        scalar = await self.session.scalar(stmt)
        if not scalar:
            raise SpamLinkNotFound()
        return scalar