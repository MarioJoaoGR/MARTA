
import pytest
from inspect import FunctionType
from dataclasses_json.utils import _is_new_type

def test_valid_case_function():
    def my_function(): pass
    assert _is_new_type(my_function) == True
    
    class MyClass: pass
    assert _is_new_type(MyClass) == True
    
    def not_a_class(): pass
    assert _is_new_type(not_a_class) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_new_type_0_test_valid_case_function
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_function.py:3:0: E0611: No name 'FunctionType' in module 'inspect' (no-name-in-module)


"""