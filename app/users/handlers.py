from flask import request
from .use_cases import add_user


def create_user():
    # parse http request
    request_body = request.get_json()

    # call use case
    added_user = add_user(request_body)

    # return http response
    return {
        'status': 'success',
        'data': {
            'addedUser': added_user
        }
    }, 201
