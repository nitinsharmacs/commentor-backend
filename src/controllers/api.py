from flask import Blueprint, jsonify, request

from src.models.Comment import Comment
from src.models.Comments import Comments

api_bp = Blueprint('api', __name__, url_prefix='/api')

comments = Comments()


@api_bp.route('/health')
def health():
    """Endpoint to check server health"""
    return jsonify({"message": "Server is healthy"})


@api_bp.route('/add-comment', methods=['POST'])
def add_comment():
    """Add comment into given topic id"""

    message = request.get_json()['comment']
    topic_id = request.get_json()['topic-id']

    comment_id = '1'
    comment = Comment(comment_id, message, 'anonymous', 'some_url')
    total_comments = comments.add(comment, topic_id)

    return jsonify({"topic-id": topic_id,
                    "comment-id": comment_id,
                    "total-comments": total_comments})


@api_bp.get('/comments/<topic_id>')
def get_comments(topic_id: str):
    """Gets all comments from the given topic id"""

    topic_comments = comments.get_all(topic_id)
    return jsonify({'topic-id': topic_id, 'comments': topic_comments})
