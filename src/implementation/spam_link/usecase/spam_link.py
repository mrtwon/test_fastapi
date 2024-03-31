from src.domain.spam_link.schema.spam_link import CreateSpamLinkSchema, SpamLinkSchema
from src.domain.spam_link.service.spam_link import SpamLinkServiceABC
from src.domain.spam_link.usecase.spam_link import SpamLinkUseCaseABC


class SpamLinkUseCase(SpamLinkUseCaseABC):

    def __init__(self, service_spam_link: SpamLinkServiceABC):
        self.service_spam_link = service_spam_link

    async def add(self, schema: CreateSpamLinkSchema) -> SpamLinkSchema:
        return await self.service_spam_link.add(schema)

    async def delete(self, spam_link: str) -> SpamLinkSchema:
        return await self.service_spam_link.delete(spam_link)

    async def get(self, spam_link: str) -> SpamLinkSchema:
        return await self.service_spam_link.get(spam_link)
