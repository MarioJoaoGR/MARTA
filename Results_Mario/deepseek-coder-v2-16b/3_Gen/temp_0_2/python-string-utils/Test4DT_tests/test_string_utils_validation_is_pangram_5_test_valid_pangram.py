
import pytest
from string import ascii_lowercase

# Assuming 'your_module_name' has a function to check if the string is full (non-empty and non-space)
def is_full_string(input_string: str) -> bool:
    return input_string.strip() != ''

# Mocking the SPACES_RE for simplicity, as it's not defined in this context
SPACES_RE = ' '  # This should be replaced with actual regex if used

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
    return set(cleaned_string).issuperset(set(ascii_lowercase))

# Test case for is_pangram function
def test_valid_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    assert is_pangram('hello world') == False
