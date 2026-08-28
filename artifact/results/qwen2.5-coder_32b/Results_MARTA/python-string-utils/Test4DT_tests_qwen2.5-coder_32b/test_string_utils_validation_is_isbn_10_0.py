
import pytest
from string_utils.validation import is_isbn_10


def test_empty_string():
    assert is_isbn_10('') == False


def test_valid_isbn_10_no_hyphens():
    assert is_isbn_10('1506715214') == True

def test_valid_isbn_10_with_hyphens():
    assert is_isbn_10('1-50-671-521-4') == True

def test_invalid_characters():
    assert is_isbn_10('123-456-789X') == False

def test_valid_isbn_10_normalize_false():
    assert is_isbn_10('1506715214', normalize=False) == True

def test_invalid_isbn_10_normalize_false():
    assert is_isbn_10('1-50-671-521-4', normalize=False) == False