
import pytest
from flutes.iterator import split_by

def test_edge_case_empty_segments():
    iterable = [1, 2, 3, 4, 5]
    result = list(split_by(iterable, empty_segments=True, criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5]]
