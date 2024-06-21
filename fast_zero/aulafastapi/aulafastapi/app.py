from http import HTTPStatus
from fastapi import FastAPI
from aulafastapi.schemas import Message, UserSchema, UserPublic, UserDB, UserList

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "ola mundo"}


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) +1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id

@app.get('/user/')
def read_users():
    return {'user': database}