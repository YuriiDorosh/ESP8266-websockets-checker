import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.report import ResponseCreateInSchema
from repositories.response_repository import ResponseRepository
from dependencies.db import get_async_session


router = APIRouter(
    prefix="/report",
    tags=["report"],
)


@router.post("/", response_model=ResponseCreateInSchema)
async def create_report(
    signal_strength: int,
    mac_address: str | None,
    db: AsyncSession = Depends(get_async_session),
):

    response_repository = ResponseRepository(db)

    try:
        response_repository.create_response(
            signal_strength=signal_strength, mac_address=mac_address
        )
        return {"status": "success", "detail": "Response created successfully."}

    except HTTPException as e:
        logging.error(f"Error creating response: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred during response creation",
        )
