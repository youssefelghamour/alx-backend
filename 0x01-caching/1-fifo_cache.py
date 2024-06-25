#!/usr/bin/env python3
""" FIFOCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ initialisation """
        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary the item value for the key key """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            # convert the dict to a list of the keys
            # and get get the key of the first item
            first_key = list(self.cache_data.keys())[0]

            # delete and return the first item
            first_item = self.cache_data.pop(first_key)

            print("DISCARD:", first_key)

    def get(self, key):
        """ returns the value in the dictionary that is linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
