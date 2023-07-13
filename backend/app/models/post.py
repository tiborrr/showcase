# post.py
# Standard library imports
from typing import List

# Third party imports
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local application imports
from backend.app.database.database import Base

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(500))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r})"