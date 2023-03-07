#!/usr/bin/env python3
"""Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache():
    """Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, value: str) -> str:
        return value.decode('utf-8')

    def get_int(self, number: int) -> int:
        return self.get(number)
