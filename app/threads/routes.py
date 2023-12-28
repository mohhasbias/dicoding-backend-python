from .handlers import create_thread, get_thread
from app import security

routes = [
    {
        'url': '/threads',
        'name': 'create_thread',
        'handler': security.login_required(create_thread),
        'methods': ['POST']
    },
    {
        'url': '/threads/<id>',
        'name': 'get_thread',
        'handler': get_thread,
        'methods': ['GET']
    }
]
