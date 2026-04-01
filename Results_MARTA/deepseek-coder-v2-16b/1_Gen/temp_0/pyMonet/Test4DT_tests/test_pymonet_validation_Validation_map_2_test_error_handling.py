
import pytest
from pymonet.validation import Validation

def test_error_handling():
    val = Validation("Success", [])
    
    # Test mapping a function over an invalid input that raises TypeError
    with pytest.raises(TypeError):
        def invalid_mapper(x):
            return x + 1  # This operation is valid for numbers, but not for strings or other types
        
        val.map(invalid_mapper)
