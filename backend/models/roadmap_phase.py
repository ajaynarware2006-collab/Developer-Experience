from sqlalchemy import (
    String,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class RoadmapPhase(Base):

    __tablename__ = "roadmap_phases"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    roadmap_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roadmaps.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    project: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    phase_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    roadmap = relationship(
        "Roadmap",
        back_populates="phases"
    )

    tasks = relationship(
        "RoadmapTask",
        back_populates="phase",
        cascade="all, delete-orphan"
    )