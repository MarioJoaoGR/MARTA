
import re
import pytest
from string_utils.validation import is_isbn_10

@pytest.mark.parametrize("invalid_isbn", [
    "123456789X",  # Invalid length
    "12345678901", # Invalid length
    "123456789-0", # Contains hyphens
    "1234567890a", # Contains non-digit characters
    "1234567890 ", # Contains whitespace
    "",             # Empty string
])
def test_invalid_isbn_10(invalid_isbn):
    assert not is_isbn_10(invalid_isbn), f"Expected {invalid_isbn} to be invalid"
