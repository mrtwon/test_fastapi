from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.base.interface import IUoW
from src.domain.reason.interface.repo import IReasonRepo
from src.domain.reason.interface.uow import IReasonUOW
from src.domain.spam_link.interface.repo import ISpamLinkRepo
from src.domain.spam_link.interface.uow import ISpamLinkUOW
from src.domain.spam_link_to_reason.interface.repo import ISpamLinkToReasonRepo
from src.domain.spam_link_to_reason.interface.uow import ISpamLinkToReasonUOW
from src.domain.spam_user.interface.repo import ISpamUserRepo
from src.domain.spam_user.interface.uow import ISpamUserUOW
from src.domain.spam_user_to_reason.interface.repo import ISpamUserToReasonRepo
from src.domain.spam_user_to_reason.interface.uow import ISpamUserToReasonUOW


class SQLAlchemyBaseUOW(IUoW):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()


class SQLAlchemyUoW(
    SQLAlchemyBaseUOW,
    IReasonUOW,
    ISpamLinkUOW,
    ISpamUserUOW,
    ISpamLinkToReasonUOW,
    ISpamUserToReasonUOW
):
    reason: type[IReasonRepo]
    spam_user: type[ISpamUserRepo]
    spam_link: type[ISpamLinkRepo]
    spam_link_to_reason: type[ISpamLinkToReasonRepo]
    spam_user_to_reason: type[ISpamUserToReasonRepo]

    def __init__(
            self,
            session: AsyncSession,
            reason: type[IReasonRepo],
            spam_user: type[ISpamUserRepo],
            spam_link: type[ISpamLinkRepo],
            spam_link_to_reason: type[ISpamLinkToReasonRepo],
            spam_user_to_reason: type[ISpamUserToReasonRepo]
    ):
        self.reason = reason(session)
        self.spam_user = spam_user(session)
        self.spam_link = spam_link(session)
        self.spam_link_to_reason = spam_link_to_reason(session)
        self.spam_user_to_reason = spam_user_to_reason(session)
        super().__init__(session)
