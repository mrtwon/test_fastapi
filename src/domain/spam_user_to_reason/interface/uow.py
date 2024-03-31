from src.domain.base.interface import IUoW
from src.domain.spam_user_to_reason.interface.repo import ISpamUserToReasonRepo


class ISpamUserToReasonUOW(IUoW):
    spam_link_to_reason: ISpamUserToReasonRepo