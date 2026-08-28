
import pytest
from pymonet.validation import Validation

# Test cases for the map method in the Validation class
def test_map_with_valid_function():
    val = Validation(10, [])
    def double(x):
        return x * 2
    
    transformed_val = val.map(double)
    assert transformed_val.value == 20
    assert len(transformed_val.errors) == 0

def test_map_with_invalid_function():
    val = Validation(10, [])
    def invalid_func(_):
        return None
    
    transformed_val = val.map(invalid_func)
    assert transformed_val.value is None
    assert len(transformed_val.errors) == 0

def test_map_with_error():
    val = Validation(10, ['Error message'])
    def double(x):
        return x * 2
    
    transformed_val = val.map(double)
    assert transformed_val.value == 20
    assert len(transformed_val.errors) == 1