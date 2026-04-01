
import pytest
from dataclasses import dataclass, fields
from typing import Union
from dataclasses_json.mm import _UnionField, is_dataclass, _get_type_origin
from copy import deepcopy
import warnings

@dataclass
class Example:
    field: Union[int, str]

def test_deserialize():
    desc = {Example: lambda v, a, d: None}
    union_field = _UnionField(desc, Example, fields(Example)[0])

    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'int', 'value': 123}, 123),
        ({'__type': 'str', 'value': 'test'}, 'test'),
        ({'value': 123}, None)  # This should trigger a warning
    ])
    def test_deserialize(value, expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.warns(UserWarning):
                with pytest.raises(expected):
                    deserialized_value = union_field._deserialize(value, 'field', {'field': value})
        else:
            if isinstance(value, dict) and '__type' not in value:
                with pytest.warns(UserWarning):
                    deserialized_value = union_field._deserialize(value, 'field', {'field': value})
                    assert deserialized_value == expected
