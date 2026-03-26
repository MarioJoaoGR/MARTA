
import pytest
from dataclasses import dataclass, fields
from typing import Union
from dataclasses_json.mm import _UnionField
from copy import deepcopy
import warnings

@dataclass
class Example:
    field: Union[int, str]

def test_valid_input():
    desc = {Example: lambda v, a, d: None}
    union_field = _UnionField(desc, Example, fields['field'])
    value = {"__type": "int", "value": 123}
    deserialized_value = union_field._deserialize(value, 'field', {'field': value})
    assert isinstance(deserialized_value, int)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input.py:15:45: E1136: Value 'fields' is unsubscriptable (unsubscriptable-object)


"""