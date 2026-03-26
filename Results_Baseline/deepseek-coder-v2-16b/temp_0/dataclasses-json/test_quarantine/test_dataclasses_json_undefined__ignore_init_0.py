
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from your_module import _RaiseUndefinedParameters, UndefinedParameterError

# Define the dataclass for testing
@dataclass
class ExampleClass:
    param1: int
    param2: str

def test_handle_from_dict_valid():
    kvs = {'param1': 1, 'param2': 'value'}
    instance = _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert isinstance(instance, ExampleClass)
    assert instance.param1 == 1
    assert instance.param2 == 'value'

def test_handle_from_dict_invalid():
    kvs = {'param1': 1, 'extra_param': 2}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(ExampleClass, kvs)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0.py:5:0: E0401: Unable to import 'your_module' (import-error)

"""