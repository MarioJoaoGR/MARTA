
import pytest
from pymonet.either import Right, Left  # Assuming the module and class are defined here

# Test for valid input scenario
def test_valid_input():
    right_instance = Right(42)
    
    def square(x): return x * x
    
    result = right_instance.bind(square)
    assert result == 1764

# Test for edge case where input is None
def test_edge_case():
    right_instance = Right(None)
    
    def square(x): return x * x
    
    with pytest.raises(TypeError):
        result = right_instance.bind(square)  # This should raise a TypeError because of the None value

# Test for invalid input scenario
def test_invalid_input():
    right_instance = Right("string")
    
    def square(x): return x * x
    
    with pytest.raises(TypeError):
        result = right_instance.bind(square)  # This should raise a TypeError because of the string value
