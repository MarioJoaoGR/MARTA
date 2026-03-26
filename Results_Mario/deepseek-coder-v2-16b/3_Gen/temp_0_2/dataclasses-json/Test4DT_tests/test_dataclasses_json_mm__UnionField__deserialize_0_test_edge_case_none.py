
import pytest
from dataclasses import dataclass
from typing import Union
from dataclasses_json.mm import _UnionField

# Define a sample dataclass for testing
@dataclass
class Example:
    value: Union[int, str]

def test_edge_case_none():
    # Define the possible types and their deserialization methods
    desc = {
        int: lambda v, a, d: int(v),
        str: lambda v, a, d: str(v)
    }
    
    # Create an instance of _UnionField with the sample dataclass and field
    uf = _UnionField(desc=desc, cls=Example, field='value')
    
    # Define test cases using pytest.mark.parametrize
    @pytest.mark.parametrize("value, expected", [
        ({'__type': 'int', 'value': 123}, int(123)),
        ({'__type': 'str', 'value': 'hello'}, str('hello')),
        ({'value': 456}, 456),  # Fallback to default deserialization
        ({'value': 'hello'}, str('hello'))  # Fallback to default deserialization
    ])
    def test_case(self, value, expected):
        result = self.uf._deserialize(value, attr='value', data=value)
        assert result == expected
    
    # Run the parametrized tests
    pytest.main()
