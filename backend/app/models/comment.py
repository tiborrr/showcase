# comment.py
# Third party imports
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local application imports
from backend.app.database.database import Base

class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship("Post", back_populates="comments")

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, text={self.content!r})"