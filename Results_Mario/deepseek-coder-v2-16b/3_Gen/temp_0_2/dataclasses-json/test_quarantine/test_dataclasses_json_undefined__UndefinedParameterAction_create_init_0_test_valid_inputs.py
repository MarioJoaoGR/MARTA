
from dataclasses_json.undefined import create_init
import pytest

def test_valid_inputs():
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
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_valid_inputs.py:2:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)


"""