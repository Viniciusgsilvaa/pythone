from http import HTTPStatus

from jwt import decode

from aulafastapi.security import create_access_token, settings


def test_jwt():
    data = {"sub": "test@test.com"}
    token = create_access_token(data)

    result = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert result["sub"] == data["sub"]
    assert result["exp"]


def test_jwt_invalid_token(client, user):
    response = client.delete(
        f"/users/{user.id}", headers={"Authorization": "Bearer token-invalido"}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {"detail": "Could not validate credentials"}
