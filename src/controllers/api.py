from flask import Blueprint, jsonify, request

from src.services.comments_service import CommentsService
from src.repositories.comments_repository import CommentsRepository
from src.util.id_generator import id_generator


def create_blueprint(config: dict):
    """Create API blueprint"""

    api_bp = Blueprint('api', __name__, url_prefix='/api')

    repository = CommentsRepository(config['store'])
    comments_service = CommentsService(repository, id_generator)

    @api_bp.route('/health')
    def health():
        """Endpoint to check server health"""
        return jsonify({"message": "Server is healthy"})

    @api_bp.post('/add-comment', strict_slashes=False)
    def add_comment():
        """Add comment into given topic id"""

        body = request.get_json()
        message = body['comment']
        topic_id = body['topic-id']

        comment_info = comments_service.add_comment(topic_id, message)

        return jsonify({"topic-id": topic_id,
                        "comment-id": comment_info['comment-id'],
                        "total-comments": comment_info['total-comments']}), 201

    @api_bp.get('/comments/<topic_id>')
    def get_comments(topic_id: str):
        """Gets all comments from the given topic id"""

        comments = comments_service.get_all(topic_id)

        return jsonify({'topic-id': topic_id, 'comments': comments})

    return api_bp
