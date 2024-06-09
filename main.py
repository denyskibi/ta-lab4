# Standard Libraries
import sys
import traceback

# Custom Modules
from utils import file_utils
from core.password_generator import PasswordGenerator
from core.anagrams_sorting import AnagramsSorting


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    password_generator = PasswordGenerator()
    anagrams_sorting = AnagramsSorting()

    try:
        # Step #1: Load anagrams from file
        loaded_anagrams = file_utils.load_anagrams_from_txt_file(file_path="files/input_anagrams.txt")

        # Task #1
        # Step #1.1: Generate password
        generated_password = password_generator.generate_password(loaded_anagrams)

        # Step #1.2: Print generated password
        print(f"[INFO] Task #1 - Generated password from anagrams: {generated_password}")

        # Task #2
        # Step #2.1: Generate strings by sorting anagrams with needed conditions
        first_row_iteration1, first_row_iteration2 = anagrams_sorting.get_strings_after_sorting(anagrams=
                                                                                                loaded_anagrams)

        # Step #2.2: Print generated strings
        print(f"[INFO] Task #2 - First row after first iteration: {first_row_iteration1}")
        print(f"[INFO] Task #2 - First row after second iteration: {first_row_iteration2}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
