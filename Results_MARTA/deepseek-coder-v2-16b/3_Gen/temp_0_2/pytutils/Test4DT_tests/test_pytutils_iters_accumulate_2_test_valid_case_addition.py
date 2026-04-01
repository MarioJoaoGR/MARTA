
import pytest
from pytutils.iters import accumulate
import operator

def test_valid_case_addition():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    assert list(accumulate([1, 2, 3, 4, 5], operator.add)) == [1, 3, 6, 10, 15]
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]
