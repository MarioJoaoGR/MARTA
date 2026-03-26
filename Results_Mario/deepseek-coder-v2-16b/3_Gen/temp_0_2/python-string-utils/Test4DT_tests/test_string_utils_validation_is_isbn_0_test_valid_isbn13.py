
import pytest
from string_utils.validation import is_isbn

def test_valid_isbn13():
    input_string = '9780312498580'
    assert is_isbn(input_string) == True
