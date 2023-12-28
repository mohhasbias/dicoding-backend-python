from .handlers import create_comment
from app import security

routes = [
    {
        "url": "/threads/<id>/comments",
        "name": "create_comment",
        "handler": security.login_required(create_comment),
        "methods": ["POST"]
    }
]