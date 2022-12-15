#!/usr/bin/env python3
'''Simple pagination module'''

import csv
import math
from typing import List


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
        '''
        Gets the start of the page and the end of the page.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pagination = index_range(page, page_size)
        dataset = self.dataset()

        return (dataset[pagination[0]:pagination[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10):
        '''
        Returns a dictionary of the page, page_size
        data, next_page, prev_page and total pages.
        '''
        hyper_dict = {}
        hyper_dict['page'] = page
        hyper_dict['data'] = []
        page_data = self.get_page(page, page_size)
        if len(page_data) > 0:
            for _page in page_data:
                hyper_dict['data'].append(_page)
        hyper_dict['page_size'] = len(page_data)
        hyper_dict['prev_page'] = page - 1
        if hyper_dict['prev_page'] == 0:
            hyper_dict['prev_page'] = None
        hyper_dict['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        hyper_dict['next_page'] = page + 1
        if hyper_dict['next_page'] > hyper_dict['total_pages']:
            hyper_dict['next_page'] = None

        return hyper_dict


def index_range(page: int, page_size: int):
    '''
    Returns a tuple of the size of start of the index and end of the inndex
    pages are 1-indexed.
    '''

    end_of_index: int = page * page_size
    start_of_index: int = end_of_index - page_size

    return (start_of_index, end_of_index)
