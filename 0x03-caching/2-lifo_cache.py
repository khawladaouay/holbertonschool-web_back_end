#!/usr/bin/python3
"""2-lifo_cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """assign to the dictionary
                self.cache_data the item value for the key"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.last_key))
                del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
