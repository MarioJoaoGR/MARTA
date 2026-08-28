
import pytest
from pymonet.either import Right, Left

# Test valid input scenario
def test_valid_input():
    right_instance = Right(42)
    
    def square(x): 
        return Right(x * x)
    
    result = right_instance.bind(square)
    assert isinstance(result, Right)
    assert result.value == 1764

# Test edge case scenario where the encapsulated value is None
def test_edge_case():
    right_instance = Right(None)
    
    def square(x): 
        return Right(x * x)
    
    with pytest.raises(TypeError):
        result = right_instance.bind(square)

# Test invalid input scenario where mapper function raises an exception
def test_invalid_input():
    right_instance = Right(42)
    
    def raise_exception(x): 
        raise ValueError("Invalid value")
    
    with pytest.raises(ValueError):
        result = right_instance.bind(raise_exception)
