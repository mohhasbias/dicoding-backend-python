import datetime

from . import entities
from . import repository


def create_thread(thread, owner):
    # validate thread
    thread = entities.new_thread({
        **thread,
        'owner': owner.get('id'),
        'date': datetime.datetime.utcnow().isoformat()
    })

    # call repository
    added_thread = repository.add_thread(thread)

    # return result
    return added_thread


def get_thread_with_comments(thread):
    # call repository, no business logic
    thread = repository.get_thread_with_comments(thread)

    return thread
