from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.base import Base


class DeveloperProfile(Base):

    __tablename__ = "developer_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        unique=True,
        nullable=False
    )

    career_goal: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    experience_level: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    experience: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    target: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    timeline: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    daily_time: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="developer_profile"
    )

    skills = relationship(
        "ProfileSkill",
        back_populates="profile",
        cascade="all, delete-orphan"
    )