
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_input():
    superstring_instance = SuperStringSubstring('Hello World', 0, 5)
    assert superstring_instance._base == 'Hello World'
    assert superstring_instance._start_index == 0
    assert superstring_instance._end_index == 5
