import json
import os
import pathlib

from pymongo import MongoClient
import certifi

from src.app import create_app
from src.stores.file_store import FileStore
from src.stores.mongodb_store import MongodbStore
from src.gchat_notificator import GChatNotificator

STORE_DIR = './db'
STORE_FILE = STORE_DIR + '/db.json'
GCHAT_SPACE = 'https://chat.googleapis.com/v1/spaces/AAAAWbfnzv4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=OjGR2nQi-rec-3tLP0MDvbnPC8eJkRuKeLap5QfGwvs%3D'

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

DB_URL = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.jx9oe.mongodb.net/?retryWrites=true&w=majority"


def store_setup():
    """Setup the store directory and store file"""
    path = pathlib.Path(STORE_FILE)
    if not path.exists():
        pathlib.Path(STORE_DIR).mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'comments': {}}), 'utf-8')


def get_mongo_client(db_url: str) -> MongoClient | None:
    """Creates and mongodb client"""
    client = MongoClient(db_url, tlsCAFile=certifi.where())
    try:
        client.server_info()
        return client
    except Exception as error:
        print(error)
        return None


store = FileStore(STORE_FILE)

db_client = get_mongo_client(DB_URL)
if db_client is not None:
    store = MongodbStore(db_client)
    print("Using mongodb store")

app = create_app({'store': store,
                  'notificator': GChatNotificator(GCHAT_SPACE)})

PORT = 4000
if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0', debug=True)
