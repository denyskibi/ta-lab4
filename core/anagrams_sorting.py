# Standard Libraries
from typing import List, Tuple

# Custom Modules
from core.counting_sort import CountingSort
from core.radix_sort import RadixSort


class AnagramsSorting:
    def __init__(self):
        self._counting_sort = CountingSort()

    def get_strings_after_sorting(self, anagrams: List[str]) -> Tuple[str, str]:
        # The first iteration of sorting by the lowest order (k = 2)
        first_iteration = self._counting_sort.sort(anagrams, 2)
        first_row_iteration1 = first_iteration[0]

        # The second iteration of sorting by average rank (k = 1)
        second_iteration = self._counting_sort.sort(first_iteration, 1)
        first_row_iteration2 = second_iteration[0]

        return first_row_iteration1, first_row_iteration2
