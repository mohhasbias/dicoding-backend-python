from pydantic import BaseModel, Field


class Auth(BaseModel):
    username: str = Field(..., min_length=5)
    password: str = Field(..., min_length=3)


def new_auth(username=None, password=None):
    auth = Auth(username=username, password=password)
    return dict(auth)
