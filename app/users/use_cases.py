from . import entities
from . import repository


def add_user(user):
    # validate user
    user = entities.new_user(**user)

    # call repository
    added_user = repository.add_user(user)

    # return result
    return added_user
