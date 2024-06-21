from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from aulafastapi.app import app




def test_read_root_deve_retornar_ok_ola_mundo(client):
    
    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "ola mundo"}

def test_create_user(client):
    

    response = client.post(
        '/users/',
        json={
            'username': "testusername",
            'password': 'password',
            'email': 'test@test.com',
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1
    }


