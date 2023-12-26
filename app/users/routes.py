from .handlers import create_user

routes = [
    {
        'url': '/users',
        'name': 'create_user',
        'handler': create_user,
        'methods': ['POST']
    }
]