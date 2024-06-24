#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination information

            Args:
                index: Starting index for pagination
                page_size: Number of items per page

            Returns: Dict containing the pagination information
        """
        assert isinstance(index, int)
        assert 0 <= index < len(self.__indexed_dataset)

        old_index = index

        while index not in self.__indexed_dataset.keys():
            if index >= len(self.__indexed_dataset):
                break
            index += 1

        data = []
        for i in range(index, index + page_size):
            data.append(self.__indexed_dataset[i])

        dct = {
            'index': old_index,
            'data': data,
            'page_size': page_size,
            'next_index': index + page_size
        }

        return dct
