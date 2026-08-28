
import re
from blib2to3.pgen2.tokenize import any
import pytest


def test_invalid_input():
    invalid_input = ('apple', 'banana')
    pattern = any(*invalid_input)
    with pytest.raises(AssertionError):
        assert re.match(pattern, "apple") is not None
        assert re.match(pattern, "banana") is not None
        assert re.match(pattern, "cherry") is None