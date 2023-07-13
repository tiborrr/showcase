# user.py
# Standard library imports
from typing import List

# Third party imports
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local application imports
from backend.app.database.database import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    posts: Mapped[List["Post"]] = relationship(
        "Post", back_populates="author", cascade="all, delete-orphan"
    )
    comments: Mapped[List["Comment"]] = relationship(
        "Comment", back_populates="author", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"