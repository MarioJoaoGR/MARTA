
import pytest
from flutes.iterator import split_by




def test_split_by_criterion_without_empty_segments():
    result = list(split_by(range(10), criterion=lambda x: x % 3 == 0, empty_segments=False))
    assert result == [[1, 2], [4, 5], [7, 8]]

def test_split_by_separator_with_empty_segments():
    result = list(split_by("a.b.c", empty_segments=True, separator='.'))
    assert result == [['a'], ['b'], ['c']]

def test_split_by_separator_without_empty_segments():
    result = list(split_by("a.b.c", empty_segments=False, separator='.'))
    assert result == [['a'], ['b'], ['c']]

def test_split_by_no_criterion_or_separator():
    with pytest.raises(ValueError):
        list(split_by(range(10)))

def test_split_by_both_criterion_and_separator():
    with pytest.raises(ValueError):
        list(split_by(range(10), criterion=lambda x: x % 3 == 0, separator=5))