from flask import Flask
from src.controllers.api import api_bp


def create_app():
    """Creates commentor flask REST API Application server"""

    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app
