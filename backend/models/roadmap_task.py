from sqlalchemy import (
    String,
    Integer,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class RoadmapTask(Base):

    __tablename__ = "roadmap_tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    phase_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roadmap_phases.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    task_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    phase = relationship(
        "RoadmapPhase",
        back_populates="tasks"
    )