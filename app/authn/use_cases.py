from flask import current_app

from . import entities
from . import repository
from . import security


def authenticate_user(user):
    # validate user
    user = entities.new_auth(**user)

    # validate credentials
    repository.validate_credentials(user)

    current_app.logger.debug("user credentials validated")

    # call repository
    authn_user = security.authenticate_user(user)

    # return result
    return authn_user


def refresh_token(token):
    # check if token is expired
    security.validate_token(token)

    # create new token
    new_token = security.new_access_token(token)

    # return result
    return new_token


def logout(token):
    # check if token exist in db
    try:
        repository.validate_refresh_token(token)
    except repository.NotExistError:
        raise security.InvalidTokenError("refresh token tidak ditemukan di database")

    # delete token from db
    repository.delete_refresh_token(token)

    # return result
    return {
        'status': 'success',
        'message': 'logout berhasil'
    }, 200
