from src.domain.reason.interface.uow import IReasonUOW
from src.domain.spam_user.interface.uow import ISpamUserUOW
from src.domain.spam_user_to_reason.interface.uow import ISpamUserToReasonUOW


class SpamUserBaseCase:
    def __init__(
            self,
            uow_spam_user: ISpamUserUOW,
            uow_spam_usr_to_reason: ISpamUserToReasonUOW
    ):
        self.uow_spam_user = uow_spam_user
        self.uow_spam_usr_to_reason = uow_spam_usr_to_reason
