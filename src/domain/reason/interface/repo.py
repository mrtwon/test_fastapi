from typing import Protocol
from uuid import UUID

from src.domain.reason.model.reason import Reason


class IReasonRepo(Protocol):
    async def add_reason(self, reason: Reason) -> Reason:
        raise NotImplementedError

    async def delete_reason(self, reason_id: UUID) -> Reason:
        raise NotImplementedError

    async def list_reasons(self) -> list[Reason]:
        raise NotImplementedError
