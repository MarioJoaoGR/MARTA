
import pytest
from pymonet.either import Right, Left, Either

# Test the creation of a Right instance and its is_right method
def test_right_creation():
    r = Right(42)
    assert r.is_right() == True

# Test the map method with a sample function
def double_value(x):
    return x * 2

def test_map_method():
    r = Right(42)
    mapped_value = r.map(double_value)
    assert mapped_value.value == 84

# Test the bind method with a sample function
def add_one(x):
    return x + 1

def test_bind_method():
    r = Right(42)
    bound_value = r.bind(add_one)