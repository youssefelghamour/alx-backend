#!/usr/bin/env python3
""" module for index_range function """
from typing import Tuple


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
