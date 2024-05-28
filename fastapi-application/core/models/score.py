from sqlalchemy import CheckConstraint, Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Score(IntIdPkMixin, Base):
    value: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('value >= 1', name='check_value_min'),
        CheckConstraint('value <= 5', name='check_value_max'),
    )

    student = relationship("Student", back_populates="scores")
