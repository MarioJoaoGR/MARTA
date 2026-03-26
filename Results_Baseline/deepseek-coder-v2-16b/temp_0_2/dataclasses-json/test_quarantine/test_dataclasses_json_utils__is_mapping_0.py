
# Module: dataclasses_json.utils
import pytest
from typing import Dict, DefaultDict, Mapping
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

# Test cases for _is_mapping function
def test_is_mapping_builtin():
    assert _is_mapping(dict) == True
    assert _is_mapping(DefaultDict[str, int]) == True

def test_is_mapping_custom():
    class MyCustomMapping: pass
    assert _is_mapping(MyCustomMapping) == False

def test_is_mapping_not_a_type():
    with pytest.raises(TypeError):
        _is_mapping("not a type")

# Helper function to mock _get_type_origin and _issubclass_safe for testing
def mock_get_type_origin(type_):
    if isinstance(type_, type) and issubclass(type_, Mapping):
        return type_
    elif isinstance(type_, type) and not issubclass(type_, Mapping):
        return None
    else:
        raise TypeError("Invalid type")

def mock_issubclass_safe(cls, class_or_tuple):
    if cls == dict or cls == DefaultDict[str, int]:
        return True
    elif cls == MyCustomMapping:
        return False
    else:
        raise ValueError("Unknown class")

# Monkey patch the functions for testing
from dataclasses_json.utils import _get_type_origin, _issubclass_safe
_get_type_origin = mock_get_type_origin
_issubclass_safe = mock_issubclass_safe

def test_is_mapping_monkey_patched():
    assert _is_mapping(dict) == True
    assert _is_mapping(DefaultDict[str, int]) == True
    assert _is_mapping(MyCustomMapping) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0.py:32:16: E0602: Undefined variable 'MyCustomMapping' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_0.py:45:23: E0602: Undefined variable 'MyCustomMapping' (undefined-variable)

"""