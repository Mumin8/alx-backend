#!/usr/bin/env python3
"""
3-hypermedia_del_pagination
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
        """
        Return a dictionary containing hypermedia index information for a given index or page number.

        Args:
            index (int): The index of the item to retrieve. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia index information.
        """
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        if index is None:
            index = 0
        assert 0 <= index < dataset_len, "Index out of range"

        current_page = index // page_size + 1
        start_index = index
        next_index = min(index + page_size, dataset_len)

        data = self.dataset()[start_index:next_index]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data }
