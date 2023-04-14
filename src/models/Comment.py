from datetime import datetime


class Comment(dict):
    """Comment schema"""

    def __init__(self, id: str,
                 message: str,
                 username: str,
                 avatar: str,
                 topic_id: str = 'id',
                 timestamp=datetime.now(),
                 ) -> None:
        super().__init__(id=id, message=message, username=username,
                         avatar=avatar, topic_id=topic_id, timestamp=timestamp)
