#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system using the LFU algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_frequency = {}
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.usage_frequency:
                self.usage_frequency[key] += 1
            else:
                self.usage_frequency[key] = 1

            if key in self.lru_order:
                self.lru_order.remove(key)
            self.lru_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                lfu_key = min(self.usage_frequency, key=lambda k: (
                    self.usage_frequency[k], self.lru_order.index(k)))
                # Remove the least frequently used item
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.lru_order.remove(lfu_key)
                print("DISCARD:", lfu_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the usage frequency
        self.usage_frequency[key] += 1
        # Update the LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
