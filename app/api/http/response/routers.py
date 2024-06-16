from api.http.response.report import router as report_router
from fastapi import APIRouter

router = APIRouter(
    prefix="/response",
    tags=["response"],
)

router.include_router(report_router)
