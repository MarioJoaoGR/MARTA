# Module: flutes.iterator
import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, List, Type

# Test cases for the `take` function
def test_basic_usage():
    result = list(take(5, range(1000000)))
    assert result == [0, 1, 2, 3, 4], f"Expected [0, 1, 2, 3, 4] but got {result}"

def test_negative_number():
    with pytest.raises(ValueError) as excinfo:
        list(take(-5, range(1000000)))
    assert str(excinfo.value) == "`n` should be non-negative", f"Expected ValueError but got {excinfo.value}"

def test_zero_elements():
    result = list(take(0, range(1000000)))
    assert result == [], f"Expected [] but got {result}"

def test_more_elements_than_available():
    result = list(take(5, [1, 2]))
    assert result == [1, 2], f"Expected [1, 2] but got {result}"
