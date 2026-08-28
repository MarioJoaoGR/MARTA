
import pytest
from string_utils.validation import is_isbn

def test_valid_isbn_10():
    assert is_isbn('9780312498580') is True

def test_valid_isbn_13():
    assert is_isbn('1506715214') is True

def test_invalid_isbn_with_hyphens():
    assert is_isbn('978-0-312-49858-0', normalize=False) is False

def test_valid_isbn_digit_only():
    assert is_isbn('9780312498580', normalize=False) is True
