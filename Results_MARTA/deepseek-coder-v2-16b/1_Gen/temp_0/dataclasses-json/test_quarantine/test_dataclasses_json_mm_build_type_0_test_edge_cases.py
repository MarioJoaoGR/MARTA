
import pytest
from dataclasses import dataclass
from marshmallow import fields
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    my_field: str

def test_build_type():
    field = inspect.Parameter(name="my_field", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=MyModel)
    result = build_type(MyModel, {}, None, field, MyModel)
    assert isinstance(result, fields.Nested)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_edge_cases.py:12:12: E0602: Undefined variable 'inspect' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_edge_cases.py:12:52: E0602: Undefined variable 'inspect' (undefined-variable)

"""