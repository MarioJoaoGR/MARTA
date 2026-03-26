
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import undefined, _ignore_init

@dataclass
class MyClass:
    arg1: str
    arg2: int
    kwarg1: str = undefined

def test_edge_cases():
    with pytest.raises(TypeError):
        # This should raise a TypeError because 'kwarg1' is not defined in the class signature
        MyClass("value1", "value2", kwarg1="value3")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_edge_cases.py:4:0: E0611: No name 'undefined' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_edge_cases.py:4:0: E0611: No name '_ignore_init' in module 'dataclasses_json.undefined' (no-name-in-module)

"""