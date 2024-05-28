from pydantic import BaseModel
from pydantic import ConfigDict


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    score_id: int


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
