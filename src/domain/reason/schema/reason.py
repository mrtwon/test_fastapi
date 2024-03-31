from src.domain.base.schemas import IdentifiableSchema, BaseSchema


class ReasonSchema(IdentifiableSchema):
    text: str


class CreateReasonSchema(BaseSchema):
    text: str
