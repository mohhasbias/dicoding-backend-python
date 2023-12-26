import uuid
from sqlalchemy import MetaData, Table
from app.db_engine import get_engine, get_session

metadata = MetaData()

users = Table('users', metadata, autoload_with=get_engine())


class AlreadyExistsError(Exception):
    pass


def add_user(user):
    stmt = users.select().where(users.c.username == user['username'])
    if get_session().execute(stmt).first():
        raise AlreadyExistsError("username tidak tersedia")

    new_user = {
        **user,
        'id': uuid.uuid4().hex
    }

    # add user to database
    get_session().execute(users.insert().values(new_user))
    get_session().commit()

    # remove password from returned user
    del new_user['password']

    return new_user
