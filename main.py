# Standard Libraries
import sys
import traceback

# Custom Modules
from utils import file_utils
from core.password_generator import PasswordGenerator


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    password_generator = PasswordGenerator()

    try:
        # Step #1: Load anagrams from file
        loaded_anagrams = file_utils.load_anagrams_from_txt_file(file_path="files/input_anagrams.txt")

        # Step #2: Fetch & print password
        generated_password = password_generator.generate_password(loaded_anagrams)
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
