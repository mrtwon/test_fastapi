from sqlalchemy import Table, Column, UUID, ForeignKey

from src.domain.spam_link_to_reason.model.spam_link_to_reason import SpamLinkToReason
from src.infrastucture.database.tables.base import mapper_registry

spam_link_to_reason_table = Table(
    "spam_link_to_reason",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("spam_link_id", UUID, ForeignKey("spam_link.id")),
    Column("reason_id", UUID, ForeignKey("reason.id"))
)


def map_spam_link_to_reason():
    mapper_registry.map_imperatively(
        SpamLinkToReason,
        spam_link_to_reason_table,
        eager_defaults=True
    )
