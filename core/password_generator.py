# Standard Libraries
from typing import List


# Custom Modules
from core.counting_sort import CountingSort
from core.radix_sort import RadixSort

from utils import file_utils


class PasswordGenerator:
    def __init__(self):
        self._counting_sort = CountingSort()
        self._radix_sort = RadixSort(self._counting_sort)

    def generate_password(self, loaded_anagrams: List[str]) -> str:
        # Step #1: Perform Radix sorting for loaded anagrams
        sorted_anagrams = self._radix_sort.sort(array=loaded_anagrams)

        pass

    def _found_most_common_latter(self):
        pass
