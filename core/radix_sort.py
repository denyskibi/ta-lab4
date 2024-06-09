# Standard Libraries
from typing import List

# Custom Modules
from core.counting_sort import CountingSort


class RadixSort:
    def __init__(self, counting_sort: CountingSort):
        self._counting_sort = counting_sort

    def sort(self, array: List[str]) -> List[str]:
        array_row_len = len(array[0])

        # Sort for each character (from the end of the line)
        for k in range(array_row_len - 1, -1, -1):
            array = self._counting_sort.sort(array, k)

        return array
