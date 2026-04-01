
import operator
from pytutils.iters import accumulate
import pytest

def test_valid_case_multiplication():
    # Test case where the iterable contains numbers and we want to multiply them cumulatively
    result = list(accumulate([1, 2, 3, 4, 5], operator.mul))
    assert result == [1, 2, 6, 24, 120]
