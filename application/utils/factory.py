from flask import Flask
import os
from flask_cors import CORS
from application.apis import api

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-3]


def create_app(app_name=PKG_NAME):
    """Initialize the core application."""
    app = Flask(app_name)
    CORS(app)

    with app.app_context():
        # Register Restx Api
        api.init_app(app)
        return app
