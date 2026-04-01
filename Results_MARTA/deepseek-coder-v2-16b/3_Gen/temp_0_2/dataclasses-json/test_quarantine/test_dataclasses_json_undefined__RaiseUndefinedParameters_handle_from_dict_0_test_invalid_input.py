
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming _RaiseUndefinedParameters and handle_from_dict are defined in a module named 'dataclasses_json'
from dataclasses_json import handle_from_dict  # Corrected the import statement

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_invalid_input():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        handle_from_dict(ExampleClass, kvs)
    assert "Received undefined initialization arguments" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_input.py:8:0: E0611: No name 'handle_from_dict' in module 'dataclasses_json' (no-name-in-module)


"""