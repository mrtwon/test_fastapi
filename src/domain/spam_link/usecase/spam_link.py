from abc import ABC

from src.domain.spam_link.schema.spam_link import CreateSpamLinkSchema, SpamLinkSchema


class SpamLinkUseCaseABC(ABC):
    async def add(self, schema: CreateSpamLinkSchema) -> SpamLinkSchema:
        raise NotImplementedError

    async def delete(self, spam_link: str) -> SpamLinkSchema:
        raise NotImplementedError

    async def get(self, spam_link: str) -> SpamLinkSchema:
        raise NotImplementedError