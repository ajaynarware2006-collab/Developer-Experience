from sqlalchemy import (
    String,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class ProfileSkill(Base):

    __tablename__ = "profile_skills"

    __table_args__ = (
        UniqueConstraint(
            "profile_id",
            "skill"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    profile_id: Mapped[int] = mapped_column(
        ForeignKey(
            "developer_profiles.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    skill: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    profile = relationship(
        "DeveloperProfile",
        back_populates="skills"
    )