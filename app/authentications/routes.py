from .handlers import login, refresh_token, logout

routes = [
    {
        'url': '/authentications',
        'name': 'login',
        'handler': login,
        'methods': ['POST']
    },
    {
        'url': '/authentications',
        'name': 'refresh_token',
        'handler': refresh_token,
        'methods': ['PUT']
    },
    {
        'url': '/authentications',
        'name': 'logout',
        'handler': logout,
        'methods': ['DELETE']
    }
]