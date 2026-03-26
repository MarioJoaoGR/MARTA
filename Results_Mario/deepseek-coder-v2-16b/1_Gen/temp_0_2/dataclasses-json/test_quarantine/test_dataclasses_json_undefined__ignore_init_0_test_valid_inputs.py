
from dataclasses import dataclass
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass:
    a: int
    b: str = "default"

def test_valid_inputs():
    # Test with valid inputs that should not raise any errors
    obj = MyClass(a=1, b="test")
    assert isinstance(obj, MyClass)
    assert obj.a == 1
    assert obj.b == "test"

    # Test with only required parameters provided
    obj_minimal = MyClass(a=2)
    assert isinstance(obj_minimal, MyClass)
    assert obj_minimal.a == 2
    assert obj_minimal.b == "default"

    # Test with additional undefined parameters (should be ignored)
    obj_undefined = MyClass(a=3, b="test", c="extra")
    assert isinstance(obj_undefined, MyClass)
    assert obj_undefined.a == 3
    assert obj_undefined.b == "test"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0_test_valid_inputs.py:25:20: E1123: Unexpected keyword argument 'c' in constructor call (unexpected-keyword-arg)


"""