from typing import Annotated

from fastapi import APIRouter, Depends

from src.app.exception.exception import NotFoundException
from src.domain.spam_user.exception.spam_user import UserIdNotFoundOnSpamUser
from src.domain.spam_user.usecase.spam_user import SpamUserUseCaseABC

router = APIRouter()


@router.get('/check')
async def check_user(
        user_id: int,
        spam_user_use_case: Annotated[SpamUserUseCaseABC, Depends()]
):
    try:
        r = await spam_user_use_case.get(user_id)
        return r
    except UserIdNotFoundOnSpamUser:
        raise NotFoundException(msg="user was not found in spam database")
