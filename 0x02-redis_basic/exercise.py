#!/usr/bin/env python3
"""

Module defining the Cache class

"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a function"""
    if not method or not hasattr(method, '__self__'):
        return
    redis_ins = getattr(method.__self__, '_redis', None)
    if not isinstance(redis_ins, redis.Redis):
        return
    method_name = method.__qualname__
    inputs = method_name + ":inputs"
    outputs = method_name + ":outputs"
    count = 0
    if redis_ins.exists(method_name):
        count = int(redis_ins.get(method_name))
    print(f"{method_name} was called {count} times:")
    inputs_list = redis_ins.lrange(inputs, 0, -1)
    outputs_list = redis_ins.lrange(outputs, 0, -1)
    for i, o in zip(inputs_list, outputs_list):
        print(f"{method_name}(*{i.decode('utf-8')}) -> {o}")


class Cache:
    """Redis Cache class"""

    def __init__(self):
        """Cache Conctructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
