# Standard Libraries
from typing import List


class CountingSort:
    _ENG_ALPH_LETTERS = 26  # number of letters in the English alphabet

    def sort(self, array: List[str], k: int) -> List[str]:
        alpha_range = self._ENG_ALPH_LETTERS
        array_len = len(array)

        initial_array = [0] * alpha_range
        result = [''] * array_len

        # Step #2: Counting the number of occurrences of each k-th character
        for word in array:
            index = ord(word[k]) - ord('a')
            initial_array[index] += 1

        # Step #3: Calculation of the cumulative sum
        for i in range(1, alpha_range):
            initial_array[i] += initial_array[i - 1]

        # Step #4: Creating a sorted array
        for word in reversed(array):
            index = ord(word[k]) - ord('a')
            result[initial_array[index] - 1] = word
            initial_array[index] -= 1

        return result
