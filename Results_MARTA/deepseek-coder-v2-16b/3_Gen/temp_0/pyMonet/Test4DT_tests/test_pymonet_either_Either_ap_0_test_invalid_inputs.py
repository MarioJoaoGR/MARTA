
import pytest
from pymonet.either import Either, Left, Right

def test_invalid_inputs():
    # Test invalid inputs to check error handling
    left_value = Either(Left("error message"))
    right_value = Either(Right(42))
    
    with pytest.raises(AttributeError):
        result = left_value.ap(left_value)  # Should raise AttributeError because the function is not applicable to the value in Left
