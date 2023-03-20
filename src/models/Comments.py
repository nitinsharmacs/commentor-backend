from src.models.Array import Array
from src.models.Map import Map
from src.models.Comment import Comment


class Comments:
    def __init__(self):
        self.comments = Map()

    def add(self, comment: Comment, topic_id: str) -> int:
        """Add comment into give topic id"""

        if self.comments.has(topic_id):
            self.comments[topic_id].unshift(comment)
        else:
            self.comments[topic_id] = Array([comment])

        return len(self.comments[topic_id])

    def getAll(self, topic_id: str) -> list:
        """Gives all the comments of topic id"""

        if self.comments.has(topic_id):
            return [comment.serialize() for comment in self.comments[topic_id]]

        return list()

    def has(self, topic_id: str) -> bool:
        """Determines whether comments of topic id exists"""

        return self.comments.has(topic_id)
