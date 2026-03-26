
from dataclasses_json.undefined import create_init
import pytest

def test_invalid_input():
    # Test that create_init raises an error when given an object without __init__ method
    class NoInitClass:
        pass
    
    with pytest.raises(AttributeError):
        create_init(NoInitClass)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_invalid_input.py:2:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)

"""