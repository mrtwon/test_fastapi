from typing import Annotated

from fastapi import APIRouter, Depends

from src.app.exception.exception import NotFoundException
from src.domain.spam_link.exception.spam_link import SpamLinkNotFound
from src.domain.spam_link.usecase.spam_link import SpamLinkUseCaseABC

router = APIRouter()


@router.get('/check')
async def check_link(
        link: str,
        spam_user_use_case: Annotated[SpamLinkUseCaseABC, Depends()]
):
    try:
        r = await spam_user_use_case.get(link)
        return r
    except SpamLinkNotFound:
        raise NotFoundException('link was not found in spam database')
