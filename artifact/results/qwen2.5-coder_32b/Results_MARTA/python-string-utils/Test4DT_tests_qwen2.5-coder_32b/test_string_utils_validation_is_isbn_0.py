
import pytest
from string_utils.validation import is_isbn

def test_valid_isbn_10():
    assert is_isbn('0-306-40615-2') == True

def test_valid_isbn_10_no_hyphens():
    assert is_isbn('0306406152', normalize=False) == True

def test_valid_isbn_13():
    assert is_isbn('978-0-312-49858-0') == True

def test_valid_isbn_13_no_hyphens():
    assert is_isbn('9780312498580', normalize=False) == True

def test_invalid_isbn_10():
    assert is_isbn('123456789X') == False

def test_invalid_isbn_13():
    assert is_isbn('978-0-312-49858-A') == False

def test_invalid_input_none():
    with pytest.raises(TypeError):
        is_isbn(None)

def test_invalid_input_non_string():
    with pytest.raises(TypeError):
        is_isbn(1234567890)
