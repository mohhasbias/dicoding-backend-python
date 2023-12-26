import uuid
from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    username: str = Field(..., min_length=5)
    password: str = Field(..., min_length=5)
    fullname: str = Field(..., min_length=5)

    @field_validator('username')
    @classmethod
    def username_not_contains_space(cls, v):
        if ' ' in v:
            raise ValueError('tidak dapat membuat user baru karena username mengandung karakter terlarang')
        return v

def new_user(username=None, password=None, fullname=None):
    # validate username, password, and fullname using pydantic
    user = User(username=username, password=password, fullname=fullname)
    return dict(user)
