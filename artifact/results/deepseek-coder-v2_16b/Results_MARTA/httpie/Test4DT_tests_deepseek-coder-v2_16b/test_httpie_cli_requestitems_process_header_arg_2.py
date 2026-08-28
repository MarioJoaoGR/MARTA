
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

@pytest.mark.parametrize("test_input, expected", [
    (KeyValueArg({'key': 'header_name', 'value': 'header_value'}), 'header_value'),
    (KeyValueArg({'key': 'another_header', 'value': None}), None),
    (KeyValueArg({'key': 'missing_header'}), None)
])
def test_process_header_arg(test_input, expected):
    assert process_header_arg(test_input) == expected
