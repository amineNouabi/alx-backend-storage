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
    def wrapper(url):
        """Wrapper function"""
        cache.incr(f'count:{url}')
        cached = cache.get(f'result:{url}')
        if cached:
            return cached.decode('utf-8')
        result = method(url)
        cache.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@cacher
def get_page(url: str) -> str:
    """Returns core HTML of a webpage"""
    return requests.get(url).text
