from src.models.Array import Array
from src.models.Map import Map
from src.models.Comment import Comment


class Comments:
    """Stores and Manages all comments per topic"""

    def __init__(self):
        self.comments = Map({'comments': {}})

    def add(self, comment: Comment, topic_id: str) -> int:
        """Add comment into give topic id"""

        if self.comments.has(topic_id):
            self.comments[topic_id].unshift(comment)
        else:
            self.comments[topic_id] = Array([comment])

        return len(self.comments[topic_id])

    def get_all(self, topic_id: str) -> list:
        """Gives all the comments of topic id"""

        if self.comments.has(topic_id):
            return self.comments[topic_id]

        return list()

    def has(self, topic_id: str) -> bool:
        """Determines whether comments of topic id exists"""

        return self.comments.has(topic_id)

    def clear(self):
        """Cleares the comments of all topics"""
        self.comments = Map()
