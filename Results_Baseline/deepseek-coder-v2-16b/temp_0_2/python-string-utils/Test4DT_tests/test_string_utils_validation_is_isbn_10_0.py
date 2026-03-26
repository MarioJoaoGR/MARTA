# Module: string_utils.validation
import pytest
from string_utils.validation import is_isbn_10

# Test cases for the is_isbn_10 function
def test_valid_isbn_10():
    assert is_isbn_10('1506715214') == True
    assert is_isbn_10('150-6715214') == True

def test_invalid_isbn_10_with_normalize():
    assert is_isbn_10('150-6715214', normalize=False) == False

def test_valid_isbn_10_without_normalize():
    assert is_isbn_10('1506715214', normalize=False) == True

def test_invalid_characters():
    assert is_isbn_10('150-6715214a') == False

def test_empty_string():
    assert is_isbn_10('') == False

def test_none_input():
    with pytest.raises(TypeError):
        is_isbn_10(None)
