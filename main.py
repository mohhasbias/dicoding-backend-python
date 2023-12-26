from app.users.routes import routes as users_routes
from app.authn.routes import routes as authn_routes
from app.web_server import create_web_server

routes = [
    *users_routes,
    *authn_routes
]

app = create_web_server(routes)

if __name__ == '__main__':
    app.run()
