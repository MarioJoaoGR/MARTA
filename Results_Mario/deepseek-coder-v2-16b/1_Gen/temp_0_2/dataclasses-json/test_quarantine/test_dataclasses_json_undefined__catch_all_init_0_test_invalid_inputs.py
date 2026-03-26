
import pytest
from dataclasses import dataclass, fields, is_dataclass
from inspect import signature
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _catch_all_init

@pytest.fixture
def setup_class():
    @dataclass
    class MyClass:
        def __init__(self, *args, **kwargs):
            _catch_all_init(self, *args, **kwargs)
    
    return MyClass

def test_invalid_inputs(setup_class):
    MyClass = setup_class()
    with pytest.raises(TypeError):
        # This should raise a TypeError because we are passing an invalid parameter
        MyClass(1, 2, param1="value1", unknown_param="unknown_value")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__catch_all_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__catch_all_init_0_test_invalid_inputs.py:5:0: E0611: No name '_catch_all_init' in module 'dataclasses_json.undefined' (no-name-in-module)


"""