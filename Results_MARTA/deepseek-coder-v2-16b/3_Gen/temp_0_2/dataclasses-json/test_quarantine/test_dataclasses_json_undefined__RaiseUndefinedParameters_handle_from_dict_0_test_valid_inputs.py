
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming handle_from_dict is defined in a module named dataclasses_json.undefined
from dataclasses_json.undefined import handle_from_dict

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_valid_inputs():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    known_params = handle_from_dict(ExampleClass, kvs)
    
    assert isinstance(known_params['field1'], int)
    assert known_params['field1'] == 1
    assert isinstance(known_params['field2'], str)
    assert known_params['field2'] == 'hello'
    
    # Check that extra parameters are not included
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(ExampleClass, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_valid_inputs.py:8:0: E0611: No name 'handle_from_dict' in module 'dataclasses_json.undefined' (no-name-in-module)


"""