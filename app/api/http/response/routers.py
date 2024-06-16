from fastapi import APIRouter
from api.http.response.report import router as report_router


router = APIRouter(
    prefix="/response",
    tags=["response"],
)

router.include_router(report_router)