
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, List
from dataclasses_json.undefined import UndefinedParameterError

# Assuming the module 'dataclasses_json.undefined' is correctly imported and contains the necessary classes and functions

@pytest.fixture
def example_class():
    @dataclass
    class ExampleClass:
        field1: int
        field2: str

    return ExampleClass

def test_handle_from_dict(example_class):
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    known_params = handle_from_dict(example_class, kvs)
    
    assert 'field1' in known_params
    assert 'extra_param' not in known_params
    assert 'field2' in known_params

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_error_handling
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_error_handling.py:20:19: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""