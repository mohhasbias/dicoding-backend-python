from pydantic import BaseModel, Field


class Thread(BaseModel):
    title: str = Field(..., min_length=3)
    body: str = Field(..., min_length=3)
    owner: str = Field(..., min_length=3)
    date: str = Field(..., min_length=3)


def new_thread(param):
    thread = Thread(**param)
    return dict(thread)
