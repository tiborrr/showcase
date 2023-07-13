# comment_schema.py
# Standard library imports
from typing import List, Optional

# Third party imports
from pydantic import BaseModel

class CommentBase(BaseModel):
    author_id: int
    content: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: Optional[str] = None

class Comment(CommentBase):
    id: int
    post_id: int

    model_config = {
        'from_attributes': True
    }
