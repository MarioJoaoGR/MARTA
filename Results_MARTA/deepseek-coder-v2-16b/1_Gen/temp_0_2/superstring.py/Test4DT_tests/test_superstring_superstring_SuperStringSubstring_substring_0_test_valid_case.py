
import pytest
from superstring.superstring import SuperStringSubstring

def test_valid_case():
    substr = SuperStringSubstring('Hello, World!', 7, 12)
    assert substr.substring(0) == 'World'
