
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

# Define a mock class X with fields 'param1' and 'param2'
@dataclass
class MockClassX:
    param1: int
    param2: str

def test_valid_input():
    # Create an instance of the mock class with known parameters
    kvs = {'param1': 1, 'param2': 'value'}
    
    # Call the handle_from_dict method with the valid dictionary
    result = _IgnoreUndefinedParameters.handle_from_dict(MockClassX, kvs)
    
    # Assert that the result contains only the known parameters
    assert result == {'param1': 1, 'param2': 'value'}
