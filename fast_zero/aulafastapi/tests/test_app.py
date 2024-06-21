from http import HTTPStatus


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
