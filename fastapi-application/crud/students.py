from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import Student
from core.schemas.student import StudentCreate


async def get_all_students(
    session: AsyncSession,
) -> Sequence[Student]:
    stmt = select(Student).options(joinedload(Student.scores)).order_by(Student.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_student(
    session: AsyncSession,
    student_create: StudentCreate,
) -> Student:
    student = Student(**student_create.model_dump())
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student


async def update_student(
        session: AsyncSession,
        student_id: int,
        student_create: StudentCreate,
):
    student = await session.get(Student, student_id)
    if not student:
        return None
    for key, value in student_create.dict().items():
        setattr(student, key, value)
    await session.commit()
    await session.refresh(student)
    return student


async def delete_student(
    session: AsyncSession,
    student_id: int,
):
    student = await session.get(Student, student_id)
    await session.delete(student)
    await session.commit()
    return student
