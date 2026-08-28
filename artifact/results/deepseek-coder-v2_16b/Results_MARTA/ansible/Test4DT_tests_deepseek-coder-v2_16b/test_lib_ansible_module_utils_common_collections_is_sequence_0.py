
import pytest
from collections.abc import Sequence

def is_sequence(seq, include_strings=False):
    """Identify whether the input is a sequence.

    Strings and bytes are not sequences here,
    unless ``include_string`` is ``True``.

    Non-indexable things are never of a sequence type.
    """
    if not include_strings and isinstance(seq, (str, bytes)):
        return False

    return isinstance(seq, Sequence)

# Test cases for the scenarios provided

def test_valid_sequence():
    seq = [1, 2, 3]
    result = is_sequence(seq)
    assert result is True, f"Expected True but got {result} for sequence {seq}"

def test_include_strings():
    seq = "Hello"
    result = is_sequence(seq, include_strings=True)
    assert result is True, f"Expected True but got {result} for sequence {seq} with include_strings=True"

def test_invalid_sequence():
    seq = 42
    result = is_sequence(seq)
    assert result is False, f"Expected False but got {result} for non-sequence input {seq}"
