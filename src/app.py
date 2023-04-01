import json
from datetime import date, datetime


from flask import Flask, request
from flask.wrappers import Response
from flask.json.provider import JSONProvider

from flask_cors import CORS

from src.controllers.api import create_blueprint


def default(obj):
    """Encoding for JSON Serialization"""
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()


class CustomJsonProvider(JSONProvider):
    """CustomJsonProvider to Serialise date or datetime"""

    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, default=default)

    def loads(self, s: str | bytes, **kwargs):
        return json.loads(s, **kwargs)


def create_app(config: dict):
    """Creates commentor flask REST API Application server"""

    app = Flask(__name__)
    app.json = CustomJsonProvider(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Handling OPTIONS preflight requests
    @app.before_request
    def handle_options():
        if request.method.lower() == 'options':
            response = Response()
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add(
                'Access-Control-Allow-Headers', 'content-type')
            return response

    app.register_blueprint(create_blueprint(config))
    return app
