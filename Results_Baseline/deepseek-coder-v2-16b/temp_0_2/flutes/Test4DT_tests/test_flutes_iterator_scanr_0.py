
import pytest
from flutes.iterator import scanr
import operator

# Test cases for scanr function
def test_scanr_with_operator_add():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_scanr_with_lambda_function():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']

def test_scanr_without_initial_value():
    result = scanr(operator.add, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]

def test_scanr_with_custom_function():
    def multiply(acc, x):
        return acc * x
    
    result = scanr(multiply, [1, 2, 3, 4])