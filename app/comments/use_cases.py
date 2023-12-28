from flask import current_app

import app.threads.repository
from . import entities
from . import repository


def add_comment_to(user, comment, thread):
    # validate thread
    thread = app.threads.repository.get_thread(thread)
    current_app.logger.debug(thread)
    # validate comment
    comment = entities.new_comment(comment)
    # save comment to db
    added_comment = repository.add_comment_to_thread(user, comment, thread)

    return added_comment
