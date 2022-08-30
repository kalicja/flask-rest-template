#lib overrides
import werkzeug
werkzeug.cached_property=werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func=flask.scaffold._endpoint_from_view_func
#lib overrides - done

from flask_restplus import Api, Namespace
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pyctuator.pyctuator import Pyctuator

from api.hello_api import api_namespace_hello_world_api

class DemoApp:

    def create_app(self, port):
        app_name='demo-app'
        flask_app = Flask(app_name)
        flask_app.logger.info('starting app')
        self._register_actuator(flask_app, app_name, port)
        self._register_resources(flask_app)
        return flask_app

    def _register_actuator(self, flask_app, app_name, port):
        Pyctuator(
            app=flask_app,
            app_name=app_name,
            app_url=f'https://0.0.0.0:{port}',
            pyctuator_endpoint_url=f'https://0.0.0.0:{port}/actuator',
            registration_url=None
        )

    def _register_db(self, flask_app):
        db=SQLAlchemy()
        db.init_app(flask_app)
        db.create_all()

    def _register_resources(self, flask_app):
        api = Api()
        api.init_app(flask_app, title='Flask Rest Demo App')
        api.add_namespace(Namespace('/', 'root'))
        api.add_namespace(api_namespace_hello_world_api)

if __name__=='__main__':
    demo_app = DemoApp()
    demo_flask_app=demo_app.create_app(8090)
    demo_flask_app.run(host='0.0.0.0', port=8090)
