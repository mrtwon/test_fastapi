from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.domain.reason.schema.reason import CreateReasonSchema
from src.implementation.reason.usecase.reason import ReasonUseCase

router = APIRouter()


@router.post('')
async def add_reason(
        create_schema: CreateReasonSchema,
        reason_use_case: Annotated[ReasonUseCase, Depends()]
):
    r = await reason_use_case.add(create_schema)
    return r


@router.delete('/{reason_id}')
async def delete_reason(
        reason_id: UUID,
        reason_use_case: Annotated[ReasonUseCase, Depends()]
):
    r = await reason_use_case.delete(reason_id)
    return r
