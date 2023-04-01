"""CommentsService"""

from types import FunctionType

from src.repositories.comments_repository import CommentsRepository
from src.models.Comment import Comment


class CommentsService:
    """Service managing comments"""

    def __init__(self,
                 comments_repository: CommentsRepository,
                 id_generator: FunctionType):
        """Initialise CommentsService"""
        self.comments_repository = comments_repository
        self.___id_generator___ = id_generator

    def __set_id_generator__(self, id_generator: FunctionType) -> None:
        """Should not be used by user"""
        self.___id_generator___: FunctionType = id_generator

    def add_comment(self, topic_id: str, comment: str) -> dict:
        """Add a comment into provided topic id"""

        comment_id = self.___id_generator___()
        username = 'anoymous'
        avatar = 'some_url'

        total_insertions = self.comments_repository.add(
            topic_id,
            Comment(comment_id, comment, username, avatar)
        )

        return {'total-comments': total_insertions, 'comment-id': comment_id}

    def get_all(self, topic_id: str) -> list:
        """Get all comments from provided topic"""

        return self.comments_repository.get(topic_id)

    def clear(self) -> None:
        """Delete all comments from all topics"""
        self.comments_repository.clear()
