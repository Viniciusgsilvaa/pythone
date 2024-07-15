from http import HTTPStatus

from aulafastapi.schemas import UserPublic


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_create_user_exist_username(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    response_same = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response_same.status_code == HTTPStatus.BAD_REQUEST
    assert response_same.json() == {"detail": "Email already exists"}


def test_create_user_exist_email(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    response_same = client.post(
        "/users/",
        json={
            "username": "alice2",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response_same.status_code == HTTPStatus.BAD_REQUEST
    assert response_same.json() == {"detail": "Email already exists"}


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_users_with_user(client, user):
    user_schemas = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": [user_schemas]}


def test_update_user(client, user, token):
    response = client.put(
        f"/users/{user.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "password": "123",
            "username": "alice2",
            "email": "alice@example.com",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "alice2",
        "email": "alice@example.com",
        "id": 1,
    }


def test_error_update_user(client, user, other_user, token):
    response_error = client.put(
        f"/users/{other_user.id}",  # ID fora dos limites
        headers={"Authorization": f"Bearer {token}"},
        json={
            "username": "nonexistent",
            "email": "nonexistent@example.com",
            "password": "password",
        },
    )

    assert response_error.status_code == HTTPStatus.FORBIDDEN
    assert response_error.json() == {"detail": "Not enough permission"}


def test_delete_user(client, user, token):
    response = client.delete(
        f"/users/{user.id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    # response_error = client.delete("/users/9999")

    # assert response_error.status_code == HTTPStatus.NOT_FOUND
    # assert response_error.json() == {"detail": "User not Found"}

    assert response.json() == {"message": "User deleted"}


def test_delete_wrong_user(client, other_user, token):
    response = client.delete(
        f"/users/{other_user.id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    # response_error = client.delete("/users/9999")

    # assert response_error.status_code == HTTPStatus.NOT_FOUND
    # assert response_error.json() == {"detail": "User not Found"}
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "Not enough permission"}
