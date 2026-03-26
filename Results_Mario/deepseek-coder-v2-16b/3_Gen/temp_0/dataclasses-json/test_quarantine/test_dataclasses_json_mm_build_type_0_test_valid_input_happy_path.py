
import pytest
from dataclasses import dataclass, fields as dataclass_fields
from marshmallow import Schema, fields
from marshmallow_dataclass import dataclass as mm_dataclass
from typing import Optional, List, Union
from enum import Enum
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    my_field: str

def test_valid_input_happy_path():
    @mm_dataclass
    class TestSchema(Schema):
        my_field: Optional[str] = None

    field = dataclass_fields['my_field']
    result = build_type(MyModel, {}, None, field, MyModel)
    
    assert isinstance(result, fields.Field)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_input_happy_path.py:5:0: E0401: Unable to import 'marshmallow_dataclass' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_input_happy_path.py:19:12: E1136: Value 'dataclass_fields' is unsubscriptable (unsubscriptable-object)


"""