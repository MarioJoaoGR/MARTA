
import re
import pytest
from string_utils.validation import is_isbn_10

# Test cases for invalid ISBN-10 numbers
invalid_isbns = [
    "123456789",  # Wrong length (should be 10)
    "123456789X", # Correct length but incorrect checksum
    "123456789Y", # Incorrect character
    "123456789-", # Contains a hyphen
    "123456789-0",# Contains a hyphen and an invalid character
    "12345678901", # Wrong length (should be 10)
]

@pytest.mark.parametrize("isbn", invalid_isbns)
def test_invalid_isbn_10(isbn):
    assert not is_isbn_10(isbn), f"Expected {isbn} to be an invalid ISBN-10 number"
