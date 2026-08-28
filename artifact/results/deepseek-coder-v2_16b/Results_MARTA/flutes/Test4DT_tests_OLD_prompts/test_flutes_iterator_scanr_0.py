
import pytest
from flutes.iterator import scanr
import operator

def test_valid_inputs():
    with pytest.raises(TypeError):
        scanr()  # No arguments provided, should raise TypeError

def test_invalid_func():
    with pytest.raises(TypeError):
        scanr("not a function", [1, 2, 3])  # Invalid func argument, should raise TypeError


def test_valid_usage():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_lambda_usage():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']