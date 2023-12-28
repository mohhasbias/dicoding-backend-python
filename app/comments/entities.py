from pydantic import BaseModel, Field


class Comment(BaseModel):
    content: str = Field(..., min_length=1)


def new_comment(comment):
    comment = Comment(**comment)
    return dict(comment)
