"gchat-notificator.py"

import json
import requests


class GChatNotificator:
    """Google chat notificator to notifiy to google chat space"""

    def __init__(self, chat_url: str) -> None:
        self.chat_url: str = chat_url

    def __prepare_msg__(self, topic: str, comment: str) -> str:
        """Prepares message from given topic and comment"""
        return f"Comment on *{topic}*\n\n`{comment}`"

    def notify(self, topic: str, comment: str) -> None:
        """Send message to gchat space using webhook"""

        headers = {'content-type': 'application/json'}
        body = json.dumps({'text': self.__prepare_msg__(topic, comment)})
        try:
            requests.post(
                self.chat_url,
                headers=headers,
                data=body,
                timeout=4
            )
        except Exception:
            pass
