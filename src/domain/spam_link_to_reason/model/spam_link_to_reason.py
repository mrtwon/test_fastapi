from uuid import UUID

from src.domain.base.models import entity, IdentifiableModel


@entity
class SpamLinkToReason(IdentifiableModel):
    spam_link_id: UUID
    reason_id: UUID

    @staticmethod
    def create(spam_link_id: UUID, reason_id: UUID) -> "SpamLinkToReason":
        return SpamLinkToReason(
            spam_link_id=spam_link_id,
            reason_id=reason_id
        )
