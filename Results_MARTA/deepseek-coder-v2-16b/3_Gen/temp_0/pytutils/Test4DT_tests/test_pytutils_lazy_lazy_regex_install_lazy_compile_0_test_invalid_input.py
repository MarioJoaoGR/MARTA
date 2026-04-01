
import pytest
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile
import re

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test invalid input by passing a non-string argument to re.compile
        re.compile(42)  # This should raise a TypeError because 42 is not a string
