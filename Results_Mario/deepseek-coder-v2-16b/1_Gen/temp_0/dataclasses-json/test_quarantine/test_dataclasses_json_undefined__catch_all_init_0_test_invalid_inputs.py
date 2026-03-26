
from dataclasses_json.undefined import _CatchAllUndefinedParameters
import pytest

def test_invalid_inputs():
    with pytest.raises(TypeError):
        class MyClass:
            def __init__(self, *args, **kwargs):
                _catch_all_init(self, *args, **kwargs)
        
        obj = MyClass(1, 2, a=3, b=4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__catch_all_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__catch_all_init_0_test_invalid_inputs.py:9:16: E0602: Undefined variable '_catch_all_init' (undefined-variable)

"""