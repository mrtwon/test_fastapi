from abc import ABC

from sqlalchemy import Integer

from src.domain.spam_user.schema.spam_user import CreateSpamUserSchema, SpamUserSchema


class SpamUserUseCaseABC(ABC):
    async def add(self, schem: CreateSpamUserSchema) -> SpamUserSchema:
        raise NotImplementedError

    async def delete(self, user_id: int) -> SpamUserSchema:
        raise NotImplementedError

    async def get(self, user_id: int) -> SpamUserSchema:
        raise NotImplementedError
