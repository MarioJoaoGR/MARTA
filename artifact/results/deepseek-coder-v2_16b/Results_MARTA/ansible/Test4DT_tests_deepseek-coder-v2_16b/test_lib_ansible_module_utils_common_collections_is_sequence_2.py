
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
    assert is_sequence(seq) == True

def test_invalid_sequence():
    seq = 'Hello'
    assert is_sequence(seq) == False

def test_include_strings():
    seq = 'Hello'
    assert is_sequence(seq, include_strings=True) == True
