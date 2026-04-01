
import pytest
from dataclasses import dataclass, fields as dc_fields
from marshmallow import Schema, fields
from typing import Optional, List, Union
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    kind: str
    value: int

def test_valid_input_dataclass():
    class MySchema(Schema):
        class Meta:
            unknown = 'EXCLUDE'
    
    schema = MySchema()
    assert isinstance(schema.fields['kind'], fields.Str)
    assert isinstance(schema.fields['value'], fields.Int)

    field_info = dc_fields('kind')
    built_field = build_type(MyModel, {}, None, field_info, MyModel)
    
    assert isinstance(built_field, fields.Nested)
    assert built_field.nested == MyModel.__dataclass_fields__['kind'].type

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_valid_input_dataclass
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_valid_input_dataclass.py:26:33: E1101: Class 'MyModel' has no '__dataclass_fields__' member (no-member)


"""