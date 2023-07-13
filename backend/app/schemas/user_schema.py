# user_schema.py
# Standard library imports
from typing import List, Optional

# Third party imports
from pydantic import BaseModel

# Local application imports
from backend.app.schemas.post_schema import Post
from backend.app.schemas.post_schema import Comment

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None

class User(UserBase):
    id: int
    posts: List[Post] = []
    comments: List[Comment] = []

    model_config = {
        'from_attributes': True
    }
