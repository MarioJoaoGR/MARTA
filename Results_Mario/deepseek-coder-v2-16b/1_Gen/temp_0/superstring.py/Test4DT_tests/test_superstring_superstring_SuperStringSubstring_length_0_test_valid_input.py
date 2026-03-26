
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_input():
    substr = SuperStringSubstring('Hello, World!', 7, 12)
    assert substr._base == 'Hello, World!'
    assert substr._start_index == 7
    assert substr._end_index == 12
    assert substr.length() == 5
