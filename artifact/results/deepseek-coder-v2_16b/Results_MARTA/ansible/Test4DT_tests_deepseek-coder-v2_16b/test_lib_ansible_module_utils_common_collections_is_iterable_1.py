
import pytest
from ansible.module_utils.common.collections import is_iterable

def test_is_iterable_list():
    assert is_iterable([1, 2, 3]) == True

def test_is_iterable_string_with_include_strings():
    assert is_iterable("Hello, World!", include_strings=True) == True

def test_is_iterable_dict():
    assert is_iterable({"key": "value"}) == True

def test_is_iterable_int():
    assert is_iterable(123) == False

def test_is_iterable_string_without_include_strings():
    assert is_iterable("Hello, World!") == False
