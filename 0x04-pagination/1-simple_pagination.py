import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


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
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        pagination = index_range(page, page_size)
        dataset = self.dataset()

        try:
            parsed_dataset = dataset[pagination[0]:pagination[1]]
        except Exception:
            return []

        return parsed_dataset
