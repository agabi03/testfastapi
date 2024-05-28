from fastapi import APIRouter

from core.config import settings

from .students import router as students_router
from .scores import router as scores_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    students_router,
    prefix=settings.api.v1.users,
)
router.include_router(
    scores_router,
    prefix=settings.api.v1.scores,
)


