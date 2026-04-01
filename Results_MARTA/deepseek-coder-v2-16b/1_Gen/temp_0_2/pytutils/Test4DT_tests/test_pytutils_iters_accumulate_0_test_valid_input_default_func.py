
import operator
from pytutils.iters import accumulate
import pytest

@pytest.mark.parametrize("iterable, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 6, 10, 15]),
    ((1, 2, 3, 4, 5), [1, 3, 6, 10, 15]),
    ([5, 4, 3, 2, 1], [5, 9, 12, 14, 15]),
    ((5, 4, 3, 2, 1), [5, 9, 12, 14, 15])
])
def test_valid_input_default_func(iterable, expected):
    result = list(accumulate(iterable))
    assert result == expected
