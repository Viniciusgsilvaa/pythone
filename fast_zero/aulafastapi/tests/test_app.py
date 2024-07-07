from http import HTTPStatus


def test_read_root_deve_retornar_ok_ola_mundo(client):
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "ola mundo"}
