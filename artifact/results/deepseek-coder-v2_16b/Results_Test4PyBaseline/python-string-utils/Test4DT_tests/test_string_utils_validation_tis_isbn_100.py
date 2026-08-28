
import pytest
from string_utils.validation import is_isbn_10

# Test cases for valid ISBN-10 numbers with default normalization (hyphens removed)
def test_valid_isbn_10_default_normalization():
    assert is_isbn_10('1506715214') == True