
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_input():
    substr = SuperStringSubstring('Hello, World!', 7, 12)
    assert substr.length() == 5
