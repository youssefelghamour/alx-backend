#!/usr/bin/env python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ initialisation """
        super().__init__()

        # key of the last added item
        self.cached_key = None

    def put(self, key, item):
        """ assigns to the dictionary the item value for the key key """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # delete the item
            self.cache_data.pop(self.cached_key)

            print("DISCARD:", self.cached_key)

        # keep track of the item added most recently
        self.cached_key = key

    def get(self, key):
        """ returns the value in the dictionary that is linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
