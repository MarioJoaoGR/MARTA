
import pytest
from dataclasses_json.undefined import UndefinedParameterError, _CatchAllUndefinedParameters
from typing import Dict, Any

class TestClass(_CatchAllUndefinedParameters):
    pass

def test_invalid_inputs():
    kvs = {'param1': 1, 'extra_param': 2}
    with pytest.raises(UndefinedParameterError):
        TestClass().handle_from_dict(kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:12:8: E1120: No value for argument 'kvs' in staticmethod call (no-value-for-parameter)

"""