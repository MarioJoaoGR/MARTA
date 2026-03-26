
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

# Additional test cases for uncovered line 737
def test_single_item_string():
    result = _as_list("single item")
    assert result == ['single item']

def test_multiple_items_with_trailing_comma():
    result = _as_list("item1, item2,")
    assert result == ['item1', 'item2']

def test_string_with_leading_and_trailing_spaces():
    result = _as_list(" apple , banana , orange ")
    assert result == ['apple', 'banana', 'orange']

def test_string_with_only_commas():
    result = _as_list(",,,")
    assert result == []

def test_string_with_only_spaces():
    result = _as_list("   ")
    assert result == []
