
import pytest
from flutes.iterator import scanr
import operator

def test_valid_case():
    # Test with operator.add and an initial value of 0
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]
    
    # Test with a lambda function and no initial value
    result_lambda = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result_lambda == ['abcd', 'bcd', 'cd', 'd']
