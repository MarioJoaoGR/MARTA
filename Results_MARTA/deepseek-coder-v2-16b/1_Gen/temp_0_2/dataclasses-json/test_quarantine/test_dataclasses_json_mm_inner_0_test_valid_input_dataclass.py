
import pytest
from dataclasses import dataclass
from marshmallow import Schema, fields
from dataclasses_json.mm import inner

@dataclass
class MyType:
    pass

def test_valid_input_dataclass():
    schema = Schema()
    field = inner(MyType, {})
    assert isinstance(field, fields.Field)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_inner_0_test_valid_input_dataclass
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_inner_0_test_valid_input_dataclass.py:5:0: E0611: No name 'inner' in module 'dataclasses_json.mm' (no-name-in-module)


"""