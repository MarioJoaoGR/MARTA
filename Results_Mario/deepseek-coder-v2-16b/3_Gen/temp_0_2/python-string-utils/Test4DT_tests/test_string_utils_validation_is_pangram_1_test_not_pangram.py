
import pytest
from string_utils.validation import is_full_string
import string

def is_pangram(input_string: str) -> bool:
    """
    Checks if the input string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once.

    This function first checks if the input string is not empty and contains at least one non-space character using `is_full_string`. If the string does not pass this check, it returns `False`.

    Then, it converts the input string to lowercase and removes all spaces, then checks if the resulting set of characters includes every letter of the English alphabet.

    *Examples:*

    - A pangram example:
      ```python
      >>> is_pangram('The quick brown fox jumps over the lazy dog')  # returns True
      ```

    - Not a pangram example:
      ```python
      >>> is_pangram('hello world')  # returns False
      ```

    :param input_string: The string to check for being a pangram.
    :type input_string: str
    :return: True if the string is a pangram, False otherwise.
    """
    if not is_full_string(input_string):
        return False

    cleaned_string = ''.join(filter(str.isalpha, input_string.lower()))
    return set(cleaned_string).issuperset(set(string.ascii_lowercase))

def test_not_pangram():
    assert not is_pangram('hello world')
