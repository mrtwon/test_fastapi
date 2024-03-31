from src.domain.base.interface import IUoW
from src.domain.reason.interface.repo import IReasonRepo


class IReasonUOW(IUoW):
    reason: IReasonRepo
