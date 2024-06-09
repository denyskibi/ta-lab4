# Standard Libraries
from typing import List
from collections import Counter


# Custom Modules
from core.counting_sort import CountingSort
from core.radix_sort import RadixSort


class PasswordGenerator:
    def __init__(self):
        self._counting_sort = CountingSort()
        self._radix_sort = RadixSort(self._counting_sort)

    def generate_password(self, anagrams: List[str]) -> str:
        # Step #1: Perform Radix sorting for loaded anagrams
        sorted_anagrams = self._radix_sort.sort(array=anagrams)

        # Step #2: Finding the most common letter among all anagrams
        most_common_letter = self._found_most_common_latter(anagrams)

        # Step #3: Create password
        first_element_of_sorted_anagrams = sorted_anagrams[0]
        last_element_of_sorted_anagrams = sorted_anagrams[-1]
        generated_password = first_element_of_sorted_anagrams + most_common_letter + last_element_of_sorted_anagrams

        return generated_password

    @staticmethod
    def _found_most_common_latter(anagrams: List[str]) -> str:
        anagrams_str = ''.join(anagrams)  # merging anagrams to one string
        most_common_latter = Counter(anagrams_str).most_common(1)[0][0]
        return most_common_latter
