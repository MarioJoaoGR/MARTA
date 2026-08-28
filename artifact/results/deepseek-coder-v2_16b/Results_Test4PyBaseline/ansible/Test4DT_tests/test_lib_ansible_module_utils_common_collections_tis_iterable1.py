
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

# Test cases for lines 76-83:
def test_is_iterable_false_for_non_iterables():
    # Testing non-iterable types that should return False
    assert is_iterable(None) == False
    assert is_iterable(123) == False
    assert is_iterable(123.45) == False
    assert is_iterable("Hello") == False  # Default behavior without include_strings=True

def test_is_iterable_true_for_iterables():
    # Testing iterable types that should return True
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable((1, 2, 3)) == True
    assert is_iterable({1, 2, 3}) == True
    assert is_iterable("Hello", include_strings=True) == True

def test_is_iterable_true_for_custom_iterables():
    # Testing custom iterators that should return True
    class CustomIterable:
        def __iter__(self):
            yield 1
            yield 2
            yield 3
    assert is_iterable(CustomIterable()) == True

if __name__ == "__main__":
    pytest.main()
