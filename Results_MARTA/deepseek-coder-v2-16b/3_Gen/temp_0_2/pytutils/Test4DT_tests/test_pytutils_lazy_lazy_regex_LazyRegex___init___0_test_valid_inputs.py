
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    assert regex._real_regex is None
    # Accessing a method to trigger the compilation of the regex
    result = regex.match("test")
    assert isinstance(result, type(None) or str)
