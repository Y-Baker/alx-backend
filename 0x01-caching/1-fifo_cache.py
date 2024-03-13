#!/usr/bin/env python3
"""BaseCache module"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - Inherits from BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            - First in (Cache), first out (FIFO)
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k, v = self.cache_data.popitem(last=False)
                print(f"DISCARD: {k}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
