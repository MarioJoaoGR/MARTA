
from dataclasses_json.undefined import create_init
import pytest

def test_invalid_input():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    with pytest.raises(TypeError):  # Since the function expects an object, invalid input should raise a TypeError
        create_init("not_a_class")()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_invalid_input.py:2:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)


"""