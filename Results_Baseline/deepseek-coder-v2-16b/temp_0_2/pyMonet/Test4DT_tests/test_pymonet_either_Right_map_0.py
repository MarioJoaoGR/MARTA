
import pytest
from pymonet.either import Right, Left  # Assuming the module is correctly imported as shown in the function documentation
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')

# Test cases for Right class from pymonet.either module
def test_right_creation():
    right_value = Right(42)  # Creating a Right instance with the value 42
    assert right_value.value == 42

def test_right_string_creation():
    another_right_value = Right("success")  # Creating a Right instance with the string "success"
    assert another_right_value.value == "success"

def test_map_method():
    right_value = Right(42)  # Creating a Right instance with the value 42
    
    def double_value(x):
        return x * 2
    
    mapped_value = right_value.map(double_value)
    assert mapped_value.value == 84  # Output will be 84 (42 * 2)

def test_bind_method():
    def add_one(x):
        return x + 1
    
    right_value = Right(42)  # Creating a Right instance with the value 42
    bound_value = right_value.bind(add_one)