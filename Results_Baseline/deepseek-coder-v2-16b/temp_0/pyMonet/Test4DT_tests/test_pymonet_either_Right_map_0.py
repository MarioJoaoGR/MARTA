# Module: pymonet.either
# Import the Right class from the pymonet.either module
from pymonet.either import Right

def test_right_initialization():
    # Test creating an instance of Right with a value
    right_value = Right(42)
    assert right_value.value == 42, "Right instance should have the provided value"

def test_map_function():
    # Create an instance of Right with a value
    right_value = Right(42)
    
    # Define a mapper function to double the value
    def double(x):
        return x * 2
    
    # Apply the map function and check the result
    mapped_value = right_value.map(double)
    assert mapped_value.value == 84, "Mapped value should be double of the original value"

def test_bind_function():
    # Create an instance of Right with a value
    right_value = Right(42)
    
    # Define a function to double the value and return a new Right instance
    def double(x):
        return Right(x * 2)
    
    # Apply the bind function and check the result
    bound_value = right_value.bind(double)
    assert bound_value.value == 84, "Bound value should be double of the original value"
