from datetime import datetime


class Comment:
    def __init__(self, id, message, username, avatar) -> None:
        self.id = id
        self.message = message
        self.username = username
        self.avatar = avatar
        self.likes = 0
        self.timestamp = datetime.now()

    def serialize(self):
        return self.__dict__
