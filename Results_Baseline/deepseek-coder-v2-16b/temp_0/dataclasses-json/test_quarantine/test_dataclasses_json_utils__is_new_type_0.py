
# Module: dataclasses_json.utils
import pytest
import inspect
from typing import FunctionType, Type

# Import the function to be tested
from dataclasses_json.utils import _is_new_type

def test_is_new_type_function():
    def my_function(): pass
    assert _is_new_type(my_function) == True, "Expected _is_new_type to return True for a function"

def test_is_new_type_class():
    class MyClass: pass
    assert _is_new_type(MyClass) == True, "Expected _is_new_type to return True for a class"

def test_is_new_type_nonfunction():
    def not_a_class(): pass
    assert _is_new_type(not_a_class) == False, "Expected _is_new_type to return False for a non-function, non-class object"

def test_is_new_type_incorrect_input():
    with pytest.raises(TypeError):
        _is_new_type("not a type")  # This should raise an error since "not a type" is not a valid input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_new_type_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0.py:5:0: E0611: No name 'FunctionType' in module 'typing' (no-name-in-module)

"""