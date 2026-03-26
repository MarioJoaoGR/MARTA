
import pytest
from pymonet.either import Either, Left, Right

def test_invalid_inputs():
    # Test with invalid input types
    left_value = Either(Left("error message"))
    right_function = Either(Right(lambda x: x + 1))
    
    with pytest.raises(AttributeError):
        result = left_value.ap(right_function)
