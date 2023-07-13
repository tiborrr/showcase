# post_schema.py
# Standard library imports
from typing import List, Optional

# Third party imports
from pydantic import BaseModel

# Local application imports
from backend.app.schemas.comment_schema import Comment

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class Post(PostBase):
    id: int
    author_id: int
    comments: List[Comment] = []

    model_config = {
        'from_attributes': True
    }
