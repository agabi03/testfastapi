from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.student import (
    StudentRead,
    StudentCreate,
)
from crud import students as students_crud

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[StudentRead])
async def get_students(
    # session: AsyncSession = Depends(db_helper.session_getter),
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    users = await students_crud.get_all_students(session=session)
    return users


@router.post("", response_model=StudentRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    student_create: StudentCreate,
):
    user = await students_crud.create_student(
        session=session,
        student_create=student_create,
    )
    return user


@router.put("/{student_id}", response_model=StudentRead)
async def update_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    student_id: int,
    student_create: StudentCreate,
):
    user = await students_crud.update_student(
        session=session,
        student_id=student_id,
        student_create=student_create,
    )
    return user


@router.delete("/{student_id}")
async def delete_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    student_id: int,
):
    await students_crud.delete_student(
        session=session,
        student_id=student_id,
    )
    return None
