import json
import pathlib

from src.app import create_app
from src.stores.file_store import FileStore

STORE_DIR = './db'
STORE_FILE = STORE_DIR + '/db.json'


def store_setup():
    """Setup the store directory and store file"""
    path = pathlib.Path(STORE_FILE)
    if not path.exists():
        pathlib.Path(STORE_DIR).mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'comments': {}}), 'utf-8')


store_setup()
app = create_app({'store': FileStore(STORE_FILE)})

PORT = 4000
if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0', debug=True)
