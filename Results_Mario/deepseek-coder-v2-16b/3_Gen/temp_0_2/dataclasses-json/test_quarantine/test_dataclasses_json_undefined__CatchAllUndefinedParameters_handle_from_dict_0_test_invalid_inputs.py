
import pytest
from dataclasses import fields, is_dataclass
from typing import Dict, Any
from dataclasses_json.undefined import handle_from_dict, UndefinedParameterError

def test_invalid_inputs():
    class ExampleClass:
        field1: int
        field2: str
    
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    
    # Test case where the catch-all field is not defined in the class
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(ExampleClass, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:5:0: E0611: No name 'handle_from_dict' in module 'dataclasses_json.undefined' (no-name-in-module)


"""