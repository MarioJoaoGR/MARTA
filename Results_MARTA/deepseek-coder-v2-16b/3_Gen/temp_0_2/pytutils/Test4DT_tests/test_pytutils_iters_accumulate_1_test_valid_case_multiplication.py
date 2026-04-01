
import pytest
from pytutils.iters import accumulate, operator

def test_valid_case_multiplication():
    # Test standard input with multiplication function
    func = operator.mul
    result = list(accumulate([1, 2, 3, 4, 5], func))
    assert result == [1, 2, 6, 24, 120]
