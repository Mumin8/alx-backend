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
        """
        Return a dictionary containing hypermedia index information for a given index or page number.

        Args:
            index (int): The index of the item to retrieve.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing hypermedia index information.
        """
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        if index is None:
            return {
                "index": None,
                "page_size": page_size,
                "current_page": None,
                "total_pages": total_pages,
                "items": {}
            }

        current_page = index // page_size + 1
        start_index = (current_page - 1) * page_size
        end_index = min(start_index + page_size, dataset_len)

        items = {i: self.dataset()[i] for i in range(start_index, end_index)}

        return {
            "index": index,
            "page_size": page_size,
            "current_page": current_page,
            "total_pages": total_pages,
            "items": items
        }
