#!/usr/bin/env python3
""" writing strings to redis"""
import redis
import uuid
from typing import List, Union

mlist = Union[str, bytes, int, float]


class Cache():
    """ cache class """
    def __init__(self) -> None:
        """initialization func"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: mlist) -> str:
        """func def"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
