from flask import request, current_app

from . import use_cases


def login():
    # parse request
    authn_creds = request.get_json()
    current_app.logger.debug(authn_creds)

    # call use case
    authn_token = use_cases.authenticate_user(authn_creds)

    # return response
    return {
        'status': 'success',
        'data': authn_token
    }, 201


def refresh_token():
    # parse request
    authn_token = request.get_json()

    # call use case
    new_authn_token = use_cases.refresh_token(authn_token)

    # return response
    return {
        'status': 'success',
        'data': new_authn_token
    }, 200


def logout():
    # parse request
    authn_token = request.get_json()

    # call use case
    use_cases.logout(authn_token)

    # return response
    return {
        'status': 'success',
        'message': 'logout berhasil'
    }, 200
