from fastapi import FastAPI, Depends
from src.domain.base.interface import IUoW
from src.domain.spam_user.service.spam_user import SpamUserServiceABC
from src.domain.spam_user.usecase.spam_user import SpamUserUseCaseABC
from src.implementation.spam_user.service.spam_user import SpamUserService
from src.implementation.spam_user.usecase.spam_user import SpamUserUseCase


def get_use_case(service: SpamUserServiceABC = Depends()):
    return SpamUserUseCase(service)


def get_service(uow: IUoW = Depends()):
    return SpamUserService(uow, uow)


def di_span_user(app: FastAPI):
    app.dependency_overrides[SpamUserServiceABC] = get_service
    app.dependency_overrides[SpamUserUseCaseABC] = get_use_case