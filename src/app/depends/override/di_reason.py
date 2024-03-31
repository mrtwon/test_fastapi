from fastapi import FastAPI, Depends

from src.domain.base.interface import IUoW
from src.domain.reason.service.reason import ReasonServiceABC
from src.domain.reason.usecase.reason import ReasonUseCaseABC
from src.implementation.reason.service.reason import ReasonService
from src.implementation.reason.usecase.reason import ReasonUseCase


def get_use_case(service: ReasonServiceABC = Depends()):
    return ReasonUseCase(service)


def get_service(uow: IUoW = Depends()):
    return ReasonService(uow)


def di_reason(app: FastAPI):
    app.dependency_overrides[ReasonServiceABC] = get_service
    app.dependency_overrides[ReasonUseCaseABC] = get_use_case
