
import pytest
from flutes.iterator import drop
from typing import Iterable, Iterator

def test_edge_case():
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))  # Ensure that negative values raise a ValueError

    result = list(drop(5, range(10)))
    assert result == [5, 6, 7, 8, 9]

    result_empty = list(drop(10, range(10)))
    assert result_empty == []
