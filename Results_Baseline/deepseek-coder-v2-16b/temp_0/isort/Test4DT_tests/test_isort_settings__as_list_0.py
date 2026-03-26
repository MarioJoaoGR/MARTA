# Module: isort.settings
import pytest

from isort.settings import _as_list


# Test cases for _as_list function
def test_basic_usage():
    result = _as_list("apple, banana, orange")
    assert result == ['apple', 'banana', 'orange']

def test_handling_newlines():
    result = _as_list("apple\nbanana\norange")
    assert result == ['apple', 'banana', 'orange']

def test_handling_commas_and_newlines_together():
    result = _as_list("apple, banana,, orange,")
    assert result == ['apple', 'banana', 'orange']

def test_empty_string():
    result = _as_list("")
    assert result == []

def test_string_with_no_separators():
    result = _as_list("no separator here")
    assert result == ['no separator here']

def test_mixed_separators():
    result = _as_list("apple, banana\norange, grape")
    assert result == ['apple', 'banana', 'orange', 'grape']
