
import pytest
from dataclasses import dataclass
import inspect
import functools
from dataclasses_json.undefined import create_init, _CatchAllUndefinedParameters

@dataclass
class ExampleDataclass:
    param1: int
    param2: str = None

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the function expects an object, not a dataclass instance directly
        create_init(ExampleDataclass)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_invalid_inputs.py:6:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)

"""