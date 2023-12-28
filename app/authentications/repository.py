from sqlalchemy import MetaData, Table, and_
from flask import current_app

from app.db_engine import get_engine, get_session, NotExistError

metadataUsers = MetaData()
metadataAuthn = MetaData()

users = Table('users', metadataUsers, autoload_with=get_engine())
authn = Table('authentications', metadataAuthn, autoload_with=get_engine())


def validate_credentials(user):
    current_app.logger.debug(user)
    stmt = (
        users
        .select()
        .where(
            and_(users.c.username == user.get('username'),
            users.c.password == user.get('password'))
        )
    )
    current_app.logger.debug(stmt)
    result = get_session().execute(stmt).mappings().first()
    current_app.logger.debug(result)
    if result:
        return result
    else:
        current_app.logger.debug("username atau password salah")
        raise NotExistError("username atau password salah")


def validate_refresh_token(token):
    stmt = (
        authn
        .select()
        .where(authn.c.token == token.get('refreshToken'))
    )
    result = get_session().execute(stmt).first()
    if not result:
        raise NotExistError("refresh token tidak ditemukan di database")


def add_refresh_token(refresh_token):
    # save refresh token to db
    get_session().execute(authn.insert().values({
        'token': refresh_token
    }))
    get_session().commit()


def delete_refresh_token(token):
    # delete refresh token from db
    get_session().execute(authn.delete().where(
        authn.c.token == token.get('refreshToken')
    ))
    get_session().commit()