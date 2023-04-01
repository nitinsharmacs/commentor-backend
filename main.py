import json
import pathlib

from src.app import create_app
from src.stores.file_store import FileStore
from src.gchat_notificator import GChatNotificator

STORE_DIR = './db'
STORE_FILE = STORE_DIR + '/db.json'
GCHAT_SPACE = 'https://chat.googleapis.com/v1/spaces/AAAAWbfnzv4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=OjGR2nQi-rec-3tLP0MDvbnPC8eJkRuKeLap5QfGwvs%3D'


def store_setup():
    """Setup the store directory and store file"""
    path = pathlib.Path(STORE_FILE)
    if not path.exists():
        pathlib.Path(STORE_DIR).mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'comments': {}}), 'utf-8')


store_setup()
app = create_app({'store': FileStore(STORE_FILE),
                 'notificator': GChatNotificator(GCHAT_SPACE)})

PORT = 4000
if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0', debug=True)
