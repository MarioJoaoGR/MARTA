
import pytest
from pymonet.utils import pipe

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    def add_one(x):
        return x + 1
    
    def multiply_by_two(x):
        return x * 2
    
    result = pipe(5, add_one, multiply_by_two)
    assert result == 12

# Test edge case where Maybe is empty (is_nothing is True)
def test_invalid_inputs():
    try:
        result = pipe(5, 'not_a_function')
    except TypeError as e:
        assert str(e) == "'str' object is not callable"

# Test with a lambda function and a predefined function
def test_lambda_and_predefined():
    def add_one(x):
        return x + 1
    
    result = pipe(20, lambda x: x + 5, add_one)
    assert result == 26
