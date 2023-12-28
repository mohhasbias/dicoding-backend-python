from app.users.routes import routes as users_routes
from app.authentications.routes import routes as authn_routes
from app.threads.routes import routes as threads_routes
from app.comments.routes import routes as comments_routes
from app.web_server import create_web_server

routes = [
    *users_routes,
    *authn_routes,
    *threads_routes,
    *comments_routes,
]

app = create_web_server(routes)

if __name__ == '__main__':
    app.run()
