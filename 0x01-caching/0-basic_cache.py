#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic caching system """

    def __init__(self):
        """ initialisation """
        super().__init__()

    def put(self, key, item):
        """ assigns to the dictionary the item value for the key key """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """  """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
