
import pytest
from ansible.module_utils.common.collections import Sequence

def is_sequence(seq, include_strings=False):
    """Identify whether the input is a sequence.

    Strings and bytes are not sequences here,
    unless ``include_string`` is ``True``.

    Non-indexable things are never of a sequence type.
    """
    if not include_strings and is_string(seq):
        return False

    return isinstance(seq, Sequence)

def is_string(obj):
    return isinstance(obj, (str, bytes))

# Test cases for valid sequences
def test_valid_sequence():
    assert is_sequence([1, 2, 3]) == True

# Test cases for edge cases
def test_edge_cases():
    assert is_sequence(None) == False
    assert is_sequence(42) == False
    assert is_sequence("Hello") == False
    assert is_sequence(b"Hello") == False

# Test cases for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        is_sequence()  # Missing argument should raise TypeError
