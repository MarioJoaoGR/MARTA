
from dataclasses_json.undefined import create_init
import pytest

def test_none_input():
    class MyClass:
        def __init__(self, value=None):
            self.value = value

    # Test with None input
    init_callable = create_init(MyClass)
    instance = init_callable(None)  # Passing None to the initializer
    assert instance.value is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_create_init_0_test_none_input.py:2:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)


"""