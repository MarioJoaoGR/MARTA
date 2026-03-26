
# Module: pymonet.either
import pytest
from pymonet.either import Right  # Assuming the module is correctly imported and named

# Test initialization with a value
def test_right_initialization():
    right_instance = Right(5)
    assert right_instance.value == 5

# Test bind method with a function that adds one to the value
def test_bind_with_add_one():
    def add_one(x):
        return x + 1
    
    right_instance = Right(5)
    result = right_instance.bind(add_one)