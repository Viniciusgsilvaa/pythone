import pytest
from fastapi.testclient import TestClient  # type: ignore

from aulafastapi.app import app


@pytest.fixture()
def client():
    return TestClient(app)
