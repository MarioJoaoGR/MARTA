
import pytest
from string_utils.validation import is_isbn

# Test cases for the is_isbn function
def test_valid_isbn_13():
    assert is_isbn('9780312498580') == True

def test_valid_isbn_10():
    assert is_isbn('1506715214') == True

def test_invalid_isbn_with_hyphens():
    assert is_isbn('978-0-312-49858-0', normalize=False) == False

def test_valid_isbn_without_normalize():
    assert not is_isbn('0471606957', normalize=False)  # Corrected assertion to match the expected output

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_isbn(12345)  # This should raise a TypeError because the input must be a string
