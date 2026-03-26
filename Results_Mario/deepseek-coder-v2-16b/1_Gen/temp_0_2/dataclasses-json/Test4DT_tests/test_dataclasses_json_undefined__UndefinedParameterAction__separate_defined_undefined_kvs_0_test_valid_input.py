
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Tuple, List, Any
from dataclasses_json.undefined import _UndefinedParameterAction

# Define a mock class for testing
@dataclass
class MockClass:
    param1: int
    param2: str

def test_valid_input():
    # Create an instance of the MockClass with known and unknown parameters
    kvs = {'param1': 1, 'param2': 'value', 'extra_param': 'extra_value'}
    
    # Call the method under test
    known_params, unknown_params = _UndefinedParameterAction._separate_defined_undefined_kvs(MockClass, kvs)
    
    # Assert that the known parameters are correctly separated
    assert known_params == {'param1': 1, 'param2': 'value'}
    assert unknown_params == {'extra_param': 'extra_value'}
