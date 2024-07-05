from http import HTTPStatus

from aulafastapi.schemas import UserPublic


def test_read_root_deve_retornar_ok_ola_mundo(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "ola mundo"}


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

    response_error = client.put(
        "/users/9999",  # ID fora dos limites
        json={
            "username": "nonexistent",
            "email": "nonexistent@example.com",
            "password": "password",
        },
    )

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {"detail": "User not Found"}

    assert response.json() == {
        "username": "alice2",
        "email": "alice@example.com",
        "id": 1,
    }


def test_delete_user(client, user):
    response = client.delete("/users/1")

    response_error = client.delete("/users/9999")

    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {"detail": "User not Found"}

    assert response.json() == {"message": "User deleted"}
