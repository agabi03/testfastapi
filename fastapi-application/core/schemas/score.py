from typing import List

from pydantic import BaseModel
from pydantic import ConfigDict

from core.schemas.student import StudentRead


class ScoreBase(BaseModel):
    value: int


class ScoreCreate(ScoreBase):
    pass


class ScoreRead(ScoreBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
