from datetime import datetime


class Comment(dict):
    def __init__(self, id, message, username, avatar) -> None:
        super().__init__(id=id, message=message, username=username,
                         avatar=avatar, timestamp=datetime.now())
