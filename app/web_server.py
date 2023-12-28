from flask import Flask
from jwt import InvalidTokenError

from .db_engine import NotExistError
from app.security import AuthenticationError
from .users.repository import AlreadyExistsError


def create_web_server(routes):
    app = Flask(__name__)

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'

    for route in routes:
        app.add_url_rule(route['url'], route['name'], route['handler'], methods=route['methods'])

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        app.logger.debug(error.errors())
        e = error.errors()[0].get('ctx').get('error') if error.errors()[0].get('type') == 'value_error' else error
        return {
            'status': 'fail',
            'message': str(e)
        }, 400

    @app.errorhandler(Exception)
    def handle_exception(error):
        if isinstance(error, AlreadyExistsError):
            return {
                'status': 'fail',
                'message': str(error)
            }, 400

        if isinstance(error, NotExistError):
            return {
                'status': 'fail',
                'message': str(error)
            }, 401

        if isinstance(error, InvalidTokenError):
            return {
                'status': 'fail',
                'message': str(error)
            }, 400

        if isinstance(error, AuthenticationError):
            return {
                'status': 'fail',
                'message': str(error)
            }, 401

        # check if flask is in debug mode
        if app.debug:
            raise error

        return {
            'status': 'error',
            'message': str(error)
        }, 500

    @app.errorhandler(404)
    def resource_not_found(e):
        return {
            'status': 'fail',
            'message': 'Resource not found'
        }, 404

    return app
