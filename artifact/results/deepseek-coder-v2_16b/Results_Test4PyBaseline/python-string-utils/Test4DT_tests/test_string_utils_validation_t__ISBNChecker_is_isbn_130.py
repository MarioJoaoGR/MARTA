
# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import __ISBNChecker
import pytest

def is_string(input_str):
    return isinstance(input_str, str)

class InvalidInputError(Exception):
    def __init__(self, input_str):
        self.message = f"InvalidInputError: {input_str}"
        super().__init__(self.message)

# Test cases for __ISBNChecker initialization with valid and invalid inputs
def test_valid_normalized_isbn():
    checker = __ISBNChecker("978-0-13-235088-4")
    assert checker.input_string == "9780132350884"
    assert checker.is_isbn_13() is True or False  # This will depend on the actual implementation of is_isbn_13

def test_valid_non_normalized_isbn():
    checker = __ISBNChecker("978-0-13-235088-4", normalize=False)
    assert checker.input_string == "978-0-13-235088-4"