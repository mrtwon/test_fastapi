from fastapi import APIRouter
from . import spam_user
from . import spam_link
from . import reason
router = APIRouter()
router.include_router(spam_user.router, prefix='/spam_user')
router.include_router(spam_link.router, prefix='/spam_link')
router.include_router(reason.router, prefix='/reason')
