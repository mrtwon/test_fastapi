from src.domain.reason.interface.uow import IReasonUOW


class ReasonBaseCase:
    def __init__(self, uow: IReasonUOW):
        self.uow = uow
