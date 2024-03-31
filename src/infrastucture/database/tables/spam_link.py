from sqlalchemy import Table, Column, UUID, String, TIMESTAMP, func

from src.domain.spam_link.model.spam_link import SpamLink
from src.infrastucture.database.tables.base import mapper_registry

spam_link_table = Table(
    "spam_link",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("link", String(), nullable=False),
    Column("created_at", TIMESTAMP, server_default=func.current_timestamp())
)


def map_spam_link_table():
    mapper_registry.map_imperatively(
        SpamLink,
        spam_link_table,
        eager_defaults=True
    )
