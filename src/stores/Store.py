"""store.py"""

from typing import TypeVar


T = TypeVar('T')


class Store:
    """Interface for store classes"""

    def get(self, key: str) -> T:
        """Gets value of given key"""
        pass

    def put(self, key: str, value: dict | list) -> bool:
        """Sets value of given key"""
        pass
