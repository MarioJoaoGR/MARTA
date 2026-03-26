
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming the module 'dataclasses_json.undefined' has been imported correctly
# from dataclasses_json.undefined import handle_from_dict

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_valid_input():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    known_params = handle_from_dict(ExampleClass, kvs)
    
    assert 'field1' in known_params
    assert 'extra_param' not in known_params
    assert 'field2' in known_params
    assert isinstance(known_params['field1'], int)
    assert isinstance(known_params['field2'], str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_valid_input.py:17:19: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""