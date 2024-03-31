from src.domain.spam_link.interface.uow import ISpamLinkUOW
from src.domain.spam_link_to_reason.interface.uow import ISpamLinkToReasonUOW


class SpamLinkBaseCase:
    def __init__(
            self,
            uow_spam_link_to_reason: ISpamLinkToReasonUOW,
            uow_spam_link: ISpamLinkUOW
    ):
        self.uow_spam_link_to_reason = uow_spam_link_to_reason
        self.uow_spam_link = uow_spam_link
