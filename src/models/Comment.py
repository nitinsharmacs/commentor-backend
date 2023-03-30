from datetime import datetime


class Comment(dict):
    """Comment schema"""

    def __init__(self, id, message, username, avatar, timestamp=datetime.now()) -> None:
        super().__init__(id=id, message=message, username=username,
                         avatar=avatar, timestamp=timestamp)
