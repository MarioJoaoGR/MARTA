
import re
import pytest
from string_utils.validation import __ISBNChecker

def test_invalid_isbn_with_hyphens():
    input_string = '978-0-312-49858-0'
    normalize = False
    checker = __ISBNChecker(input_string, normalize)
    assert not (checker.is_isbn_13() or checker.is_isbn_10()), "Expected invalid ISBN to return false"
