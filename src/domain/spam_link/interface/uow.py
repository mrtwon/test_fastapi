from src.domain.base.interface import IUoW
from src.domain.spam_link.interface.repo import ISpamLinkRepo


class ISpamLinkUOW(IUoW):
    spam_link: ISpamLinkRepo
