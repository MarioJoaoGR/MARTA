
import pytest
from dataclasses_json.undefined import _ignore_init
from dataclasses import dataclass

@dataclass
class MyClass:
    a: int
    b: int = 0
    c: int = 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because 'd' is not an expected parameter
        MyClass(_ignore_init=1, d=2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_invalid_inputs.py:3:0: E0611: No name '_ignore_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_invalid_inputs.py:15:8: E1123: Unexpected keyword argument '_ignore_init' in constructor call (unexpected-keyword-arg)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_invalid_inputs.py:15:8: E1123: Unexpected keyword argument 'd' in constructor call (unexpected-keyword-arg)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_invalid_inputs.py:15:8: E1120: No value for argument 'a' in constructor call (no-value-for-parameter)


"""