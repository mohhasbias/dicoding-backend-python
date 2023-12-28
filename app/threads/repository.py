import uuid

from flask import current_app
from sqlalchemy import Table, MetaData, text
from app.db_engine import get_engine, get_session, NotExistError

metadata_threads = MetaData()

threads = Table('threads', metadata_threads, autoload_with=get_engine())


def add_thread(thread):
    added_thread = {
        'id': uuid.uuid4().hex,
        **thread,
    }
    # save thread to db
    get_session().execute(threads.insert().values(added_thread))
    get_session().commit()

    return {
        'id': added_thread['id'],
        'title': added_thread['title'],
        'owner': added_thread['owner'],
    }


def get_thread(thread):
    current_app.logger.debug(thread)
    stmt = threads.select().where(threads.c.id == thread['id'])
    current_app.logger.debug(stmt)
    result = get_session().execute(stmt).mappings().first()
    current_app.logger.debug(result)
    if not result:
        raise NotExistError("thread tidak ditemukan")

    return result


def get_thread_with_comments(thread):
    current_app.logger.debug(thread)
    # stmt = threads.select().where(threads.c.id == thread['id'])
    # query a thread with username and all its comments
    stmt = text("""
        SELECT
        threads.id, threads.title, threads.body, threads.date, users.username
        FROM threads 
        LEFT JOIN users ON threads.owner = users.id
        WHERE threads.id = '{}'
    """.format(thread['id']))
    current_app.logger.debug(stmt)
    thread = get_session().execute(stmt).mappings().first()
    current_app.logger.debug(thread)
    if not thread:
        raise NotExistError("thread tidak ditemukan")

    # query all comments of a thread
    stmt = text("""
        SELECT
        comments.id, comments.content, comments.date, users.username
        FROM comments 
        LEFT JOIN users ON comments.owner = users.id
        WHERE comments.thread_id = '{}'
    """.format(thread['id']))
    current_app.logger.debug(stmt)
    comments = get_session().execute(stmt).mappings().all()
    current_app.logger.debug(comments)

    # merge thread with comments
    thread_with_comments = {
        **dict(thread),
        'comments': [dict(comment) for comment in comments]
    }
    current_app.logger.debug(thread_with_comments)

    return thread_with_comments
