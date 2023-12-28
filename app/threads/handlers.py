from flask import request, current_app

from app import security
from app.threads import use_cases


def create_thread():
    # parse request
    thread = request.get_json()
    user = request.user
    current_app.logger.debug(thread)
    current_app.logger.debug(user)

    # call use case
    added_thread = use_cases.create_thread(thread, user)

    # return response
    return {
        "status": "success",
        "data": {
            "addedThread": added_thread
        }
    }, 201


def get_thread(id):
    # call use case
    thread = use_cases.get_thread_with_comments({
        "id": id
    })

    return {
        "status": "success",
        "data": {
            "thread": thread
        }
    }, 200
