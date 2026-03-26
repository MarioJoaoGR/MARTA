
# Module: Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0
import pytest
from your_module import _RaiseUndefinedParameters, UndefinedParameterError
from dataclasses import dataclass

# Define the dataclass to be used in tests
@dataclass
class ExampleClass:
    param1: int
    param2: str

def test_handle_from_dict_with_undefined_parameter():
    kvs = {'param1': 1, 'extra_param': 2}
    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert str(excinfo.value) == "Received undefined initialization arguments {'extra_param'}"

def test_handle_from_dict_with_known_parameters():
    kvs = {'param1': 1, 'param2': 'test'}
    result = _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert result == ExampleClass(param1=1, param2='test')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""