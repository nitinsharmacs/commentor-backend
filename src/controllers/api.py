from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/health')
def health():
    """Endpoint to check server health"""
    return jsonify({"message": "Server is healthy"})
