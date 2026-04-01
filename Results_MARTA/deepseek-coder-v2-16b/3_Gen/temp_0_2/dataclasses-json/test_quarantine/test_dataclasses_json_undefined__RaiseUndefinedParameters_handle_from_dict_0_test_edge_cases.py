
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming the module is correctly imported from 'dataclasses_json.undefined'
# If not, you need to adjust the import statement accordingly.

@pytest.fixture
def example_class():
    @dataclass
    class ExampleClass:
        field1: int
        field2: str
    
    return ExampleClass

def test_handle_from_dict_raises_error(example_class):
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        handle_from_dict(example_class, kvs)
    
    assert "Received undefined initialization arguments" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py:22:8: E0602: Undefined variable 'handle_from_dict' (undefined-variable)


"""