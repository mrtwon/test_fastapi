from uuid import UUID

from src.domain.base.models import entity, IdentifiableModel


@entity
class SpamUserToReason(IdentifiableModel):
    spam_user_id: UUID
    reason_id: UUID

    @staticmethod
    def create(spam_user_id: UUID, reason_id: UUID) -> "SpamUserToReason":
        return SpamUserToReason(
            spam_user_id=spam_user_id,
            reason_id=reason_id
        )
