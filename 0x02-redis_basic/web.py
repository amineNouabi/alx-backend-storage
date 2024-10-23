#!/usr/bin/env python3
"""

Module defining web tracking and caching.

"""

import redis
import requests
from functools import wraps
from typing import Callable


cache = redis.Redis()


def cacher(method: Callable) -> Callable:
    """Caches output of a function"""
    @wraps(method)
    def wrapper(url: str):
        """Wrapper function"""
        cached = cache.get(url)
        if cached:
            cache.incr(f'count:{url}')
            return cached.decode('utf-8')
        result = method(url)
        cache.set(f'count:{url}', 1)
        cache.setex(f'result:{url}', 10, result)
        return result
    return wrapper


def get_page(url: str) -> str:
    """Returns core HTML of a webpage"""
    return requests.get(url).text
