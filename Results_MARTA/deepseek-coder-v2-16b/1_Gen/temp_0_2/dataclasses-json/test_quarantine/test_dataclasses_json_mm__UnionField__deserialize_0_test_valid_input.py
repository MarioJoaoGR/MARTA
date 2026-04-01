
import pytest
from dataclasses import dataclass, fields
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class DataClass1:
    field1: int

@dataclass
class DataClass2:
    field2: str

desc = {DataClass1: lambda v, a, d, **k: DataClass1(**v), DataClass2: lambda v, a, d, **k: DataClass2(**v)}
union_field = _UnionField(desc, None, None)

def test_valid_input():
    value = {'__type': 'DataClass1', '__value__': {'field1': 1}}
    deserialized_value = union_field._deserialize(value, 'field1', {})
    assert isinstance(deserialized_value, DataClass1)
    assert deserialized_value.field1 == 1

def test_invalid_input():
    value = {'__type': 'NonExistentDataClass', '__value__': {'field1': 1}}
    with pytest.warns(UserWarning):
        deserialized_value = union_field._deserialize(value, 'field1', {})
    assert isinstance(deserialized_value, dict)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input.py:22:11: E1101: Instance of 'dict' has no 'field1' member (no-member)


"""