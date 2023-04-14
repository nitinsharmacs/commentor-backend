from typing import Callable, TypeVar

T = TypeVar('T')


class Array(list):
    """List with features of javascript array"""

    def unshift(self, item) -> int:
        """Insert item in list top"""
        self.insert(0, item)
        return len(self)

    def find(self, predicate: Callable) -> T | None:
        """Finds the item by predicate"""
        for item in self:
            if predicate(item):
                return item

    def filter(self, predicate: Callable) -> list:
        """Filters the item by the predicate"""
        return [item for item in self if predicate(item)]
