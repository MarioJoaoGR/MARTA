
import pytest
from dataclasses import dataclass
from marshmallow import fields
from inspect import Parameter
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    my_field: str

def test_edge_case_none():
    field = Parameter('my_field', annotation=MyModel)
    result = build_type(MyModel, {}, None, field, MyModel)
    assert isinstance(result, fields.Nested)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_edge_case_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_edge_case_none.py:13:12: E1120: No value for argument 'kind' in constructor call (no-value-for-parameter)


"""