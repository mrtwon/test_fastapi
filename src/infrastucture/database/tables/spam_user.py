from sqlalchemy import Table, Integer, Column, TIMESTAMP, func, UUID

from src.domain.spam_user.model.spam_user import SpamUser
from src.infrastucture.database.tables.base import mapper_registry

spam_user = Table(
    "spam_user",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("user_id", Integer),
    Column("created_at", TIMESTAMP, server_default=func.current_timestamp())
)


def map_spam_user_table():
    mapper_registry.map_imperatively(
        SpamUser,
        spam_user,
        eager_defaults=True
    )
