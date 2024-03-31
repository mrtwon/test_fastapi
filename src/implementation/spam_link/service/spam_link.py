from src.domain.spam_link.exception.spam_link import SpamLinkNotFound
from src.domain.spam_link.interface.uow import ISpamLinkUOW
from src.domain.spam_link.model.spam_link import SpamLink
from src.domain.spam_link.schema.spam_link import CreateSpamLinkSchema, SpamLinkSchema
from src.domain.spam_link.service.spam_link import SpamLinkServiceABC
from src.domain.spam_link_to_reason.interface.uow import ISpamLinkToReasonUOW
from src.domain.spam_link_to_reason.model.spam_link_to_reason import SpamLinkToReason
from src.implementation.spam_link.service.base import SpamLinkBaseCase


class AddSpamLink(SpamLinkBaseCase):
    async def __call__(self, schema: CreateSpamLinkSchema):
        try:
            await self.uow_spam_link.spam_link.get_by_id(schema.link)
            raise Exception()
        except SpamLinkNotFound:
            pass
        added_spam_link = await self.uow_spam_link.spam_link.add(
            SpamLink.create(schema.link)
        )
        for one_reason in schema.reasons_id:
            await self.uow_spam_link_to_reason.spam_link_to_reason.add(
                SpamLinkToReason.create(
                    spam_link_id=added_spam_link.id,
                    reason_id=one_reason
                )
            )
        to_schema = SpamLinkSchema.model_validate(added_spam_link)
        await self.uow_spam_link.commit()
        return to_schema


class DeleteSpamLink(SpamLinkBaseCase):
    def __call__(self, *args, **kwargs):
        pass


class GetSpamLink(SpamLinkBaseCase):
    async def __call__(self, spam_link: str):
        r = self.uow_spam_link.spam_link.get_by_id(spam_link)
        return SpamLinkSchema.model_validate(r)


class SpamLinkService(SpamLinkServiceABC):
    def __init__(
            self,
            uow_spam_link_to_reason: ISpamLinkToReasonUOW,
            uow_spam_link: ISpamLinkUOW
    ):
        self.uow_spam_link_to_reason = uow_spam_link_to_reason
        self.uow_spam_link = uow_spam_link

    async def add(self, schema: CreateSpamLinkSchema) -> SpamLinkSchema:
        return await AddSpamLink(self.uow_spam_link_to_reason, self.uow_spam_link)(schema)

    async def delete(self, spam_link: str) -> SpamLinkSchema:
        raise NotImplementedError

    async def get(self, spam_link: str) -> SpamLinkSchema:
        return await GetSpamLink(self.uow_spam_link_to_reason, self.uow_spam_link)(spam_link)
