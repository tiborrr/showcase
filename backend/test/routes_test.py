# routes_test.py
# Third party imports
from fastapi.testclient import TestClient

# Local application imports
from backend.app.main.routes import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test User"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test User"
    assert data["id"] == user_id

def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()

    # Check some user in the list
    assert len(data) > 0
    for item in data:
        assert "name" in item
        assert "id" in item

def test_update_user():
    # Create a user to be updated
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]

    # Update the created user
    response = client.put(
        f"/users/{user_id}",
        json={"name": "Updated Test User"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Updated Test User"
    assert data["id"] == user_id

def test_delete_user():
    # Create a user to be deleted
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    user_id = data["id"]

    # Delete the created user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "User deleted successfully"

    # Verify the user has been deleted
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404, response.text

# Posts endpoints tests

def test_create_post():
    # First, we need a user to associate the post with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "This is a test post."
    assert "id" in data
    post_id = data["id"]

    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "This is a test post."
    assert data["id"] == post_id

def test_read_posts():
    response = client.get("/posts")
    assert response.status_code == 200, response.text
    data = response.json()

    # Check some post in the list
    assert len(data) > 0
    for item in data:
        assert "title" in item
        assert "content" in item
        assert "id" in item

def test_update_post():
    # Create a user to associate the post with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    # create a post to be updated
    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    post_data = response.json()

    # Update the created post
    response = client.put(
        f"/posts/{post_data['id']}",
        json={"title": "Updated Test Post", "content": "This is an updated test post."},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "Updated Test Post"
    assert data["content"] == "This is an updated test post."
    assert data["id"] == post_data["id"]

def test_delete_post():
    # Create a user to associate the post with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    # Create a post to be deleted
    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    post_data = response.json()

    # Delete the created post
    response = client.delete(f"/posts/{post_data['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Post deleted successfully"

    # Verify the post has been deleted
    response = client.get(f"/posts/{post_data['id']}")
    assert response.status_code == 404, response.text

# Comments endpoints tests

def test_create_comment():
    # First, we need a user to associate the post and the comment with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    # Then we need a post to associate the comment with
    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    post_data = response.json()

    response = client.post(
        f"/posts/{post_data['id']}/comments",
        json={"content": "This is a test comment.", "author_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == "This is a test comment."
    assert "id" in data
    comment_id = data["id"]

    response = client.get(f"/comments/{comment_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == "This is a test comment."
    assert data["id"] == comment_id

def test_read_comments():
    response = client.get("/comments")
    assert response.status_code == 200, response.text
    data = response.json()

    # Check some comment in the list
    assert len(data) > 0
    for item in data:
        assert "content" in item
        assert "id" in item

def test_update_comment():
    # Create a user to associate the post and the comment with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    # Then we need a post to associate the comment with
    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    post_data = response.json()

    # Create a comment to be updated
    response = client.post(
        f"/posts/{post_data['id']}/comments",
        json={"content": "This is a test comment.", "author_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    comment_data = response.json()

    # Update the created comment
    response = client.put(
        f"/comments/{comment_data['id']}",
        json={"content": "This is an updated test comment."},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == "This is an updated test comment."
    assert data["id"] == comment_data["id"]

def test_delete_comment():
    # Create a user to associate the post and the comment with
    response = client.post(
        "/users",
        json={"name": "Test User"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()

    # Then we need a post to associate the comment with
    response = client.post(
        "/posts",
        json={"title": "Test Post", "content": "This is a test post.", "user_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    post_data = response.json()

    # Create a comment to be deleted
    response = client.post(
        f"/posts/{post_data['id']}/comments",
        json={"content": "This is a test comment.", "author_id": user_data['id']},
    )
    assert response.status_code == 200, response.text
    comment_data = response.json()

    # Delete the created comment
    response = client.delete(f"/comments/{comment_data['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Comment deleted successfully"

    # Verify the comment has been deleted
    response = client.get(f"/comments/{comment_data['id']}")
    assert response.status_code == 404, response.text
