
import pytest
from superstring.superstring import SuperString, SuperStringLower

def test_valid_case():
    s = SuperString('Hello, World!')
    lower_str = SuperStringLower(s)
    
    assert lower_str.length() == len('hello, world!')
