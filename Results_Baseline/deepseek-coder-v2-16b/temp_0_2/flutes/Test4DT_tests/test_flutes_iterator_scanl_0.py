
import pytest
from flutes.iterator import scanl
import operator

def test_scanl_with_operator_add():
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]

def test_scanl_with_lambda_function():
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']

def test_scanl_with_custom_multiply():
    def multiply(acc, x):
        return acc * x
    result = list(scanl(multiply, [2, 3, 4], 1))