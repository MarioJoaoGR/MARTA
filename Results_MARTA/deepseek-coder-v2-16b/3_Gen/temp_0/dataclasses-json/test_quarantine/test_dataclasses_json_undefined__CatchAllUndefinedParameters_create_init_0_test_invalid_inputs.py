
import inspect
import functools
from dataclasses import dataclass
from dataclasses_json.undefined import _CatchAllUndefinedParameters, create_init

@dataclass
class ExampleDataclass:
    param1: int
    param2: str = None

def test_invalid_inputs():
    modified_init = create_init(ExampleDataclass)
    
    # Test with invalid inputs
    try:
        example_instance = ExampleDataclass(param1=1, param3="test")  # This should raise an error due to undefined parameter 'param3'
        assert False, "Expected TypeError but did not get one"
    except TypeError as e:
        assert str(e) == "__init__() got an unexpected keyword argument 'param3'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_invalid_inputs.py:5:0: E0611: No name 'create_init' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_invalid_inputs.py:17:27: E1123: Unexpected keyword argument 'param3' in constructor call (unexpected-keyword-arg)


"""