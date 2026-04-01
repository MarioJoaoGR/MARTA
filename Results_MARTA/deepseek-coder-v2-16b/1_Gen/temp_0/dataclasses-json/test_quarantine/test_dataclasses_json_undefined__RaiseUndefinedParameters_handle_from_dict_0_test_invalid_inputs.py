
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming _RaiseUndefinedParameters is defined in a module named 'dataclasses_json'
# from dataclasses_json import _RaiseUndefinedParameters

@pytest.mark.parametrize("invalid_input", [
    {'extra_param': 1},  # Extra parameter that should raise an error
    {'_RaiseUndefinedParameters': None}  # Invalid key name, should also raise an error
])
def test_invalid_inputs(invalid_input):
    class _RaiseUndefinedParameters:
        def __init__(self, param1=None, param2=None):
            self.param1 = param1
            self.param2 = param2

    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(_RaiseUndefinedParameters, invalid_input)
    
    assert str(excinfo.value) == f"Received undefined initialization arguments {list(invalid_input.keys())}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:21:8: E1101: Class '_RaiseUndefinedParameters' has no 'handle_from_dict' member (no-member)

"""