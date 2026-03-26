
import re
import pytest
from string_utils.validation import __ISBNChecker

def test_valid_isbn_13():
    input_string = '9780312498580'
    checker = __ISBNChecker(input_string, True)
    assert checker.is_isbn_13() is True
