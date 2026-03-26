
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming the module 'dataclasses_json.undefined' is correctly imported and contains the necessary classes and functions

@pytest.fixture
def cls():
    @dataclass
    class TestClass:
        param1: int = 0
        _catch_all: Dict[str, Any] = field(default_factory=dict, init=False)
    
    return TestClass()

def test_invalid_inputs(cls):
    kvs = {'param1': 1, 'extra_param': 2}
    with pytest.raises(UndefinedParameterError):
        handle_from_dict(cls, kvs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:14:37: E0602: Undefined variable 'field' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_from_dict_0_test_invalid_inputs.py:21:8: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""