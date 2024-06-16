from fastapi import APIRouter
from api.http.response.routers import router as response_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(response_router)
