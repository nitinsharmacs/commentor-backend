from typing import TypeVar

from src.models.Map import Map
from src.models.Array import Array
from src.stores.store import Store

T = TypeVar('T')


class MemoryStore(Store):
    """Memory store to manage key and values list"""

    def __init__(self):
        self.map = Map({})

    def __get__bucket(self, bucket_name: str) -> Array:
        """Gets the bucket by the bucket name"""
        return self.map.get(bucket_name, Array())

    async def insert(self, bucket_name: str, item: dict) -> int:
        """Inserts the item in the given bucket"""
        bucket = self.__get__bucket(bucket_name)
        bucket.append(item)
        self.map[bucket_name] = bucket
        return len(bucket)

    async def find(self, bucket_name: str, query: dict) -> list:
        """Finds the matched items by the given query"""
        bucket = self.__get__bucket(bucket_name)
        return bucket.filter(lambda item: item['topic_id'] == query['topic_id'])

    def put(self, key: str, value: dict | list) -> bool:
        """Insert value to given key"""

        self.map[key] = value

        return True

    def get(self, key: str) -> T:
        """Get all values of given key"""

        if self.map.has(key):
            return self.map[key]

        raise Exception(f'Key {key} is not present')

    def has(self, key: str) -> bool:
        """Checks if key exists in map"""

        return self.map.has(key)

    def clear(self):
        """Clears the map"""
        self.map = Map()
