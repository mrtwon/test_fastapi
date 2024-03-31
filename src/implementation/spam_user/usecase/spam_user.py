from sqlalchemy import Integer

from src.domain.spam_user.schema.spam_user import CreateSpamUserSchema, SpamUserSchema
from src.domain.spam_user.service.spam_user import SpamUserServiceABC
from src.domain.spam_user.usecase.spam_user import SpamUserUseCaseABC


class SpamUserUseCase(SpamUserUseCaseABC):

    def __init__(self, spam_user_service: SpamUserServiceABC):
        self.spam_user_service = spam_user_service

    async def add(self, schema: CreateSpamUserSchema) -> SpamUserSchema:
        return await self.spam_user_service.add(schema)

    async def delete(self, user_id: Integer) -> SpamUserSchema:
        return await self.spam_user_service.delete(user_id)

    async def get(self, user_id: Integer) -> SpamUserSchema:
        return await self.spam_user_service.get_by_id(user_id)
