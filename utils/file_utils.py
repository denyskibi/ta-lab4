# Standard Libraries
from typing import List


def load_anagrams_from_txt_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        loaded_content = file.read().splitlines()
        return loaded_content
