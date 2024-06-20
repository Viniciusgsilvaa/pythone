from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from aulafastapi.app import app


def test_read_root_deve_retornar_ok_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "ola mundo"}
