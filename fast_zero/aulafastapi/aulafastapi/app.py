from http import HTTPStatus

from fastapi import FastAPI

from aulafastapi.schemas import (Message)
from aulafastapi.routers import users

app = FastAPI()
app.include_router(users)

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "ola mundo"}
