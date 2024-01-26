#!/usr/bin/env python3
""" writing strings to redis"""
import redis
import uuid
from typing import List, Union, Callable, Optional
from functools import wraps

mlist = Union[str, bytes, int, float, None]


def count_calls(method: Callable) -> Callable:
    """decorator func"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper func"""
        key = f"{method.__module__}.{method.__qualname__}_call_count"
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache():
    """ cache class """
    def __init__(self) -> None:
        """initialization func"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: mlist) -> str:
        """func def"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> mlist:
        """get func"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn else data
        return None

    def get_str(self, key: str) -> Optional[str]:
        """func to convert data to str"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """func to convert data to int
        """
        return self.get(key, fn=int)
