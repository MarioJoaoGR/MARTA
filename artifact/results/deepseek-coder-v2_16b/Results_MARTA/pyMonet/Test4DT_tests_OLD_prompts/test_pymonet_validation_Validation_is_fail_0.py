
import pytest
from pymonet.validation import Validation

# Test for successful validation initialization
def test_successful_initialization():
    val = Validation(value=42, errors=[])
    assert not val.is_fail()
    assert val.value == 42

# Test for failed validation initialization with errors
def test_failed_initialization_with_errors():
    val = Validation(value=None, errors=['Error message'])
    assert val.is_fail()
    assert val.value is None
    assert val.errors == ['Error message']

# Test for chaining validation using map method
def test_map_method():
    def double_value(val):
        return val * 2
    
    success_validation = Validation(value=10, errors=[])
    transformed = success_validation.map(double_value)
    assert not transformed.is_fail()
    assert transformed.value == 20

# Test for chaining validation using bind method
def test_bind_method():
    def add_one(val):
        return Validation(value=val + 1, errors=[])
    
    success_validation = Validation(value=9, errors=[])
    chained = success_validation.bind(add_one)
    assert not chained.is_fail()
    assert chained.value == 10

# Test for applying a function to the value using ap method

# Test for converting to an Either monad (conceptual)