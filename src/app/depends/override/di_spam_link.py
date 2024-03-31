from fastapi import FastAPI, Depends

from src.domain.base.interface import IUoW
from src.domain.spam_link.service.spam_link import SpamLinkServiceABC
from src.domain.spam_link.usecase.spam_link import SpamLinkUseCaseABC
from src.implementation.spam_link.service.spam_link import SpamLinkService
from src.implementation.spam_link.usecase.spam_link import SpamLinkUseCase


def get_use_case(service: SpamLinkServiceABC = Depends()):
    return SpamLinkUseCase(service)


def get_service(uow: IUoW = Depends()):
    return SpamLinkService(uow, uow)


def di_span_link(app: FastAPI):
    app.dependency_overrides[SpamLinkServiceABC] = get_service
    app.dependency_overrides[SpamLinkUseCaseABC] = get_use_case
