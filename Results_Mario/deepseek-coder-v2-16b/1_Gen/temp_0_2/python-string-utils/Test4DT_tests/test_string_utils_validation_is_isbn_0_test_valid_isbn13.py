
import re
import pytest
from string_utils.validation import is_isbn

@pytest.mark.parametrize("isbn", [
    '9780312498580',  # Valid ISBN-13
    '1506715214'      # Another valid ISBN-13
])
def test_valid_isbn13(isbn):
    assert is_isbn(isbn) == True
