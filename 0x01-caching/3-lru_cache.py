#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and is a LRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
