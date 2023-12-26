import datetime
import os

import jwt
from flask import current_app
from jwt import PyJWTError

from . import repository

InvalidTokenError = jwt.InvalidTokenError

def authenticate_user(user):
    # generate access token
    access_token = create_access_token(user)

    # generate refresh token
    refresh_token = create_refresh_token(user)

    current_app.logger.debug(access_token)
    current_app.logger.debug(refresh_token)

    repository.add_refresh_token(refresh_token)

    return {
        'accessToken': access_token,
        'refreshToken': refresh_token
    }


def create_refresh_token(user):
    payload = {
        'id': user.get('id'),
        'username': user.get('username'),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    }
    secret_key = os.environ.get('REFRESH_TOKEN_SECRET_KEY')
    refresh_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return refresh_token


def create_access_token(user):
    payload = {
        'id': user.get('id'),
        'username': user.get('username'),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
    }
    secret_key = os.environ.get('ACCESS_TOKEN_SECRET_KEY')
    access_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return access_token


def new_access_token(token):
    # decode token
    secret_key = os.environ.get('REFRESH_TOKEN_SECRET_KEY')
    payload = jwt.decode(token.get('refreshToken'), secret_key, algorithms='HS256')

    # create new token
    new_token = create_access_token(payload)

    return {
        'accessToken': new_token
    }


def validate_token(token):
    # check if token exist in db
    try:
        repository.validate_refresh_token(token)
    except repository.NotExistError:
        raise InvalidTokenError("refresh token tidak valid")

    secret_key = os.environ.get('REFRESH_TOKEN_SECRET_KEY')
    try:
        # Try to decode the token
        jwt.decode(token.get('refreshToken'), secret_key, algorithms='HS256')
    except PyJWTError:
        # If the token is expired, remove it from the database
        repository.delete_refresh_token(token)
        raise
