from src.domain.base.models import entity, IdentifiableModel


@entity
class Reason(IdentifiableModel):
    text: str

    @staticmethod
    def create(
            text: str
    ) -> "Reason":
        return Reason(text=text)
