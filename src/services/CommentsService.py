"""CommentsService"""

from types import FunctionType
from src.models.Comment import Comment
from src.models.Comments import Comments


class CommentsService:
    """Service managing comments"""

    def __init__(self, id_generator: FunctionType):
        """Initialise CommentsService"""
        self.store = Comments()
        self.___id_generator___ = id_generator

    def __set_id_generator__(self, id_generator: FunctionType) -> None:
        """Should not be used by user"""
        self.___id_generator___: FunctionType = id_generator

    def add_comment(self, topic_id: str, comment: str) -> dict:
        """Add a comment into provided topic id"""

        comment_id = self.___id_generator___()
        username = 'anoymous'
        avatar = 'some_url'

        total_insertions = self.store.add(Comment(comment_id, comment,
                                                  username, avatar), topic_id)

        return {'total-comments': total_insertions, 'comment-id': comment_id}

    def get_all(self, topic_id: str) -> list:
        """Get all comments from provided topic"""

        return self.store.get_all(topic_id)

    def clear(self) -> None:
        """Delete all comments from all topics"""
        self.store.clear()
