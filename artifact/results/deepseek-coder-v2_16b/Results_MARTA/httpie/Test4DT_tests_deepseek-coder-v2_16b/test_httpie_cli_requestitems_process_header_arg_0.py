
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

# Test scenarios

@pytest.fixture
def valid_input():
    return KeyValueArg({'key': 'header_name', 'value': 'header_value'})

@pytest.fixture
def none_input():
    return KeyValueArg({'key': 'another_header', 'value': None})

@pytest.fixture
def missing_value():
    return KeyValueArg({'key': 'missing_header'})

# Test function for valid input
def test_valid_input(valid_input):
    result = process_header_arg(valid_input)
    assert result == 'header_value'

# Test function for None value
def test_none_input(none_input):
    result = process_header_arg(none_input)
    assert result is None

# Test function for missing value key
def test_missing_value(missing_value):
    result = process_header_arg(missing_value)
    assert result is None
