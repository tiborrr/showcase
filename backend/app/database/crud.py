# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from backend.app.models import user as user_models
from backend.app.models import post as post_models
from backend.app.models import comment as comment_models

from backend.app.schemas import user_schema as user_schemas
from backend.app.schemas import post_schema as post_schemas
from backend.app.schemas import comment_schema as comment_schemas

# Create methods

def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_post(db: Session, post: post_schemas.PostCreate):
    db_post = post_models.Post(title=post.title, content=post.content, author_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def create_comment(db: Session, comment: comment_schemas.CommentCreate, post_id: int):
    db_comment = comment_models.Comment(author_id=comment.author_id, content=comment.content, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# Update methods

def update_user(db: Session, user: user_schemas.UserUpdate, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user is None:
        return None
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_post(db: Session, post: post_schemas.PostUpdate, post_id: int):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if db_post is None:
        return None
    for var, value in vars(post).items():
        setattr(db_post, var, value) if value else None
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_comment(db: Session, comment: comment_schemas.CommentUpdate, comment_id: int):
    db_comment = db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()
    if db_comment is None:
        return None
    for var, value in vars(comment).items():
        setattr(db_comment, var, value) if value else None
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# Read methods

def get_user(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_models.User).order_by(user_models.User.id.asc()).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int):
    return db.query(post_models.Post).filter(post_models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(post_models.Post).order_by(post_models.Post.id.asc()).offset(skip).limit(limit).all()


def get_comment(db: Session, comment_id: int):
    return db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()


def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(comment_models.Comment).order_by(comment_models.Comment.id.asc()).offset(skip).limit(limit).all()

# Delete method

def delete_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return user_id

def delete_post(db: Session, post_id: int):
    db_post = db.query(post_models.Post).filter(post_models.Post.id == post_id).first()
    if db_post is None:
        return None
    db.delete(db_post)
    db.commit()
    return post_id

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()
    if db_comment is None:
        return None
    db.delete(db_comment)
    db.commit()
    return comment_id