
from functools import partial
import pytest
from dataclasses_json.undefined import _UndefinedParameterAction

def test_valid_input_class():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    initializer = create_init(MyClass)
    instance = initializer(10)
    assert instance.value == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_valid_input_class
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_valid_input_class.py:11:18: E0602: Undefined variable 'create_init' (undefined-variable)


"""