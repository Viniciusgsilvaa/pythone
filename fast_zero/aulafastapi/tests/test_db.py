from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from aulafastapi.models import User, table_registry


def test_create_user():
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username="Vinicius", password="1234", email="vinicius@gmail.com"
        )

        session.add(user)
        session.commit()
        result = session.scalar(
            select(User).where(User.email == 'vinicius@gmail.com')
        )

    assert result.username == 'Vinicius'
