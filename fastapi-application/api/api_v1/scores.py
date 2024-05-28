from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.score import (
    ScoreRead,
    ScoreCreate,
)
from crud import scores as scores_crud

router = APIRouter(tags=["Scores"])


@router.get("", response_model=list[ScoreRead])
async def get_scores(
    # session: AsyncSession = Depends(db_helper.session_getter),
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await scores_crud.get_all_scores(session=session)
    return users


@router.post("", response_model=ScoreRead)
async def create_score(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    score_create: ScoreCreate,
):
    user = await scores_crud.create_score(
        session=session,
        score_create=score_create,
    )
    return user


@router.put("/{score_id}", response_model=ScoreRead)
async def update_score(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    student_id: int,
    score_create: ScoreCreate,
):
    user = await scores_crud.update_score(
        session=session,
        score_id=student_id,
        score_create=score_create,
    )
    return user


@router.delete("/{score_id}")
async def delete_score(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    score_id: int,
):
    await scores_crud.delete_score(
        session=session,
        score_id=score_id,
    )
    return None
