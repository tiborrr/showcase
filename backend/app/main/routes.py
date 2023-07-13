# Standard library imports
from typing import List

# Third party imports
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Local application imports
from backend.app.database.database import Sessionmaker
from backend.app.database import crud
from backend.app.schemas import (
    comment_schema,
    post_schema,
    user_schema,
)
from backend.app.config import FRONTEND_URL

app = FastAPI(
    title="Show case",
    description="Skill showcase for future jobs"
)

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Dependency to get a database session
def get_db() -> Session:
    db = Sessionmaker()
    try:
        yield db
    finally:
        db.close()

# User endpoints

@app.get("/users", response_model=List[user_schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=user_schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db=db, user=user)
    return user

@app.put("/users/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, updated_user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db=db, user=updated_user, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Post endpoints

@app.post("/posts", response_model=post_schema.Post)
def create_user_post(post: post_schema.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts", response_model=List[post_schema.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db=db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=post_schema.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db=db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=post_schema.Post)
def update_post_data(post_id: int, post: post_schema.PostUpdate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db=db, post=post, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}")
def remove_post(post_id: int, db: Session = Depends(get_db)):
    post_id = crud.delete_post(db=db, post_id=post_id)
    if post_id is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

@app.post("/posts/{post_id}/comments", response_model=comment_schema.Comment)
def create_post_comment(post_id: int, comment: comment_schema.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment, post_id=post_id)

# Comment endpoints

@app.get("/comments", response_model=List[comment_schema.Comment])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments(db=db, skip=skip, limit=limit)
    return comments

@app.get("/comments/{comment_id}", response_model=comment_schema.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.get_comment(db=db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@app.put("/comments/{comment_id}", response_model=comment_schema.Comment)
def update_comment_data(comment_id: int, comment: comment_schema.CommentUpdate, db: Session = Depends(get_db)):
    db_comment = crud.update_comment(db=db, comment=comment, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@app.delete("/comments/{comment_id}")
def remove_comment(comment_id: int, db: Session = Depends(get_db)):
    comment_id = crud.delete_comment(db=db, comment_id=comment_id)
    if comment_id is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}