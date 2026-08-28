
import pytest
from dataclasses import dataclass, field
from typing import Union
from dataclasses_json.mm import _UnionField
from unittest.mock import patch

# Define simple schemas for serialization and deserialization
class IntegerSchema:
    @staticmethod
    def _serialize(value, attr, obj, **kwargs):
        return {"value": value}

    @staticmethod
    def _deserialize(data, attr, data_structure, **kwargs):
        return data["value"]

class StringSchema:
    @staticmethod
    def _serialize(value, attr, obj, **kwargs):
        return {"text": value}

    @staticmethod
    def _deserialize(data, attr, data_structure, **kwargs):
        return data["text"]

# Define a dataclass with Union Field
@dataclass
class MyClass:
    test_field: Union[int, str] = field(metadata={'dataclasses_json': {'mm_field': _UnionField({int: IntegerSchema, str: StringSchema}, None, "test_field")}})

def test__UnionField_instantiation():
    """Test that _UnionField can be instantiated with valid parameters."""
    union_field = _UnionField(desc={int: IntegerSchema, str: StringSchema}, cls=None, field="test_field")
    assert isinstance(union_field, _UnionField)
    assert union_field.desc == {int: IntegerSchema, str: StringSchema}
    assert union_field.cls is None
    assert union_field.field == "test_field"





