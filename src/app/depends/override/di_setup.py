from typing import TYPE_CHECKING, Protocol
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.domain.base.interface import IUoW
from src.infrastucture.database.repositories.reason.reason import ReasonRepo
from src.infrastucture.database.repositories.spam_link.spam_link import SpamLinkRepo
from src.infrastucture.database.repositories.spam_link_to_reason.spam_link_to_reason import SpamLinkToReasonRepo
from src.infrastucture.database.repositories.spam_user.spam_user import SpamUserRepo
from src.infrastucture.database.repositories.spam_user_to_reason.spam_user_to_reason import SpamUserToReasonRepo
from src.infrastucture.database.uow import SQLAlchemyUoW

from sqlalchemy.ext.asyncio import async_sessionmaker


class Session(Protocol):
    pass


async def get_session() -> AsyncSession:
    print('start get_session()')
    async_engine = create_async_engine(
        url="postgresql+asyncpg://mrtwon:12345678@localhost:5432/test_fastapi"
    )
    session = async_sessionmaker(async_engine)
    async with session() as s:
        return s


def get_uow(session: Session = Depends()):
    return SQLAlchemyUoW(
        session=session,
        reason=ReasonRepo,
        spam_user=SpamUserRepo,
        spam_link=SpamLinkRepo,
        spam_link_to_reason=SpamLinkToReasonRepo,
        spam_user_to_reason=SpamUserToReasonRepo
    )


def di_setup(app: FastAPI):
    app.dependency_overrides[Session] = get_session
    app.dependency_overrides[IUoW] = get_uow
