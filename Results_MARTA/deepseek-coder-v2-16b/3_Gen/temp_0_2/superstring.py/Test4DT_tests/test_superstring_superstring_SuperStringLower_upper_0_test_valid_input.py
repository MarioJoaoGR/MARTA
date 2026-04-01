
import pytest
from superstring.superstring import SuperStringLower

def test_valid_input():
    ssu = SuperStringLower('hello world')
    assert ssu.upper() == 'HELLO WORLD'
