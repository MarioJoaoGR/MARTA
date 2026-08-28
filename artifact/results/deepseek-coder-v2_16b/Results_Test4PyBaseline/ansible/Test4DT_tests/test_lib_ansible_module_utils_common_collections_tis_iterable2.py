
# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import is_iterable

# Test cases for is_iterable function
def test_is_iterable_list():
    assert is_iterable([1, 2, 3]) == True

def test_is_iterable_tuple():
    assert is_iterable((1, 2, 3)) == True

def test_is_iterable_set():
    assert is_iterable({1, 2, 3}) == True

def test_is_iterable_string_default():
    assert is_iterable("Hello") == False

def test_is_iterable_string_include_strings():
    assert is_iterable("Hello", include_strings=True) == True

# Additional edge cases to consider:
def test_is_iterable_none():
    assert is_iterable(None) == False

def test_is_iterable_int():
    assert is_iterable(123) == False

def test_is_iterable_float():
    assert is_iterable(123.45) == False

def test_is_iterable_dict():
    assert is_iterable({'a': 1, 'b': 2}) == True

# Test cases for uncovered lines (76-77, 79-83)
def test_is_iterable_false_for_string():
    # This tests the behavior when include_strings is False and seq is a string
    assert is_iterable("Hello") == False

def test_is_iterable_true_for_non_string_iterable():
    # This tests the behavior for non-string iterables
    assert is_iterable([1, 2, 3]) == True

def test_is_iterable_false_for_none():
    # This tests the behavior when seq is None
    assert is_iterable(None) == False

def test_is_iterable_false_for_int():
    # This tests the behavior when seq is an integer
    assert is_iterable(123) == False

def test_is_iterable_false_for_float():
    # This tests the behavior when seq is a float
    assert is_iterable(123.45) == False

if __name__ == "__main__":
    pytest.main()
