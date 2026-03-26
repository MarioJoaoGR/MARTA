
import inspect
import functools
from dataclasses import dataclass
from dataclasses_json.undefined import _CatchAllUndefinedParameters, create_init

@dataclass
class ExampleDataclass:
    param1: int
    param2: str = None

def test_edge_cases():
    modified_init = create_init(ExampleDataclass)
    example_instance = ExampleDataclass(param1=1, param3="test")  # This will call the modified initializer
    
    assert hasattr(example_instance, '_UNKNOWN0'), "Instance of 'ExampleDataclass' should have '_UNKNOWN0' member"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_edge_cases.py:5:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_edge_cases.py:14:23: E1123: Unexpected keyword argument 'param3' in constructor call (unexpected-keyword-arg)

"""