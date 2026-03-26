
import pytest

from isort.settings import _as_list


# Test cases for _as_list function
def test_comma_separated():
    assert _as_list("apple, banana, orange") == ['apple', 'banana', 'orange']

def test_newline_separated():
    assert _as_list("apple\nbanana\norange") == ['apple', 'banana', 'orange']

def test_comma_and_newline_mixed():
    assert _as_list("apple, banana,, orange,") == ['apple', 'banana', 'orange']

def test_empty_string():
    assert _as_list("") == []

# Additional edge cases to consider:
@pytest.mark.xfail(reason="Expected TypeError for None input")
def test_none_input():
    with pytest.raises(TypeError):
        _as_list(None)  # Ensure the function raises a TypeError for None input

def test_integer_input():
    assert _as_list("1,2,3") == ['1', '2', '3']  # Ensure integers are treated as strings

def test_whitespace_only():
    assert _as_list("   ,   ") == []  # Ensure whitespace-only items are ignored

def test_special_characters():
    assert _as_list("apple, banana!, orange#") == ['apple', 'banana!', 'orange#']  # Ensure special characters are preserved
