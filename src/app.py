from flask import Flask, request
from flask.wrappers import Response

from flask_cors import CORS

from src.controllers.api import api_bp


def create_app():
    """Creates commentor flask REST API Application server"""

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Handling OPTIONS preflight requests
    @app.before_request
    def handle_options():
        print(request.method)
        if request.method.lower() == 'options':
            response = Response()
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add(
                'Access-Control-Allow-Headers', 'content-type')
            return response

    app.register_blueprint(api_bp)
    return app
