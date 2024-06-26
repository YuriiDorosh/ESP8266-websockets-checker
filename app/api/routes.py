from api.http.response.routers import router as response_router
from fastapi import APIRouter

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

router.include_router(response_router)
