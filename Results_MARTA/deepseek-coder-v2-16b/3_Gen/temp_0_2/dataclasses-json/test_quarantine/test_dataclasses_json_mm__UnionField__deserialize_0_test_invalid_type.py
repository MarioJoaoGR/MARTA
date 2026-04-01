
import pytest
from dataclasses import dataclass, fields
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class Example:
    value: Union[int, str]

def test_invalid_type():
    desc = {int: lambda v, a, d: int(v), str: lambda v, a, d: str(v)}
    field = fields(Example)['value']  # Access the 'value' field from the dataclass Example
    uf = _UnionField(desc, Example, field)
    
    with pytest.raises(AttributeError):
        uf._deserialize({'__type': 'invalid_type', 'value': '123'})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_invalid_type.py:13:12: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)


"""