#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - caching system using the MRU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.mru_order:
                self.mru_order.remove(key)
            self.mru_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # The second last item is the MRU
                mru_key = self.mru_order.pop(-2)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
