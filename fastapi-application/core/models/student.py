
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Student(IntIdPkMixin, Base):
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    score_id: Mapped[int] = mapped_column(ForeignKey("scores.id"))

    scores = relationship("Score", back_populates="student")
