
from pymonet.either import Either, Left, Right

def test_valid_inputs():
    # Test case for valid inputs where value is either Left or Right
    
    left_value = Left("error message")
    right_value = Right(42)
    
    # Create instances of Either with valid inputs
    either1 = Either(left_value)
    either2 = Either(right_value)
    
    # Test equality between the two instances
    assert either1 == Either(left_value)
    assert either2 == Either(right_value)
    
    # Test inequality for different types or values
    assert either1 != Either("another error")
    assert either2 != Either(37)
