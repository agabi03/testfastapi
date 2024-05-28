from typing import Sequence, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import Score
from core.schemas.score import ScoreCreate


async def get_all_scores(session: AsyncSession) -> Sequence[Score]:
    stmt = select(Score).options(joinedload(Score.student)).order_by(Score.id)
    result = await session.execute(stmt)
    scores = result.unique().scalars().all()
    return scores


async def create_score(
    session: AsyncSession,
    score_create: ScoreCreate,
) -> Score:
    score = Score(**score_create.model_dump())
    session.add(score)
    await session.commit()
    await session.refresh(score)
    return score


async def update_score(
        session: AsyncSession,
        score_id: int,
        score_create: ScoreCreate,
):
    score = await session.get(Score, score_id)
    if not score:
        return None
    for key, value in score_create.dict().items():
        setattr(score, key, value)
    await session.commit()
    await session.refresh(score)
    return score


async def delete_score(
    session: AsyncSession,
    score_id: int,
):
    score = await session.get(Score, score_id)
    await session.delete(score)
    await session.commit()
    return score
