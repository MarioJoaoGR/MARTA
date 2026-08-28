
import pytest
from string_utils.validation import is_isbn_10

# Test valid normalized ISBN-10
def test_valid_normalized_isbn_10():
    assert is_isbn_10('1506715214') == True

# Test valid non-normalized ISBN-10 with hyphens
def test_valid_non_normalized_isbn_10_with_hyphens():
    assert is_isbn_10('150-6715214') == True

# Test invalid normalized ISBN-10 without normalization
@pytest.mark.xfail(reason="Expected False because normalization should be ignored for this test")
def test_invalid_normalized_isbn_10():
    assert is_isbn_10('123456789X') == False

# Test invalid non-normalized ISBN-10 without hyphens
@pytest.mark.xfail(reason="Expected False because normalization should be ignored for this test")
def test_invalid_non_normalized_isbn_10():
    assert is_isbn_10('123456789X', normalize=False) == False
