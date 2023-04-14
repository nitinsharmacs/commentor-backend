"mongodb_store.py"


from typing import TypeVar

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from pymongo.collection import Collection

from src.stores.store import Store
from src.models.Comment import Comment

T = TypeVar('T')


class MongodbStore(Store):
    """Mongodb store"""
    DATABASE = 'commentor'

    def __init__(self, client: MongoClient):
        self.client: MongoClient = client

    def collection(self, name: str) -> Collection:
        """Gets collection by given name"""
        return self.client[MongodbStore.DATABASE][name]

    async def find_comments(self) -> list:
        """Get all the comments"""
        return [*self.collection('comments').find()]

    async def find(self, collection: str, query: dict) -> list:
        """Get all the comments of give topic id"""
        return [*self.collection(collection).find(query)]

    async def insert(self, collection: str, comment: Comment) -> bool:
        """Insert comment to topic id"""
        try:
            self.collection(collection).insert_one(comment)
            return True
        except ServerSelectionTimeoutError as error:
            print('INSERTION ERROR', error)
            return False
