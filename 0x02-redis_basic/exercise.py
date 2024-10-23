#!/usr/bin/env python3
"""

Module defining the Cache class

"""

import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Redis Cache class"""

    def __init__(self):
        """Cache Conctructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the input data in the cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        self._redis.get
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Gets the data stored in the cache"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Gets the data stored in the cache as string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Gets the data stored in the cache as int"""
        return self.get(key, int)
