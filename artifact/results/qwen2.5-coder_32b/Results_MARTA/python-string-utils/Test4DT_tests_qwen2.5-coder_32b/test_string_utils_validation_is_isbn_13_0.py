
import pytest
from string_utils.validation import is_isbn_13

def test_none_input_normalize_true():
    with pytest.raises(TypeError):
        is_isbn_13(None, normalize=True)

def test_non_string_input_normalize_true():
    with pytest.raises(TypeError):
        is_isbn_13(1234567890123, normalize=True)

def test_valid_isbn_13_no_hyphens():
    assert is_isbn_13('9780312498580') == True

def test_valid_isbn_13_with_hyphens_normalize_true():
    assert is_isbn_13('978-0312498580', normalize=True) == True

def test_valid_isbn_13_with_hyphens_normalize_false():
    assert is_isbn_13('978-0312498580', normalize=False) == False

def test_invalid_isbn_13():
    assert is_isbn_13('9780312498581') == False

def test_empty_string_input_normalize_true():
    assert is_isbn_13('', normalize=True) == False

def test_shorter_than_13_digits():
    assert is_isbn_13('978031249858', normalize=True) == False
