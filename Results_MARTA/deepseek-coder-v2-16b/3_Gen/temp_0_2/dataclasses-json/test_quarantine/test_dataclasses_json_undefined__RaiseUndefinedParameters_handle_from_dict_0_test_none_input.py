
from dataclasses import dataclass
from typing import Dict, Any
from pytest import raises
from dataclasses_json.undefined import UndefinedParameterError, _UndefinedParameterAction

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_none_input():
    kvs = None
    with raises(TypeError):
        known_params = handle_from_dict(ExampleClass, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_none_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_none_input.py:15:23: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""