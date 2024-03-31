from src.domain.base.interface import IUoW
from src.domain.spam_user.interface.repo import ISpamUserRepo


class ISpamUserUOW(IUoW):
    spam_user: ISpamUserRepo