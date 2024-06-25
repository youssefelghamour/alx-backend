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

        self.cache_data[key] = item

        if key in self.cache_list:
            # get the index of the key
            index = self.cache_list.index(key)

            # put the recenty visited item at the end
            temp = self.cache_list[index]
            self.cache_list[index] = self.cache_list[-1]
            self.cache_list[-1] = temp
        else:
            self.cache_list.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            del_key = self.cache_list[0]

            # delete the item
            self.cache_data.pop(del_key)
            del self.cache_list[0]

            print("DISCARD:", del_key)

    def get(self, key):
        """ returns the value in the dictionary that is linked to key """
        if key is None or key not in self.cache_data.keys():
            return None

        # update the order of the list by putting the most visited item in top
        if key in self.cache_list:
            # get the index of the key
            index = self.cache_list.index(key)

            # put the recenty visited item at the end
            temp = self.cache_list[index]
            self.cache_list[index] = self.cache_list[-1]
            self.cache_list[-1] = temp

        return self.cache_data.get(key)
