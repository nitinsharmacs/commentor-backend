from src.models.Array import Array
from src.models.Map import Map
from src.models.Comment import Comment


class Comments:
    def __init__(self):
        self.comments = Map()

    def add(self, comment: Comment, topic_id: str) -> int:
        if self.comments.has(topic_id):
            self.comments[topic_id].unshift(comment)
        else:
            self.comments[topic_id] = Array([comment])

        return len(self.comments[topic_id])
