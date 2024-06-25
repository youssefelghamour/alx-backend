#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Least Recently Used caching system """

    def __init__(self):
        """ initialisation """
        super().__init__()
        # list of the keys from LRU to MRU
        self.cache_list = []

    def put(self, key, item):
        """ assigns to the dictionary the item value for the key key """
        if key is None or item is None:
            return

        if key in self.cache_list:
            # remove key to update its position later
            self.cache_list.remove(key)

        self.cache_data[key] = item

        # put the recently visited item at the end
        self.cache_list.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # get the key of the least recently used item
            del_key = self.cache_list.pop(0)
            # delete the item
            self.cache_data.pop(del_key)
            print("DISCARD:", del_key)

    def get(self, key):
        """ returns the value in the dictionary that is linked to key """
        if key is None or key not in self.cache_data.keys():
            return None

        # update the order of the list by putting the most visited item in top
        if key in self.cache_list:
            self.cache_list.remove(key)
            self.cache_list.append(key)

        return self.cache_data.get(key)
