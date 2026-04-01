
import pytest
from superstring.superstring import SuperStringSubstring

def test_invalid_input():
    try:
        substr = SuperStringSubstring('Hello, World!', -1, 5)
    except ValueError as e:
        assert str(e) == "Start index must be a non-negative integer."
