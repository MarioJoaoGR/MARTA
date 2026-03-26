
# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test creating a Validation instance with a success value and an empty errors list
def test_init():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test adding more errors to the Validation instance
def test_ap_add_error():
    val = Validation(None, [])
    def add_error(value):
        return Validation(None, ["Invalid input"])
    
    new_val = val.ap(add_error)
    assert new_val.errors == ["Invalid input"]

# Test using the Validation class with a function that returns another Validation
def test_ap_with_function():
    def add_value(value):
        return Validation(value + 10, [])
    
    val = Validation(5, [])
    new_val = val.ap(add_value)