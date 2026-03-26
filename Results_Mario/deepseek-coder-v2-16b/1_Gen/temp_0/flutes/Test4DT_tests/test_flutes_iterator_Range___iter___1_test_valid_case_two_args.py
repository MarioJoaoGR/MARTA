
import pytest
from flutes.iterator import Range

def test_valid_case_two_args():
    r = Range(1, 10)
    assert isinstance(r, Range)
    iterator = iter(r)
    values = []
    for _ in range(10):
        try:
            values.append(next(iterator))
        except StopIteration:
            break
    expected_values = list(range(1, 10))
    assert values == expected_values
