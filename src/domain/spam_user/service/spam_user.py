from abc import ABC

from sqlalchemy import Integer

from src.domain.spam_user.schema.spam_user import CreateSpamUserSchema, SpamUserSchema


class SpamUserServiceABC(ABC):
    async def add(self, schema: CreateSpamUserSchema) -> SpamUserSchema:
        raise NotImplementedError

    async def delete(self, user_id: Integer) -> SpamUserSchema:
        raise NotImplementedError

    async def get_by_id(self, user_id: Integer) -> SpamUserSchema:
        raise NotImplementedError
