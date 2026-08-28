
import pytest
from pymonet.either import Right

# Test the instantiation of a Right instance with different values
def test_right_instantiation():
    right_int = Right(10)
    assert right_int.is_right(), "Right instance with integer should be right"
    
    right_str = Right("success")
    assert right_str.is_right(), "Right instance with string should be right"

# Test the map method to transform the contained value
def test_map():
    right_instance = Right(10)
    
    def add_one(x):
        return x + 1
    
    mapped_right = right_instance.map(add_one)
    assert mapped_right.value == 11, "Mapped value should be incremented by one"

# Test the bind method with a function that checks for even numbers
def test_bind():
    right_instance = Right(10)
    
    def add_if_even(x):
        return x + 1 if x % 2 == 0 else None
    
    result = right_instance.bind(add_if_even)