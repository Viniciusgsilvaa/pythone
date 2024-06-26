from sqlalchemy import select

from aulafastapi.models import User


def test_create_user(session):
    user = User(
        username="Vinicius", password="1234", email="vinicius@gmail.com"
    )

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == "vinicius@gmail.com")
    )

    assert result.username == "Vinicius"
