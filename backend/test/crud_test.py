# crud_test.py
# Third party imports
from sqlalchemy.orm import Session

# Local application imports
from backend.app.database.crud import (
    get_user,
    create_user,
    update_user,
    delete_user,
    get_post,
    create_post,
    update_post,
    delete_post,
    get_comment,
    create_comment,
    update_comment,
    delete_comment,
)
from backend.app.schemas import user_schema as user_schemas
from backend.app.schemas import post_schema as post_schemas
from backend.app.schemas import comment_schema as comment_schemas


def test_user_crud(session: Session):
    user_create = user_schemas.UserCreate(name="Test User")
    user = create_user(session, user_create)
    assert user.name == "Test User"

    user_db = get_user(session, user.id)
    assert user_db.id == user.id

    user_update = user_schemas.UserUpdate(name="Updated Test User")
    update_user(session, user_update, user.id)
    user_db = get_user(session, user.id)
    assert user_db.name == "Updated Test User"

    delete_user(session, user.id)
    user_db = get_user(session, user.id)
    assert user_db is None


def test_post_crud(session: Session):
    # create a user first to associate the post with
    user_create = user_schemas.UserCreate(name="Test User")
    user = create_user(session, user_create)
    assert user.name == "Test User"

    post_create = post_schemas.PostCreate(
        title="Test Post", content="This is a test post.", user_id=user.id
    )
    post = create_post(session, post_create)
    assert post.title == "Test Post"

    post_db = get_post(session, post.id)
    assert post_db.id == post.id

    post_update = post_schemas.PostUpdate(
        title="Updated Test Post", content="This is an updated test post."
    )
    update_post(session, post_update, post.id)
    post_db = get_post(session, post.id)
    assert post_db.title == "Updated Test Post"

    delete_post(session, post.id)
    post_db = get_post(session, post.id)
    assert post_db is None


def test_comment_crud(session: Session):
    # create a user first to associate the post and comment with
    user_create = user_schemas.UserCreate(name="Test User")
    user = create_user(session, user_create)
    assert user.name == "Test User"

    post_create = post_schemas.PostCreate(
        title="Test Post", content="This is a test post.", user_id=user.id
    )
    post = create_post(session, post_create)
    assert post.title == "Test Post"

    comment_create = comment_schemas.CommentCreate(content="This is a test comment.", author_id=user.id)
    comment = create_comment(session, comment_create, post.id)
    assert comment.content == "This is a test comment."

    comment_db = get_comment(session, comment.id)
    assert comment_db.id == comment.id

    comment_update = comment_schemas.CommentUpdate(
        content="This is an updated test comment."
    )
    update_comment(session, comment_update, comment.id)
    comment_db = get_comment(session, comment.id)
    assert comment_db.content == "This is an updated test comment."

    delete_comment(session, comment.id)
    comment_db = get_comment(session, comment.id)
    assert comment_db is None
