from typing import Protocol
from uuid import UUID

from src.domain.spam_link.model.spam_link import SpamLink


class ISpamLinkRepo(Protocol):
    async def add(self, spam_link: SpamLink) -> SpamLink:
        raise NotImplementedError

    async def delete(self, spam_link_id: UUID) -> None:
        raise NotImplementedError

    async def get_by_id(self, spam_link: str) -> SpamLink:
        raise NotImplementedError