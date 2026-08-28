
# Module: pymonet.either
# Import the Right class from the pymonet.either module
from pymonet.either import Right

def test_right_creation():
    # Test creating a Right instance with an integer value
    right_instance = Right(10)
    assert right_instance.value == 10, "Right instance should have the provided value"

def test_map_function():
    # Create a Right instance with an initial value
    right_instance = Right(5)
    
    # Define a mapper function to add one to the value
    def add_one(x):
        return x + 1
    
    # Apply the map function and check the result
    mapped_right = right_instance.map(add_one)
    assert mapped_right.value == 6, "Mapped Right instance should have a value of 6"

def test_bind_function():
    # Create a Right instance with an initial value
    right_instance = Right(4)
    
    # Define a binding function to add one if the value is even
    def add_if_even(x):
        return x + 1 if x % 2 == 0 else None
    
    # Apply the bind function and check the result
    result = right_instance.bind(add_if_even)