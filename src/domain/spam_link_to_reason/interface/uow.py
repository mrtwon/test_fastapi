from src.domain.base.interface import IUoW
from src.domain.spam_link_to_reason.interface.repo import ISpamLinkToReasonRepo


class ISpamLinkToReasonUOW(IUoW):
    spam_link_to_reason: ISpamLinkToReasonRepo
