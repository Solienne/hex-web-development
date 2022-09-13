#!/usr/bin/env python3
"""
Find the correct indexes to paginate the dataset correctly and
return the appropriate page of the dataset
"""

import csv
from math import ceil
from typing import Tuple, List, Dict


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
        """Get the page
            Args:
                page - current page
                page_size - size of page
            Return:
                -List with pagination
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get range of a page
            Args:
                page - current page number
                page_size - length of the page
            Return:
                Dict containing
                    -length of the returned dataset page
                    -current page number
                    -dataset page
                    -number of next page
                    -number of previous page
                    -total number of pages in dataset as integer
        """
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataSet: List = self.dataset()
        totalPages = len(dataSet) if dataSet else 0
        totalPages = ceil(totalPages / page_size)
        prevPage = (page - 1) if (page - 1) >= 1 else None
        nextPage = (page + 1) if (page + 1) <= totalPages else None

        hyper: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }

        return hyper


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Range of page
       Args:
           page: actual page
           page_size: size of page
       return:
           Tuple with start index and end index
    """
    final_size = page * page_size
    start_size = final_size - page_size

    return (start_size, final_size)
