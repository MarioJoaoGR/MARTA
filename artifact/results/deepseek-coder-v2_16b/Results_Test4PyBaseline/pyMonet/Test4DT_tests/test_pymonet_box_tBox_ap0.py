
import pytest
from pymonet.box import Box

# Test initialization of Box with different types of data
def test_box_initialization():
    box_int = Box(42)
    assert box_int.value == 42
    
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

# Test the ap method with a lambda function
def test_ap_method():
    # Define a value to apply the lambda function to
    value = 5
    
    # Create a Box containing the lambda function
    box_lambda = Box(lambda x: x * 2)
    
    # Apply the lambda function stored in the Box to the value
    result_box = box_lambda.ap(Box(value))
    assert result_box.value == 10

# Test the map method with a simple function
def test_map_method():
    # Define a function that adds one to its input
    def add_one(x):
        return x + 1
    
    # Create a Box containing a value
    box = Box(42)
    
    # Map the function to the Box's value
    mapped_box = box.map(add_one)
    assert mapped_box.value == 43

# Test the bind method with a function that doubles its input
def test_bind_method():
    def double_value(x):
        return x * 2
    
    # Create a Box containing a value
    box = Box(5)
    
    # Bind the function to the Box's value
    bound_box = box.bind(double_value)