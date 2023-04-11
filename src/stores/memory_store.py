from typing import TypeVar

from src.models.Map import Map
from src.stores.store import Store

T = TypeVar('T')


class MemoryStore(Store):
    """Memory store to manage key and values list"""

    def __init__(self):
        self.map = Map({'comments': {}})

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
