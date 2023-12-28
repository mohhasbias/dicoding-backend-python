import datetime
import os
from functools import wraps

import jwt
from flask import current_app, request
from jwt import PyJWTError

import app.db_engine
from app.authentications import repository


class AuthenticationError(Exception):
    pass


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
    current_app.logger.debug(user)
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
    except app.db_engine.NotExistError:
        raise InvalidTokenError("refresh token tidak valid")

    secret_key = os.environ.get('REFRESH_TOKEN_SECRET_KEY')
    try:
        # Try to decode the token
        jwt.decode(token.get('refreshToken'), secret_key, algorithms='HS256')
    except PyJWTError:
        # If the token is expired, remove it from the database
        repository.delete_refresh_token(token)
        raise


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the header
        token = request.headers.get('Authorization', "Bearer None").split(" ")[1]
        current_app.logger.debug(token)
        # Check if the user is authenticated
        user = None
        try:
            secret_key = os.environ.get('ACCESS_TOKEN_SECRET_KEY')
            user = jwt.decode(token, secret_key, algorithms='HS256')
        except Exception:
            raise AuthenticationError("Missing authentication")

        current_app.logger.debug("user authenticated")
        current_app.logger.debug(user)
        request.user = {
            'id': user.get('id'),
            'username': user.get('username')
        }
        # If the user is authenticated, call the original function
        return f(*args, **kwargs)
    return decorated_function
