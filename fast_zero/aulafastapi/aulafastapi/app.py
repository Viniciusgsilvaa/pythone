from http import HTTPStatus

from fastapi import FastAPI

from aulafastapi.routers import auth, to_do, users
from aulafastapi.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(to_do.router)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "ola mundo"}
