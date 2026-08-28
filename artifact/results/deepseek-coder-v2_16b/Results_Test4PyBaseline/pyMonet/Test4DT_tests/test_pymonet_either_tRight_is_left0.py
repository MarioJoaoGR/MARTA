
# Module: pymonet.either
import pytest
from pymonet.either import Right

# Test the creation of a Right instance with a value
def test_right_creation():
    right_instance = Right(10)
    assert right_instance.value == 10

# Test mapping a function to the value of Right
def test_right_map():
    def add_one(x):
        return x + 1

    right_instance = Right(10)
    mapped_right = right_instance.map(add_one)
    assert mapped_right.value == 11

# Test binding a function to the value of Right
def test_right_bind():
    def add_if_even(x):
        return x + 1 if x % 2 == 0 else None

    right_instance = Right(10)
    result = right_instance.bind(add_if_even)
    assert result is not None, f"Expected a value but got {result}"
