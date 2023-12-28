import datetime
import uuid

from flask import current_app
from sqlalchemy import Table, MetaData

from app.db_engine import get_session, get_engine

metadata_threads = MetaData()
threads = Table('threads', metadata_threads, autoload_with=get_engine())

metadata_comments = MetaData()
comments = Table('comments', metadata_comments, autoload_with=get_engine())


def add_comment_to_thread(user, comment, thread):
    # prepare comment
    comment = {
        "id": uuid.uuid4().hex,
        **comment,
        "owner": user.get('id'),
        "thread_id": thread.get('id'),
        "is_delete": False,
        "date": datetime.datetime.now().isoformat()
    }
    current_app.logger.debug(comment)
    # save comment to db
    get_session().execute(comments.insert().values(comment))
    get_session().commit()
    return comment
