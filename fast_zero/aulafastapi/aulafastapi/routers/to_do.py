from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from aulafastapi.database import get_session
from aulafastapi.models import Todo, User
from aulafastapi.schemas import TodoPublic, TodoSchema
from aulafastapi.security import get_current_user

router = APIRouter(prefix="/todos", tags=["todo"])

T_Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/", response_model=TodoPublic)
def create_todo(
    todo: TodoSchema,
    user: CurrentUser,
    session: T_Session,
):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
