
import pytest
from typing import List, get_origin, is_dataclass
from dataclasses import dataclass

def _get_type_origin(type_):
    if hasattr(type_, '__origin__'):
        return type_.__origin__
    elif hasattr(type_, '__extra__'):
        return getattr(type_, '__extra__')
    else:
        return type_

def _is_generic_dataclass(type_):
    origin = _get_type_origin(type_)
    if isinstance(origin, type) and is_dataclass(origin):
        return True
    return False

# Test case to check if List[int] is recognized as a generic dataclass
def test_valid_case_generic_dataclass():
    my_list = List[int]
    assert _is_generic_dataclass(my_list) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case_generic_dataclass
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_valid_case_generic_dataclass.py:3:0: E0611: No name 'is_dataclass' in module 'typing' (no-name-in-module)


"""