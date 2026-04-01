
import pytest
from dataclasses_json import undefined
from dataclasses import dataclass, fields

@dataclass
class MyClass:
    a: int
    b: str = None
    c: float = 0.0

def test_edge_cases():
    # Test case for edge cases where only known parameters are passed to the constructor
    with pytest.raises(TypeError):
        obj = MyClass(1, "test", e=3)  # 'e' is not a parameter of the class

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_1_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_1_test_edge_cases.py:15:14: E1123: Unexpected keyword argument 'e' in constructor call (unexpected-keyword-arg)


"""