
import pytest
from unittest.mock import patch

def lenient_lowercase(lst):
    """Lowercase elements of a list.

    If an element is not a string, pass it through untouched.
    """
    lowered = []
    for value in lst:
        try:
            lowered.append(value.lower())
        except AttributeError:
            lowered.append(value)
    return lowered

# Test cases
def test_valid_input_all_strings():
    assert lenient_lowercase(['Hello', 'World', 'Python']) == ['hello', 'world', 'python']

def test_valid_input_mixed_types():
    assert lenient_lowercase(['Hello', 123, True, 'WORLD']) == ['hello', 123, True, 'world']

def test_invalid_input_none():
    with pytest.raises(TypeError):
        lenient_lowercase(None)
