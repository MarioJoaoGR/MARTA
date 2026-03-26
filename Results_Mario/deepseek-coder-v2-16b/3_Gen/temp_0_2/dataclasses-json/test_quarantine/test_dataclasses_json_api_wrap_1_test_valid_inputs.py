
from dataclasses_json.api import wrap as _wrap
import pytest

def test_valid_inputs():
    class MyClass:
        pass

    wrapped_class = _wrap(MyClass)
    assert isinstance(wrapped_class, MyClass), "The wrapped class should be an instance of the original class."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_wrap_1_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_wrap_1_test_valid_inputs.py:2:0: E0611: No name 'wrap' in module 'dataclasses_json.api' (no-name-in-module)


"""