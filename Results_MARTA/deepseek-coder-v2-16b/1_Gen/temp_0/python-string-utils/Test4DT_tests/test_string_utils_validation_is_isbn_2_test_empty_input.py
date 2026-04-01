
import pytest
from string_utils.validation import __ISBNChecker

def test_empty_input():
    input_string = ''
    checker = __ISBNChecker(input_string, normalize=True)
    assert not (checker.is_isbn_13() or checker.is_isbn_10()), "Expected False for empty string"
