
import inspect
import functools
from dataclasses import dataclass
from dataclasses_json.undefined import _CatchAllUndefinedParameters, create_init

@dataclass
class ExampleDataclass:
    param1: int
    param2: str = None

# Test the function with a valid input
def test_valid_inputs():
    modified_init = create_init(ExampleDataclass)
    example_instance = ExampleDataclass(param1=1, param3="test")  # This will call the modified initializer
    
    assert hasattr(example_instance, '_UNKNOWN0'), "Expected an unknown parameter to be captured"
    assert example_instance._UNKNOWN0 == "test", "The value of the unknown parameter should match the input"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_inputs.py:5:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_inputs.py:15:23: E1123: Unexpected keyword argument 'param3' in constructor call (unexpected-keyword-arg)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_inputs.py:18:11: E1101: Instance of 'ExampleDataclass' has no '_UNKNOWN0' member (no-member)

"""