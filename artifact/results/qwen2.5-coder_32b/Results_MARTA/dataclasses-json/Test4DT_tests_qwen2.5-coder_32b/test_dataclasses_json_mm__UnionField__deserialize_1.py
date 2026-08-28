
import pytest
from dataclasses import dataclass, field
from typing import Union
from copy import deepcopy
from dataclasses_json.mm import _UnionField
import warnings

# Define some simple schemas for demonstration purposes
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

# Define a dataclass with a union field
@dataclass
class MyClass:
    test_field: Union[int, str] = field(metadata={'dataclasses_json': {'mm_field': None}})

def test__UnionField_instantiation():
    """Test that _UnionField can be instantiated correctly."""
    union_field = _UnionField(
        desc={int: IntegerSchema, str: StringSchema},
        cls=MyClass,
        field="test_field"
    )
    assert isinstance(union_field, _UnionField)



