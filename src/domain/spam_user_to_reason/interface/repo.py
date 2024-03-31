from typing import Protocol
from uuid import UUID

from src.domain.spam_user_to_reason.model.spam_user_to_reason import SpamUserToReason


class ISpamUserToReasonRepo(Protocol):
    async def add(self, schema: SpamUserToReason) -> SpamUserToReason:
        raise NotImplementedError

    async def delete(
            self,
            spam_user_to_reason_id: UUID | None,
            spam_user_id: UUID | None
    ) -> SpamUserToReason:
        raise NotImplementedError
