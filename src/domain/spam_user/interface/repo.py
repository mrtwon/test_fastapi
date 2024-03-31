from typing import Protocol
from uuid import UUID

from sqlalchemy import Integer

from src.domain.spam_user.model.spam_user import SpamUser


class ISpamUserRepo(Protocol):
    async def add(self, spam_user: SpamUser) -> SpamUser:
        raise NotImplementedError

    async def delete(self, spam_user_id: UUID) -> None:
        raise NotImplementedError

    async def get_by_id(self, user_id: int) -> SpamUser:
        raise NotImplementedError
