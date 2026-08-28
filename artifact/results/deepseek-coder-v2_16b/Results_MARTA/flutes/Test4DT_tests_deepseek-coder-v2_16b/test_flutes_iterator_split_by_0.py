
import pytest
from flutes.iterator import split_by


def test_valid_case_without_separator():
    iterable = "Split by nothing"
    empty_segments = True
    separator = None
    with pytest.raises(ValueError):
        list(split_by(iterable, empty_segments=empty_segments, separator=separator))
