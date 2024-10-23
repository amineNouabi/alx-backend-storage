#!/usr/bin/env python3
"""

Module defining the Cache class

"""

import redis
import uuid
from typing import Union


class Cache:
    """Redis Cache class"""

    def __init__(self):
        """Cache Conctructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self: "Cache", data: Union[str, bytes, int, float]) -> str:
        """Stores the input data in the cache"""
        key = uuid.uuid4()
        self._redis.append(key, data)
        return key