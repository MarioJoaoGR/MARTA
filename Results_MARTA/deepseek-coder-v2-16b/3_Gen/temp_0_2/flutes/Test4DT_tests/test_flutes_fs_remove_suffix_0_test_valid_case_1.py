
import pytest
from flutes.fs import remove_suffix

def test_valid_case_1():
    s = 'https://github.com/huzecong/flutes'
    suffix = '/flutes'
    assert remove_suffix(s, suffix) == "https://github.com/huzecong"
