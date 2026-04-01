
import pytest
from dataclasses import dataclass, fields
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class Example:
    value: Union[int, str]

def test_valid_input():
    desc = {int: lambda v, a, d: int(v), str: lambda v, a, d: str(v)}
    field = fields(Example)['value']  # Access the 'value' field from the dataclass
    uf = _UnionField(desc, Example, field)
    
    # Test with valid input where '__type' is present in the dictionary
    deserialized_value = uf._deserialize({'__type': 'int', 'value': '123'})
    assert isinstance(deserialized_value, int)
    assert deserialized_value == 123
    
    # Test with valid input where '__type' is not present in the dictionary
    deserialized_value = uf._deserialize({'value': 'hello'})
    assert isinstance(deserialized_value, str)
    assert deserialized_value == 'hello'
    
    # Test with invalid type that does not match any specified in `desc`
    with pytest.warns(UserWarning):
        deserialized_value = uf._deserialize({'value': 123})
        assert isinstance(deserialized_value, int)
        assert deserialized_value == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_0_test_valid_input.py:13:12: E1126: Sequence index is not an int, slice, or instance with __index__ (invalid-sequence-index)


"""