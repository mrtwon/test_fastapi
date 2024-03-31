from typing import Protocol
from uuid import UUID

from src.domain.spam_link_to_reason.model.spam_link_to_reason import SpamLinkToReason


class ISpamLinkToReasonRepo(Protocol):
    async def add(self, schema: SpamLinkToReason) -> SpamLinkToReason:
        raise NotImplementedError

    async def delete(
            self,
            spam_link_to_reason_id: UUID | None,
            spam_link_id: UUID | None
    ) -> SpamLinkToReason:
        raise NotImplementedError
