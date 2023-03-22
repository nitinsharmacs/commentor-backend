from flask import Flask
from flask_cors import CORS

from src.controllers.api import api_bp


def create_app():
    """Creates commentor flask REST API Application server"""

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*", "methods": "*"}})
    app.register_blueprint(api_bp)
    return app
