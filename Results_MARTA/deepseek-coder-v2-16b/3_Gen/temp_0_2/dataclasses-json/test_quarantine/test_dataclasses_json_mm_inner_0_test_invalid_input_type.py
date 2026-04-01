
from dataclasses import dataclass
import pytest
from marshmallow import Schema, fields
from dataclasses_json.mm import inner

def test_invalid_input_type():
    # Test that invalid input type raises a warning
    with pytest.warns(UserWarning):
        field = inner(int, {})  # int is not a valid type for this function

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_inner_0_test_invalid_input_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_inner_0_test_invalid_input_type.py:5:0: E0611: No name 'inner' in module 'dataclasses_json.mm' (no-name-in-module)


"""