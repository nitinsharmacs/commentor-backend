"""store.py"""

from typing import TypeVar


T = TypeVar('T')


class Store:
    """Interface for store classes"""

    async def insert(self, bucket_name: str, item: dict) -> int:
        """Inserts into collection"""
        pass
        ""
    async def find(self, bucket_name: str, query: dict) -> list:
        """Finds all the matched items"""
        pass

    def get(self, key: str) -> T:
        """Gets value of given key"""
        pass

    def put(self, key: str, value: dict | list) -> bool:
        """Sets value of given key"""
        pass
