from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    func,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # ============================================================
    # GITHUB
    # ============================================================

    github_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    github_username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    github_avatar_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    github_access_token: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # ============================================================
    # GOOGLE
    # ============================================================

    google_id: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )

    google_avatar_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # ============================================================
    # USER DATA
    # ============================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # ============================================================
    # RELATIONSHIPS
    # ============================================================

    developer_profile = relationship(
        "DeveloperProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    roadmaps = relationship(
        "Roadmap",
        back_populates="user",
        cascade="all, delete-orphan",
    )