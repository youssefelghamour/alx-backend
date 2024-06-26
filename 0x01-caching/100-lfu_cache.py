#!/usr/bin/env python3
""" LFUCache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Least Frequently Used caching system """

    def __init__(self):
        """ initialisation """
        super().__init__()
        # dict of the keys and their frequency (nb of visits)
        self.frequency_dict = {}

    def put(self, key, item):
        """ assigns to the dictionary the item value for the key key """
        if key is None or item is None:
            return

        # check if key already exists
        if key in self.cache_data:
            # update the value for the key
            self.cache_data[key] = item
            # increment the frequency of the accessed key
            self.frequency_dict[key] += 1
        else:
            # add new key and item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # find the least frequently used item
                min_freq = min(self.frequency_dict.values())

                # list of all the keys with the same number of visits
                least_freq_keys = []
                for k, v in self.frequency_dict.items():
                    if v == min_freq:
                        least_freq_keys.append(k)

                # if multiple items have the same frequency,
                # remove the least recently used one
                lru_key = least_freq_keys[0]

                del self.cache_data[lru_key]
                del self.frequency_dict[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.frequency_dict[key] = 1

    def get(self, key):
        """ returns the value in the dictionary that is linked to key """
        if key is None or key not in self.cache_data.keys():
            return None

        # update the frequency of the accessed key
        self.frequency_dict[key] += 1

        return self.cache_data.get(key)
