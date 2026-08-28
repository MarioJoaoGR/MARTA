
import pytest
from flutes.iterator import split_by

def test_valid_case_with_dot_separator():
    iterable = "Split.by:."
    result = list(split_by(iterable, separator='.'))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]


def test_valid_case_with_dot_separator_no_empty_segments():
    iterable = "Split.by:."
    empty_segments = False
    result = list(split_by(iterable, empty_segments=empty_segments, separator='.'))
    assert result == [['S', 'p', 'l', 'i', 't'], ['b', 'y', ':']]