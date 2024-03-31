from sqlalchemy import Table, Column, UUID, String

from src.domain.reason.model.reason import Reason
from src.infrastucture.database.tables.base import mapper_registry

reason_table = Table(
    "reason",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True),
    Column("text", String(256), nullable=False)
)


def map_reason_table():
    mapper_registry.map_imperatively(
        Reason,
        reason_table,
        eager_defaults=True
    )
