
import pytest
from dataclasses import dataclass, fields as dc_fields
from marshmallow import Schema, fields
from typing import Optional, Union, List, Tuple
from enum import Enum
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    value: int

def test_build_type():
    # Test for a simple dataclass field
    class MySchema(Schema):
        my_field = build_type(MyModel, {}, None, dc_fields[0], MyModel)
    
    assert isinstance(MySchema().my_field, fields.Nested)
    assert MySchema().my_field.nested == MyModel

    # Test for a dataclass field that is not an instance of mixin
    class OtherMixin:
        pass

    @dataclass
    class AnotherModel(OtherMixin):
        value: int

    with pytest.warns(UserWarning):
        MySchema().my_field = build_type(AnotherModel, {}, OtherMixin, dc_fields[0], MyModel)
    
    # Test for a tuple field
    class TupleSchema(Schema):
        my_tuple = build_type(Tuple[int, str], {}, None, dc_fields[0], MyModel)
    
    assert isinstance(TupleSchema().my_tuple, fields.Tuple)
    assert TupleSchema().my_tuple.items == (int, str)

    # Test for an optional field
    class OptionalSchema(Schema):
        my_optional = build_type(Optional[int], {}, None, dc_fields[0], MyModel)
    
    assert isinstance(OptionalSchema().my_optional, fields.Field)
    assert OptionalSchema().my_optional.allow_none

    # Test for a union field
    class UnionSchema(Schema):
        my_union = build_type(Union[int, str], {}, None, dc_fields[0], MyModel)
    
    assert isinstance(UnionSchema().my_union, fields.Field)
    assert UnionSchema().my_union.discriminator == {int: int, str: str}

    # Test for an enum field
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    class EnumSchema(Schema):
        color = build_type(Color, {}, None, dc_fields[0], MyModel)
    
    assert isinstance(EnumSchema().color, fields.Enum)
    assert EnumSchema().color.enum == Color

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_edge_cases.py:30:71: E1136: Value 'dc_fields' is unsubscriptable (unsubscriptable-object)


"""