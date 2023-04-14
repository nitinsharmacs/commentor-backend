"file_store.py"

import json
from src.models.Array import Array
from pathlib import Path
from typing import TypeVar
from datetime import datetime, date

from src.stores.store import Store

T = TypeVar('T')


def default(obj):
    """Encoding for JSON Serialization"""
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()


class FileStore(Store):
    """FileStore to store """

    def __init__(self, store_file: str | Path) -> None:
        self.store_file = Path(store_file)

    def __get_content__(self) -> dict:
        """Loads store file content and returns parsed json"""

        file_content: dict

        with open(self.store_file, mode='r', encoding='utf-8') as file:
            file_content = json.load(file)

        return file_content

    def __write__(self, content: dict) -> None:
        """Writes the content to store file"""
        with open(self.store_file, mode='w', encoding='utf-8') as file:
            json.dump(content, file, default=default)

    def __get_bucket(self, bucket_name: str) -> Array:
        """Gets the bucket by the name"""
        content = self.__get_content__()
        return Array(content.get(bucket_name, []))

    def __write_bucket(self, bucket_name: str, bucket: Array) -> None:
        """Writes the given bucket"""
        content = self.__get_content__()
        content[bucket_name] = bucket
        self.__write__(content)

    async def insert(self, bucket_name: str, item: dict) -> int:
        """Inserts the item in bucket of given name"""
        bucket = self.__get_bucket(bucket_name)
        bucket.append(item)
        self.__write_bucket(bucket_name, bucket)
        return len(bucket)

    async def find(self, bucket_name: str, query: dict) -> list:
        """Finds the matched items by the given query"""
        bucket = self.__get_bucket(bucket_name)
        return bucket.filter(lambda item: item['topic_id'] == query['topic_id'])

    def get(self, key: str) -> T:
        """Gets value of given key"""

        content = self.__get_content__()
        try:
            return content[key]
        except Exception:
            raise Exception(f'Key {key} is not present')

    def put(self, key: str, value: dict | list) -> bool:
        """Sets value of given key"""

        content = self.__get_content__()
        content[key] = value

        self.__write__(content)

        return True
