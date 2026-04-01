
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming _RaiseUndefinedParameters is defined in a module named 'dataclasses_json'
from dataclasses_json import _RaiseUndefinedParameters as RUP

@dataclass
class ExampleClass:
    param1: int
    param2: str

def test_handle_from_dict_raises_error_for_undefined_parameters():
    kvs = {'param1': 1, 'extra_param': 2}
    with pytest.raises(UndefinedParameterError) as excinfo:
        RUP.handle_from_dict(ExampleClass, kvs)
    assert "Received undefined initialization arguments" in str(excinfo.value)

def test_handle_from_dict_returns_known_parameters():
    kvs = {'param1': 1, 'param2': 'test'}
    result = RUP.handle_from_dict(ExampleClass, kvs)
    assert result == {'param1': 1, 'param2': 'test'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py:8:0: E0611: No name '_RaiseUndefinedParameters' in module 'dataclasses_json' (no-name-in-module)

"""