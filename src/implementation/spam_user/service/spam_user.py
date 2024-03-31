from sqlalchemy import Integer

from src.domain.reason.interface.uow import IReasonUOW
from src.domain.spam_user.exception.spam_user import SpamUserAlreadyExist, UserIdNotFoundOnSpamUser
from src.domain.spam_user.interface.uow import ISpamUserUOW
from src.domain.spam_user.model.spam_user import SpamUser
from src.domain.spam_user.schema.spam_user import CreateSpamUserSchema, SpamUserSchema
from src.domain.spam_user.service.spam_user import SpamUserServiceABC
from src.domain.spam_user_to_reason.interface.uow import ISpamUserToReasonUOW
from src.domain.spam_user_to_reason.model.spam_user_to_reason import SpamUserToReason
from src.implementation.spam_user.service.base import SpamUserBaseCase


class AddSpamUser(SpamUserBaseCase):
    async def __call__(self, schema: CreateSpamUserSchema):
        try:
            await self.uow_spam_user.spam_user.get_by_id(schema.user_id)
            raise SpamUserAlreadyExist()
        except UserIdNotFoundOnSpamUser:
            pass

        add_spam_user = await self.uow_spam_user.spam_user.add(
            SpamUser.create(schema.user_id)
        )
        for one_reason in schema.reasons_id:
            create_model = SpamUserToReason.create(
                spam_user_id=add_spam_user.id,
                reason_id=one_reason
            )
            await self.uow_spam_usr_to_reason.spam_link_to_reason.add(create_model)
        to_schema = SpamUserSchema.model_validate(add_spam_user)
        await self.uow_spam_user.commit()
        return to_schema


class DeleteSpamUser(SpamUserBaseCase):
    async def __call__(self, *args, **kwargs):
        pass


class GetSpamUser(SpamUserBaseCase):
    async def __call__(self, user_id: int):
        r = await self.uow_spam_user.spam_user.get_by_id(user_id)
        return SpamUserSchema.model_validate(r)


class SpamUserService(SpamUserServiceABC):

    def __init__(
            self,
            uow_spam_user: ISpamUserUOW,
            uow_spam_usr_to_reason: ISpamUserToReasonUOW
    ):
        self.uow_spam_user = uow_spam_user
        self.uow_spam_usr_to_reason = uow_spam_usr_to_reason

    async def add(self, schema: CreateSpamUserSchema) -> SpamUserSchema:
        return await AddSpamUser(self.uow_spam_user, self.uow_spam_usr_to_reason)(schema)

    async def delete(self, user_id: int) -> SpamUserSchema:
        raise NotImplementedError

    async def get_by_id(self, user_id: int) -> SpamUserSchema:
        return await GetSpamUser(self.uow_spam_user, self.uow_spam_usr_to_reason)(user_id)
