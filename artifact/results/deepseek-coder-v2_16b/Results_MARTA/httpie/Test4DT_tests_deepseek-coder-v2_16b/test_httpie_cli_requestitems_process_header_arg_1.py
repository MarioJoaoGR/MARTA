
import pytest
from typing import Optional

class KeyValueArg:
    def __init__(self, data: dict):
        self.data = data
    
    @property
    def value(self) -> Optional[str]:
        return self.data.get('value')

def process_header_arg(arg: KeyValueArg) -> Optional[str]:
    return arg.value or None

# Test cases

@pytest.mark.parametrize("input_data, expected", [
    ({'key': 'header_name', 'value': 'header_value'}, 'header_value'),
    ({'key': 'another_header', 'value': None}, None),
    ({'key': 'missing_value_header'}, None)
])
def test_process_header_arg(input_data, expected):
    arg = KeyValueArg(input_data)
    result = process_header_arg(arg)
    assert result == expected
