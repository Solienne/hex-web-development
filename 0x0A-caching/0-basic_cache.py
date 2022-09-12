#!/usr/bin/python3
"""
Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system:
       -use self.cache_data - dictionary from parent class BaseCaching
       -This caching system have no limit
    """
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()

    def put(self, key, item):
        """Puts function definition"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets function definition"""
        if key is not None:
            for k, value in self.cache_data.items():
                if k == key:
                    return value
        return None
