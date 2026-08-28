
import pytest
from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw_with_integer():
    value = 42
    result = check_type_raw(value)
    assert result == 42, f"Expected {value}, but got {result}"

def test_check_type_raw_with_string():
    value = "hello"
    result = check_type_raw(value)
    assert result == "hello", f"Expected 'hello', but got {result}"

def test_check_type_raw_with_list():
    value = [1, 2, 3]
    result = check_type_raw(value)
    assert result == [1, 2, 3], f"Expected [1, 2, 3], but got {result}"

def test_check_type_raw_with_dict():
    value = {"key": "value"}
    result = check_type_raw(value)
    assert result == {"key": "value"}, f"Expected {{'key': 'value'}}, but got {result}"

def test_check_type_raw_with_none():
    value = None
    result = check_type_raw(value)
    assert result is None, f"Expected None, but got {result}"

def test_check_type_raw_with_complex_object():
    class MyClass:
        def __init__(self, value):
            self.value = value

    obj = MyClass("complex_object")
    result = check_type_raw(obj)
    assert result.value == "complex_object", f"Expected 'complex_object', but got {result.value}"
