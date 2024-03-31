from sqlalchemy import Table, Column, UUID, ForeignKey

from src.domain.spam_user_to_reason.model.spam_user_to_reason import SpamUserToReason
from src.infrastucture.database.tables.base import mapper_registry

spam_user_to_reason = Table(
    "spam_user_to_reason",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("spam_user_id", UUID, ForeignKey("spam_user.id")),
    Column("reason_id", UUID, ForeignKey("reason.id"))
)


def map_spam_user_to_reason():
    mapper_registry.map_imperatively(
        SpamUserToReason,
        spam_user_to_reason,
        eager_defaults=True
    )
