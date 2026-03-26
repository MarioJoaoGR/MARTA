
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _ignore_init

# Define a hypothetical dataclass with known and unknown parameters for testing
@dataclass
class MyClass:
    param1: int
    param2: str
    param3: float = 0.0

def test_ignore_init_with_known_parameters():
    # Create an instance of MyClass with only known parameters
    obj = MyClass(param1=1, param2="test")
    
    # Call _ignore_init to ensure it processes the parameters correctly
    _ignore_init(obj, param1=1, param2="test", param4=3.14)
    
    # Check that only known parameters are used in initialization
    assert obj.param1 == 1
    assert obj.param2 == "test"
    assert obj.param3 == 0.0  # Default value should remain unchanged

def test_ignore_init_with_unknown_parameters():
    # Create an instance of MyClass with unknown parameters
    obj = MyClass(param1=1)
    
    # Call _ignore_init to ensure it raises an error for unknown parameters
    with pytest.raises(TypeError):
        _ignore_init(obj, param1=1, param4="unknown")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__ignore_init_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0.py:5:0: E0611: No name '_ignore_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__ignore_init_0.py:28:10: E1120: No value for argument 'param2' in constructor call (no-value-for-parameter)

"""