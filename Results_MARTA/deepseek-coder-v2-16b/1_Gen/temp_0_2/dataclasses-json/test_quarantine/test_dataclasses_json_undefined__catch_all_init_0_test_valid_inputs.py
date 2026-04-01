
import pytest
from dataclasses_json.undefined import _catch_all_init

# Assuming this is the correct way to import the function from the module
# If 'dataclasses_json' is a package, ensure it's installed or adjust the import accordingly

def test_valid_inputs():
    class MyClass:
        def __init__(self, *args, **kwargs):
            _catch_all_init(self, *args, **kwargs)
    
    obj = MyClass(1, 2, param1="value1", unknown_param="unknown_value")
    assert hasattr(obj, 'param1')
    assert hasattr(obj, 'unknown_param')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__catch_all_init_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__catch_all_init_0_test_valid_inputs.py:3:0: E0611: No name '_catch_all_init' in module 'dataclasses_json.undefined' (no-name-in-module)


"""