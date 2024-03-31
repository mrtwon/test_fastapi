from src.domain.base.models import entity, TimestampedModel, IdentifiableModel


@entity
class SpamLink(IdentifiableModel, TimestampedModel):
    link: str

    @staticmethod
    def create(link: str) -> "SpamLink":
        return SpamLink(link=link)
