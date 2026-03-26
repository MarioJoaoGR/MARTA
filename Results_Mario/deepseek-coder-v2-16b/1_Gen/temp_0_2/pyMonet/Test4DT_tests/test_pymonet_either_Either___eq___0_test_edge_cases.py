
from pymonet.either import Either, Left, Right

def test_edge_cases():
    # Test cases for edge cases of Either class
    
    # Case 1: Equality with the same type and value
    left_value = Left("error message")
    right_value = Right(42)
    
    either_left = Either(left_value)
    either_right = Either(right_value)
    
    assert either_left == either_left  # Equality with self
    assert either_right == either_right  # Equality with self
    assert either_left != either_right  # Different types, should not be equal
    
    another_left = Left("another error message")
    another_either_left = Either(another_left)
    
    assert either_left != another_either_left  # Different values, should not be equal
    
    # Case 2: Equality with different types but same value type
    class CustomLeft:
        def __init__(self, value):
            self.value = value
    
    custom_left_value = CustomLeft("error message")
    custom_either_left = Either(custom_left_value)
    
    assert either_left != custom_either_left  # Different types, should not be equal
    
    # Case 3: Equality with the same type and value but different representations
    class CustomRight:
        def __init__(self, value):
            self.value = value
    
    custom_right_value = CustomRight(42)
    custom_either_right = Either(custom_right_value)
    
    assert either_right != custom_either_right  # Different types, should not be equal
