from datetime import datetime
from sqlalchemy.orm import registry


table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int]
    user_name: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime]