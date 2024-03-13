#!/usr/bin/env python3
"""BaseCache module"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Inherits from BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            - Last in (Cache), first out (FIFO)
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {k}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
