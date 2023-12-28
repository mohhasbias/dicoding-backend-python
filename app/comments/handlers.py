from flask import request

from . import use_cases
from app.db_engine import NotExistError


def create_comment(id):
    # parse request body
    thread = {
        "id": id
    }
    comment = request.get_json()
    user = request.user

    # call use case
    try:
        added_comment = use_cases.add_comment_to(user, comment, thread)
    except NotExistError as e:
        return {
            "status": "fail",
            "message": str(e)
        }, 404

    return {
        "status": "success",
        "data": {
            "addedComment": added_comment
        }
    }, 201
