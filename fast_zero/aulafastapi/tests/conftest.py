import pytest
from fastapi.testclient import TestClient  # type: ignore
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from aulafastapi.app import app
from aulafastapi.database import get_session
from aulafastapi.models import User, table_registry


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture()
def user(session):
    user = User(username="Test", email="test@test.com", password="testtest")
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
