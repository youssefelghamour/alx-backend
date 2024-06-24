#!/usr/bin/env python3
""" module for Server class """
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ calculate start and end indexes for pagination

        Args:
        - page: the number of the page
        - page_size: the number of items per page

        Returns a tuple indicating the index range for pagination
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset

            Args:
            - page: The number of the page to retrieve
            - page_size: The number of items (rows) per page we want

            Returns:
                A list of lists representing the rows from the
                dataset corresponding to the specified page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hypermedia pagination information for the dataset

            Args:
            - page : The number of the page to retrieve
            - page_size : The number of items (rows) per page we want

            Returns: A dictionary containing pagination information
        """
        dataset = self.dataset()
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        dct = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages
        }

        return dct
