from flask import Blueprint, jsonify, request

from src.services.CommentsService import CommentsService
from src.util.id_generator import id_generator

api_bp = Blueprint('api', __name__, url_prefix='/api')

commentsService = CommentsService(id_generator)


@api_bp.route('/health')
def health():
    """Endpoint to check server health"""
    return jsonify({"message": "Server is healthy"})


@api_bp.post('/add-comment', strict_slashes=False)
def add_comment():
    """Add comment into given topic id"""

    message = request.get_json()['comment']
    topic_id = request.get_json()['topic-id']

    comment_info = commentsService.add_comment(topic_id, message)

    return jsonify({"topic-id": topic_id,
                    "comment-id": comment_info['comment-id'],
                    "total-comments": comment_info['total-comments']}), 201


@api_bp.get('/comments/<topic_id>')
def get_comments(topic_id: str):
    """Gets all comments from the given topic id"""

    # topic_comments = comments.get_all(topic_id)

    comments = commentsService.get_all(topic_id)

    return jsonify({'topic-id': topic_id, 'comments': comments})
