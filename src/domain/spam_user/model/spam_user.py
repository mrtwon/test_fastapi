from uuid import UUID

from sqlalchemy import Integer

from src.domain.base.models import entity, TimestampedModel, IdentifiableModel


@entity
class SpamUser(IdentifiableModel, TimestampedModel):
    user_id: Integer

    @staticmethod
    def create(user_id: Integer) -> "SpamUser":
        return SpamUser(
            user_id=user_id
        )
