"comments_repository.py"

from datetime import datetime

from src.stores.file_store import FileStore
from src.models.Comment import Comment


def to_datetime(timestamp: str | datetime) -> datetime:
    """Convert iso timestamp in string to datetime instance"""
    if isinstance(timestamp, (datetime)):
        return timestamp

    return datetime.fromisoformat(timestamp)


class CommentsRepository:
    """CommentsRepository to create, store and manage comments"""

    def __init__(self, store: FileStore) -> None:
        self.store = store
        self.__KEY__ = 'comments'

    def add(self, topic_id: str, comment: Comment) -> int:
        """Add a comment into comments store"""

        comments: dict = self.store.get(self.__KEY__)
        topic_comments = comments.get(topic_id, [])
        topic_comments.insert(0, comment)
        comments[topic_id] = topic_comments
        self.store.put(self.__KEY__, comments)

        return len(comments[topic_id])

    def get(self, topic_id: str) -> list[Comment]:
        """Get all the comments under topic id"""

        comments = self.store.get(self.__KEY__)
        topic_comments = comments.get(topic_id, [])

        return [Comment(comment['id'],
                        comment['message'],
                        comment['username'],
                        comment['avatar'],
                        to_datetime(comment['timestamp']))
                for comment in topic_comments]
